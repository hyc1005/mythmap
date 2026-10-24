import assert from 'node:assert/strict';
import { mkdir, readFile } from 'node:fs/promises';
import { chromium, firefox, webkit } from 'playwright';
import { storySummary } from '../src/story-summaries.js';
import { readGeography, explorationUrl } from '../src/exploration.js';
import { geographicReferences } from '../src/geography.js';
import { mockTianditu } from './mock-tianditu.mjs';

const base = process.env.ATLAS_URL;
if (!base) throw new Error('Run through with-preview.mjs');
const catalog = JSON.parse(await readFile(new URL('../public/data/atlas/catalog.json', import.meta.url), 'utf8'));
const references = geographicReferences(catalog);
for (const event of catalog.events.filter(event => catalog.stages.some(stage => stage.id === event.properties.stage_id) && !['archive', 'group'].includes(event.properties.presentation))) {
  for (const lang of ['zh', 'en']) assert.ok(storySummary(event.id, lang), `${event.id}: ${lang} overview`);
}
assert.deepEqual(readGeography('?mode=geography&event=invalid&reference=invalid', '03', catalog, references), { open: true, eventId: null, referenceId: null });
const reference = references.find(item => item.properties.entity_id === '03-04');
assert.ok(reference);
const link = explorationUrl(base, '03', null, 'zh', { open: true, eventId: '03-04', referenceId: reference.id });
assert.equal(readGeography(link.search, '03', catalog, references).referenceId, reference.id);
assert.equal(readGeography(link.search, '04', catalog, references).referenceId, null, 'Foreign-event references are ignored');
assert.equal(explorationUrl(link, '03', null, 'en').searchParams.has('reference'), false);
const output = new URL('../../output/qa/', import.meta.url);
await mkdir(output, { recursive: true });
const filename = name => new URL(name, output).pathname.replace(/^\/([A-Za-z]:)/, '$1');

