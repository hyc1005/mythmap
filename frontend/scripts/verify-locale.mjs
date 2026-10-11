import assert from 'node:assert/strict';
import { mkdir, readFile } from 'node:fs/promises';
import { chromium } from 'playwright';
import { createServer } from 'vite';

const base = process.env.ATLAS_URL || 'http://127.0.0.1:5173';
const world = await readFile(new URL('../public/data/myth-world.json', import.meta.url), 'utf8');
const ssr = await createServer({ server: { middlewareMode: true }, appType: 'custom' });
try {
  const { localize } = await ssr.ssrLoadModule('/src/i18n.jsx');
  const original = JSON.parse(world);
  const translated = localize(original, 'en');
  assert.equal(localize(original, 'zh'), original, 'Chinese source data is preserved');
  for (const group of ['regions', 'places', 'domains', 'relations', 'beasts']) {
    assert.deepEqual(translated[group].map(item => item.id), original[group].map(item => item.id));
    for (const [index, item] of translated[group].entries()) {
      for (const field of ['name', 'label', 'source', 'quote', 'direction', 'place_basis']) {
        assert.ok(!/[\u3400-\u9fff]/.test(item[field] || ''), group + ': English map field ' + field);
      }
      if (original[group][index].quote) assert.equal(item.originalQuote, original[group][index].quote);
    }
  }
} finally {
  await ssr.close();
}
const output = new URL('../../output/qa/', import.meta.url);
await mkdir(output, { recursive: true });
const browser = await chromium.launch({ headless: true });
const errors = [];
const filename = name => new URL(name, output).pathname.replace(/^\/([A-Za-z]:)/, '$1');

async function assertEnglish(page) {
  const untranslated = await page.evaluate(() => [...document.querySelectorAll('main *, .detail-drawer *')]
    .filter(element => !element.children.length && element.getClientRects().length
      && !element.closest('.original-text,.seal,.language-switch,.beast-placeholder')
      && /[\u3400-\u9fff]/.test(element.textContent))
    .map(element => element.textContent));
  assert.deepEqual(untranslated, [], 'English UI and descriptions have no untranslated Chinese');
}

async function assertFits(page) {
  const overflow = await page.evaluate(() => ({
    page: document.documentElement.scrollWidth > window.innerWidth,
    controls: [...document.querySelectorAll('.map-overlay-controls button, .map-overlay-controls select, .map-fullscreen')]
      .filter(element => element.checkVisibility())
      .filter(element => {
        const rect = element.getBoundingClientRect();
        const map = element.closest('.myth-map-wrap').getBoundingClientRect();
        return rect.left < map.left - 1 || rect.right > map.right + 1
          || rect.top < map.top - 1 || rect.bottom > map.bottom + 1;
      }).map(element => element.textContent),
  }));
  assert.equal(overflow.page, false, 'No horizontal page overflow');
  assert.deepEqual(overflow.controls, [], 'Map controls fit within the frame');
}

