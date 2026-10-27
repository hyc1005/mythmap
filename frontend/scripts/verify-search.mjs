import assert from 'node:assert/strict';
import { mkdir, readFile, stat } from 'node:fs/promises';
import { chromium, firefox, webkit } from 'playwright';
import { searchEntries, searchIndex } from '../src/search.js';
import { itemChapter } from '../src/exploration.js';

const base = process.env.ATLAS_URL;
if (!base) throw new Error('Run through with-preview.mjs');
const read = async path => JSON.parse(await readFile(new URL(path, import.meta.url), 'utf8'));
const [world, catalog, refined, previews] = await Promise.all(['../public/data/myth-world.json', '../public/data/atlas/catalog.json', '../src/refined-artwork.json', '../src/preview-assets.json'].map(read));
const index = searchIndex(world, catalog, world, catalog);
assert.equal(searchEntries(index, '九尾狐', 'beast')[0].id, 'beast-jiuweihu');
assert.ok(searchEntries(index, '九首', 'beast').some(item => item.id === 'beast-xiangliu'));
assert.ok(searchEntries(index, '淮南子', 'source').length > 0);
assert.equal(searchEntries(index, '<script>')[0], undefined);
assert.equal(searchEntries(index, '山海经', 'beast').length, world.beasts.length);
for (const record of index) for (const id of record.entryIds || [record.id]) assert.ok(itemChapter(id, world, catalog), `${record.key}: result links to a supported entry`);
const markerAssets = Object.values(refined).flatMap(variants => variants.map ? [variants.map] : []);
const creatureMarkers = Object.entries(refined).filter(([source, variants]) => variants.map
  && world.beasts.some(item => `/data/atlas/myth-icons/${item.artwork}` === source));
for (const source of [
  '/data/atlas/myth-icons/jingwei.webp',
  '/data/atlas/myth-icons/beasts/beast-jiuweihu.webp',
  '/data/atlas/myth-icons/beasts/beast-xuangui.webp',
  '/data/atlas/myth-icons/nanshan/guanguan-v1.webp',
]) assert.ok(refined[source]?.map, `${source}: existing map marker retained`);
for (const asset of markerAssets) {
  assert.ok(asset.bytes < 16000, `${asset.path}: tiny marker byte budget`);
  assert.equal((await stat(new URL('../public' + asset.path, import.meta.url))).size, asset.bytes);
}
const output = new URL('../../output/qa/', import.meta.url);
await mkdir(output, { recursive: true });
const filename = name => new URL(name, output).pathname.replace(/^\/([A-Za-z]:)/, '$1');
const dialog = page => page.locator('.global-search-dialog');
const input = page => page.locator('.global-search-input');