for (const name of (process.env.ATLAS_BROWSERS || 'chromium,webkit').split(',')) {
  const browser = await ({ chromium, firefox, webkit }[name]).launch();
  try {
    const context = await browser.newContext({ viewport: { width: 390, height: 844 }, reducedMotion: 'reduce' });
    await mockTianditu(context);
    const page = await context.newPage(), errors = [];
    let phase = 'search';
    page.on('pageerror', error => errors.push({ phase, message: (error.stack || error.message).replace(/tk=[^&\s]+/g, 'tk=[redacted]') }));
    const settle = async target => {
      await target.evaluate(() => new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve))));
      await target.waitForLoadState('networkidle');
    };
    const visit = async url => { await settle(page); await page.goto(url); };
    const search = page.locator('.global-search-dialog');
    await visit(`${base}?chapter=03&lang=zh`);
    await page.locator('.global-search-trigger').click();
    await page.locator('.global-search-input').fill('精卫');
    await search.getByLabel('搜索范围').selectOption('story');
    await search.locator('[data-result-id="03-04"]').click();
    await page.locator('.detail-drawer[data-entry-id="03-04"]').waitFor();
    assert.match(await page.locator('.story-summary').innerText(), /女娃.*东海/);
    await page.locator('.return-search').click();
    await search.waitFor();
    assert.equal(await page.locator('.global-search-input').inputValue(), '精卫');
    assert.equal(await search.getByLabel('搜索范围').inputValue(), 'story');
    await page.waitForFunction(() => document.activeElement?.dataset.resultId === '03-04');
    await page.goBack();
    await search.waitFor({ state: 'hidden' });
    await page.goForward();
    await search.waitFor();
    await page.goForward();
    await page.locator('.detail-drawer[data-entry-id="03-04"]').waitFor();
    await page.locator('.drawer-close').click();
    await search.waitFor();
    await page.keyboard.press('Escape');
    await search.waitFor({ state: 'hidden' });
    assert.equal(await page.locator('#root').evaluate(node => node.inert), false);

    await page.locator('.global-search-trigger').click();
    await search.getByLabel('搜索范围').selectOption('all');
    await page.locator('.global-search-input').fill('山海经');
    const more = search.locator('.search-more');
    if (await more.count()) await more.click();
    const last = search.locator('.search-result:not([data-result-kind="geography"])').last();
    await last.scrollIntoViewIfNeeded();
    const scroll = await search.locator('.global-search-results').evaluate(node => node.scrollTop);
    const lastId = await last.getAttribute('data-result-id');
    await last.click();
    await page.locator(`.detail-drawer[data-entry-id="${lastId}"]`).waitFor();
    await page.locator('.return-search').click();
    await search.waitFor();
    await page.waitForFunction(expected => Math.abs(document.querySelector('.global-search-results').scrollTop - expected) < 2, scroll);
    await page.keyboard.press('Escape');
    await search.waitFor({ state: 'hidden' });

    phase = 'geography';
    await visit(`${base}?chapter=03&item=03-04&lang=zh`);
    await page.getByRole('button', { name: '在地图中查看', exact: true }).click();
    await page.getByRole('button', { name: '真实地理', exact: true }).click();
    await page.waitForFunction(() => document.querySelector('.geography-atlas')?.dataset.eventId === '03-04');
    await page.locator(`[data-candidate-id="${reference.id}"]`).click();
    await page.waitForFunction(id => new URL(location.href).searchParams.get('reference') === id, reference.id);
    assert.equal(new URL(page.url()).searchParams.get('event'), '03-04');
    await page.locator('.global-search-trigger').click();
    await page.locator('.global-search-input').fill('盘古');
    await search.getByLabel('搜索范围').selectOption('story');
    await search.locator('[data-result-id="01-01"]').click();
    await page.locator('.detail-drawer[data-entry-id="01-01"]').waitFor();
    assert.equal(new URL(page.url()).searchParams.get('event'), '01-01', 'Cross-chapter details produce a valid event link');
    await page.locator('.return-search').click();
    await search.waitFor();
    await page.keyboard.press('Escape');
    await search.waitFor({ state: 'hidden' });
    await page.locator(`[data-candidate-id="${reference.id}"][aria-pressed="true"]`).waitFor();
    assert.equal(new URL(page.url()).searchParams.get('event'), '03-04', 'Returning restores the background geographic event');
    assert.equal(await page.locator('.geo-share-status').count(), 0);
    const shared = page.url();
    await settle(page);
    phase = 'reload';
    await page.reload();
    await page.waitForFunction(() => document.querySelector('.myth-map-wrap')?.dataset.mapMode === 'geography');
    await page.locator(`[data-candidate-id="${reference.id}"][aria-pressed="true"]`).waitFor();
    assert.ok((await page.locator('.geo-detail-heading').innerText()).includes(reference.properties.label));
    const tab = await context.newPage();
    phase = 'shared tab';
    await tab.goto(shared);
    await tab.locator(`[data-candidate-id="${reference.id}"][aria-pressed="true"]`).waitFor();
    await settle(tab);
    await tab.close();
    await settle(page);
    phase = 'mode history';
    await page.getByRole('button', { name: '木刻叙事', exact: true }).click();
    await page.goBack();
    await page.waitForFunction(() => document.querySelector('.myth-map-wrap')?.dataset.mapMode === 'geography');

    for (const [width, height] of [[320, 700], [390, 844], [844, 390], [1440, 1000]]) {
      for (const lang of ['zh', 'en']) {
        phase = `layout ${width} ${lang}`;
        await settle(page);
        await page.setViewportSize({ width, height });
        await visit(`${base}?chapter=03&lang=${lang}`);
        await page.evaluate(() => document.fonts.ready);
        assert.equal(await page.evaluate(() => document.documentElement.scrollWidth > innerWidth), false, `${width} ${lang}: body fits`);
        const nav = page.locator('.mobile-explore-nav');
        if (width <= 768) {
          assert.ok(await nav.evaluate(node => node.getBoundingClientRect().bottom <= document.querySelector('.map-surface').getBoundingClientRect().top));
          await page.getByRole('button', { name: lang === 'zh' ? '真实地理' : 'Real geography', exact: true }).click();
          await page.locator('.geo-result-actions').scrollIntoViewIfNeeded();
          assert.ok(await nav.evaluate(node => node.getBoundingClientRect().top >= -1 && node.getBoundingClientRect().bottom <= innerHeight), 'Navigation stays reachable while reading geographic data');
          await nav.locator('button').first().click();
          await page.locator('.explore-sheet').waitFor();
          await page.keyboard.press('Escape');
        }
        await visit(`${base}?chapter=03&item=03-04&lang=${lang}`);
        await page.locator('.story-summary').waitFor();
        assert.equal(await page.locator('.detail-drawer').evaluate(node => node.scrollWidth > node.clientWidth), false);
        if (name === 'chromium' && lang === 'zh' && [390, 1440].includes(width)) await page.screenshot({ path: filename(`ux-overview-${width}.png`) });
      }
    }
    await visit(`${base}?chapter=03&lang=zh`);
    await page.locator('.timeline-steps button').nth(5).click();
    await page.waitForFunction(() => document.querySelector('.world-layout').dataset.chapter === '05');
    await page.goBack();
    await page.waitForFunction(() => document.querySelector('.world-layout').dataset.chapter === '03');
    assert.deepEqual(errors, []);
    await context.close();
    console.log(`PASS ${name}: event continuity, search return/history/scroll/focus, bilingual overviews, geographic deep links/reload, sticky mobile navigation and 8 layouts`);
  } finally { await browser.close(); }
}
