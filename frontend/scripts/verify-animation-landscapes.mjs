import assert from 'node:assert/strict';
import { mkdir } from 'node:fs/promises';
import { chromium } from 'playwright';

const base = process.env.ATLAS_URL;
if (!base) throw new Error('Run through with-preview.mjs');
const out = process.env.ATLAS_QA_DIR || '../output/qa/animation-landscapes/';
await mkdir(out, { recursive: true });
const paths = {
  jingwei: ['/data/atlas/optimized/myth-icons/terrain/ridge.webp', '/data/atlas/optimized/myth-icons/terrain/sea-cloud.webp'],
  kuafu: ['/data/atlas/optimized/myth-icons/terrain/ridge.webp', '/data/atlas/myth-icons/animations/landscape-marsh-v1.webp'],
  dayu: ['/data/atlas/optimized/myth-icons/terrain/ridge.webp'],
};
const viewports = [['desktop', { width: 1440, height: 1000 }], ['mobile', { width: 390, height: 844 }]];
const routePatterns = Object.values(paths).flat().map(path => `**/${path.split('/').pop()}`);

async function enterAtlas(page, { lang = 'zh' } = {}) {
  const target = new URL(base);
  target.searchParams.set('splash', '0');
  target.searchParams.set('lang', lang);
  await page.goto(target.href);
  await page.locator('.world-layout').waitFor();
  if (await page.locator('.onboarding-skip').count()) await page.locator('.onboarding-skip').click();
}

async function selectChapter(page, index) {
  if (!await page.locator('.timeline-steps button').count()) await page.locator('.mobile-explore-nav button').first().click();
  await page.locator('.timeline-steps button').nth(index).click();
  await page.waitForTimeout(700);
}

async function selectStory(page, id) {
  await page.locator('.map-animation-choice select').selectOption(id);
}

async function waitPhase(page, selector, phase) {
  await page.waitForFunction(({ selector, phase }) => document.querySelector(selector)?.dataset.phase === phase, { selector, phase }, { timeout: 45000 });
}

async function waitLandmarks(page, selector, count) {
  await page.waitForFunction(({ selector, count }) => Number(document.querySelector(selector)?.dataset.landmarks) === count, { selector, count }, { timeout: 15000 });
}

async function waitLandscapes(page, count) {
  await page.waitForFunction(count => Number(document.querySelector('.kuafu-journey:not(.story-animation)')?.dataset.landscapes) === count, count, { timeout: 15000 });
}

function track(page) {
  const errors = [], failed = [];
  page.on('pageerror', error => errors.push(error.message));
  page.on('response', response => { if (response.status() >= 400 && response.url().startsWith(base)) failed.push(`${response.status()} ${response.url()}`); });
  return { errors, failed };
}

