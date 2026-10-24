import assert from 'node:assert/strict';
import { mkdir } from 'node:fs/promises';
import { chromium, firefox, webkit } from 'playwright';

const base = process.env.ATLAS_URL;
if (!base) throw new Error('Run through with-preview.mjs');
const output = new URL('../../output/qa/', import.meta.url);
await mkdir(output, { recursive: true });
const filename = name => new URL(name, output).pathname.replace(/^\/([A-Za-z]:)/, '$1');
const settle = page => page.evaluate(() => new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve))));
async function fits(page, expected) {
  await page.locator(`.onboarding-guide[data-step="${expected}"]`).waitFor();
  if (expected !== 'welcome') await page.locator(`[data-onboarding-target="${expected}"]`).waitFor();
  await settle(page);
  const bounds = await page.evaluate(() => {
    const card = document.querySelector('.onboarding-card'), box = card.getBoundingClientRect();
    const target = document.querySelector('[data-onboarding-target]'), rect = target?.getBoundingClientRect();
    const center = rect && document.elementFromPoint(rect.left + rect.width / 2, rect.top + rect.height / 2);
    return { inside: box.left >= 0 && box.right <= innerWidth + 1 && box.top >= 0 && box.bottom <= innerHeight + 1,
      overlap: rect && Math.min(box.right, rect.right) > Math.max(box.left, rect.left) && Math.min(box.bottom, rect.bottom) > Math.max(box.top, rect.top),
      reachable: !target || target === center || target.contains(center),
      overflow: document.documentElement.scrollWidth > innerWidth,
      buttons: [...card.querySelectorAll('button')].every(node => node.getBoundingClientRect().height >= 44),
      textVisible: card.querySelector('#onboarding-description').getBoundingClientRect().bottom <= card.querySelector('footer').getBoundingClientRect().top + 1,
      shade: document.querySelector('.onboarding-shade > rect').getAttribute('fill'),
      reduced: getComputedStyle(card).animationName === 'none' };
  });
  assert.ok(bounds.inside && !bounds.overlap && bounds.reachable, JSON.stringify(bounds));
  assert.ok(!bounds.overflow && bounds.buttons && bounds.reduced && bounds.textVisible, JSON.stringify(bounds));
  assert.equal(bounds.shade, 'rgba(0,0,0,.64)');
  for (let i = 0; i < 5; i++) {
    await page.keyboard.press('Tab');
    assert.ok(await page.evaluate(() => document.activeElement.closest('.onboarding-card, [data-onboarding-target]')), 'Keyboard focus stays with the guide and real target');
  }
}