try {
  for (const [width, height] of [[1440, 1000], [390, 844], [320, 700], [844, 390]]) {
    const context = await browser.newContext({ viewport: { width, height }, reducedMotion: 'reduce' });
    const page = await context.newPage();
    page.on('pageerror', error => errors.push(error.stack || error.message));
    page.on('response', response => {
      if (response.status() >= 400 && !response.url().endsWith('/api/world')) errors.push(response.url());
    });
    await page.route('**/api/world', route => route.fulfill({ contentType: 'application/json', body: world }));
    await page.goto(base + '/?lang=en');
    await page.getByText('Reduced motion enabled', { exact: true }).waitFor();
    await page.evaluate(() => document.fonts.ready);
    assert.deepEqual(await page.evaluate(() => [...document.fonts]
      .filter(font => font.status === 'loaded')
      .map(font => font.family.replaceAll('"', ''))
      .filter(family => ['Lora Variable', 'Source Sans 3 Variable'].includes(family))
      .sort()), ['Lora Variable', 'Source Sans 3 Variable'], 'Both local English fonts load');
    assert.equal(await page.locator('html').getAttribute('lang'), 'en');
    assert.ok((await page.title()).startsWith('Shanhai Atlas'));
    assert.equal(await page.locator('.language-switch button[aria-pressed="true"]').textContent(), 'EN');

    if (width === 1440) {
      const waves = page.locator('.seal .mark-waves');
      await page.mouse.move(800, 900);
      assert.equal(await waves.evaluate(element => getComputedStyle(element).animationName), 'none');
      await page.emulateMedia({ reducedMotion: 'no-preference' });
      await page.locator('.myth-header>a').hover();
      assert.equal(await waves.evaluate(element => getComputedStyle(element).animationName), 'mark-tide');
      const sun = page.locator('.seal .mark-sun');
      const startY = await sun.evaluate(element => new DOMMatrix(getComputedStyle(element).transform).m42);
      const startInk = await waves.evaluate(element => parseFloat(getComputedStyle(element).strokeDashoffset));
      await page.waitForTimeout(1600);
      const risenY = await sun.evaluate(element => new DOMMatrix(getComputedStyle(element).transform).m42);
      const flowingInk = await waves.evaluate(element => parseFloat(getComputedStyle(element).strokeDashoffset));
      assert.ok(startY - risenY > 5, 'Hover visibly raises the sun, rather than only declaring an animation');
      assert.ok(Math.abs(flowingInk - startInk) > .3, 'Hover moves the ink along the sea paths');
      await page.mouse.move(800, 900);
      assert.equal(await waves.evaluate(element => getComputedStyle(element).animationName), 'none');
      await page.locator('.myth-header>a').focus();
      assert.equal(await waves.evaluate(element => getComputedStyle(element).animationName), 'mark-tide');
      await page.emulateMedia({ reducedMotion: 'reduce' });
      assert.equal(await waves.evaluate(element => getComputedStyle(element).animationName), 'none');
      await page.locator('.myth-header>a').blur();
    }

    for (let chapter = 0; chapter < 8; chapter++) {
      await page.locator('.timeline-steps button').nth(chapter).click();
      if (chapter > 0 && await page.locator('.map-animation-choice').count()) {
        await page.getByLabel('Choose a story animation').selectOption('');
      }
      await assertEnglish(page);
      await assertFits(page);
      if (width === 1440) {
        for (const entry of await page.locator('.story-entry').all()) {
          await entry.click();
          await assertEnglish(page);
          await page.locator('.original-text summary').click();
          assert.ok(await page.locator('.original-text blockquote').getAttribute('lang') === 'zh-CN');
          await page.getByRole('button', { name: 'Close', exact: true }).click();
        }
      }
    }

    await page.locator('.bestiary-toggle').click();
    assert.equal(await page.locator('.beast-card').count(), 32);
    await assertEnglish(page);
    if (width === 1440) {
      for (const card of await page.locator('.beast-card').all()) {
        await card.click();
        await assertEnglish(page);
        await page.getByRole('button', { name: 'Close', exact: true }).click();
      }
    }
    await page.getByLabel('Search creatures', { exact: true }).fill('JINGWEI');
    assert.equal(await page.locator('.beast-card').count(), 1);
    await page.getByLabel('Search creatures', { exact: true }).fill('精卫');
    assert.equal(await page.locator('.beast-card').count(), 1);
    await page.locator('.bestiary-toggle').click();
    await page.locator('.timeline-steps button').nth(3).click();
    await page.getByLabel('Choose a story animation').selectOption('');
    await page.locator('.language-switch button').first().click();
    assert.equal(await page.locator('.chapter-rail h2').textContent(), '炎黄');
    await page.locator('.language-switch button').last().click();
    assert.equal(await page.locator('.chapter-rail h2').textContent(), 'Yan & Huang');
    await assertEnglish(page);

    await page.evaluate(() => { Element.prototype.requestFullscreen = undefined; });
    await page.locator('.map-fullscreen').click();
    await page.locator('.is-fallback-fullscreen').waitFor();
    await assertFits(page);
    await page.getByRole('button', { name: 'Next →', exact: true }).click();
    await page.waitForFunction(() => document.querySelector('.chapter-rail h2').textContent === 'Later Sage Kings');
    await assertEnglish(page);
    await page.locator('.map-fullscreen').click();
    await page.locator('.is-map-fullscreen').waitFor({ state: 'detached' });

    await page.locator('.timeline-steps button').nth(3).click();
    await page.getByLabel('Choose a story animation').selectOption('');
    await page.evaluate(() => window.scrollTo(0, 0));
    await page.screenshot({ path: filename('international-' + width + 'x' + height + '.png') });
    await page.goto(base + '/');
    assert.equal(await page.locator('html').getAttribute('lang'), 'en', 'Language preference persists');
    await page.goto(base + '/?lang=zh');
    assert.equal(await page.locator('html').getAttribute('lang'), 'zh-CN', 'URL overrides saved preference');
    await context.close();
    console.log('PASS: bilingual content, search, persistence and layout at ' + width + 'x' + height);
  }
  const motionPage = await browser.newPage({ viewport: { width: 1366, height: 768 } });
  motionPage.on('pageerror', error => errors.push(error.stack || error.message));
  await motionPage.clock.install();
  await motionPage.goto(base + '/?lang=en');
  await motionPage.getByRole('button', { name: 'Pause Pangu prologue', exact: true }).waitFor();
  await motionPage.getByRole('button', { name: 'Pause Pangu prologue', exact: true }).click();
  await assertEnglish(motionPage);
  for (const [chapter, id] of [[1, '01-02'], [2, '02-04'], [3, '03-05'], [3, '03-04'], [4, '04-02'], [5, '05-01']]) {
    await motionPage.locator('.timeline-steps button').nth(chapter).click();
    await motionPage.getByLabel('Choose a story animation').selectOption(id);
    const animation = motionPage.locator('.kuafu-journey');
    await animation.locator('button').first().waitFor();
    await motionPage.waitForFunction(() => document.querySelector('.kuafu-journey')?.dataset.status === 'playing');
    await motionPage.clock.runFor(1500);
    await assertEnglish(motionPage);
    await animation.locator('button').first().click();
    await motionPage.clock.runFor(100);
    const elapsed = await animation.getAttribute('data-elapsed');
    await motionPage.clock.runFor(1000);
    assert.equal(await animation.getAttribute('data-elapsed'), elapsed, id + ': pause freezes the animation');
    await animation.getByRole('button', { name: 'Source text ↗', exact: true }).click();
    await assertEnglish(motionPage);
    await motionPage.getByRole('button', { name: 'Close', exact: true }).click();
    await motionPage.getByLabel('Choose a story animation').selectOption('');
  }
  await motionPage.close();
  console.log('PASS: English prologue and six story animations, pause and source details');
  assert.deepEqual(errors, []);
} finally {
  await browser.close();
}
