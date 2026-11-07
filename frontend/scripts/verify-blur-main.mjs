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
      const settle = () => page.evaluate(() => new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve))));
      const top = async () => { await page.evaluate(() => scrollTo({ top: 0, behavior: 'instant' })); await settle(); };
      for (let chapter = 0; chapter < 8; chapter++) {
        if (chapter) {
          if (width <= 768) {
            await page.locator('.mobile-explore-nav button').first().click();
            await page.locator('.explore-sheet .timeline-steps button').nth(chapter).click();
          } else await page.locator('.timeline-current button').last().click();
        }
        await top();
        const id = String(chapter).padStart(2, '0');
        assert.equal(await page.locator('.world-layout').getAttribute('data-chapter'), id);
        assert.equal(await page.locator('.chapter-rail h2 > span').getAttribute('data-reveal-key'), `chapter:${id}:title:${lang}`);
        assert.equal(await page.locator('.chapter-rail .ink-word').count(), 0, 'Old chapter word animation replaced');
        assert.equal(await page.locator('.chapter-rail h2 > span').evaluate(node => getComputedStyle(node).filter), 'blur(0px)', 'Chapter landing immediately clear');
      }
      if (width > 768) {
        const rail = page.locator('.chapter-rail');
        const canScroll = await rail.evaluate(node => node.scrollHeight > node.clientHeight + 150);
        if (canScroll) {
          await rail.evaluate(node => { node.scrollTop = node.scrollHeight; }); await settle();
          assert.equal(await page.locator('.chapter-rail h2 > span').getAttribute('data-reveal-state'), 'waiting', 'Clipped heading rearms');
          const maximum = await rail.evaluate(node => node.scrollTop);
          for (let position = maximum; position >= 0; position -= 30) {
            await rail.evaluate((node, position) => { node.scrollTop = position; }, position); await settle();
          }
          await rail.evaluate(node => { node.scrollTop = 0; }); await page.waitForTimeout(1250);
          assert.equal(await page.locator('.chapter-rail h2 > span').evaluate(node => getComputedStyle(node).filter), 'blur(0px)');
        }
      }
      for (const selector of ['.myth-header h1', '.chapter-rail h2', '.best-page-heading h2', '#reading-notes h2', '.beast-card b']) assert.ok(await page.locator(`${selector} .blur-reveal-text`).count(), `Covered title: ${selector}`);
      assert.equal(await page.locator('.bestiary-tools .blur-reveal-text').count(), 0);
      assert.ok(await page.locator('.beast-card').count() <= 12, 'Initial main cards unchanged');
      const title = page.locator('.best-page-heading h2 > span');
      const y = await title.evaluate(node => node.getBoundingClientRect().top + scrollY);
      await page.mouse.move(width - 3, 420);
      for (let cycle = 0; cycle < 3; cycle++) {
        await page.evaluate(y => scrollTo({ top: y - 900, behavior: 'instant' }), y); await settle();
        let entered = false;
        for (let step = 0; step < 12; step++) {
          await page.mouse.wheel(0, 20); await page.waitForTimeout(45);
          const current = await title.evaluate(node => ({ state: node.dataset.revealState, duration: getComputedStyle(node).transitionDuration, opacity: +getComputedStyle(node).opacity }));
          if (current.state === 'revealing') {
            entered = true; assert.equal(current.duration, '1.2s'); assert.equal(current.opacity, 1);
          }
        }
        assert.ok(entered, 'Bestiary real-wheel entry');
        await page.waitForTimeout(1250);
        assert.equal(await title.evaluate(node => getComputedStyle(node).filter), 'blur(0px)');
        await page.mouse.wheel(0, -20); await page.waitForTimeout(70);
        assert.equal(await title.getAttribute('data-reveal-state'), 'clear', 'Same viewport reversal stays clear');
      }
      await top();
      const other = lang === 'zh' ? 'en' : 'zh';
      await page.locator(`.language-switch button[lang="${other === 'zh' ? 'zh-CN' : 'en'}"]`).click();
      await settle();
      assert.match(await page.locator('.chapter-rail h2 > span').getAttribute('data-reveal-key'), new RegExp(`:${other}$`));
      assert.equal(await page.locator('.chapter-rail h2 > span').evaluate(node => getComputedStyle(node).filter), 'blur(0px)');
      await page.emulateMedia({ reducedMotion: 'reduce' });
      assert.ok(await page.locator('.blur-reveal-text').evaluateAll(nodes => nodes.every(node => getComputedStyle(node).filter === 'none')));
      assert.equal(await page.evaluate(() => document.documentElement.scrollWidth > innerWidth), false);
      assert.deepEqual(errors, []);
      await page.close();
      console.log(`PASS ${name} ${width} ${lang}: eight chapters, no word overlay, bestiary reentry, locale, reduced motion, pagination`);
    }
  } finally { await browser.close(); }
}
