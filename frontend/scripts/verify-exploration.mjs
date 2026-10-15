import assert from 'node:assert/strict';
import { mkdir, readFile } from 'node:fs/promises';
import { chromium } from 'playwright';

const base = (process.env.ATLAS_URL || 'http://127.0.0.1:5173/').replace(/\/+$/, '') + '/';
const output = new URL('../../output/qa/', import.meta.url);
await mkdir(output, { recursive: true });
const browser = await chromium.launch();
const errors = [];
const filename = name => new URL(name, output).pathname.replace(/^\/([A-Za-z]:)/, '$1');
async function tools(page) {
  const panel = page.locator('.map-tools');
  if (await panel.getAttribute('open') === null) await panel.locator('summary').click();
}
async function fits(page) {
  const bad = await page.evaluate(() => [...document.querySelectorAll('.map-overlay-controls button, .map-overlay-controls select, .map-fullscreen, .journey-actions button')]
    .filter(element => element.checkVisibility()).filter(element => {
      const rect = element.getBoundingClientRect();
      const map = element.closest('.myth-map-wrap').getBoundingClientRect();
      return rect.left < map.left - 1 || rect.right > map.right + 1 || rect.top < map.top - 1 || rect.bottom > map.bottom + 1;
    }).map(element => ({ text: element.textContent, bounds: element.getBoundingClientRect().toJSON(), frame: element.closest('.myth-map-wrap').getBoundingClientRect().toJSON(), viewport: innerWidth })));
  assert.deepEqual(bad, [], 'Controls stay inside the map');
  assert.ok(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth), 'No page overflow');
}
try {
  for (const locale of ['zh', 'en']) for (const [width, height] of [[1440, 1000], [390, 844], [320, 700], [844, 390]]) {
    console.log('Checking exploration ' + locale + ' ' + width + 'x' + height);
    const context = await browser.newContext({ viewport: { width, height }, reducedMotion: 'reduce' });
    const page = await context.newPage();
    page.on('pageerror', error => errors.push(error.message));
    await page.goto(`${base}?lang=${locale}&chapter=03&item=03-05`);
    await page.locator('.detail-drawer').waitFor();
    assert.equal(await page.locator('.world-layout').getAttribute('data-chapter'), '03');
    assert.equal(await page.locator('.kuafu-journey').count(), 0, 'Shared location never auto-plays');
    await page.locator('.drawer-close').click();
    await page.evaluate(() => document.fonts.ready);
    assert.deepEqual(await page.locator('.timeline-steps button').evaluateAll(buttons => buttons.filter(button => button.scrollWidth > button.clientWidth + 1).map(button => button.textContent)), [], 'Chapter names fit their timeline buttons');
    const entryBounds = await page.locator('.begin-journey').boundingBox();
    assert.ok(entryBounds.y >= 0 && entryBounds.y + entryBounds.height <= height, 'Journey entry stays in the first viewport');
    if (locale === 'zh') assert.ok(await page.evaluate(() => [...document.fonts].some(font => font.family === 'Shanhai Title' && font.status === 'loaded')), 'Chinese title subset loads');
    assert.equal(new URL(page.url()).searchParams.has('item'), false);
    const mobile = width <= 768;
    if (mobile) await page.locator('.mobile-explore-nav button').last().click();
    const entry = page.locator('.chapter-entries [data-entry-id="03-05"]');
    await entry.focus(); await page.keyboard.press('Enter');
    await page.locator('.detail-drawer').waitFor();
    assert.equal(new URL(page.url()).searchParams.get('item'), '03-05');
    await page.keyboard.press('Escape');
    if (mobile) await page.waitForFunction(() => document.activeElement === document.querySelector('.mobile-explore-nav button:last-child'));
    else {
      await page.waitForFunction(() => document.activeElement?.dataset.entryId === '03-05');
      assert.ok(await entry.evaluate(element => document.activeElement === element), 'Closing detail restores keyboard focus');
    }
    await tools(page);
    await page.getByLabel(locale === 'zh' ? '异兽谱' : 'Bestiary', { exact: true }).check();
    if (mobile) await page.locator('.mobile-explore-nav button').last().click();
    assert.ok(await page.locator('.chapter-entries .map-entry-button').count() > 5, 'Enabled beasts remain in unified entries');
    if (mobile) await page.keyboard.press('Escape');
    await fits(page);
    if (width <= 768 || height <= 480) {
      assert.ok(await page.locator('.map-tools summary').evaluate(element => element.getBoundingClientRect().height >= 44));
      await page.locator('.map-tools summary').click();
    }
    await page.getByLabel(locale === 'zh' ? '选择地图故事动画' : 'Choose a story animation').selectOption('03-05');
    await page.locator('.kuafu-journey[data-status="reduced"]').waitFor();
    await page.getByRole('button', { name: locale === 'zh' ? '下一幕' : 'Next scene', exact: true }).click();
    await page.waitForFunction(() => document.querySelector('.kuafu-journey')?.dataset.phase === 'drink');
    assert.ok(await page.locator('.journey-heading .ink-word').first().evaluate(element => getComputedStyle(element).animationName === 'none'), 'Reduced motion shows complete text immediately');
    await fits(page);
    await page.screenshot({ path: filename(`exploration-${locale}-${width}x${height}.png`), fullPage: true });
    await context.close();
  }

  const page = await browser.newPage({ viewport: { width: 1440, height: 1000 } });
  const exportSource = await readFile(new URL('../src/map-export.js', import.meta.url), 'utf8');
  const requested = [];
  page.on('response', response => requested.push(new URL(response.url()).pathname));
  page.on('pageerror', error => errors.push(error.message));
  await page.goto(`${base}?lang=zh&chapter=00`);
  const composition = await page.evaluate(async source => {
    const { drawMapLayers } = await import('data:text/javascript;base64,' + btoa(source));
    const parent = document.createElement('div'); parent.style.opacity = '.6';
    const layer = document.createElement('canvas'); layer.width = layer.height = 8;
    layer.style.opacity = '.5'; layer.style.filter = 'saturate(.72) sepia(.14)';
    layer.style.transform = 'matrix(1, 0, 0, 1, 2, 3)'; parent.append(layer); document.body.append(parent);
    const ink = layer.getContext('2d'); ink.fillStyle = 'rgb(200, 40, 20)'; ink.fillRect(0, 0, 8, 8);
    const output = document.createElement('canvas'); output.width = output.height = 20;
    const context = output.getContext('2d'); drawMapLayers(context, [layer]);
    const expected = document.createElement('canvas'); expected.width = expected.height = 20;
    const reference = expected.getContext('2d'); reference.globalAlpha = .3;
    reference.filter = getComputedStyle(layer).filter; reference.setTransform(1, 0, 0, 1, 2, 3); reference.drawImage(layer, 0, 0);
    const actualPixel = [...context.getImageData(3, 4, 1, 1).data];
    const expectedPixel = [...reference.getImageData(3, 4, 1, 1).data];
    const restored = context.filter === 'none' && context.globalAlpha === 1;
    context.fillStyle = '#544431'; context.fillRect(12, 12, 1, 1);
    const titlePixel = [...context.getImageData(12, 12, 1, 1).data]; parent.remove();
    return { actualPixel, expectedPixel, restored, titlePixel };
  }, exportSource);
  assert.deepEqual(composition.actualPixel, composition.expectedPixel, 'PNG composition reproduces preview filter, transform and opacity');
  assert.ok(composition.restored);
  assert.deepEqual(composition.titlePixel, [84, 68, 49, 255], 'Caption color is unaffected by the layer filter');
  await page.locator('.exploration-guide').waitFor();
  await page.getByRole('button', { name: '关闭引导', exact: true }).click();
  await page.reload();
  assert.equal(await page.locator('.exploration-guide').count(), 0, 'Guide dismissal persists');
  await page.evaluate(() => {
    document.querySelectorAll('.timeline-steps button')[1].click();
    document.querySelectorAll('.timeline-steps button')[2].click();
    document.querySelectorAll('.timeline-steps button')[4].click();
  });
  assert.equal(await page.locator('.world-layout').getAttribute('data-chapter'), '04');
  await page.waitForTimeout(400);
  assert.equal(await page.locator('.chapter-transition-veil.is-visible').count(), 0);
  assert.equal(await page.locator('.chapter-rail h2 .ink-word').first().evaluate(element => getComputedStyle(element).animationName), 'ink-title');
  await page.waitForTimeout(350);
  assert.equal(await page.locator('.chapter-rail h2 .ink-word').first().evaluate(element => getComputedStyle(element).animationName), 'none', 'Title motion finishes once');
  await page.getByRole('button', { name: 'EN', exact: true }).click();
  assert.equal(await page.locator('.chapter-rail h2 .ink-word').first().evaluate(element => getComputedStyle(element).animationName), 'none', 'Language changes do not replay chapter motion');
  await page.getByRole('button', { name: '中文', exact: true }).click();
  assert.equal(await page.locator('.chapter-rail h2 .ink-word').first().evaluate(element => getComputedStyle(element).animationName), 'none');

  await page.goto(`${base}?chapter=invalid&item=03-05&lang=en`);
  assert.equal(await page.locator('.world-layout').getAttribute('data-chapter'), '00');
  assert.equal(await page.locator('.detail-drawer').count(), 0);
  await page.goto(`${base}?chapter=03&lang=zh`);
  await page.getByRole('button', { name: '复制探索链接', exact: true }).click();
  await page.waitForFunction(() => document.querySelector('.toolbar-share-status')?.textContent || document.querySelector('.toolbar-share-status input'));

  await page.locator('.bestiary-toggle').click();
  await page.route('**/beast-shengsheng.webp', route => route.abort());
  await page.locator('.beast-card[data-beast-id="beast-shengsheng"]').click();
  await page.locator('.detail-drawer .artwork-fallback').waitFor();
  assert.ok(await page.locator('.detail-description').textContent(), 'Image failure keeps original text readable');
  await page.unroute('**/beast-shengsheng.webp');
  await page.getByRole('button', { name: '重试插画', exact: true }).click();
  await page.locator('.detail-drawer img').waitFor();
  await page.getByRole('button', { name: '在地图中查看', exact: true }).click();
  await page.locator('.ink-hover-card').waitFor();
  assert.ok(await page.getByLabel('异兽谱', { exact: true }).isChecked());

  await page.evaluate(() => {
    window.originalToDataURL = HTMLCanvasElement.prototype.toDataURL;
    HTMLCanvasElement.prototype.toDataURL = () => { throw new Error('Injected export failure'); };
  });
  await page.getByRole('button', { name: '存为本章 PNG', exact: true }).click();
  await page.getByText('导出失败，请重试', { exact: true }).waitFor();
  await page.evaluate(() => { HTMLCanvasElement.prototype.toDataURL = window.originalToDataURL; });
  const download = page.waitForEvent('download');
  await page.getByRole('button', { name: '存为本章 PNG', exact: true }).click();
  assert.ok((await download).suggestedFilename().endsWith('.png'));
  await page.getByText('PNG 已生成', { exact: true }).waitFor();

  await page.goto(`${base}?chapter=00&lang=zh`);
  await page.locator('.beast-card[data-beast-id="beast-shengsheng"]').click();
  assert.equal(new URL(page.url()).searchParams.get('chapter'), '03', 'Sharing a future-chapter beast uses its related chapter');
  const saved = page.url();
  await page.goto(saved);
  await page.locator('.detail-drawer').waitFor();
  assert.equal(new URL(page.url()).searchParams.get('item'), 'beast-shengsheng');
  assert.equal(await page.locator('.world-layout').getAttribute('data-chapter'), '03');

  await page.goto(`${base}?chapter=03&lang=zh`);
  await page.getByRole('button', { name: '连续游历', exact: true }).click();
  assert.equal(await page.locator('.world-layout').getAttribute('data-timeline-playing'), 'true');
  await page.locator('.kuafu-journey, .story-animation').waitFor();
  assert.ok(requested.some(path => path.endsWith('/optimized/myth-icons/scenes/pangu-opening.webp')), 'The publishing version is requested');
  assert.ok(!requested.some(path => /\/data\/atlas\/myth-icons\/scenes\/pangu-/.test(path)), 'Original large prologue assets are not requested');
  await page.close();
  const historyPage = await browser.newPage();
  historyPage.on('pageerror', error => errors.push(error.message));
  await historyPage.goto(`${base}?lang=zh&chapter=01`);
  await historyPage.getByRole('button', { name: 'EN', exact: true }).click();
  await historyPage.locator('.myth-header a[href="#creatures"]').click();
  await historyPage.getByRole('button', { name: '中文', exact: true }).click();
  await historyPage.evaluate(() => {
    const url = new URL(location.href); url.searchParams.set('chapter', '03'); url.searchParams.set('item', '03-05'); url.hash = 'world';
    history.pushState(null, '', url); dispatchEvent(new PopStateEvent('popstate'));
  });
  await historyPage.locator('.detail-drawer').waitFor();
  await historyPage.goBack();
  await historyPage.waitForFunction(() => document.querySelector('.world-layout')?.dataset.chapter === '01' && !document.querySelector('.detail-drawer'));
  await historyPage.goBack();
  await historyPage.waitForFunction(() => document.documentElement.lang === 'en');
  assert.equal(new URL(historyPage.url()).searchParams.get('lang'), 'en');
  assert.equal(await historyPage.locator('.language-switch [aria-pressed="true"]').textContent(), 'EN');
  await historyPage.goForward();
  await historyPage.waitForFunction(() => document.documentElement.lang === 'zh-CN');
  await historyPage.goForward();
  await historyPage.waitForFunction(() => document.querySelector('.world-layout')?.dataset.chapter === '03' && document.querySelector('.detail-drawer'));
  await historyPage.reload();
  await historyPage.locator('.detail-drawer').waitFor();
  assert.equal(await historyPage.locator('.kuafu-journey').count(), 0, 'History refresh does not auto-play');
  assert.equal(new URL(historyPage.url()).searchParams.get('lang'), 'zh');
  await historyPage.close();
  assert.deepEqual(errors, []);
  console.log('PASS: 8 bilingual viewports, first-screen entry/title font, share and history restoration, keyboard map entries, reduced motion, onboarding, image retry, PNG color and failure/retry.');
} finally {
  await browser.close();
}
