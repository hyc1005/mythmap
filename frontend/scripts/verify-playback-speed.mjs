import { clickPlaybackControl } from './ui-controls.mjs';
import assert from 'node:assert/strict';
import { chromium, firefox, webkit } from 'playwright';
import { BASE_PLAYBACK_RATE } from '../src/playback.js';

const base = process.env.ATLAS_URL;
if (!base) throw new Error('Run through with-preview.mjs');
assert.equal(BASE_PLAYBACK_RATE, 1.3);
for (const name of (process.env.ATLAS_BROWSERS || 'chromium,webkit').split(',')) {
  const browser = await ({ chromium, firefox, webkit }[name]).launch();
  try {
    for (const [chapter, story, selector] of [['00', null, '.pangu-player-wrap'], ['03', '03-05', '.kuafu-journey'], ['02', '02-04', '.story-animation']]) {
      const page = await browser.newPage({ viewport: { width: 1440, height: 1000 } });
      const errors = [];
      page.on('pageerror', error => errors.push(error.message));
      await page.clock.install();
      await page.goto(`${base}?chapter=${chapter}&lang=zh`);
      if (story) await page.getByLabel('选择地图故事动画').selectOption(story);
      else await page.getByRole('button', { name: '播放盘古序章', exact: true }).click();
      const panel = page.locator(selector);
      await page.locator(selector + '[data-status=playing]').waitFor();
      await page.clock.pauseAt(await page.evaluate(() => Date.now() + 1000));
      await clickPlaybackControl(page, story ? '重播' : '重播盘古序章');
      await page.clock.runFor(200);
      const time = () => story ? panel.getAttribute('data-elapsed').then(Number)
        : page.locator('.pangu-player-controls progress').getAttribute('value').then(value => Number(value) / 30 * 1000);
      for (const multiplier of [1, 2]) {
        if (multiplier === 2) await clickPlaybackControl(page, "播放速度 1倍");
        await page.clock.runFor(200);
        const before = await time();
        await page.clock.runFor(1000);
        const delta = (await time()) - before;
        assert.ok(Math.abs(delta - 1000 * BASE_PLAYBACK_RATE * multiplier) < 170, `${name} ${chapter}: expected ${1300 * multiplier} story ms, got ${delta}`);
      }
      await page.getByRole('button', { name: /^暂停/ }).click();
      await page.clock.runFor(100);
      const frozen = await time();
      await clickPlaybackControl(page, "播放速度 2倍");
      await page.clock.runFor(500);
      assert.equal(await time(), frozen, 'Changing speed while paused does not advance the story');
      await clickPlaybackControl(page, story ? '重播' : '重播盘古序章');
      await page.clock.runFor(100);
      assert.ok(await time() < 180, 'Replay starts at the beginning with the default rate');
      const duration = story ? Number(await panel.locator('progress').getAttribute('max')) : 13000;
      await page.clock.runFor(Math.ceil(duration / BASE_PLAYBACK_RATE) + 200);
      assert.equal(await panel.getAttribute('data-status'), 'completed');
      if (story) assert.equal(await time(), duration, 'The last story time is clamped to the full duration');
      else assert.equal(await page.locator('.pangu-composition').getAttribute('data-frame'), '389');
      assert.deepEqual(errors, []);
      await page.close();
    }
    console.log(`PASS ${name}: all three clocks run at 1.3x / 2.6x, pause, replay and reach their endings`);
  } finally { await browser.close(); }
}
