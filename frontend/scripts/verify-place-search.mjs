import assert from 'node:assert/strict';
import { readFile, mkdir } from 'node:fs/promises';
import { chromium, firefox, webkit } from 'playwright';
import { searchEntries, searchIndex } from '../src/search.js';
import { geographicReferences, geographicEvents, referenceNarrative } from '../src/geography.js';
import { mockTianditu } from './mock-tianditu.mjs';

const base = process.env.ATLAS_URL;
if (!base) throw new Error('Run through with-preview.mjs');
const read = async path => JSON.parse(await readFile(new URL(path, import.meta.url), 'utf8'));
const [world, catalog, english] = await Promise.all(['../public/data/myth-world.json', '../public/data/atlas/catalog.json', '../src/locale-en.json'].map(read));
const references = geographicReferences(catalog), events = geographicEvents(catalog);
const records = searchIndex(world, catalog, world, catalog).filter(item => item.kind === 'geography');
assert.equal(records.length, references.length);
assert.equal(new Set(records.map(item => item.key)).size, records.length, 'Same city in different events retains separate records');
for (const result of records) assert.ok(references.some(item => item.id === result.referenceId && item.properties.entity_id === result.id));
for (const record of references) for (const lang of ['zh', 'en']) assert.ok(referenceNarrative(record, lang).trim(), `${record.id} has a ${lang} narrative`);
assert.ok(searchEntries(records, '怀来县', 'geography').length > 0);
const englishIndex = searchIndex(world, catalog, world, catalog, 'en', value => english[value] || value);
assert.ok(searchEntries(englishIndex, 'Huailai', 'geography').length > 0);
assert.ok(searchEntries(englishIndex, '怀来县', 'geography').length > 0);
const localizedCandidates = { ...catalog, candidates: catalog.candidates.map(record => ({ ...record, properties: { ...record.properties, label: english[record.properties.label] || record.properties.label } })) };
assert.ok(searchEntries(searchIndex(world, localizedCandidates, world, catalog, 'en', value => english[value] || value), '怀来县', 'geography').length > 0, 'Localized records retain original Chinese names');
const emptyEvents = events.filter(event => !references.some(record => record.properties.entity_id === event.id));
assert.ok(emptyEvents.length);
const output = new URL('../../output/qa/', import.meta.url);
await mkdir(output, { recursive: true });
const filename = name => new URL(name, output).pathname.replace(/^\/([A-Za-z]:)/, '$1');
const settle = async page => {
  await page.evaluate(() => new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve))));
  await page.waitForLoadState('networkidle');
};

