import assert from 'node:assert/strict';
import { mkdir, readFile, stat } from 'node:fs/promises';
import { chromium, firefox, webkit } from 'playwright';
import { worldEntries } from '../src/entries.js';
import { searchEntries, searchIndex } from '../src/search.js';
import { readExploration } from '../src/exploration.js';
import { entryRelations, relatedEntries } from '../src/entry-relations.js';
import { mockTianditu } from './mock-tianditu.mjs';

const base = process.env.ATLAS_URL;
if (!base) throw new Error('Run through with-preview.mjs');
const json = async path => JSON.parse(await readFile(new URL(path, import.meta.url), 'utf8'));
const [world, catalog, english, manifest] = await Promise.all(['../public/data/myth-world.json', '../public/data/atlas/catalog.json', '../src/locale-content-en.json', '../public/data/atlas/artwork-manifest.json'].map(json));
const firstBatchIds = ['place-zhaoyao', 'place-niuyang', 'plant-zhuyu', 'plant-migu', 'water-liji', 'water-guai', 'water-xianyi', 'water-ying-qingqiu', 'water-jiyi', 'material-yupei', 'beast-guanguan'];
const index = new Map(worldEntries(world).map(item => [item.id, item]));
const newEntries = [...index.values()].filter(item => item.content_batch === 'nanshan-entities');
const coverage = await json('../../data/nanshan-entity-coverage.json');
const generation = await json('../artwork-source/nanshan/entities-generation.json');
const jobs = new Map(generation.assets.map(asset => [`nanshan/${asset.name}-v1.webp`, asset]));
const ids = [...firstBatchIds, ...newEntries.map(item => item.id)];
assert.equal(newEntries.length, 97);
assert.equal(coverage.mountain_ids.length, 39);
assert.equal(new Set(coverage.mountain_ids).size, 39);
for (const id of coverage.mountain_ids) assert.equal(index.get(id)?.kind, 'place', id);
for (const entry of newEntries) {
  assert.ok(!('x' in entry || 'y' in entry || 'coordinates' in entry), `${entry.id}: no invented coordinates`);
  assert.ok(entry.source_passage_ids.every(id => relatedEntries(entry.id, index).some(item => item.id === id)), `${entry.id}: source passage links`);
  if (entry.artwork && jobs.has(entry.artwork)) assert.equal(jobs.get(entry.artwork).status, 'reviewed', `${entry.id}: only reviewed art is published`);
  if (entry.artwork_pending) assert.ok(!entry.artwork && entry.planned_artwork, `${entry.id}: pending art has no runtime URL`);
}
assert.equal(world.beasts.filter(item => item.region === '南山经').length, 23);
assert.equal(index.get('beast-guan').name, '讙');
assert.equal(index.get('beast-guanguan').name, '灌灌');
assert.equal(world.natural_features.filter(item => item.region === '南山经').length, 35);
const search = searchIndex(world, catalog, world, catalog);
for (const id of ids) {
  const entry = index.get(id);
  assert.ok(entry?.quote && entry.source_locator && entry.source_pages.length && entry.editorial_note, id);
  assert.ok(english[id]?.description && english[id]?.quote && english[id]?.source_locator, `${id}: English content`);
  assert.ok(searchEntries(search, entry.name, entry.kind).some(item => item.id === id), `${id}: Chinese-name search`);
  assert.equal(readExploration(`?chapter=03&item=${id}`, world, catalog).item, id);
  assert.ok(entry.source.includes('四部丛刊'));
}
assert.ok(!index.get('material-yupei').artwork);
assert.ok(index.get('material-yupei').commentary_quote.includes('未詳'));
assert.ok(!index.get('water-xianyi').place_id, 'Confluence target is not assigned a mountain habitat');
for (const entry of world.natural_features) assert.ok(!('x' in entry || 'y' in entry));
for (const relation of entryRelations.filter(r => r.labels)) {
  const sources = relation.ids.flatMap(id => {
    const entry = index.get(id);
    return [entry, ...(entry?.source_passage_ids || []).map(id => index.get(id))];
  });
  assert.ok(sources.some(entry => entry?.quote?.includes(relation.quote)), `${relation.ids}: exact quotation evidence in card or its source passage`);
}
const artworkPaths = [...new Set([...firstBatchIds, 'place-qingqiu'].map(id => index.get(id).artwork).filter(path => path?.includes('nanshan/')))];
assert.equal(artworkPaths.length, 6);
for (const path of artworkPaths) for (const variant of ['full', 'preview', 'card']) {
  const asset = manifest.assets.find(asset => asset.destination.endsWith(path)).variants[variant];
  assert.equal((await stat(new URL('../public' + asset.path, import.meta.url))).size, asset.bytes);
}
await mkdir(new URL('../../output/qa/', import.meta.url), { recursive: true });
for (const name of (process.env.ATLAS_BROWSERS || 'chromium,webkit').split(',')) {
  const browser = await ({ chromium, firefox, webkit }[name]).launch();
  try {
    const context = await browser.newContext({ viewport: { width: 390, height: 844 }, reducedMotion: 'reduce' });
    await mockTianditu(context);
    const page = await context.newPage(), errors = [], requests = [], failed = [];
    page.on('pageerror', e => errors.push(e.message));
    page.on('request', r => requests.push(r.url()));
    page.on('response', r => { if (r.status() >= 400 && r.url().startsWith(base)) failed.push(r.url()); });
    await page.goto(`${base}?lang=zh`);
    await page.locator('.onboarding-skip').click();
    assert.equal(requests.filter(url => /nanshan\/.*-v1\.webp/.test(url)).length, 0, 'First screen does not fetch full batch artwork');
    const drawer = page.locator('.detail-drawer');
    const ready = async id => {
      await page.waitForFunction(id => {
        const node = document.querySelector('.detail-drawer');
        return node?.dataset.entryId === id && node.dataset.readingRestoring === 'false';
      }, id);
    };
    for (const lang of ['zh', 'en']) {
      for (const id of ids) {
        await page.goto(`${base}?chapter=03&item=${id}&lang=${lang}`);
        await ready(id);
        assert.equal(await drawer.locator('>.content-origin').getAttribute('data-origin'), 'shanhaijing');
        assert.equal(await drawer.evaluate(node => node.scrollWidth > node.clientWidth), false, `${id} ${lang}: drawer width`);
        if (lang === 'en') assert.equal(await drawer.locator('.detail-description').innerText(), english[id].description);
        if (!index.get(id).artwork) {
          assert.equal(await drawer.locator('img').count(), 0, `${id}: no invented illustration`);
          assert.equal(await drawer.locator('.artwork-pending').count(), 0);
        }
        else {
          console.log(`Checking Southern artwork ${id} ${lang}`);
          await page.waitForFunction(() => {
            const img = document.querySelector('.detail-drawer .drawer-art');
            return img?.complete && img.naturalWidth > 0;
          });
          await drawer.locator('.drawer-art').evaluate(img => img.decode());
          await drawer.locator('.drawer-art').scrollIntoViewIfNeeded();
          assert.ok(await drawer.locator('.drawer-art').evaluate(img => img.complete && img.naturalWidth > 0), `${id}: image loaded`);
        }
        for (const action of [0, 1]) {
          const button = drawer.locator('.detail-reading-actions button').nth(action);
          await button.scrollIntoViewIfNeeded();
          await button.waitFor({ state: 'visible' });
          assert.ok(await button.isEnabled(), `${id} ${lang}: reading action enabled`);
          await button.focus();
          await page.keyboard.press('Space');
          await page.waitForFunction(({ action, expected }) => document.querySelectorAll('.detail-drawer .detail-reading-actions button')[action]?.getAttribute('aria-pressed') === expected,
            { action, expected: lang === 'zh' ? 'true' : 'false' });
        }
        await page.reload(); await ready(id);
        assert.ok(await drawer.locator('.detail-reading-actions button').evaluateAll(nodes => nodes.every(n => n.getAttribute('aria-pressed') === (document.documentElement.lang === 'en' ? 'false' : 'true'))), 'New marks persist and can be toggled in both languages');
      }
      await page.goto(`${base}?chapter=02&item=place-qingqiu&lang=${lang}`); await ready('place-qingqiu');
      await drawer.locator('[data-related-id="beast-guanguan"]').click(); await ready('beast-guanguan');
      assert.equal(new URL(page.url()).searchParams.get('chapter'), '02', 'Related reading preserves chapter');
      await page.reload(); await ready('beast-guanguan');
      assert.equal(await page.locator('.world-layout').getAttribute('data-chapter'), '02');
      assert.equal(await page.locator('.myth-map-wrap').getAttribute('data-map-mode'), 'woodcut');
      await drawer.locator('[data-related-id="place-qingqiu"]').click(); await ready('place-qingqiu');
      await page.goBack(); await ready('beast-guanguan');
      await page.goto(`${base}?chapter=02&item=place-zhaoyao&lang=${lang}`); await ready('place-zhaoyao');
      await drawer.locator('[data-related-id="plant-zhuyu"]').click(); await ready('plant-zhuyu');
      await drawer.locator('.return-related').click(); await ready('place-zhaoyao');
      await drawer.locator('[data-related-id="water-liji"]').click(); await ready('water-liji');
      await drawer.locator('[data-related-id="material-yupei"]').click(); await ready('material-yupei');
      await drawer.locator('[data-reading-anchor="source"]').scrollIntoViewIfNeeded();
      await page.waitForTimeout(250);
      await page.goto(`${base}?lang=${lang}`);
      await page.locator('.resume-reading').click(); await ready('material-yupei');
      assert.ok(await drawer.evaluate(node => node.scrollTop > 0), 'Natural entries support resume');
      await page.goto(`${base}?chapter=02&lang=${lang}`);
      await page.locator('.global-search-trigger').click();
      await page.locator('.global-search-input').fill('迷谷');
      await page.locator('.global-search-tools select').selectOption('plant');
      await page.locator('.search-result[data-result-id="plant-migu"]').click(); await ready('plant-migu');
      await drawer.locator('.return-search').click();
      assert.equal(await page.locator('.global-search-input').inputValue(), '迷谷');
      for (const kind of ['place', 'beast', 'water', 'plant', 'animal', 'valley', 'wind', 'deity', 'rite']) {
        const entry = newEntries.find(item => item.kind === kind);
        await page.locator('.global-search-tools select').selectOption(kind);
        await page.locator('.global-search-input').fill(entry.name);
        await page.locator(`.search-result[data-result-id="${entry.id}"]`).click(); await ready(entry.id);
        await drawer.locator('.return-search').click();
      }
      await page.goto(`${base}?chapter=02&item=water-nanshan-fang&lang=${lang}`); await ready('water-nanshan-fang');
      await drawer.locator('[data-related-id="water-nanshan-yu-receiver"]').click(); await ready('water-nanshan-yu-receiver');
      await page.goBack(); await ready('water-nanshan-fang');
      for (const place of ['tangting', 'fashuang']) {
        await page.goto(`${base}?chapter=02&item=place-nanshan-${place}&lang=${lang}`); await ready(`place-nanshan-${place}`);
        await drawer.locator('.detail-place-contents [data-related-id="animal-nanshan-white-ape"]').click(); await ready('animal-nanshan-white-ape');
        await drawer.locator('.return-related').click(); await ready(`place-nanshan-${place}`);
      }
      await page.goto(`${base}?chapter=02&item=deity-nanshan-3&lang=${lang}`); await ready('deity-nanshan-3');
      await drawer.locator('[data-reading-anchor="source"]').scrollIntoViewIfNeeded();
      await page.waitForTimeout(250);
      await page.goto(`${base}?lang=${lang}`);
      await page.locator('.resume-reading').click(); await ready('deity-nanshan-3');
      assert.ok(await drawer.evaluate(node => node.scrollTop > 0), 'New entity supports resume');
      const directoryIds = new Set();
      for (const chapter of ['02', '03']) {
        await page.goto(`${base}?chapter=${chapter}&lang=${lang}`);
        await page.locator('.mobile-explore-nav button').nth(1).click();
        const entries = page.locator('.chapter-entries:visible');
        for (const id of await entries.locator('[data-entry-id]').evaluateAll(nodes => nodes.map(node => node.dataset.entryId))) directoryIds.add(id);
        if (chapter === '02') {
          assert.ok(await entries.locator('.entry-kind-group').count() >= 8, 'Large directory groups entities by kind');
          const button = entries.locator('[data-entry-id="deity-nanshan-3"]');
          await button.evaluate(node => { for (let parent = node.parentElement; parent; parent = parent.parentElement) if (parent.tagName === 'DETAILS') parent.open = true; });
          await button.click(); await ready('deity-nanshan-3');
        }
      }
      for (const entry of newEntries) assert.ok(directoryIds.has(entry.id), `${entry.id}: chapter directory entry`);
    }
    for (const [width, height] of [[320, 700], [390, 844], [844, 390], [1440, 1000]]) for (const lang of ['zh', 'en']) {
      await page.setViewportSize({ width, height });
      await page.goto(`${base}?chapter=02&item=place-nanshan-daoguo&lang=${lang}`); await ready('place-nanshan-daoguo');
      assert.equal(await drawer.evaluate(node => node.scrollWidth > node.clientWidth), false);
      assert.ok(await drawer.locator('.detail-place-contents button').evaluateAll(nodes => nodes.every(n => n.getBoundingClientRect().height >= 44)));
      if (name === 'chromium' && width === 390) await page.screenshot({ path: new URL(`../../output/qa/nanshan-${lang}.png`, import.meta.url).pathname.replace(/^\/([A-Za-z]:)/, '$1') });
    }
    assert.deepEqual(errors, []);
    assert.deepEqual(failed, [], 'No missing artwork or same-origin resources');
    await context.close();
    console.log(`PASS ${name}: 11 original + 97 new entries, 39 mountains, bilingual search, reviewed artwork, persistent marks, water/multi-place relations, history/refresh/resume and 8 layouts`);
  } finally { await browser.close(); }
}
