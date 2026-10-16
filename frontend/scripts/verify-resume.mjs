import assert from 'node:assert/strict';
import { mkdir } from 'node:fs/promises';
import { chromium, firefox, webkit } from 'playwright';
import { mockTianditu } from './mock-tianditu.mjs';

const base = process.env.ATLAS_URL;
if (!base) throw new Error('Run through with-preview.mjs');
const key = 'shanhai-last-reading-v1';
const output = new URL('../../output/qa/', import.meta.url);
await mkdir(output, { recursive: true });
const filename = name => new URL(name, output).pathname.replace(/^\/([A-Za-z]:)/, '$1');
const drawer = page => page.locator('.detail-drawer');
async function ready(page, scrolled = false) {
  await page.waitForFunction(scrolled => {
    const node = document.querySelector('.detail-drawer');
    return node && node.dataset.readingRestoring === 'false' && (!scrolled || node.scrollTop > 0) && [...node.querySelectorAll('img')].every(image => image.complete);
  }, scrolled);
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(60);
}
async function scrollToSource(page) {
  await ready(page);
  await drawer(page).evaluate(node => {
    const source = node.querySelector('[data-reading-anchor="source"]');
    node.scrollTop += source.getBoundingClientRect().top - node.getBoundingClientRect().top - 170;
  });
  await page.waitForTimeout(250);
  return drawer(page).evaluate(node => node.scrollTop);
}
const stored = page => page.evaluate(key => JSON.parse(localStorage.getItem(key)), key);
async function continueReading(page) {
  await page.locator('.resume-reading').click();
  await ready(page, true);
}