for (const name of (process.env.ATLAS_BROWSERS || 'chromium,webkit').split(',')) {
  const browser = await ({ chromium, firefox, webkit }[name]).launch();
  try {
    const context = await browser.newContext({ viewport: { width: 390, height: 844 } });
    const network = await mockTianditu(context);
    let page = await context.newPage();
    const errors = [];
    let phase = 'initial';
    const monitor = target => target.on('pageerror', error => errors.push(`${phase}: ${error.message}`.replace(/tk=[^&\s]+/g, 'tk=[redacted]')));
    monitor(page);
    const visit = async url => { await settle(page); await page.goto(url); };
    const search = page.locator('.global-search-dialog');
    for (const lang of ['zh', 'en']) {
      phase = `search-${lang}`;
      await visit(`${base}?chapter=00&lang=${lang}`);
      await page.locator('.global-search-trigger').click();
      await page.locator('.global-search-input').fill(lang === 'zh' ? '怀来县' : 'Huailai');
      await search.getByLabel(lang === 'zh' ? '搜索范围' : 'Search scope').selectOption('geography');
      const result = search.locator('[data-result-kind="geography"]').first();
      const referenceId = await result.getAttribute('data-reference-id');
      const eventId = await result.getAttribute('data-result-id');
      assert.ok((await result.innerText()).includes(lang === 'zh' ? '不代表事件发生地' : 'not an established event site'));
      if (name === 'chromium') await page.screenshot({ path: filename(`modern-place-search-${lang}.png`) });
      await result.click();
      await page.locator(`.detail-drawer[data-entry-id="${eventId}"]`).waitFor();
      assert.equal(await page.locator('.myth-map-wrap').getAttribute('data-map-mode'), 'woodcut', 'Modern place search starts with the story');
      await page.locator('.detail-open-place').click();
      await page.locator(`[data-candidate-id="${referenceId}"][aria-pressed="true"]`).waitFor();
      await page.waitForFunction(() => document.activeElement === document.querySelector('.geo-detail-heading h3'));
      assert.equal(new URL(page.url()).searchParams.get('event'), eventId);
      assert.equal(new URL(page.url()).searchParams.get('reference'), referenceId);
      assert.equal(await page.locator('.detail-drawer').count(), 0, 'The explicit place action opens geographic evidence');
      assert.ok(await page.locator('.geo-reference').evaluate(node => Boolean(node.querySelector('.geo-place-story').compareDocumentPosition(node.querySelector('.geo-account')) & Node.DOCUMENT_POSITION_FOLLOWING)), 'The story precedes evidence limits');
      assert.equal(await page.locator('.geography-trigger').count(), 0);
      assert.equal(await page.getByRole('button', { name: /复制当前地点资料链接|Copy link to this place record/ }).count(), 0);
      const center = JSON.parse(await page.locator('.geo-map').getAttribute('data-center'));
      const coordinate = references.find(item => item.id === referenceId).geometry.coordinates;
      assert.ok(center.every((value, index) => Math.abs(value - coordinate[index]) < .001), 'Search explicitly locates the source coordinate');
      await settle(page);
      await page.locator('.geo-return-search').click(); await search.waitFor();
      assert.equal(await page.locator('.global-search-input').inputValue(), lang === 'zh' ? '怀来县' : 'Huailai');
      await page.waitForFunction(key => document.activeElement?.dataset.resultKey === key, `geography:${referenceId}`);
      await page.keyboard.press('Escape'); await search.waitFor({ state: 'hidden' });
      await settle(page);
      await page.goBack(); await page.locator('.detail-drawer').waitFor();
      assert.equal(await page.locator('.myth-map-wrap').getAttribute('data-map-mode'), 'woodcut');
      await settle(page); await page.goBack(); await search.waitFor();
      assert.equal(await search.getByLabel(lang === 'zh' ? '搜索范围' : 'Search scope').inputValue(), 'geography');
      await settle(page); await page.goForward(); await page.locator('.detail-drawer').waitFor();
      await page.locator('.return-search').click(); await search.waitFor();
      if (lang === 'en') {
        await page.locator('.global-search-input').fill('怀来县');
        assert.ok(await search.locator('[data-result-kind="geography"]').count(), 'Chinese modern-place aliases work in English');
      }
      await page.locator('.global-search-input').fill(lang === 'zh' ? '桐柏县' : 'Tongbai');
      const pangu = search.locator('[data-result-kind="geography"][data-result-id="01-01"]').first();
      const panguReference = await pangu.getAttribute('data-reference-id');
      await pangu.click();
      await page.locator('.detail-open-place').click();
      await page.locator(`[data-candidate-id="${panguReference}"][aria-pressed="true"]`).waitFor();
      assert.equal(await page.locator('.world-layout').getAttribute('data-chapter'), '00', 'Cross-chapter search keeps the selected prologue reference');
      await settle(page); await page.reload();
      await page.locator(`[data-candidate-id="${panguReference}"][aria-pressed="true"]`).waitFor();
    }

    for (const [width, height] of [[320, 700], [390, 844], [844, 390], [1440, 1000]]) for (const lang of ['zh', 'en']) {
      phase = `layout-${width}-${lang}`;
      await settle(page); await page.close();
      page = await context.newPage(); monitor(page);
      await page.setViewportSize({ width, height });
      const empty = emptyEvents[0];
      await visit(`${base}?chapter=${empty.properties.stage_id}&mode=geography&event=${empty.id}&lang=${lang}`);
      const panel = page.locator('.geo-empty-state');
      await panel.waitFor();
      assert.equal(await page.locator('.geo-result-list button').count(), 0);
      assert.equal(await page.evaluate(() => document.documentElement.scrollWidth > innerWidth), false);
      const readStory = panel.getByRole('button', { name: lang === 'zh' ? '阅读本故事' : 'Read this story', exact: true });
      await readStory.click(); await page.locator(`.detail-drawer[data-entry-id="${empty.id}"]`).waitFor();
      await page.locator('.drawer-close').click(); await page.locator('.detail-drawer').waitFor({ state: 'hidden' });
      await page.waitForFunction(label => document.activeElement?.textContent === label, lang === 'zh' ? '阅读本故事' : 'Read this story');
      await panel.getByRole('button', { name: lang === 'zh' ? '浏览有地点资料的事件' : 'Browse events with place references', exact: true }).click();
      const choices = panel.locator('[data-available-event]');
      assert.ok(await choices.count() > 0);
      for (const id of await choices.evaluateAll(nodes => nodes.map(node => node.dataset.availableEvent))) assert.ok(references.some(record => record.properties.entity_id === id));
      assert.ok(await panel.locator('button').evaluateAll(nodes => nodes.every(node => node.getBoundingClientRect().height >= 44)));
      if (name === 'chromium' && [390, 1440].includes(width)) await panel.screenshot({ path: filename(`geographic-empty-${width}-${lang}.png`) });
      const chosenEvent = await choices.first().getAttribute('data-available-event');
      await choices.first().click();
      await page.waitForFunction(id => document.querySelector('.geography-atlas')?.dataset.eventId === id, chosenEvent);
      await panel.waitFor({ state: 'hidden' });
      await page.waitForFunction(() => document.activeElement === document.querySelector('.geo-map'));
      await settle(page);
      assert.ok(await page.locator('.geo-result-list button').count() > 0);
      const filter = page.locator('.geo-search');
      if (!await filter.evaluate(node => node.open)) await filter.locator('summary').click();
      await page.locator('.geo-search input').fill('no-matching-place-xyz');
      await page.locator('.geo-clear-filter').click();
      assert.equal(await page.locator('.geo-search input').inputValue(), '');
      assert.ok(await page.locator('.geo-result-list button').count() > 0);
    }
    phase = 'tile-failure';
    network.fail = true;
    await visit(`${base}?chapter=03&mode=geography&event=03-01&lang=zh`);
    await page.locator('.geography-atlas [role="alert"]').waitFor();
    assert.equal(await page.locator('.geo-empty-state').count(), 0, 'Tile failure is not mistaken for absent geographic evidence');
    assert.ok(await page.locator('.geo-result-list button').count());
    await settle(page);
    assert.deepEqual(errors, []);
    await context.close();
    console.log(`PASS ${name}: 32 modern reference records, bilingual story-first search/aliases/optional geography/narrative order/location/return/history/reload, actionable empty states and 8 layouts`);
  } finally { await browser.close(); }
}
