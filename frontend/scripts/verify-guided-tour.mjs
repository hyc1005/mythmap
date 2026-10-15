import assert from 'node:assert/strict';
import { mkdir, readFile } from 'node:fs/promises';
import { chromium, firefox, webkit } from 'playwright';
import { chapterStoryIds } from '../src/chapter-stories.js';

const base = process.env.ATLAS_URL;
if (!base) throw new Error('Run with with-preview.mjs');
const read = async name => JSON.parse(await readFile(new URL(`../public/data/atlas/${name}.json`, import.meta.url), 'utf8'));
const [catalog, animations, kuafu] = await Promise.all(['catalog', 'story-animations', 'kuafu-journey'].map(read));
assert.deepEqual(chapterStoryIds('03', catalog, animations, kuafu), ['03-04', '03-05']);
assert.deepEqual(chapterStoryIds('06', catalog, animations, kuafu), []);
assert.deepEqual(chapterStoryIds('07', catalog, animations, kuafu), []);
const output = new URL('../../output/qa/', import.meta.url);
await mkdir(output, { recursive: true });
const filename = name => new URL(name, output).pathname.replace(/^\/([A-Za-z]:)/, '$1');

async function selectChapter(page, index) {
  await page.waitForFunction(() => [...document.querySelectorAll('.timeline-steps button, .mobile-explore-nav button')].some(node => node.getBoundingClientRect().height > 0));
  if (!await page.locator('.timeline-steps button').first().isVisible()) await page.locator('.mobile-explore-nav button').first().click();
  await page.locator('.timeline-steps button').nth(index).click();
}
async function finishManual(page) {
  for (let i = 0; i < 20; i++) {
    const next = page.locator('.journey-actions').getByRole('button', { name: /^(下一幕|完成故事|Next scene|Finish story)$/ });
    if (!await next.count()) return;
    await next.click();
  }
  throw new Error('Manual story did not complete');
}
async function actorFits(page) {
  await page.evaluate(() => new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve))));
  const result = await page.waitForFunction(() => {
    const node = document.querySelector('.kuafu-journey');
    const bounds = document.querySelector('.myth-map-canvas')?.getBoundingClientRect();
    if (!node || !bounds) return false;
    const actor = { x: Number(node.dataset.screenX), y: Number(node.dataset.screenY), size: Number(node.dataset.size) };
    const canvas = { width: bounds.width, height: bounds.height };
    return Number.isFinite(actor.x) && actor.size > 0 && actor.x - actor.size / 2 >= -1 && actor.x + actor.size / 2 <= canvas.width + 1 && actor.y - actor.size >= -1 && actor.y <= canvas.height + 1 ? { actor, canvas } : false;
  }, null, { timeout: 3000 });
  const { actor, canvas } = await result.jsonValue();
  await result.dispose();
  assert.ok(actor.x - actor.size / 2 >= -1 && actor.x + actor.size / 2 <= canvas.width + 1 && actor.y - actor.size >= -1 && actor.y <= canvas.height + 1, `Actor fits ${JSON.stringify({ actor, canvas })}`);
}