for (const name of (process.env.ATLAS_BROWSERS || 'chromium,webkit').split(',')) {
  const browser = await ({ chromium, firefox, webkit }[name]).launch();
  try {
    const context = await browser.newContext({ viewport: { width: 390, height: 844 }, reducedMotion: 'reduce' });
    await mockTianditu(context);
    const page = await context.newPage();
    const errors = [];
    page.on('pageerror', error => errors.push(error.message));
    await page.goto(`${base}?chapter=03&item=03-01&lang=zh`);
    const top = await scrollToSource(page);
    assert.ok(top > 150);
    const art = await page.locator('.drawer-art').getAttribute('src');
    const record = await stored(page);
    assert.equal(record.id, '03-01');
    assert.equal(record.chapter, '03');
    assert.ok(record.position.fraction >= 0 && record.position.fraction <= 1);
    await page.reload();
    await ready(page, true);
    assert.ok(Math.abs(await drawer(page).evaluate(node => node.scrollTop) - top) <= 3, 'Reload restores reading position');
    await drawer(page).evaluate(node => { node.scrollTop -= 60; });
    const immediate = await drawer(page).evaluate(node => node.scrollTop);
    await page.reload();
    await ready(page, true);
    assert.ok(Math.abs(await drawer(page).evaluate(node => node.scrollTop) - immediate) <= 3, 'Page hide flushes pending scroll writes');
    await page.locator('.drawer-close').click();
    await continueReading(page);
    assert.ok(Math.abs(await drawer(page).evaluate(node => node.scrollTop) - immediate) <= 3);
    await page.goto(`${base}?lang=zh`);
    assert.equal(await drawer(page).count(), 0, 'Homepage does not automatically open a reader');
    await page.locator('.resume-reading').getByText('阪泉之战', { exact: true }).waitFor();
    assert.equal(await page.locator('.world-layout').getAttribute('data-chapter'), '00');
    if (name === 'chromium') await page.locator('.map-reading-actions').screenshot({ path: filename('continue-reading-controls-390.png') });
    await continueReading(page);
    assert.equal(await page.locator('.world-layout').getAttribute('data-chapter'), '03');
    assert.equal(await drawer(page).getAttribute('data-entry-id'), '03-01');
    assert.ok(Math.abs(await drawer(page).evaluate(node => node.scrollTop) - immediate) <= 3);
    await page.locator('.drawer-close').click();
    assert.equal(await page.locator('.resume-reading').evaluate(node => node === document.activeElement), true, 'Resume restores focus to its map-below entry');
    await page.locator('.map-mode-switch').getByRole('button', { name: '真实地理', exact: true }).click();
    await page.locator('.geography-main .resume-reading').waitFor();
    assert.equal(await page.locator('.map-reading-actions').count(), 1);
    assert.equal(await page.locator('.begin-journey:visible').count(), 0);
    const resumeBounds = await page.locator('.resume-reading').boundingBox();
    const readoutBounds = await page.locator('.geo-readout').boundingBox();
    assert.ok(resumeBounds.y >= readoutBounds.y + readoutBounds.height, 'Geographic resume follows the coordinate readout');
    await continueReading(page);
    assert.equal(await drawer(page).getAttribute('data-entry-id'), '03-01');
    await page.locator('.drawer-close').click();
    assert.equal(await page.locator('.resume-reading').evaluate(node => node === document.activeElement), true, 'Geographic resume also restores focus');
    await page.locator('.map-mode-switch').getByRole('button', { name: '木刻叙事', exact: true }).click();
    await page.locator('.explore-playback .resume-reading').waitFor();
    await page.getByRole('button', { name: 'EN', exact: true }).click();
    await continueReading(page);
    assert.equal(new URL(page.url()).searchParams.get('lang'), 'en', 'Continue honors the current language');
    assert.ok(await drawer(page).evaluate(node => node.scrollTop > 150));
    await drawer(page).locator('.original-text summary').click();
    await drawer(page).evaluate(node => {
      const original = node.querySelector('.original-text');
      node.scrollTop += original.getBoundingClientRect().top - node.getBoundingClientRect().top - 170;
    });
    await page.waitForTimeout(250);
    assert.equal((await stored(page)).position.originalOpen, true);
    await page.reload();
    await ready(page, true);
    assert.equal(await drawer(page).locator('.original-text').evaluate(node => node.open), true, 'Expanded Chinese original is restored');
    await page.locator('.drawer-close').click();
    await page.getByRole('button', { name: '中文', exact: true }).click();
    await continueReading(page);
    await drawer(page).getByRole('button', { name: '下一条', exact: true }).click();
    await ready(page);
    assert.equal(await drawer(page).getAttribute('data-entry-id'), '03-02');
    assert.ok(await drawer(page).evaluate(node => node.scrollTop < 2), 'Next entry starts at the beginning');
    await page.goto(`${base}?chapter=03&item=03-01&lang=zh`);
    await ready(page);
    assert.ok(await drawer(page).evaluate(node => node.scrollTop < 2), 'An explicit entry opens at the beginning');
    await scrollToSource(page);
    const shared = await context.newPage();
    await shared.goto(page.url());
    await ready(shared);
    assert.ok(await drawer(shared).evaluate(node => node.scrollTop < 2), 'Shared links do not inherit personal scroll position');
    await shared.close();
    await scrollToSource(page);
    await page.goto(`${base}?chapter=01&item=01-02&lang=zh`);
    await ready(page);
    assert.equal(await drawer(page).getAttribute('data-entry-id'), '01-02', 'Explicit links take priority over the saved entry');
    assert.ok(await drawer(page).evaluate(node => node.scrollTop < 2));
    await page.goto(`${base}?chapter=03&item=03-01&lang=zh`);
    await scrollToSource(page);
    await page.goto(`${base}?lang=zh`);
    await page.setViewportSize({ width: 320, height: 700 });
    await continueReading(page);
    assert.ok(await drawer(page).evaluate(node => node.scrollWidth <= node.clientWidth + 1));
    const sourceBounds = await drawer(page).locator('[data-reading-anchor="source"]').boundingBox();
    assert.ok(sourceBounds.y >= 0 && sourceBounds.y < 700, 'Source section remains visible on the narrower screen');
    await scrollToSource(page);
    const savedTop = await drawer(page).evaluate(node => node.scrollTop);
    await page.goto(`${base}?lang=zh`);
    let release;
    const held = new Promise(resolve => { release = resolve; });
    await page.route(`**/${art.split('/').at(-1)}`, async route => { await held; await route.continue(); });
    await page.locator('.resume-reading').click();
    await drawer(page).waitFor();
    await page.waitForTimeout(250);
    assert.equal(await drawer(page).getAttribute('data-reading-restoring'), 'true', 'Restoration waits for the illustration layout');
    release();
    await ready(page, true);
    assert.ok(Math.abs(await drawer(page).evaluate(node => node.scrollTop) - savedTop) <= 3);
    await page.unroute(`**/${art.split('/').at(-1)}`);
    await page.locator('.drawer-close').click();
    await continueReading(page);
    assert.equal(await drawer(page).getByRole('button', { name: '标为已读', exact: true }).getAttribute('aria-pressed'), 'false', 'Continue does not mark an entry as read');
    assert.deepEqual(errors, []);
    await context.close();
    console.log(`PASS ${name}: continue, reload, immediate page-hide save, chapter/language, expanded original, explicit/shared links, narrow screen and delayed artwork`);

    const broken = await browser.newContext({ reducedMotion: 'reduce' });
    await broken.addInitScript(() => {
      Storage.prototype.getItem = () => { throw new DOMException('Disabled', 'SecurityError'); };
      Storage.prototype.setItem = () => { throw new DOMException('Disabled', 'SecurityError'); };
    });
    const fallback = await broken.newPage();
    await fallback.goto(`${base}?chapter=03&item=03-01&lang=zh`);
    const fallbackTop = await scrollToSource(fallback);
    await drawer(fallback).getByText('阅读位置暂不能保存，关闭页面后将失效。', { exact: true }).waitFor();
    await fallback.locator('.drawer-close').click();
    await continueReading(fallback);
    assert.ok(Math.abs(await drawer(fallback).evaluate(node => node.scrollTop) - fallbackTop) <= 3, 'Unavailable storage retains in-page reading progress');
    await broken.close();
    for (const value of ['{bad json', JSON.stringify({ version: 1, id: '03-01', chapter: '07', position: { anchor: 'source', fraction: .5 } })]) {
      const invalid = await browser.newPage();
      await invalid.addInitScript(({ key, value }) => localStorage.setItem(key, value), { key, value });
      await invalid.goto(`${base}?lang=zh`);
      assert.equal(await invalid.locator('.resume-reading').count(), 0, 'Invalid saved records are ignored');
      await invalid.close();
    }
    console.log(`PASS ${name}: unavailable storage, malformed data and invalid chapter references`);
  } finally { await browser.close(); }
}
