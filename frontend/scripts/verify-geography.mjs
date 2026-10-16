import assert from 'node:assert/strict';
import { readFile, stat, mkdir } from 'node:fs/promises';
import { chromium, firefox, webkit } from 'playwright';
import { referenceCollection, validReference, groupReferences, unlocatedStories, geographicReferences, geographicEvents, defaultGeographicEvent } from '../src/geography.js';

const base = process.env.ATLAS_URL;
if (!base) throw new Error('Run through with-preview.mjs');
const catalog = JSON.parse(await readFile(new URL('../public/data/atlas/catalog.json', import.meta.url), 'utf8'));
const relief = JSON.parse(await readFile(new URL('../src/geography-basemap.json', import.meta.url), 'utf8'));
assert.equal(catalog.candidates.filter(validReference).length, 28);
const references = geographicReferences(catalog);
assert.equal(references.length, 31);
assert.equal(defaultGeographicEvent(catalog, '00'), '01-01');
assert.equal(defaultGeographicEvent(catalog, '03', '03-04'), '03-04');
assert.equal(defaultGeographicEvent(catalog, '03', '01-01'), '03-01');
assert.ok(!geographicEvents(catalog).some(event => event.id === '02-02' || event.id.startsWith('08-')));
for (const eventId of ['01-01', '03-04', '03-01']) {
  const records = references.filter(item => item.properties.entity_id === eventId);
  assert.ok(records.length >= 2);
  assert.ok(records.some(item => item.properties.evidence_status === 'source_checked'));
  assert.ok(records.every(item => item.properties.location_precision && item.properties.coordinate_source));
}
assert.ok(references.filter(item => item.properties.association_type === 'local_tradition').every(item => item.properties.evidence.length));

assert.equal(referenceCollection(catalog.events).features.length, 0, 'Unlocated stories never become invented geographic points');
assert.ok(unlocatedStories(catalog).every(item => !item.id.startsWith('08-') && !['archive', 'group'].includes(item.properties.presentation)), 'Archived material is not restored to normal story navigation');
assert.equal(validReference({ ...catalog.candidates[0], geometry: { type: 'Point', coordinates: [181, 35] } }), false);
assert.equal(validReference({ ...catalog.candidates[0], geometry: { type: 'Point', coordinates: [115, NaN] } }), false);
assert.ok(groupReferences(catalog.candidates).length < catalog.candidates.length, 'Coincident interpretations are grouped, not displaced');
assert.deepEqual(relief.extent, [65, 15, 140, 55]);
assert.equal(relief.projection, 'EPSG:4326');
assert.equal((await stat(new URL('../public' + relief.path, import.meta.url))).size, relief.bytes);
assert.ok(relief.bytes < 1200000);
const output = new URL('../../output/qa/', import.meta.url);
await mkdir(output, { recursive: true });
const dialog = page => page.locator('.geography-dialog');
const close = page => dialog(page).locator(':scope > header button').click();
const rows = page => dialog(page).locator('[data-candidate-id]');

