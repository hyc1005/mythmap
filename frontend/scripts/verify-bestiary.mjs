import { openBestiaryFilters } from './ui-controls.mjs';
import assert from 'node:assert/strict';
import { readFile, mkdir } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import { chromium, webkit } from 'playwright';
import { BESTIARY_INITIAL, BESTIARY_BATCH, FORM_LABELS, FEATURE_LABELS, bestiaryEntries, filterBestiary, groupBestiary, bestiaryNamesakes, morphologyReview } from '../src/bestiary.js';
import { searchIndex, searchEntries } from '../src/search.js';
import guideRoutes from '../src/guide-routes.json' with { type: 'json' };

const read = async path => JSON.parse(await readFile(new URL(path, import.meta.url), 'utf8'));
const [world, catalog, metadata] = await Promise.all(['../public/data/myth-world.json', '../public/data/atlas/catalog.json', '../src/bestiary-metadata.json'].map(read));
const semanticTags = await read('../src/bestiary-semantic-tags.json');
async function openEvidence(page, drawer) {
  const group = drawer.locator('.detail-evidence');
  if (!await group.count()) return;
  if (!await group.evaluate(node => node.open)) {
    await group.locator(':scope > summary').click();
    await page.waitForTimeout(360);
  }
}
const EFFECT_TAGS = ['ward_fire', 'ward_war', 'ward_evil', 'ward_plague', 'cure_disease', 'travel', 'calm', 'nourish'];
const OMEN_TAGS = ['flood', 'drought', 'war', 'famine', 'plague', 'fire', 'wind', 'bountiful', 'peace', 'other_omen'];
for (const [id, record] of Object.entries(semanticTags.entries)) {
  assert.ok(metadata[id], `${id}: semantic tag entry has metadata`);
  assert.ok(['text', 'commentary', 'comparison'].includes(record.basis), `${id}: basis is known`);
  assert.equal(record.basis, metadata[id].classification.basis, `${id}: basis matches metadata`);
  assert.ok(['auto', 'reviewed'].includes(record.status), `${id}: review status`);
  if (record.status === 'reviewed') assert.ok(record.reviewed_at && record.review_method, `${id}: reviewed entries keep a review record`);
  for (const tag of record.effect) assert.ok(EFFECT_TAGS.includes(tag.tag), `${id}: effect tag ${tag.tag}`);
  for (const tag of record.omen) assert.ok(OMEN_TAGS.includes(tag.tag), `${id}: omen tag ${tag.tag}`);
  for (const tag of [...record.effect, ...record.omen]) assert.ok(tag.match && tag.evidence && ['quote', 'commentary_quote', 'description'].includes(tag.source), `${id}: tag keeps match, evidence and source`);
}
assert.ok(Object.keys(semanticTags.entries).length >= 90, 'Semantic tags cover the expected accounts');
assert.equal(Object.values(semanticTags.entries).filter(record => record.status === 'reviewed').length, 95, 'Spot-checked tags stay reviewed unless their extracted output changes');
for (const route of guideRoutes.routes) {
  assert.ok(route.id && route.title?.zh && route.title?.en && route.intro?.zh && route.intro?.en, `${route.id}: bilingual title and intro`);
  assert.ok(!/[\u3400-\u9fff]/.test(route.title.en + route.intro.en), `${route.id}: English route copy`);
  assert.equal(new Set(route.stops.map(stop => stop.entryId)).size, route.stops.length, `${route.id}: unique stops`);
  for (const stop of route.stops) {
    assert.ok(metadata[stop.entryId], `${route.id}: route stop ${stop.entryId} exists`);
    assert.ok(stop.label?.zh && stop.label?.en && !/[\u3400-\u9fff]/.test(stop.label.en), `${route.id}/${stop.entryId}: bilingual label`);
  }
}
const original = structuredClone(world);
const entries = bestiaryEntries(world);
const droughtIds = entries.filter(item => item.role === 'beast' && semanticTags.entries[item.id]?.omen.some(tag => tag.tag === 'drought')).map(item => item.id).sort();
assert.deepEqual(filterBestiary(entries, { role: 'beast', omen: 'drought' }).map(item => item.id).sort(), droughtIds, 'Omen filter matches the extracted tags');
const fireIds = entries.filter(item => item.role === 'beast' && semanticTags.entries[item.id]?.effect.some(tag => tag.tag === 'ward_fire')).map(item => item.id).sort();
assert.deepEqual(filterBestiary(entries, { role: 'beast', effect: 'ward_fire' }).map(item => item.id).sort(), fireIds, 'Effect filter matches the extracted tags');
assert.equal(BESTIARY_INITIAL, 12);
assert.equal(BESTIARY_BATCH, 24);
for (const group of groupBestiary(entries)) assert.deepEqual(bestiaryNamesakes(world, group.entries[0].id).map(entry => entry.id).sort(), group.entries.map(entry => entry.id).sort());
assert.deepEqual(bestiaryNamesakes(world, '03-04'), []);
const source = [...world.beasts, ...world.text_entities.filter(item => item.kind === 'deity')];
assert.equal(world.beasts.length, 317);
assert.deepEqual(new Set(entries.map(item => item.id)), new Set(source.map(item => item.id)));
assert.deepEqual(Object.keys(metadata).sort(), source.map(item => item.id).sort(), 'Metadata covers every creature and deity, with no stale IDs');
for (const item of entries) {
  const raw = source.find(value => value.id === item.id);
  for (const field of ['id', 'name', 'quote', 'url', 'source_passage_ids', 'related_entry_ids', 'artwork']) assert.deepEqual(item[field], raw[field]);
  assert.ok(item.classification.evidence && raw[item.classification.source_field].includes(item.classification.evidence), `${item.id}: cited classification evidence`);
  assert.ok(FORM_LABELS[item.formGroup]);
  assert.ok(item.featureTags.every(tag => FEATURE_LABELS[tag]));
  for (const locale of ['zh', 'en']) assert.ok(metadata[item.id].display_name[locale]);
  assert.ok(!/[\u3400-\u9fff\ud800-\udfff]/u.test(metadata[item.id].display_name.en), `${item.id}: English short name`);
  assert.ok(!/[（(]/.test(metadata[item.id].display_name.zh), `${item.id}: qualifier kept separately`);
}
assert.deepEqual(world, original, 'Presentation and classification never rewrite source data');
const byId = new Map(entries.map(item => [item.id, item]));
const reviews = await read('../src/bestiary-morphology-review.json');
const chapterReading = await read('../src/chapter-reading.json');
assert.equal(Object.keys(reviews).length, 46);
const passageById = new Map(world.passages.map(item => [item.id, item]));
const continuous = text => text.replace(/〔影印页[^〕]*〕/g, '').replace(/\s/g, '');
for (const [id, review] of Object.entries(reviews)) {
  assert.ok(byId.has(id));
  assert.deepEqual(review.source_passage_ids, byId.get(id).source_passage_ids);
  const passages = review.source_passage_ids.map(id => passageById.get(id));
  const field = review.basis === 'text' ? 'quote' : 'commentary_quote';
  const text = continuous(passages.map(p => p[field] || '').join(''));
  for (const excerpt of review.evidence.split(/[；;]/)) assert.ok(text.includes(continuous(excerpt)), `${id}: evidence occurs in its own text layer`);
  assert.ok(review.source_urls.length && review.source_urls.every(url => passages.some(p => p.source_pages.includes(url))));
  for (const lang of ['zh', 'en']) assert.ok(morphologyReview(id, lang).label && morphologyReview(id, lang).note);
}
assert.equal(byId.get('beast-beishan-xiao-liangqu').formGroup, 'bird');
assert.equal(byId.get('beast-dongshan-kuafu-like-chai').formGroup, 'beast');
assert.equal(byId.get('beast-dijiang').classification.review_status, 'reviewed');
assert.equal(byId.get('deity-zhongshan-tian-shi-range5').classification.basis, 'commentary');
assert.equal(Object.values(metadata).filter(item => item.classification.review_status === 'unresolved').length, 45);
const rechecked = Object.entries(reviews).filter(([, review]) => review.recheck);
assert.equal(rechecked.length, 45);
for (const [id, review] of rechecked) {
  assert.equal(metadata[id].classification.review_status, 'unresolved');
  assert.equal(review.recheck.certainty, review.status);
  assert.equal(review.recheck.evidence_layer, review.basis);
}
const artwork = await read('../src/refined-artwork.json');
const renyuZhu = byId.get('beast-xishan-renyu-zhushan');
const renyuLonghou = byId.get('beast-beishan-renyu-longhou');
assert.notEqual(renyuZhu.id, renyuLonghou.id);
assert.notDeepEqual(renyuZhu.source_passage_ids, renyuLonghou.source_passage_ids);
const previews = await read('../src/preview-assets.json');
const zhuArt = `/data/atlas/myth-icons/${renyuZhu.artwork}`;
const longhouArt = `/data/atlas/myth-icons/${renyuLonghou.artwork}`;
assert.equal(artwork[zhuArt].full.path, longhouArt);
for (const variant of ['card', 'preview']) assert.equal(artwork[zhuArt][variant].path, previews[longhouArt][variant].path);
assert.deepEqual(Object.keys(chapterReading), world.stages.map(stage => stage.id));
for (const [id, guide] of Object.entries(chapterReading)) {
  assert.deepEqual(guide.event_ids, catalog.events.filter(event => event.properties.stage_id === id).map(event => event.id));
  for (const field of ['intro', 'source_note', 'transition']) {
    assert.ok(guide[field].zh && guide[field].en);
    assert.ok(!/[\u3400-\u9fff]/u.test(guide[field].en));
  }
}

for (const [id, form] of [
  ['beast-zhongshan-mingshe-xian', 'serpent'], ['beast-wenyaoyu', 'fish'], ['beast-qinyuan', 'insect'],
  ['beast-zhongshan-wenwen-fanggao', 'insect'], ['beast-zhongshan-huashe-yang', 'beast'],
  ['beast-xishan-manman-gangwei', 'beast'], ['bird-xishan-manman-chongwu', 'bird'],
  ['beast-zhongshan-feiyu-niushou', 'fish'], ['beast-zhongshan-feiyu-gui', 'beast'],
  ['beast-beishan-huomin-xiushan', 'other'],
]) assert.equal(byId.get(id).formGroup, form, id);
assert.equal(byId.get('beast-beishan-huomin-xiushan').classification.review_status, 'unresolved');
assert.equal(byId.get('beast-luwu').role, 'deity');
assert.equal(byId.get('beast-dijiang').role, 'deity');
assert.equal(byId.get('beast-beishan-heluo-qiaoming').displayName, '何罗鱼');
assert.equal(byId.get('beast-xiangliu').formGroup, 'serpent');
assert.ok(byId.get('beast-xiangliu').featureTags.includes('human_face'));
assert.equal(metadata['beast-xiangliu'].book_key, '海外北经');
assert.ok(world.beasts.find(item => item.id === 'beast-xiangliu').quote.includes('九首人面，蛇身而青'));
const qiongqi = filterBestiary(entries, { query: '穷奇' });
assert.equal(qiongqi.length, 2);
assert.equal(groupBestiary(qiongqi).length, 1);
assert.equal(filterBestiary(entries, { query: '窮竒' })[0].id, 'beast-qiongqi-xishan');
assert.equal(filterBestiary(entries, { query: '飞鱼', form: 'fish', book: '中山经' })[0].id, 'beast-zhongshan-feiyu-niushou');
assert.equal(filterBestiary(entries, { query: '飞鱼', form: 'bird' }).length, 0, 'Flying name does not imply bird morphology');
const index = searchIndex(world, catalog, world, catalog);
assert.equal(searchEntries(index, '何罗鱼', 'beast')[0].id, 'beast-beishan-heluo-qiaoming');
assert.equal(searchEntries(index, '滑鱼', 'beast').filter(item => item.rank === 0).length, 2);
assert.equal(searchEntries(index, '陆吾', 'beast')[0].id, 'beast-luwu', 'Legacy search kind and link remain compatible');
console.log(`PASS metadata: ${entries.length} preserved accounts, bilingual short names, cited body forms, aliases, independent variants and legacy links`);

if (!process.env.ATLAS_URL) {
  if (process.env.ATLAS_DATA_ONLY !== '1') throw new Error('Run through with-preview.mjs, or set ATLAS_DATA_ONLY=1 for metadata checks');
} else for (const name of (process.env.ATLAS_BROWSERS || 'chromium,webkit').split(',')) {
  const browser = await ({ chromium, webkit }[name]).launch();
  try {
    const page = await browser.newPage({ viewport: { width: 1440, height: 1000 }, reducedMotion: 'reduce' });
    const errors = [], requests = [];
    page.on('request', request => requests.push({ url: request.url(), type: request.resourceType() }));
    page.on('pageerror', error => errors.push(error.message));
    await page.addInitScript(() => {
      localStorage.setItem('shanhai-onboarding-v1', '1');
      localStorage.setItem('shanhai-guide-dismissed', '1');
    });
    await page.goto(`${process.env.ATLAS_URL}?chapter=05&lang=zh`);
    const grid = page.locator('.beast-grid');
    await page.locator('#creatures').evaluate(node => node.scrollIntoView({ block: 'start', behavior: 'instant' }));
    await grid.locator('.beast-art img').first().waitFor({ state: 'attached' });
    await grid.locator('.beast-art img').first().evaluate(image => image.decode());
    const bestiaryFont = await page.evaluate(async () => {
      const fonts = await document.fonts.load('600 20px ShanhaiRare', '鲛鸾鼍');
      return fonts.some(font => font.status === 'loaded' && font.unicodeRange.toUpperCase().includes('U+9F0D'));
    });
    assert.equal(bestiaryFont, true, 'Simplified names load the bundled font supplement');
    if (name === 'chromium') {
      await mkdir(new URL('../../output/qa/', import.meta.url), { recursive: true });
      await page.locator('#creatures').evaluate(node => node.scrollIntoView({ block: 'start', behavior: 'instant' }));
      await page.screenshot({ path: fileURLToPath(new URL('../../output/qa/bestiary-groups-desktop.png', import.meta.url)) });
    }
    assert.equal(await grid.locator('.beast-group').count(), BESTIARY_INITIAL);
    assert.equal(await grid.locator('.beast-card').count(), BESTIARY_INITIAL);
    assert.ok(await grid.locator('img').evaluateAll(images => images.every(image => image.loading === 'lazy')));
    await page.waitForTimeout(2000);
    const beforeMore = [...requests];
    const initialSources = new Set(await grid.locator('.beast-art').evaluateAll(nodes => nodes.map(node => new URL(node.dataset.artworkSrc, location.href).href)));
    assert.ok(!beforeMore.some(request => request.type === 'fetch' && /\.(webp|png|avif)(?:[?#]|$)/i.test(request.url)), 'Idle exploration does not prefetch another chapter image');
    assert.ok(!beforeMore.some(request => /reference-scans|\.djvu|tianditu\.gov\.cn|tile\.openstreetmap\.org/i.test(request.url)), 'Unopened scans and geography do not load');
    await page.locator('.bestiary-toggle').click();
    assert.equal(await grid.locator('.beast-group').count(), 36);
    assert.equal(await grid.locator('.beast-card').count(), 36);
    const appendedSources = await grid.locator('.beast-art').evaluateAll(nodes => nodes.slice(12).map(node => new URL(node.dataset.artworkSrc, location.href).href));
    for (const url of appendedSources.filter(url => !initialSources.has(url))) assert.ok(!beforeMore.some(request => request.url === url), 'An unexpanded card was not fetched: ' + url);
    const firstArt = grid.locator('.beast-art').first(), lastArt = grid.locator('.beast-art').last();
    await lastArt.scrollIntoViewIfNeeded();
    await lastArt.locator('img').waitFor({ state: 'attached' });
    await lastArt.locator('img').evaluate(image => image.decode());
    await firstArt.locator('img').waitFor({ state: 'detached' });
    const input = page.getByLabel('搜索异兽', { exact: true });
    await input.fill('滑鱼');
    const namesakes = grid.locator('.beast-group').filter({ has: page.locator('b', { hasText: /^滑鱼$/ }) });
    assert.equal(await namesakes.count(), 1);
    assert.equal(await namesakes.locator('.beast-card').count(), 1);
    const originalId = await namesakes.locator('.beast-card').getAttribute('data-beast-id');
    await namesakes.locator('.beast-variants-toggle').click();
    const variantsDrawer = page.locator('.detail-drawer');
    await variantsDrawer.locator('.detail-evidence').waitFor();
    await openEvidence(page, variantsDrawer);
    await variantsDrawer.locator('.detail-namesakes').waitFor();
    const variantIds = await variantsDrawer.locator('.detail-namesakes option').evaluateAll(nodes => nodes.map(node => node.value));
    assert.deepEqual(new Set(variantIds), new Set(['beast-xishan-huayu-leyou', 'beast-beishan-huayu-qiuru']));
    const otherId = variantIds.find(id => id !== originalId);
    await variantsDrawer.locator('.detail-namesakes select').selectOption(otherId);
    await page.waitForFunction(id => document.querySelector('.detail-drawer')?.dataset.entryId === id && document.querySelector('.detail-drawer').dataset.readingRestoring === 'false', otherId);
    assert.equal(new URL(page.url()).searchParams.get('item'), otherId);
    await variantsDrawer.locator('.return-related').click();
    await page.waitForFunction(id => document.querySelector('.detail-drawer')?.dataset.entryId === id, originalId);
    await page.waitForFunction(() => document.activeElement?.matches('.detail-namesakes select'));
    await variantsDrawer.locator('.drawer-close').click();
    await variantsDrawer.waitFor({ state: 'hidden' });
    assert.equal(await namesakes.locator('.beast-card').count(), 1);
    await input.fill('穷奇');
    await grid.locator('.beast-card').click();
    const parallelDrawer = page.locator('.detail-drawer');
    await parallelDrawer.waitFor();
    await openEvidence(page, parallelDrawer);
    await parallelDrawer.getByRole('button', { name: '并列校读', exact: true }).click();
    assert.equal(await parallelDrawer.locator('.detail-parallel-card').count(), 2, 'Two same-name accounts are compared side by side');
    const parallelText = await parallelDrawer.locator('.detail-parallel').innerText();
    assert.ok(parallelText.includes('西山经') && parallelText.includes('海内北经'), 'Both source books are labelled');
    assert.ok(await parallelDrawer.locator('.detail-parallel mark').count() > 0, 'Differing characters are marked without rewriting the text');
    await parallelDrawer.getByRole('button', { name: '收起并列校读', exact: true }).click();
    assert.equal(await parallelDrawer.locator('.detail-parallel').count(), 0);
    await parallelDrawer.locator('.drawer-close').click();
    await parallelDrawer.waitFor({ state: 'hidden' });
    await input.fill('飞鱼');
    await page.getByLabel('按篇目筛选').selectOption('中山经');
    assert.equal(await page.locator('.bestiary-filter-chip').count(), 2);
    await page.locator('[data-filter-key="query"]').click();
    assert.equal(await input.inputValue(), '');
    assert.equal(await page.getByLabel('按篇目筛选').inputValue(), '中山经', 'Removing one filter preserves the other');
    assert.equal(await input.evaluate(node => node === document.activeElement), true, 'Removed query chip restores input focus');
    await input.fill('飞鱼');

    assert.equal(await grid.locator('.beast-card').count(), 1);
    await openBestiaryFilters(page);
    await page.getByLabel('按形貌筛选').selectOption('fish');
    assert.equal(await grid.locator('.beast-card').count(), 1);
    assert.equal(await grid.locator('b').textContent(), '飞鱼');
    assert.ok((await grid.locator('.beast-provenance').textContent()).includes('牛首'));
    await grid.locator('.beast-card').click();
    const detail = page.locator('.detail-drawer');
    await detail.waitFor();
    assert.equal(await detail.locator('h2').textContent(), '飛魚（牛首）');
    assert.equal(new URL(page.url()).searchParams.get('item'), 'beast-zhongshan-feiyu-niushou');
    await page.locator('.drawer-close').click();
    await page.waitForFunction(() => document.activeElement?.dataset.beastId === 'beast-zhongshan-feiyu-niushou');
    await page.getByRole('button', { name: '清除筛选', exact: true }).click();
    assert.equal(await grid.locator('.beast-group').count(), 12);
    await input.fill('青耕');
    await grid.locator('.beast-card').click();
    const tagDrawer = page.locator('.detail-drawer');
    await openEvidence(page, tagDrawer);
    await tagDrawer.locator('.detail-semantic').waitFor();
    await tagDrawer.locator('.detail-semantic-tags button').first().click();
    await tagDrawer.waitFor({ state: 'hidden' });
    assert.ok(await page.locator('.bestiary-filter-chip').evaluateAll(nodes => nodes.some(node => /功效|征兆|Effect|Omen/.test(node.textContent))), 'A tag click applies the matching filter');
    await page.getByRole('button', { name: '清除筛选', exact: true }).click();
    await input.fill('鸣蛇');
    await page.getByLabel('按篇目筛选').selectOption('中山经');
    await page.getByLabel('按特征筛选').selectOption('four_wings');
    assert.equal(await grid.locator('.beast-card').getAttribute('data-form-group'), 'serpent');
    for (const [width, height] of [[1440, 1000], [390, 844], [320, 700], [844, 390]]) {
      await page.setViewportSize({ width, height });
      for (const lang of ['en', 'zh']) {
        await page.getByRole('button', { name: lang === 'en' ? 'EN' : '中文', exact: true }).click();
        assert.equal(await grid.locator('.beast-card').getAttribute('data-beast-id'), 'beast-zhongshan-mingshe-xian');
        assert.equal(await grid.locator('b').textContent(), lang === 'zh' ? '鸣蛇' : 'Ming snakes');
        if (name === 'chromium' && width === 320 && lang === 'en') await page.locator('#creatures').screenshot({ path: fileURLToPath(new URL('../../output/qa/bestiary-filter-mobile-en.png', import.meta.url)) });
        assert.ok(await page.locator('#creatures').evaluate(node => node.scrollWidth <= node.clientWidth + 1), `${name} ${lang} ${width}: bestiary overflow`);
        assert.ok(await page.locator('.bestiary-tools :is(input,select,button), .bestiary-roles button').evaluateAll(nodes => nodes.filter(node => node.checkVisibility()).every(node => node.getBoundingClientRect().height >= 44)));
      }
    }
    await page.locator('[data-bestiary-role="deity"]').click();
    await input.fill('陆吾');
    assert.equal(await grid.locator('b').textContent(), '陆吾');
    await grid.locator('.beast-card').click();
    await page.locator('.detail-drawer[data-entry-id="beast-luwu"]').waitFor();
    assert.equal(await detail.locator('h2').textContent(), '陸吾');
    await page.locator('.drawer-close').click();
    await input.fill('帝之二女');
    await grid.locator('.beast-card').click();
    const comparisonDrawer = page.locator('.detail-drawer');
    await comparisonDrawer.waitFor();
    await openEvidence(page, comparisonDrawer);
    await comparisonDrawer.locator('.detail-comparisons').waitFor();
    assert.equal(await comparisonDrawer.locator('.detail-comparisons button').count(), 3, 'Variant readings stay separate from same-name accounts');
    assert.equal(await comparisonDrawer.locator('.detail-namesakes').count(), 0, 'Comparison accounts are not rendered as same-name entries');
    await comparisonDrawer.locator('.drawer-close').click();
    await comparisonDrawer.waitFor({ state: 'hidden' });
    await page.getByRole('button', { name: '清除筛选', exact: true }).click();
    while (await page.locator('.bestiary-toggle').count()) await page.locator('.bestiary-toggle').click();
    assert.equal(await grid.locator('.beast-card').count(), groupBestiary(entries.filter(item => item.role === 'deity')).length);
    for (const lang of ['zh', 'en']) {
      await page.setViewportSize({ width: lang === 'zh' ? 1440 : 390, height: lang === 'zh' ? 1000 : 844 });
      for (const entry of [renyuZhu, renyuLonghou]) {
        await page.goto(process.env.ATLAS_URL + `?chapter=05&lang=${lang}&item=${entry.id}`);
        const fish = page.locator(`.detail-drawer[data-entry-id="${entry.id}"]`);
        await fish.waitFor();
        const image = fish.locator('.drawer-art');
        await image.evaluate(image => image.decode());
        assert.equal(new URL(await image.getAttribute('src'), page.url()).pathname, new URL(process.env.ATLAS_URL).pathname + 'data/atlas/myth-icons/beishan/fish-renyu-longhou-v1.webp');
        assert.equal(new URL(page.url()).searchParams.get('item'), entry.id);
      }
    }
    const noObserver = await browser.newPage({ viewport: { width: 390, height: 844 }, reducedMotion: 'reduce' });
    noObserver.on('pageerror', error => errors.push(error.message));
    await noObserver.addInitScript(() => Object.defineProperty(window, 'IntersectionObserver', { value: undefined, configurable: true }));
    await noObserver.goto(process.env.ATLAS_URL + '?chapter=05&lang=zh');
    await noObserver.locator('#creatures').scrollIntoViewIfNeeded();
    assert.equal(await noObserver.locator('.beast-card').count(), 12);
    await noObserver.locator('.beast-card').first().scrollIntoViewIfNeeded();
    await noObserver.locator('.beast-art img').first().evaluate(image => image.decode());
    await noObserver.close();

    const broken = await browser.newPage({ viewport: { width: 390, height: 844 }, reducedMotion: 'reduce' });
    broken.on('pageerror', error => errors.push(error.message));
    await broken.route('**/data/atlas/**', route => route.request().resourceType() === 'image' ? route.abort() : route.continue());
    await broken.goto(process.env.ATLAS_URL + '?chapter=05&lang=zh');
    const brokenCard = broken.locator('.beast-card').first();
    await brokenCard.scrollIntoViewIfNeeded();
    await brokenCard.locator('.artwork-fallback').waitFor();
    assert.equal(await brokenCard.locator('.beast-art').getAttribute('aria-busy'), 'false', 'Failed image stops its loading state');
    assert.equal(await brokenCard.locator('.beast-art-loading').count(), 0);
    await brokenCard.click();
    await broken.locator('.detail-drawer .artwork-fallback button').waitFor();
    await broken.unroute('**/data/atlas/**');
    await broken.locator('.detail-drawer .artwork-fallback button').click();
    await broken.locator('.detail-drawer .drawer-art').evaluate(image => image.decode());
    await broken.close();
    const routesPage = await browser.newPage({ viewport: { width: 1280, height: 900 } });
    routesPage.on('pageerror', error => errors.push(error.message));
    await routesPage.goto(process.env.ATLAS_URL + '?splash=0&lang=zh');
    await routesPage.waitForTimeout(1200);
    if (await routesPage.locator('.onboarding-skip').count()) await routesPage.locator('.onboarding-skip').click();
    await routesPage.locator('#routes').scrollIntoViewIfNeeded();
    assert.equal(await routesPage.locator('.guide-route-tabs button').count(), guideRoutes.routes.length);
    const firstStop = guideRoutes.routes[0].stops[0];
    await routesPage.locator(`[data-route-stop="${firstStop.entryId}"]`).click();
    await routesPage.locator(`.detail-drawer[data-entry-id="${firstStop.entryId}"]`).waitFor();
    assert.equal(await routesPage.locator('.world-layout').getAttribute('data-timeline-playing'), 'false', 'Routes do not start the guided tour');
    await routesPage.close();
    assert.deepEqual(errors, []);
    console.log(`PASS ${name}: 12 initial + 24 added cards, viewport image lifetime, no unopened image requests, independent namesake selection, morphology/features/books, bilingual layouts, original details and legacy deity links`);
  } finally { await browser.close(); }
}
