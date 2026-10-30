import { mkdir, writeFile } from 'node:fs/promises';
import { resolve } from 'node:path';

const safeUrl = value => String(value).replace(/([?&](?:tk|key|token|access_token|api_key)=)[^&\s"']+/gi, '$1[redacted]');

export function browserDiagnostics(context, name) {
  const pending = new Map(), failures = [], pages = new Set();
  const request = item => pending.set(item, { url: safeUrl(item.url()), type: item.resourceType(), started: Date.now() });
  const finished = item => pending.delete(item);
  const failed = item => {
    failures.push({ url: safeUrl(item.url()), type: item.resourceType(), error: safeUrl(item.failure()?.errorText) });
    pending.delete(item);
  };
  const response = item => {
    if (item.status() >= 400) failures.push({ url: safeUrl(item.url()), status: item.status() });
  };
  const page = item => {
    pages.add(item);
    item.on('pageerror', error => failures.push({ pageError: safeUrl(error.message) }));
  };
  context.on('request', request);
  context.on('requestfinished', finished);
  context.on('requestfailed', failed);
  context.on('response', response);
  context.on('page', page);
  context.pages().forEach(page);
  return async error => {
    const directory = resolve('../output/qa/browser-failures', name);
    await mkdir(directory, { recursive: true });
    const snapshots = [];
    for (const [index, item] of [...pages].filter(item => !item.isClosed()).entries()) {
      try {
        const snapshot = await item.locator('html').evaluate(() => ({
          url: location.href, readyState: document.readyState,
          drawer: [...document.querySelectorAll('.detail-drawer')].map(node => ({ id: node.dataset.entryId, restoring: node.dataset.readingRestoring })),
          images: [...document.images].map(image => ({ src: image.currentSrc || image.src, complete: image.complete, width: image.naturalWidth, height: image.naturalHeight })),
          fonts: [...document.fonts].map(font => ({ family: font.family, status: font.status })),
          resources: performance.getEntriesByType('resource').map(resource => ({ url: resource.name, duration: resource.duration, transferSize: resource.transferSize })),
        }), undefined, { timeout: 5000 });
        snapshots.push(snapshot);
      } catch (captureError) { snapshots.push({ captureError: safeUrl(captureError.message) }); }
      try { await item.screenshot({ path: resolve(directory, `page-${index}.png`), timeout: 5000 }); }
      catch (captureError) { snapshots.push({ screenshotError: safeUrl(captureError.message) }); }
    }
    const report = { node: process.version, platform: process.platform, error: safeUrl(error.stack || error.message), pending: [...pending.values()], failures, pages: snapshots };
    await writeFile(resolve(directory, 'failure.json'), safeUrl(JSON.stringify(report, null, 2)) + '\n');
  };
}