for (const name of (process.env.ATLAS_BROWSERS || 'chromium,webkit').split(',')) {
  const browser = await ({ chromium, firefox, webkit }[name]).launch();
  try {
    const page = await browser.newPage({ viewport: { width: 390, height: 844 } });
    const errors = [];
    page.on('pageerror', error => errors.push(error.message));
    await page.goto(`${base}?chapter=03&lang=zh`);
    await page.getByLabel('选择地图故事动画').selectOption('03-05');
    await page.locator('.kuafu-journey[data-status=playing]').waitFor();
    await page.waitForFunction(() => Number(document.querySelector('.kuafu-journey').dataset.elapsed) > 200);
    await page.locator('.geography-trigger').click();
    await page.locator('.kuafu-journey[data-status=paused]').waitFor();
    const elapsed = await page.locator('.kuafu-journey').getAttribute('data-elapsed');
    await page.evaluate(() => new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve))));
    const view = await page.locator('.myth-map-canvas').getAttribute('data-view');
    await dialog(page).locator('.geo-map canvas').first().waitFor();
    assert.equal(await rows(page).count(), 0, 'Kuafu has no reliable place references; other events must not leak in');
    assert.equal(await dialog(page).getByLabel('地理事件').inputValue(), '03-05');
    await dialog(page).getByLabel('地理事件').selectOption('03-01');
    assert.equal(await rows(page).count(), 3);
    assert.equal(await page.locator('#root').evaluate(node => node.inert), true);
    await page.waitForTimeout(250);
    assert.equal(await page.locator('.kuafu-journey').getAttribute('data-elapsed'), elapsed);
    assert.equal(await page.locator('.myth-map-canvas').getAttribute('data-view'), view);
    await dialog(page).getByLabel('搜索地理参考点').fill('涿鹿');
    assert.equal(await rows(page).count(), 1, 'Search is restricted to the current event');
    await rows(page).first().click();
    await dialog(page).locator('.geo-reference h3').waitFor();
    assert.match(await dialog(page).locator('.geo-reference').innerText(), /地理考证/);
    const chosen = await rows(page).first().getAttribute('data-candidate-id');
    const savedExtent = JSON.parse(await dialog(page).locator('.geo-map').getAttribute('data-extent'));
    await close(page);
    await page.waitForFunction(() => document.activeElement === document.querySelector('.geography-trigger'));
    await page.locator('.kuafu-journey[data-status=playing]').waitFor();
    await page.locator('.language-switch button[lang=en]').click();
    await page.locator('.geography-trigger').click();
    await page.waitForFunction(() => !!document.querySelector('.geo-map')?.dataset.extent);
    assert.equal(await rows(page).count(), 1, 'Chinese locality queries still match after switching to English');
    assert.equal(await dialog(page).locator('[data-candidate-id][aria-pressed=true]').getAttribute('data-candidate-id'), chosen);
    const restoredExtent = JSON.parse(await dialog(page).locator('.geo-map').getAttribute('data-extent'));
    assert.ok(restoredExtent.every((value, index) => Math.abs(value - savedExtent[index]) < .00001), 'Language changes preserve the geographic camera');
    await close(page);
    await page.locator('.language-switch button[lang=zh-CN]').click();
    await page.locator('.geography-trigger').click();
    assert.equal(await dialog(page).getByLabel('搜索地理参考点').inputValue(), '涿鹿');
    assert.equal(await dialog(page).locator('[data-candidate-id][aria-pressed=true]').getAttribute('data-candidate-id'), chosen);
    assert.equal(await dialog(page).locator('.ol-viewport').count(), 1);
    await dialog(page).getByRole('button', { name: '查看关联故事与出处', exact: true }).click();
    await page.locator('.detail-drawer[data-entry-id="03-01"]').waitFor();
    assert.equal(await dialog(page).count(), 0);
    assert.equal(await page.locator('.world-layout').getAttribute('data-chapter'), '03');
    await page.locator('.drawer-close').click();
    await page.waitForFunction(() => document.activeElement === document.querySelector('.geography-trigger'));
    for (const [width, height] of [[1440, 1000], [390, 844], [320, 700], [844, 390]]) {
      for (const lang of ['zh', 'en']) {
        await page.setViewportSize({ width, height });
        await page.goto(`${base}?chapter=03&lang=${lang}`);
        await page.locator('.geography-trigger').click();
        await dialog(page).locator('.geo-map canvas').first().waitFor();
        await dialog(page).getByRole('button', { name: lang === 'zh' ? '适配参考点' : 'Fit references', exact: true }).click();
        await page.evaluate(() => document.fonts.ready);
        await page.waitForFunction(() => !!document.querySelector('.geo-map')?.dataset.extent);
        const extent = JSON.parse(await dialog(page).locator('.geo-map').getAttribute('data-extent'));
        for (const record of references.filter(item => item.properties.entity_id === '03-01')) {
          const [x, y] = record.geometry.coordinates;
          assert.ok(x > extent[0] && x < extent[2] && y > extent[1] && y < extent[3], 'All event references fit inside the geographic viewport');
        }

        assert.equal(await page.evaluate(() => document.documentElement.scrollWidth > innerWidth), false);
        assert.equal(await dialog(page).evaluate(node => node.scrollWidth > node.clientWidth + 1), false);
        assert.ok(await dialog(page).locator('button, input:not([type=checkbox]), select').evaluateAll(nodes => nodes.filter(node => node.checkVisibility()).every(node => node.getBoundingClientRect().height >= 44)));
        await rows(page).first().click();
        await dialog(page).getByRole('button', { name: lang === 'zh' ? '对照本事件资料' : 'Compare event accounts', exact: true }).click();
        assert.equal(await dialog(page).locator('[data-comparison-id]').count(), 2);
        assert.ok(await dialog(page).locator('[data-comparison-id]').evaluateAll(nodes => nodes.every(node => node.dataset.comparisonId.startsWith('03-01-'))));
        assert.equal(await dialog(page).evaluate(node => node.scrollWidth > node.clientWidth + 1), false);
        const columns = await dialog(page).locator('.geo-compare-grid').evaluate(node => getComputedStyle(node).gridTemplateColumns.split(' ').length);
        assert.equal(columns, width <= 768 ? 1 : 2);
        if (name === 'chromium' && width === 1440 && lang === 'zh') await dialog(page).locator('.geo-comparison').screenshot({ path: new URL('geography-comparison-desktop.png', output).pathname.replace(/^\/([A-Za-z]:)/, '$1') });
        if (lang === 'en') {
          const untranslated = await dialog(page).evaluate(node => [...node.querySelectorAll('*')].filter(item => !item.children.length && item.checkVisibility() && !item.closest('.original-text') && /[\u3400-\u9fff]/.test(item.textContent)).map(item => item.textContent));
          assert.deepEqual(untranslated, []);
        }
        if (name === 'chromium' && lang === 'zh') {
          await dialog(page).evaluate(node => { node.scrollTop = 0; });
          await dialog(page).screenshot({ path: new URL(`geography-${width}x${height}.png`, output).pathname.replace(/^\/([A-Za-z]:)/, '$1') });
        }
        await page.keyboard.press('Escape');
        await dialog(page).waitFor({ state: 'detached' });
        assert.equal(await page.locator('#root').evaluate(node => node.inert), false);
      }
    }
    await page.goto(`${base}?chapter=03&lang=zh`);
    await page.locator('.geography-trigger').click();
    await dialog(page).getByLabel('地理事件').selectOption('03-04');
    assert.equal(await rows(page).count(), 3);
    await dialog(page).getByRole('button', { name: '对照本事件资料', exact: true }).click();
    const compareFirst = dialog(page).getByLabel('对照条目一', { exact: true });
    const compareSecond = dialog(page).getByLabel('对照条目二', { exact: true });
    await compareSecond.selectOption('03-04-tradition-changzi');
    await dialog(page).locator('[data-comparison-id="03-04-tradition-changzi"]').waitFor();
    assert.equal(await compareFirst.locator('option[value="03-04-tradition-changzi"]').evaluate(node => node.disabled), true, 'The same account cannot occupy both sides');
    assert.equal(await dialog(page).locator('[data-comparison-id]').last().getAttribute('data-comparison-id'), '03-04-tradition-changzi');
    assert.match(await dialog(page).locator('[data-comparison-id]').last().innerText(), /地方传说/);
    await dialog(page).getByLabel('搜索地理参考点').fill('高平');
    assert.equal(await rows(page).count(), 1);
    assert.equal(await compareSecond.inputValue(), '03-04-tradition-changzi', 'Searching the map list does not erase comparison choices');
    await dialog(page).getByLabel('搜索地理参考点').fill('');
    await dialog(page).getByRole('button', { name: '关闭对照', exact: true }).click();
    await page.waitForFunction(() => document.activeElement?.getAttribute('aria-controls') === 'geo-comparison');
    await dialog(page).getByRole('button', { name: '对照本事件资料', exact: true }).click();
    await close(page);
    await page.locator('.geography-trigger').click();
    assert.equal(await dialog(page).getByLabel('对照条目二', { exact: true }).inputValue(), '03-04-tradition-changzi', 'Reopening restores comparison selections');

    assert.equal(await dialog(page).locator('.geo-result-list button').filter({ hasText: '地方传说' }).count(), 1);
    const download = page.waitForEvent('download');
    await dialog(page).getByRole('button', { name: '导出参考点 GeoJSON', exact: true }).click();
    const stream = await (await download).createReadStream(), chunks = [];
    for await (const chunk of stream) chunks.push(chunk);
    const exported = JSON.parse(Buffer.concat(chunks).toString());
    assert.equal(exported.features.length, 3);
    assert.ok(exported.features.every(item => validReference(item) && item.properties.reference_only && item.properties.entity_id === '03-04' && item.properties.location_precision && Array.isArray(item.properties.evidence)));
    assert.deepEqual(exported.features[0].geometry, references.find(item => item.properties.entity_id === '03-04').geometry, 'Exports retain WGS84 coordinates, not display projection');
    await dialog(page).getByRole('button', { name: '两点测距', exact: true }).click();
    await dialog(page).getByRole('button', { name: '以视图中心取点', exact: true }).click();
    await dialog(page).getByRole('button', { name: '地理地图放大', exact: true }).click();
    await dialog(page).locator('.geo-map').focus();
    await page.keyboard.press('ArrowRight');
    await page.waitForTimeout(400);
    await dialog(page).getByRole('button', { name: '以视图中心取点', exact: true }).click();
    assert.ok(Number((await dialog(page).locator('.geo-distance').textContent()).match(/[\d.]+/)[0]) > 0);
    await dialog(page).getByRole('button', { name: '清除量测', exact: true }).click();
    assert.equal(await dialog(page).locator('.geo-distance').count(), 0);
    await dialog(page).getByLabel('地理事件').selectOption('01-01');
    assert.equal(await rows(page).count(), 2);
    assert.equal(await dialog(page).locator('[data-comparison-id]').count(), 0, 'Switching events clears the previous comparison');
    await dialog(page).getByRole('button', { name: '对照本事件资料', exact: true }).click();
    assert.ok(await dialog(page).locator('[data-comparison-id]').evaluateAll(nodes => nodes.every(node => node.dataset.comparisonId.startsWith('01-01-'))));

    await rows(page).first().click();
    assert.match(await dialog(page).locator('.geo-reference').innerText(), /县域代表点/);
    await dialog(page).getByLabel('地理事件').selectOption('03-05');
    assert.equal(await rows(page).count(), 0);
    assert.equal(await dialog(page).locator('[data-comparison-id]').count(), 0);
    assert.equal(await dialog(page).getByRole('button', { name: '对照本事件资料', exact: true }).isDisabled(), true);
    assert.equal(await dialog(page).getByRole('button', { name: '导出参考点 GeoJSON', exact: true }).isDisabled(), true);
    await close(page);
    for (const [chapter, story, selector] of [['02', '02-04', '.story-animation'], ['00', null, '.pangu-player-wrap']]) {
      await page.goto(`${base}?chapter=${chapter}&lang=zh`);
      if (story) await page.getByLabel('选择地图故事动画').selectOption(story);
      else await page.getByRole('button', { name: '播放盘古序章', exact: true }).click();
      await page.locator(selector + '[data-status=playing]').waitFor();
      await page.locator('.geography-trigger').click();
      await page.locator(selector + '[data-status=paused]').waitFor();
      assert.equal(await dialog(page).getByLabel('地理事件').inputValue(), story || '01-01');
      await page.keyboard.press('Escape');
      await page.locator(selector + '[data-status=playing]').waitFor();
    }
    for (const [chapter, eventId, count] of [['00', '01-01', 2], ['03', '03-04', 3]]) {
      await page.goto(`${base}?chapter=${chapter}&lang=en`);
      await page.locator('.geography-trigger').click();
      await dialog(page).getByLabel('Geographic event').selectOption(eventId);
      assert.equal(await rows(page).count(), count);
      await dialog(page).locator('[data-candidate-id*=tradition]').first().click();
      if (name === 'chromium') {
        await page.setViewportSize({ width: 390, height: 844 });
        await dialog(page).evaluate(node => { node.scrollTop = 0; });
        await dialog(page).screenshot({ path: new URL(`geography-event-${eventId}.png`, output).pathname.replace(/^\/([A-Za-z]:)/, '$1') });
      }
      assert.equal(await dialog(page).locator('.geo-reference a[href^="https://www."]').count() >= 1, true);
      const untranslated = await dialog(page).evaluate(node => [...node.querySelectorAll('*')].filter(item => !item.children.length && item.checkVisibility() && !item.closest('.original-text') && /[\u3400-\u9fff]/.test(item.textContent)).map(item => item.textContent));
      assert.deepEqual(untranslated, [], 'Pilot tradition details have English labels and summaries');
      await close(page);
    }
    await page.route('**/data/geography/relief.webp', route => route.abort());
    await page.goto(`${base}?chapter=03&lang=zh`);
    await page.locator('.geography-trigger').click();
    await dialog(page).getByRole('alert').waitFor();
    assert.equal(await rows(page).count(), 3);
    await page.unroute('**/data/geography/relief.webp');
    await dialog(page).getByRole('button', { name: '重试地理底图', exact: true }).click();
    await dialog(page).locator('.geography-atlas[data-relief-loaded=true]').waitFor();
    await dialog(page).getByRole('alert').waitFor({ state: 'detached' });
    await close(page);
    assert.deepEqual(errors, []);
    console.log(`PASS ${name}: single-event geography, checked pilot sources, 8 bilingual layouts, all three players preserved, focus/snapshot/source links, WGS84 export, spherical measure and relief retry`);
  } finally { await browser.close(); }
}
