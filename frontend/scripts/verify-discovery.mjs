import assert from 'node:assert/strict';
import { mkdir, readFile } from 'node:fs/promises';
import { chromium, firefox, webkit } from 'playwright';
import { searchEntries, searchIndex, highlightTerms } from '../src/search.js';
import { animationForEvent } from '../src/chapter-stories.js';
import { entryRelations, relatedEntries } from '../src/entry-relations.js';
import { mockTianditu } from './mock-tianditu.mjs';

const base = process.env.ATLAS_URL;
if (!base) throw new Error('Run through with-preview.mjs');
const json = async path => JSON.parse(await readFile(new URL(path, import.meta.url), 'utf8'));
const [world, catalog, animations, kuafu] = await Promise.all(['../public/data/myth-world.json', '../public/data/atlas/catalog.json', '../public/data/atlas/story-animations.json', '../public/data/atlas/kuafu-journey.json'].map(json));
const index = new Map([...world.beasts, ...world.places, ...world.domains, ...world.natural_features, ...world.passages, ...world.text_entities, ...catalog.events].map(item => [item.id, item]));
for (const relation of entryRelations) {
  assert.equal(relation.ids.length, 2);
  assert.ok(relation.ids.every(id => index.has(id)));
  const sources = relation.ids.flatMap(id => {
    const record = index.get(id);
    return [record, ...(record.source_passage_ids || []).map(id => index.get(id))];
  });
  assert.ok(sources.some(record => {
    return (record.quote || record.properties?.source_quote || '').includes(relation.quote);
  }), `${relation.ids}: original-text evidence in card or its source passage`);
  for (const id of relation.ids) assert.ok(relatedEntries(id, index).some(item => item.id === relation.ids.find(other => other !== id)), 'Bidirectional explicit relations');
}
assert.ok(relatedEntries('beast-jiuweihu', index).some(item => item.id === 'place-qingqiu'), 'Qingqiu relation has explicit passage evidence');
assert.equal(animationForEvent('01-01', catalog, animations, kuafu), '00-opening');
assert.equal(animationForEvent('03-05', catalog, animations, kuafu), '03-05');
for (const id of ['06-03', '07-03', 'beast-jingwei', 'invalid']) assert.equal(animationForEvent(id, catalog, animations, kuafu), null);
const zh = searchEntries(searchIndex(world, catalog, world, catalog), '填平东海', 'story');
assert.equal(zh[0].id, '03-04'); assert.equal(zh[0].snippetKind, 'summary');
const en = searchEntries(searchIndex(world, catalog, world, catalog, 'en'), 'repeatedly carries', 'story');
assert.equal(en[0].id, '03-04'); assert.equal(en[0].snippetLanguage, 'en');
assert.ok(highlightTerms(en[0].snippet, 'REPEATEDLY carries').filter(part => part.matched).length >= 2);
assert.doesNotThrow(() => highlightTerms('<script> (test) [x]', '<script> ( [x]'));
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
    await mockTianditu(context);
    const page = await context.newPage(), errors = [];
    page.on('pageerror', error => errors.push((error.stack || error.message).replace(/tk=[^&\s]+/g, 'tk=[redacted]')));
    const drawer = page.locator('.detail-drawer');
    const entry = id => page.locator(`.detail-drawer[data-entry-id="${id}"]`);
    const restored = async id => {
      await entry(id).waitFor();
      await page.waitForFunction(id => document.querySelector('.detail-drawer')?.dataset.entryId === id && document.querySelector('.detail-drawer').dataset.readingRestoring === 'false', id);
    };
    for (const lang of ['zh', 'en']) {
      await page.goto(`${base}?chapter=03&lang=${lang}`);
      await page.locator('.global-search-trigger').click();
      const query = lang === 'zh' ? '填平东海' : 'repeatedly carries';
      await page.locator('.global-search-input').fill(query);
      const result = page.locator('.search-result[data-result-kind="story"][data-result-id="03-04"]');
      await result.waitFor();
      assert.equal(await result.locator('.content-origin').getAttribute('data-origin'), 'shanhaijing');
      assert.equal(await result.locator('.content-origin').textContent(), lang === 'zh' ? '《山海经》所载' : 'Shanhaijing');
      assert.equal(await result.locator('.search-snippet-kind').innerText(), lang === 'zh' ? '故事梗概' : 'Story overview');
      assert.ok(await result.locator('mark').count());
      if (name === 'chromium') await page.screenshot({ path: filename(`discovery-search-${lang}.png`) });
      await result.click(); await restored('03-04');
      const related = drawer.locator('[data-related-id="beast-jingwei"]');
      await related.scrollIntoViewIfNeeded();
      const scrollTop = await drawer.evaluate(node => node.scrollTop);
      const camera = await page.locator('.myth-map-canvas').getAttribute('data-view');
      await related.click(); await restored('beast-jingwei');
      assert.equal(await drawer.locator('.detail-play-story').count(), 0, 'Creature details do not play a similarly named story');
      assert.equal(await page.locator('.story-animation, .kuafu-journey').count(), 0);
      await drawer.locator('[data-related-id="place-fajiu"]').click(); await restored('place-fajiu');
      assert.equal(new URL(page.url()).searchParams.get('item'), 'place-fajiu');
      assert.ok(await drawer.locator('[data-related-id="03-04"]').count());
      await drawer.locator('.return-related').click(); await restored('beast-jingwei');
      await page.waitForFunction(() => document.activeElement?.dataset.relatedId === 'place-fajiu');
      await page.goBack(); await restored('03-04');
      await page.waitForFunction(() => document.activeElement?.dataset.relatedId === 'beast-jingwei');
      assert.ok(Math.abs(await drawer.evaluate(node => node.scrollTop) - scrollTop) <= 3, 'Related navigation restores the reading position');
      assert.equal(await page.locator('.myth-map-canvas').getAttribute('data-view'), camera, 'Related entries preserve the background camera');
      await page.goForward(); await restored('beast-jingwei');
      await drawer.locator('.return-related').click(); await restored('03-04');

      const play = drawer.locator('.detail-play-story');
      await play.scrollIntoViewIfNeeded();
      const beforePlay = await drawer.evaluate(node => node.scrollTop);
      await play.click();
      await page.locator('.story-animation[data-story="03-04"][data-status="playing"]').waitFor();
      assert.equal(await drawer.count(), 0);
      assert.equal(await page.locator('.world-layout').getAttribute('data-tour-active'), 'false');
      await page.locator('.return-to-reading').click(); await restored('03-04');
      await page.waitForFunction(() => document.activeElement?.classList.contains('detail-play-story'));
      assert.ok(Math.abs(await drawer.evaluate(node => node.scrollTop) - beforePlay) <= 3, 'Playback returns to the same reading position');
      await page.locator('.story-animation[data-status="paused"]').waitFor();
      const paused = await page.locator('.story-animation').getAttribute('data-elapsed');
      await drawer.locator('[data-related-id="beast-jingwei"]').click(); await restored('beast-jingwei');
      await drawer.locator('.return-related').click(); await restored('03-04');
      assert.equal(await page.locator('.story-animation').getAttribute('data-elapsed'), paused, 'Related reading keeps the background animation paused at the same point');
      await drawer.locator('.return-search').click();
      await page.locator('.global-search-dialog').waitFor();
      assert.equal(await page.locator('.global-search-input').inputValue(), query);
      await page.keyboard.press('Escape');
      await page.locator('.global-search-dialog').waitFor({ state: 'hidden' });
    }

    for (const [chapter, id, selector] of [['00', '01-01', '.pangu-player-wrap'], ['03', '03-05', '.kuafu-journey']]) {
      await page.goto(`${base}?chapter=${chapter}&item=${id}&lang=zh`);
      await drawer.locator('.detail-play-story').click();
      await page.locator(`${selector}[data-status="playing"]`).waitFor();
      await page.locator('.return-to-reading').click(); await restored(id);
    }
    await page.goto(`${base}?chapter=06&item=06-03&lang=en`);
    await drawer.waitFor();
    assert.equal(await drawer.locator('.detail-play-story').count(), 0, 'Reading-only chapters offer no unavailable animation');

    for (const [width, height] of [[320, 700], [390, 844], [844, 390], [1440, 1000]]) for (const lang of ['zh', 'en']) {
      await page.setViewportSize({ width, height });
      await page.goto(`${base}?chapter=03&item=03-04&lang=${lang}`);
      await restored('03-04');
      assert.equal(await drawer.locator('>.content-origin').getAttribute('data-origin'), 'shanhaijing');
      assert.equal(await drawer.evaluate(node => node.scrollWidth > node.clientWidth), false);
      assert.ok(await drawer.locator('.detail-play-story, .detail-related button').evaluateAll(nodes => nodes.every(node => node.getBoundingClientRect().height >= 44)));
      await drawer.locator('[data-related-id="beast-jingwei"]').click(); await restored('beast-jingwei');
      assert.equal(await drawer.evaluate(node => node.scrollWidth > node.clientWidth), false);
      assert.ok(await drawer.locator('.return-related').evaluate(node => node.getBoundingClientRect().height >= 44));
      if (name === 'chromium' && width === 390) await page.screenshot({ path: filename(`discovery-related-${lang}.png`) });
      await page.goto(`${base}?chapter=01&item=01-02&lang=${lang}`);
      await restored('01-02');
      const origin = drawer.locator('>.content-origin');
      assert.equal(await origin.getAttribute('data-origin'), 'other_classic');
      assert.equal(await origin.textContent(), lang === 'zh' ? '其他古籍所载' : 'Other ancient texts');
      assert.ok(await origin.evaluate(node => {
        const r = node.getBoundingClientRect(), drawer = node.closest('.detail-drawer').getBoundingClientRect();
        return r.left >= drawer.left && r.right <= drawer.right;
      }), 'Source badges fit narrow drawers');
      if (name === 'chromium' && [390, 844].includes(width)) await page.screenshot({ path: filename(`content-origin-${lang}-${width}.png`) });
    }

    await page.setViewportSize({ width: 1440, height: 1000 });
    await page.goto(`${base}?chapter=03&lang=zh`);
    await page.locator('.map-fullscreen').click(); await page.locator('.is-map-fullscreen').waitFor();
    await page.locator('.map-entry-list > summary').click();
    await page.locator('.map-entry-list [data-entry-id="03-04"]').click(); await restored('03-04');
    await drawer.locator('[data-related-id="beast-jingwei"]').click(); await restored('beast-jingwei');
    await drawer.locator('.return-related').click(); await restored('03-04');
    await drawer.locator('.detail-play-story').click();
    await page.locator('.is-map-fullscreen .story-animation[data-status="playing"]').waitFor();
    await page.locator('.return-to-reading').click(); await restored('03-04');
    assert.ok(await drawer.evaluate(node => Boolean(node.closest('.is-map-fullscreen'))), 'Detail/playback round trips preserve fullscreen');
    await drawer.locator('.drawer-close').click(); await drawer.waitFor({ state: 'hidden' });
    await page.locator('.map-fullscreen').click(); await page.locator('.is-map-fullscreen').waitFor({ state: 'hidden' });

    await page.goto(`${base}?chapter=03&mode=geography&event=03-04&lang=zh`);
    await page.locator('.geo-result-list button').first().click();
    const candidate = await page.locator('[data-candidate-id][aria-pressed="true"]').getAttribute('data-candidate-id');
    await settle(page);
    const geographicView = await page.locator('.geo-map').getAttribute('data-extent');
    await page.locator('.global-search-trigger').click(); await page.locator('.global-search-input').fill('填平东海');
    await page.locator('.search-result[data-result-id="03-04"]').click(); await restored('03-04');
    await drawer.locator('[data-related-id="place-fajiu"]').click(); await restored('place-fajiu');
    await drawer.locator('.return-related').click(); await restored('03-04');
    await drawer.locator('.detail-play-story').click();
    await page.locator('.story-animation[data-status="playing"]').waitFor();
    await page.locator('.return-to-reading').click(); await restored('03-04');
    assert.equal(await page.locator('.myth-map-wrap').getAttribute('data-map-mode'), 'geography', 'Playback returns to the original map mode');
    await drawer.locator('.return-search').click(); await page.locator('.global-search-dialog').waitFor();
    await page.keyboard.press('Escape'); await page.locator('.global-search-dialog').waitFor({ state: 'hidden' });
    assert.equal(new URL(page.url()).searchParams.get('reference'), candidate);
    assert.equal(await page.locator('.geo-map').getAttribute('data-extent'), geographicView);
    await settle(page);
    await page.goto(`${base}?chapter=00&mode=geography&event=01-01&reference=01-01-tradition-biyang&lang=en`);
    await page.locator('.geo-place-story [data-origin="local_tradition"]').waitFor();
    assert.equal(await page.locator('.geo-place-story .content-origin').textContent(), 'Local tradition');
    assert.deepEqual(errors, []);
    await context.close();
    console.log(`PASS ${name}: bilingual overview search/highlights, explicit related-entry round trips/history/position/focus, direct playback/return for 3 animation clocks, geographic context and 8 layouts`);
  } finally { await browser.close(); }
}
