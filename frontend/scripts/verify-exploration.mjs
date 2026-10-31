import assert from 'node:assert/strict';
import { browserDiagnostics } from './browser-diagnostics.mjs';
import { mkdir, readFile } from 'node:fs/promises';
import { chromium, webkit } from 'playwright';
import { storySummary } from '../src/story-summaries.js';

const base = (process.env.ATLAS_URL || 'http://127.0.0.1:5173/').replace(/\/+$/, '') + '/';
const output = new URL('../../output/qa/', import.meta.url);
await mkdir(output, { recursive: true });
const browserName = process.env.ATLAS_BROWSER || 'chromium';
const browser = await ({ chromium, webkit }[browserName]).launch();
const errors = [];
const filename = name => new URL(name, output).pathname.replace(/^\/([A-Za-z]:)/, '$1');
const toolDiagnostics = new WeakMap();
async function tools(page) {
  const panel = page.locator('.map-tools');
  if (await panel.getAttribute('open') !== null) return;
  const context = page.context();
  if (!toolDiagnostics.has(context)) toolDiagnostics.set(context, browserDiagnostics(context, `candidate-tools-${browserName}-${page.viewportSize().width}`));
  await page.evaluate(() => {
    window.qaToolRects = [];
    const sample = () => { const n = document.querySelector('.map-tools summary'); if (!n) return; window.qaToolRects.push({ rect: n.getBoundingClientRect().toJSON(), scrollY, inert: Boolean(n.closest('[inert]')) }); if (window.qaToolRects.length < 60) requestAnimationFrame(sample); };
    requestAnimationFrame(sample);
  });
  try { await panel.locator('summary').click(); }
  catch (error) {
    try {
      console.error('TOOLS_STATE '+JSON.stringify(await page.evaluate(() => ({ url: location.pathname+location.search.replace(/tk=[^&]+/g,'tk=[redacted]'), open: document.querySelector('.map-tools')?.open, samples: window.qaToolRects, focusTag: document.activeElement?.tagName }))));
      await toolDiagnostics.get(context)(error);
    } catch (captureError) { console.error('Failure capture failed:', captureError.message); }
    throw error;
  }
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
  assert.ok(await page.locator('.map-reading-hint').evaluateAll(nodes => nodes.every(node => node.getBoundingClientRect().right <= innerWidth)), 'Visible seal hints remain readable on narrow screens');
}
const settle = page => page.evaluate(() => new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve))));
const stableCamera = page => page.evaluate(() => new Promise((resolve, reject) => {
  let previous = null, stable = 0, frames = 0;
  const tick = () => {
    const canvas = document.querySelector('.myth-map-canvas');
    const view = JSON.parse(canvas.dataset.view), box = canvas.getBoundingClientRect();
    const aligned = Math.abs(view.size[0] - box.width) < 1 && Math.abs(view.size[1] - box.height) < 1;
    stable = aligned && canvas.dataset.view === previous ? stable + 1 : 0;
    previous = canvas.dataset.view;
    if (stable >= 3) return resolve(previous);
    if (++frames > 600) return reject(new Error(`Map camera never settled: ${previous}`));
    requestAnimationFrame(tick);
  };
  requestAnimationFrame(tick);
}));
async function sealPoint(page, name, active) {
  return page.locator('.myth-map-canvas').evaluate((node, { name, active }) => {
    const view = JSON.parse(node.dataset.view), box = node.getBoundingClientRect();
    const context = document.createElement('canvas').getContext('2d');
    context.font = `${active ? 'bold 14px' : '13px'} ${document.documentElement.lang === 'en' ? '"Source Sans 3 Variable", Arial, sans-serif' : '"Noto Serif SC", SimSun, serif'}`;
    return { x: box.left + view.size[0] / 2 + (900 - view.center[0]) / view.resolution - context.measureText(name).width / 2 - 9,
      y: box.top + view.size[1] / 2 - (245 - view.center[1]) / view.resolution - 20 };
  }, { name, active });
}
async function sealInk(page, point) {
  return page.evaluate(({ x, y }) => [...document.querySelectorAll('.myth-map-canvas .ol-layer canvas')].reduce((sum, node) => {
    const box = node.getBoundingClientRect(), ratio = node.width / box.width;
    const left = Math.floor((x - box.left - 7) * ratio), top = Math.floor((y - box.top - 7) * ratio), size = Math.ceil(14 * ratio);
    if (left < 0 || top < 0 || left + size > node.width || top + size > node.height) return sum;
    const pixels = node.getContext('2d').getImageData(left, top, size, size).data;
    for (let i = 0; i < pixels.length; i += 4) if (pixels[i] > pixels[i + 1] * 1.5 && pixels[i] > pixels[i + 2] * 1.5 && pixels[i + 3] > 50) sum++;
    return sum;
  }, 0), point);
}
try {
  for (const locale of ['zh', 'en']) for (const width of [1440, 390, 320, 844]) {
    console.log(`Checking reading seals ${locale} ${width}: ${width === 390 ? 'touch' : 'mouse'}`);
    const context = await browser.newContext({ viewport: { width, height: width === 844 ? 390 : 1000 }, reducedMotion: 'reduce', hasTouch: width <= 390 });
    const page = await context.newPage();
    page.on('pageerror', error => errors.push(error.message));
    await page.goto(`${base}?chapter=03&lang=${locale}&item=03-04`);
    await page.locator('.detail-drawer').waitFor();
    const selectedName = await page.locator('.detail-drawer h2').textContent();
    assert.equal(await page.getByRole('button', { name: /复制探索链接|Copy exploration link/ }).count(), 0, 'Expanded original has no copy-link action');
    assert.equal(await page.locator('.detail-drawer input[readonly]').count(), 0, 'Removed sharing has no fallback link field');
    await page.getByRole('button', { name: locale === 'zh' ? '在地图中查看' : 'View on the map', exact: true }).click();
    await page.mouse.move(0, 0);
    await page.waitForFunction(name => document.querySelector('.ink-hover-card b')?.textContent === name, selectedName);
    await page.locator('.ink-hover-card').waitFor();
    await page.evaluate(() => document.fonts.ready);
    await page.waitForLoadState('networkidle');
    await page.locator('.myth-map-canvas').scrollIntoViewIfNeeded();
    const name = await page.locator('.ink-hover-card b').textContent();
    const box = await page.locator('.myth-map-canvas').boundingBox();
    if (width === 390) await page.touchscreen.tap(box.x + box.width - 20, box.y + 20);
    else await page.mouse.click(box.x + box.width - 20, box.y + 20);
    await page.locator('.ink-hover-card').waitFor({ state: 'hidden' }); await settle(page);
    const view = await stableCamera(page);
    let idlePoint, idleInk;
    const paintDeadline = Date.now() + 5000;
    do {
      await settle(page);
      idlePoint = await sealPoint(page, name, false);
      idleInk = await sealInk(page, idlePoint);
    } while (idleInk <= 4 && Date.now() < paintDeadline);
    assert.ok(idleInk > 4, 'A red seal is actually painted beside the name');
    if (width === 390) await page.touchscreen.tap(idlePoint.x, idlePoint.y);
    else await page.mouse.move(idlePoint.x, idlePoint.y);
    await page.locator('.ink-hover-card').waitFor(); await settle(page);
    assert.equal(await page.locator('.preview-body p').textContent(), storySummary('03-04', locale), 'Preview starts with the plain-language story');
    assert.equal(await page.locator('.ink-hover-card>.content-origin').getAttribute('data-origin'), 'shanhaijing');
    await page.locator('.preview-art').evaluate(image => image.decode());
    const previewBounds = await page.locator('.ink-hover-card').boundingBox();
    const mapBounds = await page.locator('.map-surface').boundingBox();
    assert.ok(previewBounds.x >= mapBounds.x && previewBounds.y >= mapBounds.y && previewBounds.x + previewBounds.width <= mapBounds.x + mapBounds.width + 1 && previewBounds.y + previewBounds.height <= mapBounds.y + mapBounds.height + 1, 'The whole preview fits inside the map');
    assert.ok(await page.locator('.ink-hover-card button, .preview-art').evaluateAll(nodes => nodes.every(node => {
      const r = node.getBoundingClientRect(), c = node.closest('.ink-hover-card').getBoundingClientRect();
      return r.top >= c.top && r.bottom <= c.bottom && r.left >= c.left && r.right <= c.right && (node.tagName !== 'BUTTON' || r.height >= 44 && r.width >= 44);
    })), 'Artwork stays inside the card and actions retain 44px targets');
    assert.equal(await page.locator('.ink-hover-card b').textContent(), name, 'The seal selects its own entry');
    assert.equal(await stableCamera(page), view, 'Reading feedback does not move the map');
    assert.ok(await sealInk(page, await sealPoint(page, name, true)) > idleInk, 'Hover and touch gently strengthen the seal');
    await page.locator('.map-reading-hint').waitFor();
    assert.ok(await page.locator('.map-reading-hint').evaluate(node => node.getBoundingClientRect().right <= innerWidth), 'The idle map shows its complete reading hint');
    await page.locator('.myth-map-wrap').screenshot({ path: filename(`reading-seal-active-${locale}-${width}.png`) });
    await page.locator('.preview-close').click();
    await page.locator('.ink-hover-card').waitFor({ state: 'hidden' });
    assert.ok(await page.locator('.myth-map-wrap').evaluate(node => node === document.activeElement), 'Closing a preview returns focus to the map');
    assert.equal(await stableCamera(page), view, 'Closing the preview preserves the camera');
    await page.locator('.myth-map-canvas').scrollIntoViewIfNeeded();
    const reopenPoint = await sealPoint(page, name, false);
    await page.mouse.click(reopenPoint.x, reopenPoint.y);
    await page.locator('.ink-hover-card').waitFor();
    await page.waitForTimeout(350); // OpenLayers confirms a single click after its double-click window.
    await page.evaluate(() => { Element.prototype.requestFullscreen = undefined; });
    await page.locator('.map-fullscreen').click();
    await page.locator('.is-fallback-fullscreen .ink-hover-card').waitFor();
    await settle(page);
    assert.ok(await page.locator('.fullscreen-dock .ink-hover-card button').evaluateAll(nodes => nodes.every(node => {
      const r = node.getBoundingClientRect(), slot = node.closest('.fullscreen-preview-slot').getBoundingClientRect();
      return r.height >= 44 && r.top >= slot.top && r.bottom <= slot.bottom + 1 && r.right <= slot.right && document.elementFromPoint(r.x + r.width / 2, r.y + r.height / 2) === node;
    })), 'Fullscreen preview actions are fully visible and directly clickable');
    const fullscreenView = await stableCamera(page);
    await page.locator('.myth-map-wrap').screenshot({ path: filename(`preview-fullscreen-${locale}-${width}.png`) });
    await page.locator('.preview-close').click();
    await settle(page);
    assert.equal(await stableCamera(page), fullscreenView, 'Dismissing the fullscreen preview keeps the canvas stable');
    if (width === 390) {
      await page.getByLabel(locale === 'zh' ? '选择地图故事动画' : 'Choose a story animation').selectOption('03-05');
      await page.locator('.kuafu-journey[data-status="reduced"]').waitFor();
      await page.locator('.myth-map-canvas').hover();
      await page.mouse.wheel(0, 2200);
      await stableCamera(page);
      await settle(page);
      const storyPoint = await sealPoint(page, name, false);
      await page.mouse.click(storyPoint.x, storyPoint.y);
      await page.locator('.ink-hover-card').waitFor();
      await page.waitForTimeout(350);
      assert.ok(await page.locator('.fullscreen-dock .ink-hover-card button').evaluateAll(nodes => nodes.every(node => {
        const r = node.getBoundingClientRect(), slot = node.closest('.fullscreen-preview-slot').getBoundingClientRect();
        return r.height >= 44 && r.top >= slot.top && r.bottom <= slot.bottom + 1 && r.right <= slot.right && document.elementFromPoint(r.x + r.width / 2, r.y + r.height / 2) === node;
      })), 'Preview actions remain available alongside a paused story');
      assert.equal(await page.locator('.story-view-controls').count(), 0);
      assert.ok(await page.locator('.restore-view').isVisible(), 'Preview does not hide the toolbar restore entry');
      await page.locator('.preview-close').click();
      await page.locator('.ink-hover-card').waitFor({ state: 'hidden' });
      await page.locator('.restore-view').waitFor({ state: 'visible' });
      assert.ok(await page.locator('.restore-view').isVisible(), 'Closing the preview keeps restore available');
    }
    await page.locator('.map-fullscreen').click();
    await context.close();
  }
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
    const mapBounds = await page.locator('.map-surface').boundingBox();
    assert.ok(entryBounds.y >= mapBounds.y + mapBounds.height - 1, 'Journey entry belongs below the map');
    assert.equal(await page.locator('.chapter-rail .begin-journey, .chapter-rail .resume-reading').count(), 0);
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
    assert.ok(await page.locator('.map-tools summary').evaluate(element => element.getBoundingClientRect().height >= 44));
    if (await page.locator('.map-tools').evaluate(node => node.open)) await page.locator('.map-tools summary').click();
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
    const context = output.getContext('2d'), supportsFilter = 'filter' in context;
    drawMapLayers(context, [layer]);
    const expected = document.createElement('canvas'); expected.width = expected.height = 20;
    const reference = expected.getContext('2d'); reference.globalAlpha = .3;
    reference.filter = getComputedStyle(layer).filter; reference.setTransform(1, 0, 0, 1, 2, 3); reference.drawImage(layer, 0, 0);
    const actualPixel = [...context.getImageData(3, 4, 1, 1).data];
    const expectedPixel = [...reference.getImageData(3, 4, 1, 1).data];
    const restored = (!supportsFilter || context.filter === 'none') && context.globalAlpha === 1;
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
  await page.locator('.timeline-steps button').nth(4).waitFor();
  assert.equal(await page.locator('.exploration-guide').count(), 0, 'Guide dismissal persists');
  await page.evaluate(() => {
    document.querySelectorAll('.timeline-steps button')[1].click();
    document.querySelectorAll('.timeline-steps button')[2].click();
    document.querySelectorAll('.timeline-steps button')[4].click();
  });
  assert.equal(await page.locator('.world-layout').getAttribute('data-chapter'), '04');
  await page.waitForTimeout(600);
  assert.equal(await page.locator('.chapter-transition-veil.is-visible').count(), 1, 'Chapter title has a readable dwell');
  await page.locator('.chapter-transition-veil.is-visible').waitFor({ state: 'detached' });
  assert.equal(await page.locator('.chapter-transition-veil.is-visible').count(), 0);
  assert.equal(await page.locator('.chapter-rail h2 .ink-word').first().evaluate(element => getComputedStyle(element).animationName), 'none', 'Title motion finishes once');
  await page.getByRole('button', { name: 'EN', exact: true }).click();
  assert.equal(await page.locator('.chapter-rail h2 .ink-word').first().evaluate(element => getComputedStyle(element).animationName), 'none', 'Language changes do not replay chapter motion');
  await page.getByRole('button', { name: '中文', exact: true }).click();
  assert.equal(await page.locator('.chapter-rail h2 .ink-word').first().evaluate(element => getComputedStyle(element).animationName), 'none');

  await page.goto(`${base}?chapter=invalid&item=03-05&lang=en`);
  assert.equal(await page.locator('.world-layout').getAttribute('data-chapter'), '00');
  assert.equal(await page.locator('.detail-drawer').count(), 0);
  await page.goto(`${base}?chapter=03&lang=zh`);
  assert.equal(await page.getByRole('button', { name: '复制探索链接', exact: true }).count(), 0, 'Map sharing control is removed; URL restoration remains supported');

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

  await tools(page);
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
  await page.getByRole('button', { name: '开始游历', exact: true }).click();
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
  console.log(`PASS ${browserName}: painted reading seals, mouse/touch feedback, no copy action, 8 bilingual viewports, history/focus, reduced motion, image retry and PNG export.`);
} finally {
  await browser.close();
}
