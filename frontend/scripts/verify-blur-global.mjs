import { captureBrowserFailure } from './browser-diagnostics.mjs';
import assert from 'node:assert/strict';
import { chromium, webkit } from 'playwright';

const base = process.env.ATLAS_URL;
if (!base) throw new Error('Run through with-preview.mjs');
const settle = page => page.evaluate(() => new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve))));
const clearVisible = async (locator) => {
  const states = await locator.locator('.blur-reveal-text').evaluateAll(nodes => nodes.filter(node => {
    if (typeof node.checkVisibility === 'function' && !node.checkVisibility()) return false;
    const box = node.getBoundingClientRect();
    if (!box.width || !box.height || box.bottom <= 0 || box.top >= innerHeight) return false;
    for (let parent = node.parentElement; parent; parent = parent.parentElement) {
      if (/(auto|scroll|hidden)/.test(getComputedStyle(parent).overflowY)) {
        const bounds = parent.getBoundingClientRect();
        if (box.bottom <= bounds.top || box.top >= bounds.bottom) return false;
      }
    }
    return true;
  }).map(node => ({ text: node.textContent, filter: getComputedStyle(node).filter })));
  for (const state of states) assert.equal(state.filter, 'blur(0px)', `Clear UI landing: ${state.text}`);
};
for (const name of (process.env.ATLAS_BROWSERS || 'chromium,webkit').split(',')) {
  const browser = await ({ chromium, webkit }[name]).launch();
  try {
    for (const [width, height] of [[320, 700], [390, 844], [768, 1024], [844, 390], [1024, 768], [1440, 1000]]) for (const lang of ['zh', 'en']) {
      const page = await browser.newPage({ viewport: { width, height }, reducedMotion: 'no-preference' });
      const errors = [];
      page.on('pageerror', error => { errors.push(error.message); console.error('Global blur page error', error.stack); });
      await page.addInitScript(() => {
        localStorage.setItem('shanhai-onboarding-v1', '1');
        const observers = new Map(), Native = IntersectionObserver;
        window.IntersectionObserver = class extends Native {
          constructor(...args) { super(...args); observers.set(this, new Set()); }
          observe(node) { if (node.classList.contains('blur-reveal-text')) observers.get(this).add(node); super.observe(node); }
          unobserve(node) { observers.get(this)?.delete(node); super.unobserve(node); }
          disconnect() { observers.delete(this); super.disconnect(); }
        };
        window.__blurObserved = () => [...observers.values()].flatMap(nodes => [...nodes]);
      });
      await page.goto(`${base}?chapter=03&lang=${lang}`);
      await page.locator('.world-layout').waitFor(); await settle(page);
      assert.equal(await page.locator('.ink-word').count(), 0);
      await clearVisible(page.locator('body'));
      assert.equal(await page.locator('input .blur-reveal-text, select .blur-reveal-text, .bestiary-tools .blur-reveal-text').count(), 0);
      const readingCopy = page.locator('.reading-notes-copy.blur-reveal-prose');
      assert.equal(await readingCopy.count(), 1, 'The complete reading note animates as one block');
      assert.equal(await readingCopy.locator('p').count(), 5);
      assert.equal(await readingCopy.locator('.blur-reveal-text').count(), 0, 'Paragraphs do not reveal independently inside the note');
      assert.ok(await page.locator('.beast-card').count() <= 12);
      assert.equal(await page.evaluate(() => __blurObserved().filter(node => !node.checkVisibility()).length), 0, `Closed branches do not observe hidden text: ${JSON.stringify(await page.evaluate(() => __blurObserved().filter(node => !node.checkVisibility()).map(node=>({text:node.textContent,key:node.dataset.revealKey,parent:node.parentElement.outerHTML.slice(0,500)}))))}`);
      if (width === 1440 && lang === 'zh') {
        for (const story of ['03-05', '03-04']) {
          await page.getByLabel('选择地图故事动画').selectOption(story);
          await page.locator('.kuafu-journey[data-status="playing"]').waitFor();
          await page.locator('.journey-actions button').first().click();
          await page.locator('.map-mode-switch button').nth(1).click();
          await page.locator('.geography-atlas[data-basemap-state="ready"]').waitFor(); await settle(page);
          assert.equal(await page.evaluate(() => __blurObserved().some(node => node.dataset.revealKey === 'story-title')), false, 'Hidden portal title unregisters');
          await page.locator('.map-mode-switch button').first().click(); await settle(page);
          assert.equal(await page.evaluate(() => __blurObserved().filter(node => !node.checkVisibility()).length), 0, 'Hidden geography releases its text registrations');
          assert.equal(await page.locator('.journey-heading b > .blur-reveal-text').evaluate(node => getComputedStyle(node).filter), 'blur(0px)');
        }
      }
      await page.locator('.global-search-trigger').click();
      await page.locator('.global-search-input').fill('山');
      await page.locator('.search-result').first().waitFor(); await settle(page);
      assert.equal(await page.locator('.search-result').count(), await page.locator('.search-result b > .blur-reveal-text').count());
      await clearVisible(page.locator('.global-search-dialog'));
      await page.locator('.global-search-results').evaluate(node => { node.scrollTop = node.scrollHeight; }); await settle(page);
      await page.locator('.global-search-input').fill(lang === 'zh' ? '女娲' : 'Nuwa'); await settle(page);
      await clearVisible(page.locator('.global-search-dialog'));
      await page.keyboard.press('Escape');
      if (width <= 768) await page.locator('.mobile-explore-nav button').nth(1).click();
      const entries = page.locator(width <= 768 ? '.explore-sheet .chapter-entries' : '.chapter-rail .chapter-entries');
      const library = entries.locator('.chapter-library');
      await library.locator(':scope > summary').click(); await settle(page);
      const book = library.locator('[data-source-book="1"]');
      await book.locator(':scope > summary').click(); await settle(page);
      const range = book.locator('.passage-range').first();
      await range.locator(':scope > summary').click(); await settle(page);
      await clearVisible(entries);
      assert.ok(await range.locator('b > .blur-reveal-text').count());
      if (width <= 768) await page.keyboard.press('Escape');
      await page.goto(`${base}?chapter=03&item=03-01&lang=${lang}`);
      await page.waitForFunction(() => document.querySelector('.detail-drawer')?.dataset.readingRestoring === 'false'); await settle(page);
      const drawer = page.locator('.detail-drawer');
      for (const anchor of ['title', 'quote', 'location', 'notes']) assert.equal(await drawer.locator(`[data-reading-anchor="${anchor}"] > .blur-reveal-text`).count(), 1);
      assert.ok(await drawer.locator('[data-reading-anchor="source"] .blur-reveal-text').count() > 0, 'Source group keeps its revealed summary');
      await clearVisible(drawer);
      await page.keyboard.press('Control+f'); await settle(page); await clearVisible(drawer);
      await page.emulateMedia({ media: 'print' });
      assert.ok(await drawer.locator('.blur-reveal-text').evaluateAll(nodes => nodes.every(node => getComputedStyle(node).filter === 'none')));
      await page.emulateMedia({ media: 'screen', reducedMotion: 'reduce' });
      assert.ok(await drawer.locator('.blur-reveal-text').evaluateAll(nodes => nodes.every(node => getComputedStyle(node).filter === 'none')));
      assert.equal(await page.evaluate(() => document.documentElement.scrollWidth > innerWidth), false);
      assert.deepEqual(errors, []);
      await page.close();
      console.log(`PASS ${name} ${width}x${height} ${lang}: global title matrix, search/filter, nested expansion, clear landing/find/print/reduced motion`);
    }
  } catch (error) {
    await captureBrowserFailure(browser, `blur-global-${name}`, error);
    throw error;
  } finally { await browser.close(); }
}