for (const name of (process.env.ATLAS_BROWSERS || 'chromium,webkit').split(',')) {
  const browser = await ({ chromium, firefox, webkit }[name]).launch();
  try {
    const page = await browser.newPage({ viewport: { width: 390, height: 844 } });
    const errors = [], requested = new Set();
    page.on('pageerror', error => errors.push(error.message));
    page.on('response', response => {
      if (response.url().includes('/refined/') || response.url().includes('/nanshan/')) {
        requested.add(new URL(response.url()).pathname);
        if (!response.ok()) errors.push(`HTTP ${response.status()}: ${response.url()}`);
      }
    });
    await page.goto(`${base}?chapter=03&lang=zh`);
    await page.getByLabel('选择地图故事动画').selectOption('03-05');
    await page.locator('.kuafu-journey[data-status="playing"]').waitFor();
    await page.waitForFunction(() => +document.querySelector('.kuafu-journey').dataset.elapsed > 200);
    await page.locator('.global-search-trigger').click();
    await page.locator('.kuafu-journey[data-status="paused"]').waitFor();
    assert.equal(await input(page).evaluate(node => node === document.activeElement), true);
    assert.equal(await page.locator('#root').evaluate(node => node.inert), true);
    await page.waitForTimeout(200);
    const elapsed = await page.locator('.kuafu-journey').getAttribute('data-elapsed');
    await page.waitForTimeout(250);
    assert.equal(await page.locator('.kuafu-journey').getAttribute('data-elapsed'), elapsed, 'Search pauses the background story');
    await input(page).fill('精卫');
    await dialog(page).locator('[data-result-id="beast-jingwei"][data-result-kind="beast"]').waitFor();
    await dialog(page).locator('[data-result-id="03-04"][data-result-kind="story"]').waitFor();
    await dialog(page).locator('[data-result-id="beast-jingwei"][data-result-kind="beast"]').click();
    await page.locator('.detail-drawer[data-entry-id="beast-jingwei"]').waitFor();
    assert.equal(await page.locator('.world-layout').getAttribute('data-chapter'), '03');
    assert.equal(await page.locator('.kuafu-journey').getAttribute('data-elapsed'), elapsed);
    await page.locator('.drawer-close').click();
    await dialog(page).waitFor();
    await page.waitForFunction(() => document.activeElement?.dataset.resultId === 'beast-jingwei');
    await page.keyboard.press('Escape');
    await page.waitForFunction(() => document.activeElement === document.querySelector('.global-search-trigger'));
    await page.locator('.kuafu-journey[data-status="playing"]').waitFor();
    await page.locator('.global-search-trigger').click();
    await dialog(page).getByLabel('搜索范围').selectOption('source');
    await input(page).fill('淮南子');
    assert.ok(await dialog(page).locator('.search-result').count() > 0);
    assert.ok(await dialog(page).locator('.search-result').evaluateAll(nodes => nodes.every(node => node.dataset.resultKind === 'source')));
    const sourceId = await dialog(page).locator('.search-result').first().getAttribute('data-result-id');
    await dialog(page).locator('.search-result').first().click();
    await page.locator(`.detail-drawer[data-entry-id="${sourceId}"]`).waitFor();
    assert.equal(new URL(page.url()).searchParams.get('chapter'), itemChapter(sourceId, world, catalog), 'Source search produces valid shared chapter');
    await page.locator('.drawer-close').click();
    await dialog(page).waitFor(); await page.keyboard.press('Escape');
    await page.locator('.global-search-trigger').click();
    await dialog(page).getByLabel('搜索范围').selectOption('beast');
    await input(page).fill('九首');
    await dialog(page).locator('[data-result-id="beast-xiangliu"]').click();
    await page.locator('.drawer-art').evaluate(image => image.decode());
    assert.ok((await page.locator('.drawer-art').getAttribute('src')).endsWith('/refined/xiangliu-nine-heads-v2-full.webp'));
    await page.locator('.drawer-close').click();
    await dialog(page).waitFor(); await page.keyboard.press('Escape');
    await page.getByRole('button', { name: 'EN', exact: true }).click();
    await page.locator('.global-search-trigger').click();
    await input(page).fill('九尾狐');
    await dialog(page).locator('[data-result-id="beast-jiuweihu"]').waitFor();
    await dialog(page).getByLabel('Search scope').selectOption('source');
    await input(page).fill('南山经');
    assert.ok(await dialog(page).locator('.search-result').count() > 0, 'Chinese source aliases work in English');
    await dialog(page).getByLabel('Search scope').selectOption('all');
    await input(page).fill('<script>');
    await dialog(page).getByText('No matches. Try a shorter keyword or a different scope.', { exact: true }).waitFor();
    await dialog(page).getByRole('button', { name: 'Clear search', exact: true }).click();
    await dialog(page).getByRole('button', { name: 'Jingwei', exact: true }).click();
    assert.ok(await dialog(page).locator('.search-result').count() > 0);
    const controls = dialog(page).locator('button:not(:disabled), input, select');
    await controls.first().focus(); await page.keyboard.press('Shift+Tab');
    assert.equal(await controls.last().evaluate(node => node === document.activeElement), true);
    await page.keyboard.press('Escape');
    await dialog(page).waitFor({ state: 'hidden' });
    assert.equal(await dialog(page).count(), 0);
    assert.equal(await page.locator('#root').evaluate(node => node.inert), false);
    for (const [width, height] of [[320, 700], [390, 844], [844, 390], [1440, 1000]]) {
      for (const lang of ['zh', 'en']) {
        await page.setViewportSize({ width, height });
        await page.goto(`${base}?chapter=03&lang=${lang}`);
        await page.locator('.global-search-trigger').click();
        await dialog(page).getByLabel(lang === 'zh' ? '搜索范围' : 'Search scope').selectOption('beast');
        await input(page).fill('怀来县');
        const recovery = dialog(page).locator('.search-empty button').first();
        await recovery.waitFor();
        assert.match(await recovery.textContent(), /[1-9]/, 'Empty state exposes matches outside the selected scope');
        assert.ok(await recovery.evaluate(node => node.getBoundingClientRect().height >= 44));
        await recovery.click();
        assert.equal(await input(page).inputValue(), '怀来县', 'Widening the scope preserves the keyword');
        await dialog(page).locator('[data-result-kind="geography"]').first().waitFor();
        assert.equal(await dialog(page).getByLabel(lang === 'zh' ? '搜索范围' : 'Search scope').inputValue(), 'all');
        await input(page).fill('zzzz-no-matches');
        await dialog(page).locator('.search-empty button').last().click();
        assert.equal(await input(page).inputValue(), '');
        assert.ok(await input(page).evaluate(node => node === document.activeElement), 'Trying again focuses the keyword field');
        await input(page).fill('山海经');
        await page.evaluate(() => document.fonts.ready);
        const more = dialog(page).getByRole('button', { name: lang === 'zh' ? '显示更多结果' : 'Show more results', exact: true });
        if (await more.count()) { const before = await dialog(page).locator('.search-result').count(); await more.click(); assert.ok(await dialog(page).locator('.search-result').count() > before); }
        assert.equal(await page.evaluate(() => document.documentElement.scrollWidth > innerWidth), false, `${name} ${width} ${lang} body overflow`);
        assert.ok(await dialog(page).evaluate(node => node.scrollWidth <= node.clientWidth + 1));
        assert.ok(await dialog(page).locator('button, input, select').evaluateAll(nodes => nodes.every(node => node.getBoundingClientRect().height >= 44)));
        if (name === 'chromium' && lang === 'zh' && [320, 1440].includes(width)) await dialog(page).screenshot({ path: filename(`search-${width}x${height}.png`) });
        await page.keyboard.press('Escape');
      }
    }
    await page.goto(`${base}?chapter=03&lang=zh`);
    await page.getByRole('checkbox', { name: '异兽谱', exact: true }).check();
    await page.waitForFunction(paths => {
      const resources = performance.getEntriesByType('resource').map(item => item.name);
      return paths.every(path => resources.some(url => url.endsWith(path)));
    }, creatureMarkers.map(([, variants]) => variants.map.path));
    for (const [, variants] of creatureMarkers) assert.ok([...requested].some(path => path.endsWith(variants.map.path)), 'Map uses the dedicated marker variant');
    if (name === 'chromium') {
      await page.evaluate(async pairs => {
        const section = document.createElement('section'); section.id = 'artwork-review';
        Object.assign(section.style, { position: 'relative', padding: '24px', background: '#f7f1df', color: '#30291f', width: '760px' });
        for (const pair of pairs) {
          const row = document.createElement('div'); row.style.cssText = 'display:flex;align-items:center;gap:24px;margin:16px 0';
          const label = document.createElement('span'); label.textContent = pair.name; label.style.width = '80px'; row.append(label);
          for (const size of [32, 48, 96]) for (const src of [pair.old, pair.next]) {
            const image = new Image(); image.src = new URL(src.slice(1), document.baseURI); image.width = size; image.height = size; image.style.objectFit = 'contain'; await image.decode(); row.append(image);
          }
          section.append(row);
        }
        document.body.append(section);
      }, creatureMarkers.map(([path, variants]) => ({ name: world.beasts.find(item => `/data/atlas/myth-icons/${item.artwork}` === path).name, old: previews[path].card.path, next: variants.map.path })));
      await page.locator('#artwork-review').screenshot({ path: filename('map-icons-before-after.png') });
    }
    await page.goto(`${base}?chapter=00&lang=zh`);
    await page.getByRole('button', { name: '播放盘古序章', exact: true }).click();
    await page.locator('.pangu-player-wrap[data-status="playing"]').waitFor();
    await page.locator('.global-search-trigger').click();
    await page.locator('.pangu-player-wrap[data-status="paused"]').waitFor();
    await page.waitForTimeout(200);
    const pangu = await page.locator('.pangu-composition').getAttribute('data-frame');
    await page.waitForTimeout(200);
    assert.equal(await page.locator('.pangu-composition').getAttribute('data-frame'), pangu);
    await page.keyboard.press('Escape');
    await page.locator('.pangu-player-wrap[data-status="playing"]').waitFor();
    await page.goto(`${base}?chapter=02&lang=zh`);
    await page.getByLabel('选择地图故事动画').selectOption('02-04');
    await page.locator('.story-animation[data-status="playing"]').waitFor();
    await page.locator('.global-search-trigger').click();
    await page.locator('.story-animation[data-status="paused"]').waitFor();
    await page.waitForTimeout(150);
    const story = await page.locator('.story-animation').getAttribute('data-elapsed');
    await page.waitForTimeout(200);
    assert.equal(await page.locator('.story-animation').getAttribute('data-elapsed'), story);
    await page.keyboard.press('Escape');
    await page.locator('.story-animation[data-status="playing"]').waitFor();
    assert.deepEqual(errors, []);
    await page.close();
    console.log(`PASS ${name}: ranked search, body/source matching, bilingual aliases, valid entry links, focus/scroll lock, animation pause, 8 layouts and dedicated map assets`);
  } finally { await browser.close(); }
}
