import assert from 'node:assert/strict';
import { mkdir } from 'node:fs/promises';
import { chromium, webkit } from 'playwright';
import { mockNaturalEarth } from './mock-natural-earth.mjs';

const base = process.env.ATLAS_URL;
if (!base) throw new Error('Run through with-preview.mjs');
const output = new URL('../../output/ink-splash-lab/integration-preview/', import.meta.url);
await mkdir(output, { recursive: true });
const filename = name => new URL(name, output).pathname.replace(/^\/([A-Za-z]:)/, '$1');

for (const name of (process.env.ATLAS_BROWSERS || 'chromium,webkit').split(',')) {
  const browser = await ({ chromium, webkit }[name]).launch();
  try {
    for (const width of [390, 1440]) {
      const context = await browser.newContext({ viewport: { width, height: 900 } });
      await mockNaturalEarth(context);
      const page = await context.newPage();
      const errors = [];
      page.on('pageerror', error => errors.push(error.message));
      await page.addInitScript(() => localStorage.setItem('shanhai-onboarding-v1', '1'));
      await page.goto(`${base}?chapter=03&lang=zh`);
      const modes = page.locator('.map-mode-switch.paper-tabs');
      await modes.waitFor();
      await page.evaluate(() => document.fonts.ready);
      await modes.locator('button').nth(1).click();
      await page.locator('.geography-atlas[data-basemap-state="ready"]').waitFor();
      for (const lang of ['en', 'zh']) {
        await page.locator(`.language-switch button[lang=${lang === 'zh' ? 'zh-CN' : 'en'}]`).click();
        await page.waitForTimeout(300);
        for (const selector of ['.map-mode-switch', '.language-switch']) {
          const metrics = await page.locator(selector).evaluate(group => {
            const selected = group.querySelector('[aria-pressed=true]');
            return {
              x: parseFloat(group.style.getPropertyValue('--paper-tab-x')), left: selected.offsetLeft,
              width: parseFloat(group.style.getPropertyValue('--paper-tab-width')), actual: selected.offsetWidth,
            };
          });
          assert.equal(metrics.x, metrics.left, `${selector}: selected position follows locale`);
          assert.equal(metrics.width, metrics.actual, `${selector}: selected width follows locale`);
        }
      }
      await modes.locator('button').first().click();
      await page.waitForTimeout(300);
      await page.screenshot({ path: filename(`paper-header-${name}-${width}.png`) });
      const roles = page.locator('.bestiary-roles.paper-tabs');
      await roles.locator('button').nth(1).click();
      assert.equal(await roles.locator('button').nth(1).getAttribute('aria-pressed'), 'true');
      await page.waitForTimeout(300);
      await page.screenshot({ path: filename(`paper-bestiary-${name}-${width}.png`) });

      await page.goto(`${base}?chapter=07&item=beast-beishan-xiao-liangqu&lang=zh`);
      await page.waitForFunction(() => document.querySelector('.detail-drawer')?.dataset.readingRestoring === 'false');
      const evidence = page.locator('.detail-drawer .detail-evidence');
      await evidence.locator(':scope > summary').click();
      await page.waitForTimeout(360);
      const details = page.locator('.detail-drawer .morphology-review');
      const summary = details.locator(':scope > summary');
      await summary.click();
      await page.waitForTimeout(60);
      assert.equal(await details.evaluate(node => node.getAnimations().length), 1);
      await page.waitForTimeout(300);
      assert.equal(await details.evaluate(node => node.open), true);
      await page.screenshot({ path: filename(`paper-disclosure-${name}-${width}.png`) });
      await summary.click();
      await page.waitForTimeout(350);
      assert.equal(await details.evaluate(node => node.open), false);
      await summary.focus();
      await page.keyboard.press('Enter');
      await page.waitForTimeout(350);
      assert.equal(await details.evaluate(node => node.open), true, 'Keyboard opens native details');
      await summary.click();
      await page.waitForTimeout(40);
      await summary.click();
      await page.waitForTimeout(350);
      assert.equal(await details.evaluate(node => node.open), true, 'Rapid reversal settles open');
      await page.emulateMedia({ reducedMotion: 'reduce' });
      await summary.click();
      await page.waitForTimeout(40);
      assert.equal(await details.evaluate(node => node.open), false);
      assert.equal(await details.evaluate(node => node.getAnimations().length), 0);
      assert.ok(await modes.evaluate(node => parseFloat(getComputedStyle(node, '::before').transitionDuration) <= .001));

      await page.emulateMedia({ reducedMotion: 'no-preference' });
      await page.goto(`${base}?splash=0`);
      await page.locator('.reading-notes-details>summary').press('Enter');
      const prose = page.locator('.reading-notes-copy');
      await prose.waitFor();
      await page.evaluate(() => document.fonts.ready);
      await page.evaluate(() => {
        document.documentElement.style.scrollBehavior = 'auto';
        const node = document.querySelector('.reading-notes-copy');
        scrollTo(0, node.getBoundingClientRect().top + scrollY - innerHeight - 35);
      });
      await page.waitForTimeout(1250);
      await page.mouse.wheel(0, 140);
      await page.waitForTimeout(70);
      assert.equal(await prose.getAttribute('data-reveal-state'), 'revealing');
      assert.equal(await prose.evaluate(node => getComputedStyle(node).transitionDuration), '1.2s');
      await page.waitForTimeout(1250);
      assert.equal(await prose.evaluate(node => getComputedStyle(node).filter), 'blur(0px)');
      assert.equal(await page.evaluate(() => document.documentElement.scrollWidth > innerWidth), false);
      assert.deepEqual(errors, []);
      console.log(`PASS ${name} ${width}: tabs/locale/filter, disclosure/keyboard/reversal/reduced motion, whole-prose 1.2s`);
      await context.close();
    }
  } finally { await browser.close(); }
}
