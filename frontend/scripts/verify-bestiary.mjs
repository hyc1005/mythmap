import assert from 'node:assert/strict';
import { readFile, mkdir } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import { chromium, webkit } from 'playwright';
import { BESTIARY_BATCH, FORM_LABELS, FEATURE_LABELS, bestiaryEntries, filterBestiary, groupBestiary } from '../src/bestiary.js';
import { searchIndex, searchEntries } from '../src/search.js';

const read = async path => JSON.parse(await readFile(new URL(path, import.meta.url), 'utf8'));
const [world, catalog, metadata] = await Promise.all(['../public/data/myth-world.json', '../public/data/atlas/catalog.json', '../src/bestiary-metadata.json'].map(read));
const original = structuredClone(world);
const entries = bestiaryEntries(world);
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
    const errors = [];
    page.on('pageerror', error => errors.push(error.message));
    await page.addInitScript(() => {
      localStorage.setItem('shanhai-onboarding-v1', '1');
      localStorage.setItem('shanhai-guide-dismissed', '1');
    });
    await page.goto(`${process.env.ATLAS_URL}?chapter=05&lang=zh`);
    const grid = page.locator('.beast-grid');
    await grid.scrollIntoViewIfNeeded();
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
    assert.equal(await grid.locator('.beast-group').count(), BESTIARY_BATCH);
    assert.equal(await grid.locator('.beast-card').count(), BESTIARY_BATCH);
    assert.ok(await grid.locator('img').evaluateAll(images => images.every(image => image.loading === 'lazy')));
    await page.locator('.bestiary-toggle').click();
    assert.equal(await grid.locator('.beast-group').count(), 48);
    const input = page.getByLabel('搜索异兽', { exact: true });
    await input.fill('滑鱼');
    const namesakes = grid.locator('.beast-group').filter({ has: page.locator('b', { hasText: /^滑鱼$/ }) });
    assert.equal(await namesakes.count(), 1);
    assert.equal(await namesakes.locator('.beast-card').count(), 2);
    const toggle = namesakes.locator('.beast-variants-toggle');
    await toggle.click();
    assert.equal(await namesakes.locator('.beast-card').count(), 1);
    await toggle.focus(); await page.keyboard.press('Enter');
    assert.equal(await namesakes.locator('.beast-card').count(), 2);
    await input.fill('飞鱼');
    await page.getByLabel('按篇目筛选').selectOption('中山经');
    assert.equal(await grid.locator('.beast-card').count(), 2);
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
    assert.equal(await grid.locator('.beast-group').count(), 24);
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
        assert.ok(await page.locator('.bestiary-tools :is(input,select,button), .bestiary-roles button').evaluateAll(nodes => nodes.every(node => node.getBoundingClientRect().height >= 44)));
      }
    }
    await page.locator('[data-bestiary-role="deity"]').click();
    await input.fill('陆吾');
    assert.equal(await grid.locator('b').textContent(), '陆吾');
    await grid.locator('.beast-card').click();
    await page.locator('.detail-drawer[data-entry-id="beast-luwu"]').waitFor();
    assert.equal(await detail.locator('h2').textContent(), '陸吾');
    await page.locator('.drawer-close').click();
    await page.getByRole('button', { name: '清除筛选', exact: true }).click();
    while (await page.locator('.bestiary-toggle').count()) await page.locator('.bestiary-toggle').click();
    while (await page.locator('.beast-variants-toggle[aria-expanded="false"]').count()) await page.locator('.beast-variants-toggle[aria-expanded="false"]').first().click();
    assert.equal(await grid.locator('.beast-card').count(), entries.filter(item => item.role === 'deity').length);
    assert.deepEqual(errors, []);
    console.log(`PASS ${name}: 24-group paging, independent namesakes, morphology/features/books, bilingual layouts, original details and legacy deity links`);
  } finally { await browser.close(); }
}