for (const name of (process.env.ATLAS_BROWSERS || 'chromium,webkit').split(',')) {
  const browser = await ({ chromium, firefox, webkit }[name]).launch();
  const errors = [];
  const monitor = page => page.on('pageerror', error => errors.push(error.message.replace(/tk=[^&\s]+/g, 'tk=[redacted]')));
  try {
    for (const [width, height] of [[320, 700], [390, 844], [844, 390], [1440, 1000]]) for (const lang of ['zh', 'en']) {
      const context = await browser.newContext({ viewport: { width, height }, reducedMotion: 'reduce', hasTouch: width < 768 });
      const page = await context.newPage(); monitor(page);
      await page.goto(`${base}?lang=${lang}`);
      await fits(page, 'welcome');
      if (name === 'chromium' && width === 390) await page.screenshot({ path: filename(`onboarding-welcome-${lang}.png`) });
      await page.mouse.click(2, 2);
      assert.equal(await page.locator('.onboarding-guide').getAttribute('data-step'), 'welcome', 'Background clicks do not dismiss or navigate');
      await page.locator('.onboarding-next').click();
      for (const step of ['read', 'chapters', 'search', 'modes']) {
        await fits(page, step);
        if (name === 'chromium' && [390, 844, 1440].includes(width) && ['read', 'modes'].includes(step)) await page.screenshot({ path: filename(`onboarding-${step}-${lang}-${width}.png`) });
        assert.equal(await page.locator('.myth-map-wrap').getAttribute('data-map-mode'), 'woodcut', 'Hints never switch map modes');
        await page.locator('.onboarding-next').click();
      }
      await page.locator('.onboarding-guide').waitFor({ state: 'hidden' });
      assert.equal(await page.locator('[data-onboarding-target]').count(), 0);
      assert.equal(await page.evaluate(() => localStorage.getItem('shanhai-onboarding-v1')), '1');
      await page.goto(`${base}?lang=${lang}`); await page.locator('.guide-replay').waitFor();
      assert.equal(await page.locator('.onboarding-guide').count(), 0, 'Completed guidance stays dismissed');
      await page.locator('.guide-replay').click(); await fits(page, 'welcome');
      await page.locator('.onboarding-next').click(); await fits(page, 'read');
      await page.locator('.onboarding-card footer > button').first().click(); await fits(page, 'welcome');
      await page.keyboard.press('Escape'); await page.locator('.onboarding-guide').waitFor({ state: 'hidden' });
      await page.waitForFunction(() => document.activeElement?.matches('.guide-replay'));
      assert.equal(await page.locator('#root').evaluate(node => node.inert), false);
      await context.close();
    }

    for (const width of [390, 1440]) {
      const context = await browser.newContext({ viewport: { width, height: 1000 }, reducedMotion: 'reduce' });
      const page = await context.newPage(); monitor(page);
      await page.goto(base);
      if (width === 1440) {
        await page.locator('.onboarding-language button[lang=en]').click();
        await page.waitForFunction(() => document.documentElement.lang === 'en');
        assert.equal(await page.locator('.onboarding-card h2').textContent(), 'Step into the stories');
        await page.locator('.onboarding-language button[lang=zh-CN]').click();
        await page.waitForFunction(() => document.documentElement.lang === 'zh-CN');
      }
      await page.locator('.onboarding-next').click();
      await page.locator('[data-onboarding-target=read]').click(); await page.locator('.detail-drawer').waitFor();
      assert.equal(await page.locator('.onboarding-guide').count(), 0, 'Original text can be read without a guide overlay');
      await page.locator('.drawer-close').click(); await fits(page, 'chapters');
      await page.locator('[data-onboarding-target=chapters]').click();
      if (width === 390) {
        await page.locator('.explore-sheet').waitFor();
        assert.equal(await page.locator('.onboarding-guide').count(), 0);
        await page.locator('.explore-sheet .timeline-steps button').nth(3).click();
      }
      await fits(page, 'search');
      await page.locator('[data-onboarding-target=search]').click(); await page.locator('.global-search-dialog').waitFor();
      assert.equal(await page.locator('.onboarding-guide').count(), 0);
      await page.locator('.global-search-input').fill('精卫');
      assert.ok(await page.locator('.search-result').count());
      await page.keyboard.press('Escape'); await fits(page, 'modes');
      await page.locator('[data-onboarding-target=modes] button').first().click();
      await page.locator('.onboarding-guide').waitFor({ state: 'hidden' });
      assert.equal(await page.locator('.myth-map-wrap').getAttribute('data-map-mode'), 'woodcut');
      await context.close();
    }

    const context = await browser.newContext({ viewport: { width: 1440, height: 1000 } });
    const page = await context.newPage(); monitor(page);
    await page.goto(`${base}?chapter=03&item=03-04&lang=zh`); await page.locator('.detail-drawer').waitFor();
    assert.equal(await page.locator('.onboarding-guide').count(), 0, 'Direct reading links are not interrupted');
    await page.locator('.drawer-close').click();
    await page.getByLabel('选择地图故事动画').selectOption('03-05');
    await page.locator('.kuafu-journey[data-status=playing]').waitFor();
    await page.waitForFunction(() => Number(document.querySelector('.kuafu-journey')?.dataset.elapsed) > 100);
    await page.locator('.guide-replay').click(); await page.locator('.kuafu-journey[data-status=paused]').waitFor({ state: 'attached' });
    const elapsed = await page.locator('.kuafu-journey').getAttribute('data-elapsed');
    await page.waitForTimeout(200);
    assert.equal(await page.locator('.kuafu-journey').getAttribute('data-elapsed'), elapsed);
    await page.locator('.onboarding-skip').click(); await page.locator('.kuafu-journey[data-status=playing]').waitFor();
    await page.waitForFunction(value => Number(document.querySelector('.kuafu-journey')?.dataset.elapsed) > Number(value), elapsed);
    await context.close();

    const denied = await browser.newContext();
    await denied.addInitScript(() => { Storage.prototype.setItem = () => { throw new Error('Storage unavailable'); }; });
    const fallback = await denied.newPage(); monitor(fallback); await fallback.goto(base);
    await fallback.locator('.onboarding-skip').click(); await fallback.locator('.onboarding-guide').waitFor({ state: 'hidden' });
    await denied.close();
    assert.deepEqual(errors, []);
    console.log(`PASS ${name}: spotlight/real controls, 8 bilingual layouts, keyboard, skip/replay/persistence, modal continuation, deep links, reduced motion, storage failure and playback preservation`);
  } finally { await browser.close(); }
}
