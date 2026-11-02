import assert from 'node:assert/strict';
import { chromium, webkit } from 'playwright';

const base = process.env.ATLAS_URL;
if (!base) throw new Error('Run through with-preview.mjs');
const ready = page => page.waitForFunction(() => {
  const node = document.querySelector('.detail-drawer');
  return node?.dataset.readingRestoring === 'false' && [...node.querySelectorAll('img')].every(image => image.complete);
});
const settle = page => page.evaluate(() => new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve))));
const visibleHeadings = page => page.locator('.detail-drawer').evaluate(root => {
  const bounds = root.getBoundingClientRect();
  return [...root.querySelectorAll('.blur-reveal-text')].filter(node => {
    const box = node.getBoundingClientRect();
    return box.bottom > Math.max(0, bounds.top + root.clientTop) && box.top < Math.min(innerHeight, bounds.top + root.clientTop + root.clientHeight);
  }).map(node => ({ text: node.textContent, filter: getComputedStyle(node).filter, opacity: getComputedStyle(node).opacity }));
});
const clearVisible = async page => {
  for (const item of await visibleHeadings(page)) {
    assert.equal(item.filter, 'blur(0px)', `${item.text}: reading position stays clear`);
    assert.equal(item.opacity, '1');
  }
};
for (const name of (process.env.ATLAS_BROWSERS || 'chromium,webkit').split(',')) {
  const browser = await ({ chromium, webkit }[name]).launch();
  try {
    for (const width of [390, 1440]) for (const lang of ['zh', 'en']) {
      const page = await browser.newPage({ viewport: { width, height: 844 }, reducedMotion: 'no-preference' });
      const errors = [];
      page.on('pageerror', error => errors.push(error.message));
      await page.goto(`${base}?chapter=03&item=03-01&lang=${lang}`);
      await ready(page); await settle(page);
      const drawer = page.locator('.detail-drawer');
      const title = drawer.locator('[data-reading-anchor="title"] > span');
      assert.equal(await title.getAttribute('data-reveal-key'), `detail:03-01:title:${lang}`);
      await clearVisible(page);
      assert.equal(await drawer.locator('p .blur-reveal-text, blockquote .blur-reveal-text, [data-reading-anchor="source"] .blur-reveal-text, [data-reading-anchor="quote"] .blur-reveal-text').count(), 0);
      assert.equal(await drawer.evaluate(node => getComputedStyle(node).filter), 'none', 'No whole-drawer filter');
      const pagePosition = await page.evaluate(() => scrollY);
      const bounds = await drawer.boundingBox();
      await page.mouse.move(bounds.x + bounds.width - 8, bounds.y + bounds.height / 2);
      const targets = [title];
      const sectionHeading = drawer.locator('.story-summary h3 > .blur-reveal-text');
      if (await sectionHeading.count()) targets.push(sectionHeading);
      for (const target of targets) for (let cycle = 0; cycle < (target === title ? 3 : 1); cycle++) {
        await target.evaluate(node => {
          const root = node.closest('.detail-drawer');
          root.scrollTop += node.getBoundingClientRect().bottom - root.getBoundingClientRect().top + 100;
        });
        await settle(page);
        assert.equal(await target.getAttribute('data-reveal-state'), 'waiting', 'Heading fully left the drawer');
        let entered = false;
        for (let step = 0; step < 45; step++) {
          await page.mouse.wheel(0, -20); await page.waitForTimeout(40);
          if (await target.getAttribute('data-reveal-state') === 'revealing') { entered = true; break; }
        }
        assert.ok(entered, 'Real drawer wheel reentry');
        assert.equal(await target.evaluate(node => getComputedStyle(node).transitionDuration), '1.5s');
        assert.equal(await target.evaluate(node => getComputedStyle(node).opacity), '1');
        await page.waitForTimeout(1550);
        assert.equal(await target.evaluate(node => getComputedStyle(node).filter), 'blur(0px)');
        await page.mouse.wheel(0, 5); await settle(page);
        assert.equal(await target.getAttribute('data-reveal-state'), 'clear', 'Direction reversal keeps clear text');
        assert.equal(await page.evaluate(() => scrollY), pagePosition, 'Drawer scroll does not move the page');
      }
      const quote = await drawer.locator('blockquote').first().textContent();
      await drawer.evaluate(node => {
        const target = node.querySelector('[data-reading-anchor="source"]');
        node.scrollTop += target.getBoundingClientRect().top - node.getBoundingClientRect().top - 100;
      });
      await page.waitForTimeout(300);
      let savedTop = await drawer.evaluate(node => node.scrollTop);
      await page.reload(); await ready(page); await settle(page);
      assert.ok(Math.abs(await drawer.evaluate(node => node.scrollTop) - savedTop) <= 3, 'Reload preserves reading position');
      await clearVisible(page);
      assert.equal(await drawer.locator('blockquote').first().textContent(), quote);
      if (await drawer.locator('.story-summary h3').count()) {
        await drawer.evaluate(node => {
          const target = node.querySelector('.story-summary h3');
          node.scrollTop += target.getBoundingClientRect().top - node.getBoundingClientRect().top - 20;
        });
        await page.waitForTimeout(300);
        savedTop = await drawer.evaluate(node => node.scrollTop);
        await page.reload(); await ready(page); await settle(page);
        assert.ok(Math.abs(await drawer.evaluate(node => node.scrollTop) - savedTop) <= 3, 'Reload preserves the description-heading position');
        assert.ok((await visibleHeadings(page)).length > 0, 'Restored animated heading is actually visible');
        await clearVisible(page);
      }

      await drawer.locator('.drawer-close').click();
      await drawer.waitFor({ state: 'detached' });
      await page.locator('.resume-reading').click(); await ready(page); await settle(page);
      assert.ok(Math.abs(await drawer.evaluate(node => node.scrollTop) - savedTop) <= 3, 'Resume preserves reading position');
      await clearVisible(page);
      await drawer.locator('.detail-entry-nav button').last().click();
      await page.waitForFunction(() => document.querySelector('.detail-drawer')?.dataset.entryId !== '03-01');
      await ready(page); await settle(page);
      await clearVisible(page);
      await page.goto(`${base}?chapter=07&item=beast-beishan-huayu-qiuru&lang=${lang}`);
      await ready(page); await settle(page);
      const options = await drawer.locator('.detail-namesakes option').evaluateAll(nodes => nodes.map(node => node.value));
      assert.ok(options.length > 1, 'Independent namesake accounts available');
      const other = options.find(id => id !== 'beast-beishan-huayu-qiuru');
      await drawer.evaluate(node => { node.scrollTop = node.scrollHeight; });
      await drawer.locator('.detail-namesakes select').selectOption(other);
      await page.waitForFunction(id => document.querySelector('.detail-drawer')?.dataset.entryId === id, other);
      await ready(page); await settle(page);
      assert.equal(await drawer.locator('[data-reading-anchor="title"] > span').getAttribute('data-reveal-key'), `detail:${other}:title:${lang}`);
      await clearVisible(page);
      assert.equal(await drawer.locator('[data-reading-anchor="description"] > .blur-reveal-text').count(), 1);
      assert.equal(await drawer.locator('.detail-description').evaluate(node => getComputedStyle(node).filter), 'none');
      await page.keyboard.press('Control+f');
      await clearVisible(page);
      await page.emulateMedia({ reducedMotion: 'reduce' });
      assert.ok(await drawer.locator('.blur-reveal-text').evaluateAll(nodes => nodes.every(node => getComputedStyle(node).filter === 'none')));
      assert.equal(await drawer.evaluate(node => node.scrollWidth > node.clientWidth), false);
      assert.deepEqual(errors, []);
      await page.close();
      console.log(`PASS ${name} ${width} ${lang}: drawer title/section reentry, page isolation, reload/resume, next entry, namesakes, clear body, find and reduced motion`);
    }
  } finally { await browser.close(); }
}