const browser = await chromium.launch();
try {
  for (const [label, viewport] of viewports) {
    const page = await browser.newPage({ viewport, reducedMotion: 'no-preference' });
    const { errors, failed } = track(page);
    const requests = new Set();
    page.on('request', request => requests.add(new URL(request.url()).pathname));
    await enterAtlas(page);
    await selectChapter(page, 3);

    await selectStory(page, '03-04');
    await waitLandmarks(page, '.story-animation[data-story="03-04"]', 2);
    assert.ok(requests.has(paths.jingwei[0]), `jingwei requests ${paths.jingwei[0]}`);
    const jingwei = page.locator('.story-animation[data-story="03-04"]');
    await jingwei.waitFor();
    await page.waitForTimeout(1200);
    assert.equal(await jingwei.getAttribute('data-status'), 'playing');
    await page.locator('.myth-map-wrap').screenshot({ path: `${out}${label}-jingwei-start.png` });
    if (label === 'desktop') {
      const mapBox = await page.locator('.myth-map-wrap').boundingBox();
      await page.mouse.move(mapBox.x + mapBox.width / 2, mapBox.y + mapBox.height / 2);
      await page.mouse.wheel(0, -480);
      await page.waitForTimeout(700);
      assert.equal(await jingwei.getAttribute('data-landmarks'), '2', 'landmarks survive a manual zoom');
      await page.locator('.myth-map-wrap').screenshot({ path: `${out}${label}-jingwei-zoom.png` });
    }
    await page.waitForFunction(() => Number(document.querySelector('.story-animation[data-story="03-04"]')?.dataset.elapsed || 0) >= 4800, null, { timeout: 30000 });
    await page.locator('.myth-map-wrap').screenshot({ path: `${out}${label}-jingwei-drop.png` });

    await selectStory(page, '03-05');
    await waitLandscapes(page, 2);
    for (const path of paths.kuafu) assert.ok(requests.has(path), `kuafu requests ${path}`);
    await waitPhase(page, '.kuafu-journey:not(.story-animation)', 'drink');
    await page.locator('.myth-map-wrap').screenshot({ path: `${out}${label}-kuafu-rivers.png` });
    await waitPhase(page, '.kuafu-journey:not(.story-animation)', 'forest');
    await page.waitForTimeout(600);
    await page.locator('.myth-map-wrap').screenshot({ path: `${out}${label}-kuafu-forest.png` });

    await selectChapter(page, 5);
    await selectStory(page, '05-01');
    await waitLandmarks(page, '.story-animation[data-story="05-01"]', 1);
    assert.ok(requests.has(paths.dayu[0]), `dayu requests ${paths.dayu[0]}`);
    const dayu = page.locator('.story-animation[data-story="05-01"]');
    await page.waitForTimeout(1200);
    assert.equal(await dayu.getAttribute('data-status'), 'playing');
    await page.locator('.myth-map-wrap').screenshot({ path: `${out}${label}-dayu-start.png` });
    await page.waitForTimeout(3800);
    await page.locator('.myth-map-wrap').screenshot({ path: `${out}${label}-dayu-channel.png` });
    await page.waitForTimeout(3800);
    await page.locator('.myth-map-wrap').screenshot({ path: `${out}${label}-dayu-recede.png` });

    await page.getByRole('button', { name: '跳过', exact: true }).click();
    await dayu.waitFor({ state: 'detached' });
    assert.equal(await page.locator('.story-animation, .kuafu-journey').count(), 0, 'skip removes the animation layer');
    assert.deepEqual(errors, [], `${label}: page errors`);
    assert.deepEqual(failed, [], `${label}: failed responses`);
    await page.close();
  }

  const reducedPage = await browser.newPage({ viewport: { width: 1280, height: 800 }, reducedMotion: 'reduce' });
  const reduced = track(reducedPage);
  await enterAtlas(reducedPage);
  await selectChapter(reducedPage, 3);
  await selectStory(reducedPage, '03-05');
  await waitLandscapes(reducedPage, 2);
  await reducedPage.locator('.kuafu-journey[data-status="reduced"]').waitFor();
  await reducedPage.getByRole('button', { name: '下一幕', exact: true }).click();
  await reducedPage.waitForTimeout(300);
  assert.ok(await reducedPage.locator('.kuafu-journey').getAttribute('data-phase'));
  assert.deepEqual(reduced.errors, [], 'reduced motion: page errors');
  await reducedPage.close();

  const englishPage = await browser.newPage({ viewport: { width: 1440, height: 1000 } });
  const english = track(englishPage);
  await enterAtlas(englishPage, { lang: 'en' });
  await selectChapter(englishPage, 3);
  await selectStory(englishPage, '03-04');
  await waitLandmarks(englishPage, '.story-animation[data-story="03-04"]', 2);
  await englishPage.waitForTimeout(900);
  await englishPage.locator('.myth-map-wrap').screenshot({ path: `${out}english-jingwei.png` });
  assert.deepEqual(english.errors, [], 'english: page errors');
  await englishPage.close();

  const slowPage = await browser.newPage({ viewport: { width: 1440, height: 1000 } });
  const slow = track(slowPage);
  await enterAtlas(slowPage);
  for (const pattern of routePatterns) await slowPage.route(pattern, async route => { await new Promise(resolve => setTimeout(resolve, 5000)); await route.continue(); });
  await selectChapter(slowPage, 3);
  await selectStory(slowPage, '03-04');
  const slowStory = slowPage.locator('.story-animation[data-story="03-04"]');
  await slowStory.waitFor();
  await slowPage.waitForTimeout(400);
  assert.equal(await slowStory.getAttribute('data-landmarks'), '0', 'playback starts before slow landmarks arrive');
  assert.equal(await slowStory.getAttribute('data-status'), 'playing', 'slow landmarks do not block playback');
  await waitLandmarks(slowPage, '.story-animation[data-story="03-04"]', 2);
  assert.deepEqual(slow.errors, [], 'slow images: page errors');
  await slowPage.close();

  const fallbackPage = await browser.newPage({ viewport: { width: 1440, height: 1000 } });
  const fallback = track(fallbackPage);
  for (const pattern of routePatterns) await fallbackPage.route(pattern, route => route.abort());
  await enterAtlas(fallbackPage);
  await selectChapter(fallbackPage, 3);
  await selectStory(fallbackPage, '03-04');
  await fallbackPage.locator('.story-animation[data-story="03-04"]').waitFor();
  await fallbackPage.waitForTimeout(1000);
  assert.equal(await fallbackPage.locator('.story-animation[data-story="03-04"]').getAttribute('data-landmarks'), '0', 'missing images drop landmarks');
  assert.equal(await fallbackPage.locator('.story-animation[data-story="03-04"]').getAttribute('data-status'), 'playing', 'missing images keep playback');
  await fallbackPage.locator('.myth-map-wrap').screenshot({ path: `${out}fallback-jingwei.png` });
  await selectStory(fallbackPage, '03-05');
  await fallbackPage.locator('.kuafu-journey:not(.story-animation)').waitFor();
  await fallbackPage.waitForTimeout(1000);
  assert.equal(await fallbackPage.locator('.kuafu-journey:not(.story-animation)').getAttribute('data-landscapes'), '0');
  assert.notEqual(await fallbackPage.locator('.kuafu-journey:not(.story-animation)').getAttribute('data-status'), 'error');
  await fallbackPage.locator('.myth-map-wrap').screenshot({ path: `${out}fallback-kuafu.png` });
  assert.deepEqual(fallback.errors, [], 'missing images: page errors');
  await fallbackPage.close();
} finally {
  await browser.close();
}
console.log('PASS: three animation landscapes on desktop/mobile, layer cleanup, English, reduced motion, slow and missing images');
