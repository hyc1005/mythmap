import { openBestiaryFilters } from './ui-controls.mjs';
import assert from 'node:assert/strict';
import { mkdir } from 'node:fs/promises';
import { chromium, firefox, webkit } from 'playwright';

const base = process.env.ATLAS_URL;
if (!base) throw new Error('Run through with-preview.mjs');
const key = 'shanhai-reading-v1';
const output = new URL('../../output/qa/', import.meta.url);
await mkdir(output, { recursive: true });
const filename = name => new URL(name, output).pathname.replace(/^\/([A-Za-z]:)/, '$1');
const detail = page => page.locator('.detail-drawer');
const entry = async (page, id) => {
  await page.locator(`.detail-drawer[data-entry-id="${id}"]`).waitFor();
};
async function entries(page) {
  await page.locator('.mobile-explore-nav button').last().click();
}
async function chapter(page, index) {
  await page.locator('.mobile-explore-nav button').first().click();
  await page.locator('.timeline-steps button').nth(index).click();
}

for (const name of (process.env.ATLAS_BROWSERS || 'chromium,webkit').split(',')) {
  const browser = await ({ chromium, firefox, webkit }[name]).launch();
  try {
    const context = await browser.newContext({ viewport: { width: 390, height: 844 }, reducedMotion: 'reduce' });
    const page = await context.newPage();
    const errors = [];
    context.on('page', child => child.on('pageerror', error => errors.push(error.message)));
    page.on('pageerror', error => errors.push(error.message));
    await page.goto(`${base}?chapter=03&lang=zh`);
    await page.getByLabel('选择地图故事动画').selectOption('03-05');
    await page.locator('.kuafu-journey[data-status="reduced"]').waitFor();
    await page.getByRole('button', { name: '下一幕', exact: true }).click();
    await page.waitForFunction(() => Number(document.querySelector('.kuafu-journey')?.dataset.elapsed) > 0);
    const elapsed = await page.locator('.kuafu-journey').getAttribute('data-elapsed');
    await page.waitForTimeout(150);
    const camera = await page.locator('.myth-map-canvas').getAttribute('data-view');
    await entries(page);
    await page.locator('.explore-sheet [data-entry-id="03-01"]').click();
    await entry(page, '03-01');
    assert.ok(await detail(page).evaluate(node => {
      const quote = node.querySelector('[data-reading-anchor="quote"]');
      return ['.detail-entry-nav', '.detail-reading-actions', '.reading-storage-note', '.drawer-art', '.detail-play-story'].every(selector => {
        const secondary = node.querySelector(selector);
        return !secondary || Boolean(quote.compareDocumentPosition(secondary) & Node.DOCUMENT_POSITION_FOLLOWING);
      });
    }), 'Original text precedes secondary actions and artwork');
    assert.equal(await detail(page).getByRole('button', { name: '标为已读', exact: true }).getAttribute('aria-pressed'), 'false', 'Opening is not reading');
    await detail(page).getByRole('button', { name: '标为已读', exact: true }).click();
    await detail(page).getByRole('button', { name: '收藏条目', exact: true }).click();
    await detail(page).evaluate(node => { node.scrollTop = node.scrollHeight; });
    await detail(page).getByRole('button', { name: '下一条', exact: true }).click();
    await entry(page, '03-02');
    assert.ok(await detail(page).evaluate(node => node.scrollTop < 2), 'Next entry starts at the top');
    assert.equal(await detail(page).getByRole('button', { name: '下一条', exact: true }).evaluate(node => node === document.activeElement), true, 'Keyboard focus stays on navigation');
    await detail(page).getByRole('button', { name: '收藏条目', exact: true }).click();
    await detail(page).getByRole('button', { name: '上一条', exact: true }).click();
    await entry(page, '03-01');
    assert.equal(await detail(page).getByRole('button', { name: '已读 · 撤销', exact: true }).getAttribute('aria-pressed'), 'true');
    await page.locator('.drawer-close').click();
    assert.equal(await page.locator('.world-layout').getAttribute('data-chapter'), '03');
    assert.equal(await page.locator('.kuafu-journey').getAttribute('data-elapsed'), elapsed, 'Entry navigation preserves story progress');
    assert.equal(await page.locator('.myth-map-canvas').getAttribute('data-view'), camera, 'Entry navigation preserves the map camera');
    await page.waitForFunction(() => document.activeElement === document.querySelector('.mobile-explore-nav button:last-child'));
    await entries(page);
    assert.match(await page.locator('.explore-sheet [data-entry-id="03-01"] .reading-marks').textContent(), /已读.*已收藏/);
    await page.keyboard.press('Escape');
    await chapter(page, 7);
    await entries(page);
    await page.locator('.explore-sheet .reading-collection summary').click();
    await page.locator('.explore-sheet [data-collection-id="03-01"]').click();
    await entry(page, '03-01');
    assert.equal(await page.locator('.world-layout').getAttribute('data-chapter'), '07', 'Reading favorites keeps the underlying chapter');
    assert.equal(new URL(page.url()).searchParams.get('chapter'), '03', 'Shared stories use their source chapter');
    const sharedUrl = page.url();
    assert.deepEqual([...new URL(sharedUrl).searchParams.keys()].sort(), ['chapter', 'item', 'lang']);
    await detail(page).getByRole('button', { name: '下一条', exact: true }).click();
    await entry(page, '03-02');
    assert.equal(await page.locator('.detail-entry-position').textContent(), '2 / 2', 'Favorite navigation follows the saved list');
    await detail(page).getByRole('button', { name: '已收藏 · 取消', exact: true }).click();
    await page.locator('.drawer-close').click();
    await page.getByRole('button', { name: 'EN', exact: true }).click();
    await page.goto(sharedUrl.replace('lang=zh', 'lang=en'));
    await entry(page, '03-01');
    await detail(page).getByRole('button', { name: 'Read · undo', exact: true }).waitFor();
    await detail(page).getByRole('button', { name: 'Saved · remove', exact: true }).waitFor();
    await detail(page).getByRole('button', { name: 'Read · undo', exact: true }).click();
    await detail(page).getByRole('button', { name: 'Mark as read', exact: true }).waitFor();
    await page.reload();
    await detail(page).getByRole('button', { name: 'Mark as read', exact: true }).waitFor();
    await detail(page).getByRole('button', { name: 'Saved · remove', exact: true }).waitFor();

    const other = await context.newPage();
    await other.goto(sharedUrl);
    await entry(other, '03-01');
    await detail(other).getByRole('button', { name: '标为已读', exact: true }).click();
    await detail(page).getByRole('button', { name: 'Read · undo', exact: true }).waitFor();
    await other.close();
    await page.locator('.drawer-close').click();
    await page.getByRole('button', { name: '中文', exact: true }).click();
    await page.getByLabel('搜索异兽', { exact: true }).fill('穷奇');
    assert.equal(await page.locator('.beast-card').count(), 1, 'Same-name accounts share one primary card');
    const primaryId = await page.locator('.beast-card').first().getAttribute('data-beast-id');
    await page.locator('.beast-card').first().click();
    const ids = await detail(page).locator('.detail-namesakes option').evaluateAll(nodes => nodes.map(node => node.value));
    assert.equal(ids.length, 2, 'Both independent accounts remain available');
    assert.equal(ids[0], primaryId);
    await entry(page, ids[0]);
    assert.equal(await page.locator('.detail-entry-position').textContent(), '1 / 2');
    await detail(page).getByRole('button', { name: '标为已读', exact: true }).click();
    await detail(page).getByRole('button', { name: '下一条', exact: true }).click();
    await entry(page, ids[1]);
    await detail(page).getByRole('button', { name: '标为已读', exact: true }).click();
    await detail(page).getByRole('button', { name: '收藏条目', exact: true }).click();
    assert.equal(await detail(page).getByRole('button', { name: '下一条', exact: true }).isDisabled(), true, 'Last filtered entry does not wrap into unrelated entries');
    await page.locator('.drawer-close').click();
    await page.waitForFunction(id => {
      const card = document.querySelector(`.beast-card[data-beast-id="${id}"]`);
      return card === document.activeElement && !card.closest('[inert]');
    }, ids[0]);
    await openBestiaryFilters(page);
    await page.getByLabel('按阅读状态筛选').selectOption('read');
    assert.equal(await page.locator('.beast-card').count(), 1);
    assert.match(await page.locator('.bestiary-count').innerText(), /2 条记载/);
    await page.getByLabel('按阅读状态筛选').selectOption('unread');
    assert.equal(await page.locator('.beast-card').count(), 0);
    await page.getByLabel('按阅读状态筛选').selectOption('favorites');
    assert.equal(await page.locator('.beast-card').count(), 1);
    assert.equal(await page.locator('.beast-card').getAttribute('data-beast-id'), ids[1]);
    await page.getByRole('button', { name: '清除筛选', exact: true }).click();
    assert.equal(await page.getByLabel('按阅读状态筛选').inputValue(), '');
    await page.goto(sharedUrl);
    for (const [width, height] of [[320, 700], [390, 844], [844, 390], [1440, 1000]]) {
      await page.setViewportSize({ width, height });
      for (const lang of ['en', 'zh']) {
        await page.goto(sharedUrl.replace('lang=zh', `lang=${lang}`));
        await entry(page, '03-01');
        await page.evaluate(() => document.fonts.ready);
        assert.ok(await detail(page).evaluate(node => node.scrollWidth <= node.clientWidth + 1), `${name} ${width} ${lang} drawer overflow`);
        assert.ok(await detail(page).locator('.detail-entry-nav button, .detail-reading-actions button').evaluateAll(nodes => nodes.every(node => node.getBoundingClientRect().height >= 44)));
        const controls = detail(page).locator('button:not(:disabled), a[href], summary');
        await controls.first().focus(); await page.keyboard.press('Shift+Tab');
        assert.equal(await controls.last().evaluate(node => node === document.activeElement), true, JSON.stringify(await detail(page).evaluate(node => ({active: document.activeElement?.outerHTML, controls:[...node.querySelectorAll('button:not(:disabled), a[href]')].map(item=>({text:item.textContent,visible:item.checkVisibility()}))}))));
        if (name === 'chromium' && lang === 'zh' && [320, 1440].includes(width)) {
          await detail(page).evaluate(node => { node.scrollTop = 0; });
          await page.waitForTimeout(100);
          await detail(page).screenshot({ path: filename(`reading-${width}x${height}.png`) });
        }
      }
    }
    await page.goto(`${base}?chapter=03&lang=zh`);
    await page.getByRole('button', { name: '地图全屏', exact: true }).click();
    await page.locator('.is-map-fullscreen .map-entry-list summary').first().click();
    await page.locator('.is-map-fullscreen [data-entry-id="03-01"]').click();
    await entry(page, '03-01');
    await detail(page).getByRole('button', { name: '下一条', exact: true }).click();
    await entry(page, '03-02');
    await page.locator('.drawer-close').click();
    assert.equal(await page.locator('.is-map-fullscreen').count(), 1, 'Navigation retains fullscreen');
    await page.getByRole('button', { name: '退出地图全屏', exact: true }).click();
    await page.goto(`${base}?chapter=03&item=03-01&lang=zh`);
    await entry(page, '03-01');
    await detail(page).evaluate(node => { node.scrollTop = node.scrollHeight; });
    const navBounds = await page.locator('.detail-entry-nav').boundingBox();
    assert.ok(navBounds.y >= 0 && navBounds.y + navBounds.height <= 1000, 'Long-form navigation remains on screen');
    await detail(page).getByRole('button', { name: '读完，下一条 →', exact: true }).click();
    await entry(page, '03-02');
    const progress = JSON.parse(await page.evaluate(key => localStorage.getItem(key), key));
    assert.ok(progress.read.includes('03-01'));
    await page.goto(`${base}?chapter=07&item=07-04&lang=zh`);
    await entry(page, '07-04');
    await detail(page).getByRole('button', { name: '读完，关闭', exact: true }).click();
    await detail(page).waitFor({ state: 'detached' });
    assert.ok(JSON.parse(await page.evaluate(key => localStorage.getItem(key), key)).read.includes('07-04'));
    const stored = JSON.parse(await page.evaluate(key => localStorage.getItem(key), key));
    assert.ok(stored.read.includes(ids[0]) && stored.favorites.includes(ids[1]));
    assert.ok(!stored.favorites.includes('03-02'), 'Removal persists');
    assert.deepEqual(errors, []);
    await context.close();
    console.log(`PASS ${name}: explicit read/save, persistence, undo, cross-tab updates, filtered navigation, shared favorites, focus, fullscreen and 8 bilingual layouts`);

    const blocked = await browser.newContext({ reducedMotion: 'reduce' });
    await blocked.addInitScript(() => {
      Storage.prototype.getItem = () => { throw new DOMException('Storage disabled', 'SecurityError'); };
      Storage.prototype.setItem = () => { throw new DOMException('Storage disabled', 'SecurityError'); };
    });
    const fallback = await blocked.newPage();
    await fallback.goto(sharedUrl);
    await detail(fallback).getByRole('button', { name: '标为已读', exact: true }).click();
    await detail(fallback).getByRole('button', { name: '收藏条目', exact: true }).click();
    await detail(fallback).getByText('浏览器暂不能保存，标记仅在当前页面有效。', { exact: true }).waitFor();
    await detail(fallback).getByRole('button', { name: '已读 · 撤销', exact: true }).waitFor();
    await fallback.reload();
    await detail(fallback).getByRole('button', { name: '标为已读', exact: true }).waitFor();
    await blocked.close();
    const corrupt = await browser.newPage();
    await corrupt.addInitScript(key => localStorage.setItem(key, '{bad json'), key);
    await corrupt.goto(sharedUrl);
    await detail(corrupt).getByRole('button', { name: '标为已读', exact: true }).click();
    assert.deepEqual(JSON.parse(await corrupt.evaluate(key => localStorage.getItem(key), key)).read, ['03-01']);
    await corrupt.close();
    console.log(`PASS ${name}: unavailable and corrupt storage recover without breaking details`);
  } finally { await browser.close(); }
}
