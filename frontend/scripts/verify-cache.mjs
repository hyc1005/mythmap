import assert from 'node:assert/strict';
import { createServer } from 'vite';
import { readFile, stat } from 'node:fs/promises';

const server = await createServer({ server: { middlewareMode: true, hmr: false }, appType: 'custom', optimizeDeps: { noDiscovery: true, include: [] } });
const originalImage = globalThis.Image;
const jobs = [];
globalThis.Image = class {
  naturalWidth = 2048;
  naturalHeight = 2048;
  decode() { return new Promise((resolve, reject) => jobs.push({ src: this.src, resolve, reject })); }
};
try {
  const { loadImage, cachedSprites, chapterPrefetchPaths, prefetchNextChapter, PREFETCH_BUDGET } = await server.ssrLoadModule('/src/asset-cache.js');
  const world = JSON.parse(await readFile(new URL('../public/data/myth-world.json', import.meta.url), 'utf8'));
  const catalog = JSON.parse(await readFile(new URL('../public/data/atlas/catalog.json', import.meta.url), 'utf8'));
  for (const chapter of world.stages) {
    const paths = chapterPrefetchPaths(chapter.id, world, catalog);
    let bytes = 0;
    for (const path of paths) bytes += (await stat(new URL('../public' + path, import.meta.url))).size;
    assert.ok(bytes <= PREFETCH_BUDGET);
    assert.ok(paths.every(path => !path.includes('/animations/')), 'Large action sheets load on demand');
  }
  const old = loadImage('/cache-a').catch(() => null);
  for (let index = 0; index < 8; index++) loadImage(`/cache-filler-${index}`).catch(() => null);
  assert.equal(jobs.filter(job => job.src === '/cache-a').length, 1);
  const pending = loadImage('/cache-a');
  jobs[0].reject(new Error('Network failure'));
  await old;
  await assert.rejects(pending);
  const replacement = loadImage('/cache-a');
  assert.equal(loadImage('/cache-a'), replacement, 'In-flight requests survive cache pressure');
  assert.equal(jobs.filter(job => job.src === '/cache-a').length, 2, 'No third duplicate request');
  jobs.slice(1).forEach(job => job.resolve({}));
  await replacement;
  const timedOut = loadImage('/cache-timeout', 5);
  await assert.rejects(timedOut, /timed out/);
  const retry = loadImage('/cache-timeout');
  jobs.at(-1).resolve();
  await retry;
  const evicted = loadImage('/cache-filler-0');
  assert.equal(jobs.filter(job => job.src === '/cache-filler-0').length, 2, 'Decoded byte budget evicts old images');
  jobs.at(-1).resolve();
  await evicted;

  let builds = 0;
  const canvas = () => ({ width: 1024, height: 1024, getContext() {} });
  const load = async () => { builds++; return { image: canvas() }; };
  await cachedSprites('budget-0', load);
  await cachedSprites('budget-0', load);
  assert.equal(builds, 1, 'A cached sheet is reused');
  for (let index = 1; index < 6; index++) await cachedSprites(`budget-${index}`, load);
  await cachedSprites('budget-0', load);
  await cachedSprites('budget-6', load);
  const before = builds;
  await cachedSprites('budget-0', load);
  assert.equal(builds, before, 'The recently accessed sheet survives budget eviction');
  await cachedSprites('budget-1', load);
  assert.equal(builds, before + 1, 'The oldest sheet is evicted when the 24 MiB budget is exceeded');
  await assert.rejects(cachedSprites('retry', () => { throw new Error('Decode failed'); }));
  assert.deepEqual(await cachedSprites('retry', async () => ({ ready: true })), { ready: true }, 'Failed sheets can be retried');
  const previousWindow = globalThis.window, previousFetch = globalThis.fetch;
  const timers = new Map(), requests = [];
  let timerId = 0;
  globalThis.window = {
    setTimeout(callback) { timers.set(++timerId, callback); return timerId; },
    clearTimeout(id) { timers.delete(id); },
  };
  globalThis.fetch = (url, options) => new Promise(resolve => requests.push({ url, options, resolve }));
  try {
    const beforeStart = prefetchNextChapter('03', world, catalog);
    beforeStart();
    assert.equal(timers.size, 0, 'Leaving before the delay prevents prefetch');
    const stop = prefetchNextChapter('03', world, catalog);
    [...timers.values()][0]();
    assert.equal(requests.length, 2, 'At most two prefetch requests start together');
    stop();
    for (const request of requests) {
      assert.equal(request.options.keepalive, true, 'In-flight cache fills may complete across navigation');
      assert.equal(request.options.signal, undefined, 'Leaving a chapter does not abort an active response');
      request.resolve({ ok: true, arrayBuffer: async () => new ArrayBuffer(0) });
    }
    await new Promise(setImmediate);
    assert.equal(requests.length, 2, 'Leaving stops queued requests after active responses finish');
  } finally {
    if (previousWindow === undefined) delete globalThis.window;
    else globalThis.window = previousWindow;
    globalThis.fetch = previousFetch;
  }
  console.log('PASS: late rejection, in-flight image reuse, sprite LRU budget, retry and prefetch navigation cleanup.');
} finally {
  globalThis.Image = originalImage;
  await server.close();
}
