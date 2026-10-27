import assert from 'node:assert/strict';
import { mkdir } from 'node:fs/promises';
import { chromium, firefox, webkit } from 'playwright';
import { mockTianditu, isTileAccessControlNoise } from './mock-tianditu.mjs';
import { CHAPTER_TRANSITION_MS } from '../src/map-timing.js';

const base = process.env.ATLAS_URL;
if (!base) throw new Error('Run through with-preview.mjs');
assert.equal(CHAPTER_TRANSITION_MS, 1200);
const output = new URL('../../output/qa/', import.meta.url);
await mkdir(output, { recursive: true });
for (const name of (process.env.ATLAS_BROWSERS || 'chromium,webkit').split(',')) {
  const browser = await ({ chromium, firefox, webkit }[name]).launch();
  try {
    const context = await browser.newContext({ viewport: { width: 1920, height: 1080 } });
    await mockTianditu(context);
    const page = await context.newPage();
    const errors = []; page.on('pageerror', error => { if (!isTileAccessControlNoise(error.message)) errors.push(error.message); });
    await page.goto(`${base}?chapter=01&lang=zh`);
    await page.locator('canvas[data-paper-ready=true]').waitFor();
    await page.locator('.map-fullscreen').click();
    await page.locator('.is-map-fullscreen').waitFor();
    assert.equal(await page.locator('.fullscreen-orientation:visible').count(), 1);
    const frame = page.locator('canvas[data-paper-ready=true]');
    const texture = () => frame.evaluate(canvas => {
      const context = canvas.getContext('2d');
      return [[2,2],[canvas.width-32,2],[2,canvas.height-32],[canvas.width-32,canvas.height-32]].map(([x,y]) => {
        const pixels = context.getImageData(x,y,30,30).data;
        const colors = new Set();
        for (let i=0;i<pixels.length;i+=4) colors.add(`${pixels[i]},${pixels[i+1]},${pixels[i+2]}`);
        return colors.size;
      });
    });
    assert.ok((await texture()).every(count => count > 3), 'Paper texture reaches every viewport corner');
    await page.locator('.myth-map-canvas').hover(); await page.mouse.wheel(0, 2200); await page.waitForTimeout(500);
    assert.ok((await texture()).every(count => count > 3), 'Zooming out cannot expose a solid paper frame');
    if (name === 'chromium') await page.screenshot({ path: new URL('woodcut-fullscreen-filled.png', output).pathname.replace(/^\/([A-Za-z]:)/, '$1') });
    await page.keyboard.press('Escape');
    await page.goto(`${base}?chapter=04&lang=zh`);
    await page.getByLabel('选择地图故事动画').selectOption('04-02');
    await page.locator('.story-animation[data-status=playing]').waitFor();
    await page.goto(`${base}?chapter=03&lang=zh`);
    await page.getByLabel('选择地图故事动画').selectOption('03-05');
    await page.locator('.kuafu-journey[data-status=playing]').waitFor();
    const clockStart = new Date();
    await page.clock.install({ time: clockStart });
    await page.clock.pauseAt(new Date(clockStart.getTime() + 1000));
    await page.evaluate(() => {
      window.noticeCheck = { started: null, duration: null, pausedSamples: [] };
      const sample = () => {
        const check = window.noticeCheck;
        const visible = document.querySelector('.map-surface .chapter-transition-veil.is-visible');
        if (visible) {
          check.started ??= performance.now();
          const story = document.querySelector('.story-animation[data-status=paused]');
          if (story) check.pausedSamples.push(Number(story.dataset.elapsed));
        } else if (check.started !== null) { check.duration = performance.now() - check.started; return; }
        requestAnimationFrame(sample);
      };
      requestAnimationFrame(sample);
    });
    await page.locator('.timeline-steps button').nth(4).click();
    await page.locator('.map-surface .chapter-transition-veil.is-visible').waitFor();
    await page.getByLabel('选择地图故事动画').evaluate(select => { select.value = '04-02'; select.dispatchEvent(new Event('change', { bubbles: true })); });
    await page.locator('.story-animation[data-status=paused]').waitFor();
    await page.clock.runFor(CHAPTER_TRANSITION_MS + 100);
    await page.waitForFunction(() => window.noticeCheck.duration !== null);
    const check = await page.evaluate(() => window.noticeCheck);
    assert.ok(check.duration >= 1100, `${name}: chapter notice lasted ${check.duration}ms`);
    assert.ok(check.pausedSamples.length > 0, 'The covered story is paused');
    assert.ok(check.pausedSamples.every(time => time === 0), 'A covered story does not play behind the chapter notice');
    await page.clock.resume();
    await page.waitForFunction(() => Number(document.querySelector('.story-animation')?.dataset.elapsed) > 200);
    await page.locator('.map-mode-switch').getByRole('button', { name: '真实地理', exact: true }).click();
    await page.getByLabel('地理事件').selectOption('03-05');
    await page.locator('.geo-map-stage .chapter-transition-veil.is-visible').waitFor();
    await page.waitForTimeout(1300);
    await page.locator('.geo-empty-notice').waitFor();
    await page.waitForTimeout(2000);
    assert.equal(await page.locator('.geo-empty-notice').count(), 1);
    await page.waitForTimeout(600);
    await page.locator('.geo-empty-notice').waitFor({ state: 'detached' });
    assert.match(await page.locator('.geo-results').innerText(), /暂无可靠地点资料/);
    await page.getByLabel('地理事件').selectOption('03-04');
    await page.getByLabel('地理事件').selectOption('03-05');
    await page.locator('.geo-empty-notice').waitFor();
    await page.getByLabel('地理事件').selectOption('03-04');
    await page.waitForTimeout(3000);
    assert.equal(await page.locator('.geo-empty-notice').count(), 0, 'A stale empty notice cannot survive a rapid event switch');
    if (!await page.locator('.geo-search').evaluate(node => node.open)) await page.locator('.geo-search summary').click();
    await page.getByLabel('搜索地理参考点').fill('不存在的地名');
    assert.equal(await page.locator('[data-candidate-id]').count(), 0);
    assert.equal(await page.locator('.geo-empty-notice').count(), 0, 'No search match is distinct from missing geographic evidence');
    assert.deepEqual(errors, []);
    await context.close();
    const reduced = await browser.newContext({ reducedMotion: 'reduce', viewport: { width: 1440, height: 1000 } });
    const rp = await reduced.newPage();
    await rp.goto(`${base}?chapter=01&lang=zh`);
    await rp.locator('.timeline-steps button').nth(2).click();
    await rp.locator('.chapter-transition-veil.is-visible').waitFor();
    assert.equal(await rp.locator('.chapter-transition-veil.is-visible').evaluate(node => getComputedStyle(node).animationName), 'none');
    await rp.waitForTimeout(600);
    assert.equal(await rp.locator('.chapter-transition-veil.is-visible').isVisible(), true, 'Reduced motion keeps the readable dwell');
    await reduced.close();
    console.log(`PASS ${name}: continuous paper at wide fullscreen/zoom-out, one compass, 1200ms chapter dwell, covered-story pause, 2500ms empty notice/cancellation and reduced motion`);
  } finally { await browser.close(); }
}