for (const name of (process.env.ATLAS_BROWSERS || 'chromium,webkit').split(',')) {
  const browser = await ({ chromium, firefox, webkit }[name]).launch();
  try {
    const page = await browser.newPage({ viewport: { width: 390, height: 844 }, reducedMotion: 'reduce' });
    const errors = [];
    page.on('pageerror', error => errors.push(error.message));
    await page.goto(`${base}?chapter=03&lang=zh`);
    await page.locator('.myth-map-canvas canvas').first().waitFor();
    for (const chapter of [4, 3, 4, 3]) {
      await selectChapter(page, chapter);
      await page.waitForTimeout(150);
      assert.equal(await page.locator('.kuafu-journey').count(), 0, 'First visit and revisit stay static');
      assert.equal(await page.locator('.world-layout').getAttribute('data-tour-active'), 'false');
    }
    await page.getByLabel('选择地图故事动画').selectOption('03-04');
    await page.locator('.story-animation[data-status="reduced"]').waitFor();
    await page.getByRole('button', { name: '下一幕', exact: true }).click();
    await page.waitForFunction(() => Number(document.querySelector('.story-animation')?.dataset.elapsed) > 0);
    await actorFits(page);
    const elapsed = await page.locator('.story-animation').getAttribute('data-elapsed');
    const closeSize = Number(await page.locator('.story-animation').getAttribute('data-size'));
    await page.getByRole('button', { name: '本章全图', exact: true }).click();
    await page.waitForFunction(() => document.querySelector('.story-animation')?.dataset.closeup === 'false');
    assert.equal(await page.locator('.story-animation').getAttribute('data-elapsed'), elapsed);
    await page.waitForFunction(size => Number(document.querySelector('.story-animation')?.dataset.size) < size, closeSize, { timeout: 3000 });
    const overviewSize = Number(await page.locator('.story-animation').getAttribute('data-size'));
    assert.ok(closeSize > overviewSize, 'Mobile close-up enlarges the actor');
    await page.getByRole('button', { name: '故事近景', exact: true }).click();
    await page.waitForFunction(() => document.querySelector('.story-animation')?.dataset.closeup === 'true');
    await actorFits(page);
    assert.equal(await page.locator('.story-animation').getAttribute('data-elapsed'), elapsed);
    const bounds = await page.locator('.myth-map-canvas').boundingBox();
    await page.mouse.move(bounds.x + bounds.width / 2, bounds.y + bounds.height / 2);
    await page.mouse.down();
    await page.mouse.move(bounds.x + bounds.width / 2 + 40, bounds.y + bounds.height / 2 + 20, { steps: 8 });
    await page.mouse.up();
    await page.waitForFunction(() => document.querySelector('.story-animation')?.dataset.follow === 'false');
    await page.waitForTimeout(1500);
    const draggedView = await page.locator('.myth-map-canvas').getAttribute('data-view');
    await page.waitForTimeout(200);
    assert.equal(await page.locator('.myth-map-canvas').getAttribute('data-view'), draggedView, 'Manual pan keeps the reader camera');
    await page.getByRole('button', { name: '故事近景', exact: true }).click();
    await page.waitForFunction(() => document.querySelector('.story-animation')?.dataset.follow === 'true');
    assert.equal(await page.locator('.story-animation').getAttribute('data-elapsed'), elapsed);
    await page.getByRole('button', { name: '连续游历', exact: true }).click();
    await page.locator('.story-animation[data-story="03-04"]').waitFor();
    await page.waitForFunction(() => document.querySelector('.story-animation')?.dataset.elapsed === '0');
    assert.match(await page.locator('.tour-progress').textContent(), /1 \/ 2/);
    await finishManual(page);
    await page.locator('.kuafu-journey:not(.story-animation)').waitFor();
    assert.equal(await page.locator('.world-layout').getAttribute('data-chapter'), '03', 'Second story stays in the same chapter');
    assert.match(await page.locator('.tour-progress').textContent(), /2 \/ 2/);
    await page.getByRole('button', { name: '下一幕', exact: true }).click();
    await actorFits(page);
    const kuafuElapsed = await page.locator('.kuafu-journey').getAttribute('data-elapsed');
    await page.getByRole('button', { name: 'EN', exact: true }).click();
    assert.equal(await page.locator('.kuafu-journey').getAttribute('data-elapsed'), kuafuElapsed);
    assert.match(await page.locator('.tour-progress').textContent(), /2 \/ 2/);
    await finishManual(page);
    await page.locator('.story-animation[data-story="04-02"]').waitFor();
    await page.locator('.story-animation').getByRole('button', { name: 'Skip', exact: true }).click();
    await page.locator('.story-animation[data-story="05-01"]').waitFor();
    await page.locator('.story-animation').getByRole('button', { name: 'Skip', exact: true }).click();
    await page.waitForFunction(() => document.querySelector('.world-layout').dataset.chapter === '06');
    await page.waitForTimeout(1600);
    assert.equal(await page.locator('.world-layout').getAttribute('data-chapter'), '06', 'Text chapters wait for the reader');
    assert.equal(await page.locator('.world-layout').getAttribute('data-tour-reading'), 'true');
    await page.locator('.mobile-explore-nav button').last().click();
    await page.locator('.explore-sheet .story-entry').first().click();
    await page.locator('.drawer-close').click();
    assert.equal(await page.locator('.world-layout').getAttribute('data-tour-reading'), 'true');
    await page.getByRole('button', { name: 'Atlas fullscreen', exact: true }).click();
    await page.locator('.is-map-fullscreen .tour-reading button').click();
    await page.waitForFunction(() => document.querySelector('.world-layout').dataset.chapter === '07');
    await page.waitForTimeout(1600);
    assert.equal(await page.locator('.world-layout').getAttribute('data-chapter'), '07');
    await page.locator('.is-map-fullscreen .tour-reading button').click();
    await page.waitForFunction(() => document.querySelector('.world-layout').dataset.tourActive === 'false');
    await page.getByRole('button', { name: 'Exit atlas fullscreen', exact: true }).click();
    await page.getByRole('button', { name: 'Start guided tour', exact: true }).click();
    await page.waitForFunction(() => document.querySelector('.world-layout').dataset.chapter === '00');
    await page.getByRole('button', { name: 'Pause guided tour', exact: true }).waitFor();
    console.log(`PASS ${name}: static navigation, story order, progress, language, reading stop, fullscreen and restart`);

    await page.getByRole('button', { name: '中文', exact: true }).click();
    for (const [width, height] of [[390, 844], [320, 700], [844, 390]]) {
      await page.setViewportSize({ width, height });
      for (const [chapter, id] of [[1, '01-02'], [2, '02-04'], [3, '03-04'], [3, '03-05'], [4, '04-02'], [5, '05-01']]) {
        await selectChapter(page, chapter);
        await page.getByLabel('选择地图故事动画').selectOption(id);
        await page.locator('.kuafu-journey[data-status="reduced"]').waitFor();
        await page.getByRole('button', { name: '下一幕', exact: true }).click();
        await actorFits(page);
        assert.ok(await page.locator('.story-view-controls button').evaluateAll(nodes => nodes.every(node => node.getBoundingClientRect().height >= 44)));
        if (name === 'chromium' && width === 390) await page.locator('.myth-map-wrap').screenshot({ path: filename(`closeup-${id}.png`) });
        await page.getByRole('button', { name: '本章全图', exact: true }).click();
        await page.waitForFunction(() => document.querySelector('.myth-map-wrap').dataset.cameraMode === 'overview');
        await actorFits(page);
      }
      console.log(`PASS ${name} ${width}x${height}: six story close-ups and overview`);
    }
    assert.deepEqual(errors, []);
    await page.close();

    const motion = await browser.newPage({ viewport: { width: 390, height: 844 } });
    await motion.goto(`${base}?chapter=00&lang=zh`);
    await motion.getByRole('button', { name: '播放盘古序章', exact: true }).waitFor();
    assert.equal(await motion.locator('.pangu-player-controls progress').getAttribute('value'), '0');
    await motion.getByRole('button', { name: '播放盘古序章', exact: true }).click();
    await motion.getByRole('button', { name: '暂停盘古序章', exact: true }).waitFor();
    await selectChapter(motion, 3);
    assert.equal(await motion.locator('.kuafu-journey').count(), 0);
    await selectChapter(motion, 0);
    await motion.getByRole('button', { name: '播放盘古序章', exact: true }).waitFor();
    assert.equal(await motion.locator('.pangu-player-controls progress').getAttribute('value'), '0');
    await motion.close();
    console.log(`PASS ${name}: prologue requires explicit playback on first visit and revisit`);

    const desktop = await browser.newPage({ viewport: { width: 1440, height: 1000 }, reducedMotion: 'reduce' });
    await desktop.goto(`${base}?chapter=05&lang=zh#world`);
    await desktop.locator('.myth-map-canvas canvas').first().waitFor();
    await desktop.locator('.myth-map-wrap').scrollIntoViewIfNeeded();
    await desktop.waitForTimeout(800);
    const mapBounds = await desktop.locator('.myth-map-canvas').boundingBox();
    const view = JSON.parse(await desktop.locator('.myth-map-canvas').getAttribute('data-view'));
    const coordinate = catalog.events.find(item => item.id === '05-01').properties.layout_hint;
    await desktop.mouse.move(mapBounds.x + mapBounds.width / 2 + (coordinate[0] - view.center[0]) / view.resolution, mapBounds.y + mapBounds.height / 2 - (coordinate[1] - view.center[1]) / view.resolution);
    await desktop.locator('.ink-hover-card').hover();
    await desktop.waitForTimeout(400);
    await desktop.getByRole('button', { name: '展开原文与出处 ↗', exact: true }).click();
    await desktop.locator('.detail-drawer').waitFor();
    await desktop.close();
    console.log(`PASS ${name}: moving from map marker to source card keeps it clickable`);

  } finally { await browser.close(); }
}
