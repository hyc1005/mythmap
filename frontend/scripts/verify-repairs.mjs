import assert from 'node:assert/strict';
import { chromium, firefox, webkit } from 'playwright';

const base = (process.env.ATLAS_URL || 'http://127.0.0.1:5173/').replace(/\/+$/, '') + '/';
const engines = { chromium, firefox, webkit };
for (const name of (process.env.ATLAS_BROWSERS || 'chromium,firefox,webkit').split(',')) {
  const browser = await engines[name].launch();
  try {
    const page = await browser.newPage({ viewport: { width: 390, height: 844 }, reducedMotion: 'reduce' });
    const errors = [];
    page.on('pageerror', error => errors.push(error.message));
    page.on('response', response => {
      if (response.request().resourceType() === 'image' && response.status() !== 304
        && (response.status() >= 400 || response.headers()['content-type']?.includes('text/html'))) errors.push(`Invalid image response: ${response.url()}`);
    });
    await page.goto(`${base}?chapter=03&lang=zh&item=03-04`);
    await page.locator('.detail-drawer').waitFor();
    assert.match(await page.locator('.source-link').getAttribute('href'), /bei-shan-jing/);
    const initialScroll = await page.evaluate(() => scrollY);
    await page.mouse.move(2, 400); await page.mouse.wheel(0, 500);
    await page.waitForTimeout(200);
    assert.equal(await page.evaluate(() => scrollY), initialScroll, 'Modal locks background scroll');
    assert.equal(await page.locator('#root').evaluate(element => element.inert), true);
    await page.getByRole('button', { name: '在地图中查看', exact: true }).click();
    await page.locator('.ink-hover-card').waitFor();
    assert.match(await page.locator('.ink-hover-card').textContent(), /精卫/);
    assert.equal(await page.locator('#root').evaluate(element => element.inert), false);

    await page.goto(`${base}?chapter=01&lang=zh&item=01-03-a`);
    await page.locator('.story-siblings button').nth(1).click();
    await page.locator('.drawer-close').click();
    await page.waitForFunction(() => document.activeElement?.matches('.myth-map-wrap'));

    await page.goto(`${base}?chapter=03&lang=zh`);
    await page.getByRole('button', { name: '连续游历', exact: true }).click();
    await page.locator('.story-animation[data-story="03-04"] .journey-actions').getByRole('button', { name: '跳过', exact: true }).click();
    const journey = page.locator('.kuafu-journey:not(.story-animation)');
    await journey.locator('button').first().waitFor();
    await page.waitForFunction(() => document.querySelector('.kuafu-journey')?.dataset.status === 'reduced');
    await page.waitForTimeout(4200);
    assert.equal(await page.locator('.world-layout').getAttribute('data-chapter'), '03', 'Manual story is not skipped by a timer');
    await page.getByRole('button', { name: '下一幕', exact: true }).click();
    await page.waitForFunction(() => Number(document.querySelector('.kuafu-journey')?.dataset.elapsed) > 0);
    const elapsed = await journey.getAttribute('data-elapsed');
    await page.evaluate(() => { window.reviewViewport = document.querySelector('.ol-viewport'); });
    const before = JSON.parse(await page.locator('.myth-map-canvas').getAttribute('data-view'));
    await page.getByRole('button', { name: 'EN', exact: true }).click();
    assert.equal(await journey.getAttribute('data-elapsed'), elapsed, 'Language keeps story progress');
    assert.equal(await page.evaluate(() => window.reviewViewport === document.querySelector('.ol-viewport')), true, 'Language keeps the map instance');
    const after = JSON.parse(await page.locator('.myth-map-canvas').getAttribute('data-view'));
    assert.ok(Math.abs(before.resolution - after.resolution) < .01);
    for (let i = 0; i < 8 && await journey.count(); i++) {
      const next = journey.getByRole('button', { name: /^(Next scene|Finish story)$/ });
      if (!await next.count()) break;
      await next.click();
    }
    await page.waitForFunction(() => document.querySelector('.world-layout')?.dataset.chapter === '04');
    assert.deepEqual(errors, []);
    await page.goto(`${base}?chapter=06&lang=zh`);
    await page.locator('.mobile-explore-nav button').first().click();
    await page.locator('.timeline-steps button').nth(6).click();
    await page.getByRole('button', { name: '连续游历', exact: true }).click();
    await page.waitForTimeout(1500);
    assert.equal(await page.locator('.world-layout').getAttribute('data-chapter'), '06');
    await page.getByRole('button', { name: '阅读完毕，下一章', exact: true }).click();
    await page.waitForFunction(() => document.querySelector('.world-layout').dataset.chapter === '07');
    await page.waitForTimeout(1500);
    await page.getByRole('button', { name: '结束游历', exact: true }).click();
    await page.getByRole('button', { name: '连续游历', exact: true }).waitFor();
    assert.equal(await page.locator('.world-layout').getAttribute('data-timeline-playing'), 'false', 'Final chapter ends guided tour');
    await page.getByRole('button', { name: '连续游历', exact: true }).click();
    await page.waitForFunction(() => document.querySelector('.world-layout').dataset.chapter === '00');
    await page.getByRole('button', { name: '暂停游历', exact: true }).waitFor();
    await page.close();

    const motion = await browser.newPage({ viewport: { width: 1440, height: 1000 } });
    await motion.goto(`${base}?chapter=02&lang=zh`);
    await motion.getByRole('button', { name: '连续游历', exact: true }).click();
    await motion.locator('.story-animation[data-status="playing"]').waitFor();
    await motion.locator('.begin-journey').click();
    await motion.locator('.story-animation[data-status="paused"]').waitFor();
    await motion.waitForTimeout(200);
    const frozen = await motion.locator('.story-animation').getAttribute('data-elapsed');
    await motion.waitForTimeout(400);
    assert.equal(await motion.locator('.story-animation').getAttribute('data-elapsed'), frozen);
    await motion.locator('.begin-journey').click();
    await motion.locator('.story-animation[data-status="playing"]').waitFor();
    await motion.locator('.story-animation .journey-actions button').first().click();
    await motion.getByRole('button', { name: '继续游历', exact: true }).waitFor();
    await motion.locator('.begin-journey').click();
    await motion.locator('.story-animation[data-status="playing"]').waitFor();
    await motion.locator('.begin-journey').click();
    await motion.locator('.story-animation').getByRole('button', { name: '继续燧人取火', exact: true }).click();
    await motion.getByRole('button', { name: '暂停游历', exact: true }).waitFor();
    await motion.locator('.story-animation[data-status="playing"]').waitFor();
    await motion.goto(`${base}?chapter=00&lang=zh`);
    await motion.getByRole('button', { name: '连续游历', exact: true }).click();
    await motion.locator('.pangu-player-wrap[data-status="playing"]').waitFor();
    await motion.getByRole('button', { name: '暂停盘古序章', exact: true }).click();
    await motion.getByRole('button', { name: '继续游历', exact: true }).waitFor();
    await motion.locator('.begin-journey').click();
    await motion.locator('.pangu-player-wrap[data-status="playing"]').waitFor();
    await motion.locator('.begin-journey').click();
    await motion.getByRole('button', { name: '继续播放盘古序章', exact: true }).click();
    await motion.getByRole('button', { name: '暂停游历', exact: true }).waitFor();
    await motion.locator('.pangu-player-wrap[data-status="playing"]').waitFor();
    await motion.close();

    if (name === 'chromium') {
      for (const [module, chapter, next] of [['PanguOpening', '00', '01'], ['StoryAnimation', '02', '03'], ['KuafuJourney', '03', '04']]) {
        const failure = await browser.newPage();
        await failure.route(`**/assets/${module}-*.js`, route => route.abort());
        await failure.goto(`${base}?chapter=${chapter}&lang=zh`);
        await failure.getByRole('button', { name: '连续游历', exact: true }).click();
        if (module === 'KuafuJourney') await failure.locator('.story-animation').getByRole('button', { name: '跳过', exact: true }).click();
        await failure.locator('.animation-failure').waitFor();
        assert.equal(await failure.locator('main').count(), 1);
        await failure.locator('.animation-failure').getByRole('button', { name: '跳过', exact: true }).click();
        await failure.waitForFunction(next => document.querySelector('.world-layout')?.dataset.chapter === next, next);
        await failure.close();
      }

      const retry = await browser.newPage();
      await retry.route('**/suiren-after-fire-v3.webp', route => route.abort());
      await retry.goto(`${base}?chapter=02&lang=zh`);
      await retry.getByRole('button', { name: '连续游历', exact: true }).click();
      await retry.locator('.story-animation[data-status="error"]').waitFor();
      await retry.waitForTimeout(1300);
      assert.equal(await retry.locator('.world-layout').getAttribute('data-chapter'), '02');
      await retry.unroute('**/suiren-after-fire-v3.webp');
      await retry.getByRole('button', { name: '重新载入', exact: true }).click();
      await retry.locator('.story-animation[data-status="playing"]').waitFor();
      await retry.close();
    }
    console.log(`PASS: ${name} source links, modal scroll/focus, story location, language preservation, manual completion and tour pause.`);
  } finally { await browser.close(); }
}
