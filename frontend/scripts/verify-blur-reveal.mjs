import assert from 'node:assert/strict';
import { chromium, webkit } from 'playwright';

const base = process.env.ATLAS_URL;
if (!base) throw new Error('Run through with-preview.mjs');
for (const name of (process.env.ATLAS_BROWSERS || 'chromium,webkit').split(',')) {
  const browser = await ({ chromium, webkit }[name]).launch();
  try {
    for (const width of [390, 1440]) for (const lang of ['zh', 'en']) {
      const page = await browser.newPage({ viewport: { width, height: 844 }, reducedMotion: 'no-preference' });
      const errors = [];
      page.on('pageerror', error => errors.push(error.message));
      await page.goto(`${base}?lang=${lang}`);
      await page.locator('.onboarding-skip').click();
      await page.waitForTimeout(500);
      await page.evaluate(() => document.fonts.ready);
      const title = page.locator('#reading-notes-title > span');
      const y = await title.evaluate(node => node.getBoundingClientRect().top + scrollY);
      const move = async top => {
        await page.evaluate(top => scrollTo({ top, behavior: 'instant' }), top);
        await page.evaluate(() => new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve))));
      };
      const state = () => title.evaluate(node => ({ state: node.dataset.revealState, mode: node.dataset.revealMode, opacity: +getComputedStyle(node).opacity, filter: getComputedStyle(node).filter }));
      await page.mouse.move(width / 2, 420);
      for (let cycle = 0; cycle < 3; cycle++) {
        await move(y - 900);
        await page.waitForTimeout(1550);
        // Let preceding card titles release the shared three-block budget before this heading enters.
        await page.mouse.wheel(0, 20);
        await page.waitForTimeout(1550);
        let entered = false;
        for (let step = 0; step < 12; step++) {
          await page.mouse.wheel(0, 20); await page.waitForTimeout(45);
          const current = await state();
          if (current.state === 'revealing') {
            entered = true;
            assert.equal(current.mode, undefined);
            assert.equal(current.opacity, 1);
          }
        }
        assert.ok(entered, `Real wheel entry observed: ${name} ${width} ${lang} cycle ${cycle}; ${JSON.stringify(await title.evaluate(node => ({state: node.dataset.revealState, y:node.getBoundingClientRect().top, active:[...document.querySelectorAll('[data-reveal-state=revealing]')].map(n=>n.textContent)})))}`);
        await move(y - 440);
        await page.waitForTimeout(1550);
        assert.equal((await state()).state, 'clear');
        await page.mouse.wheel(0, -20); await page.waitForTimeout(60);
        assert.equal((await state()).state, 'clear', 'Reversal within viewport stays clear');
      }
      await page.emulateMedia({ reducedMotion: 'reduce' });
      await move(y - 900); await move(y - 810);
      assert.equal((await state()).filter, 'none');
      assert.equal((await state()).opacity, 1);
      assert.equal(await page.evaluate(() => document.documentElement.scrollWidth > innerWidth), false);
      assert.deepEqual(errors, []);
      await page.close();
    }
    console.log(`PASS ${name}: blur reveal pure blur/reentry/reversal/reduced motion in both languages and widths`);
  } finally { await browser.close(); }
}
