import assert from 'node:assert/strict';
import { createServer } from 'vite';

const server = await createServer({ server: { middlewareMode: true, hmr: false }, appType: 'custom', optimizeDeps: { noDiscovery: true, include: [] } });
const originalImage = globalThis.Image;
const jobs = [];
globalThis.Image = class {
  naturalWidth = 2048;
  naturalHeight = 2048;
  decode() { return new Promise((resolve, reject) => jobs.push({ src: this.src, resolve, reject })); }
};
try {
  const { loadImage, cachedSprites } = await server.ssrLoadModule('/src/asset-cache.js');
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
  console.log('PASS: late rejection, in-flight image reuse, image and sprite LRU budgets, and retry.');
} finally {
  globalThis.Image = originalImage;
  await server.close();
}
