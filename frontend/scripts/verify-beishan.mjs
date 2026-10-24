import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
import { readFile, stat } from 'node:fs/promises';
import { resolve, sep } from 'node:path';
import { chromium, webkit } from 'playwright';
import { worldEntries } from '../src/entries.js';
import { readExploration } from '../src/exploration.js';
import { mockTianditu } from './mock-tianditu.mjs';

const json = async path => JSON.parse(await readFile(new URL(path, import.meta.url), 'utf8'));
const [world, english, inventory, review, scans, snapshot, catalog] = await Promise.all([
  '../public/data/myth-world.json', '../src/locale-content-en.json', '../../data/shanhaijing-inventory.json',
  '../../data/beishan-edition-review.json', '../../data/reference-scans/beishan/sources.json',
  '../../data/shanhaijing-reference.json', '../public/data/atlas/catalog.json',
].map(json));
const entries = worldEntries(world), index = new Map(entries.map(e => [e.id, e]));
const selected = entries.filter(e => e.content_batch?.startsWith('beishan-'));
const newBatches = ['danxun','shizhe','bianchun','manlian','danzhang'].map(s => 'beishan-'+s);
const activeBatches = process.env.ATLAS_BATCH ? [process.env.ATLAS_BATCH] : newBatches;
assert.ok(activeBatches.every(b => newBatches.includes(b)));
const browserEntries = selected.filter(e => activeBatches.includes(e.content_batch) || e.id === 'water-beishan-he' && activeBatches.includes('beishan-shizhe') || e.id === 'water-beishan-gang' && activeBatches.includes('beishan-danzhang'));
const activePassages = world.passages.filter(p => activeBatches.includes(p.content_batch));
const layoutEntries = [...activePassages, ...activePassages.map(p => {
  const creatures=browserEntries.filter(e=>e.content_batch===p.content_batch&&e.artwork&&e.kind==='beast');
  return creatures.find(e=>/youyu|heluo|xixi/.test(e.id))||creatures[0];
}).filter(Boolean)];
const passage = index.get('passage-beishan-danhu');
const place = index.get('place-beishan-danhu');
assert.equal(index.size, entries.length);
assert.equal(selected.length, 92);
assert.equal(review.entry_ids.length, 80);
assert.equal(world.passages.filter(p => p.id.startsWith('passage-nanshan-')).length, 43);
assert.equal(world.passages.filter(p => p.source_book === 2).length, 82);
assert.equal(world.passages.filter(p => p.source_book === 3).length, 12);
assert.deepEqual(passage.source_unit_ids, ['source-03-0002', 'source-03-0003', 'source-03-0004']);
assert.equal(passage.quote, snapshot.chapters[2].lines.slice(1, 4).map(l => l.text).join(''));
assert.equal(passage.captured_text, passage.quote);
assert.ok(!passage.quote.includes('求如'));
assert.ok(passage.commentary_quote.includes('出蜀中音\n〔影印页76〕飢；音逢'));
assert.ok(index.get('plant-beishan-ji-danhu').commentary_quote.endsWith('音飢'));
assert.deepEqual(passage.captured_commentary.map(r => r.annotations), snapshot.chapters[2].lines.slice(1, 4).map(l => l.annotations));
assert.equal(inventory.chapters[2].explained_blocks, 52);
assert.equal(inventory.chapters[2].semantic_review, 'partial');
assert.equal(inventory.chapters[2].pending_candidate_passages, 78);
assert.equal(inventory.units.find(u => u.id === 'source-03-0001').status, 'heading_metadata');
assert.equal(inventory.units.find(u => u.id === 'source-03-0054').status, 'pending_review');
for (const [id,page,captured] of [['source-03-0018',77,78],['source-03-0027',78,79],['source-03-0036',79,80],['source-03-0045',80,81]]) {
  const u=inventory.units.find(u=>u.id===id); assert.ok(u.page_url.endsWith('/'+page)); assert.ok(u.captured_page_url.endsWith('/'+captured));
}
assert.deepEqual(world.passages.filter(p=>p.source_book===3).map(p=>p.order),Array.from({length:12},(_,i)=>i+1));
const covered=new Set(world.passages.filter(p=>p.source_book===3).flatMap(p=>p.source_unit_ids));
assert.equal(covered.size,52);
for(let i=2;i<=53;i++)assert.ok(covered.has('source-03-'+String(i).padStart(4,'0')));
assert.ok(index.get('beast-beishan-youyu-daishan').quote.includes('三尾六足四首'));
assert.ok(index.get('beast-beishan-heluo-qiaoming').quote.includes('一首而十身'));
assert.ok(index.get('beast-beishan-xixi-zhuoguang').quote.includes('十翼鱗皆在羽端'));
assert.ok(index.get('beast-beishan-qitu-daishan').quote.includes('如烏五彩而赤文'));
assert.equal(index.get('water-beishan-he').source_passage_ids.length,5);
assert.ok(inventory.units.find(u => u.id === 'source-03-0009').page_url.endsWith('/76'));
assert.ok(inventory.units.find(u => u.id === 'source-03-0009').captured_page_url.endsWith('/77'));
assert.ok(index.get('beast-beishan-huayu-qiuru').quote.includes('如鱓赤背'));
assert.ok(index.get('beast-beishan-shuima-qiuru').quote.includes('文臂牛尾'));
assert.equal(index.get('place-beishan-zhupi-qiuru').commentary_quote, '水出諸毗山也');
for (const e of selected) {
  assert.ok(english[e.id]?.name && english[e.id]?.description && english[e.id]?.quote, e.id);
  assert.ok(!/[\u3400-\u9fff]/u.test(english[e.id].quote), e.id + ' English quote');
  assert.equal(e.review_status, 'facsimile_reviewed');
  if (e.kind === 'beast') assert.ok(e.artwork?.startsWith('beishan/') || e.id === 'beast-zhu-jian' && e.artwork === 'beasts/beast-zhu-jian.webp' || e.appearance_unknown, e.id);
  else assert.equal(e.artwork, undefined, 'No borrowed or invented illustrations');
  assert.equal(readExploration(`?chapter=03&item=${e.id}`, world, catalog).item, e.id);
  for (const id of [...e.related_entry_ids, ...(e.source_passage_ids || [])]) assert.ok(index.has(id), id);
}
assert.ok(!place.context_place_id, 'No self-reference');
assert.equal(entries.filter(e => e.context_place_id === place.id).length, 6);
assert.ok(index.get('water-beishan-feng-danhu').related_entry_ids.includes('water-beishan-you-danhu'));
assert.notEqual(index.get('water-beishan-you-danhu').id, index.get('water-xishan-you-changsha').id);
for (const id of ['03-04', 'beast-jingwei', 'beast-zhu-jian', 'place-fajiu', 'place-north-ranges']) {
  assert.ok(index.has(id) || catalog.events.some(e => e.id === id), 'Retained ' + id);
}
for (const scan of scans) {
  const bytes = await readFile(new URL('../../' + scan.local_path, import.meta.url));
  assert.equal(createHash('sha256').update(bytes).digest('hex'), scan.sha256);
}
assert.equal(createHash('sha256').update(await readFile(new URL('../../data/shanhaijing-reference.json', import.meta.url))).digest('hex'), review.snapshot_sha256);
assert.equal(createHash('sha256').update(await readFile(new URL('../../' + review.title_font_supplement.path, import.meta.url))).digest('hex'), review.title_font_supplement.sha256);
const generation = await json('../artwork-source/beishan/generation.json');
generation.assets.push(...(await json('../artwork-source/beishan/entities-generation.json')).assets);
for (const a of generation.assets) {
  assert.equal(a.status, 'reviewed');
  assert.equal(createHash('sha256').update(await readFile(new URL('../artwork-source/beishan/' + a.source_file, import.meta.url))).digest('hex'), a.sha256);
  assert.equal(index.get(a.entry_id).artwork, 'beishan/' + a.name + '-v1.webp');
}
assert.equal(generation.assets.length,15);
for(const id of ['beast-beishan-lingyang-zhuoguang','beast-beishan-fan-zhuoguang','beast-beishan-tuotuo-guoshan'])assert.ok(index.get(id).appearance_unknown&&!index.get(id).artwork);
assert.equal(index.get('beast-zhu-jian').place_id,'place-north-ranges');
assert.equal(index.get('beast-zhu-jian').context_place_id,'place-beishan-danzhang');
assert.equal(index.get('beast-zhu-jian').reveal_chapter,'03');
assert.ok(index.get('beast-zhu-jian').aliases.includes('诸犍'));
assert.ok(index.get('beast-beishan-ershu-danxun').quote.includes('以其尾飛'));
assert.ok(index.get('beast-beishan-zuzi-manlian').quote.includes('牛尾文臂馬蹄'));
assert.ok(index.get('beast-beishan-baiye-danzhang').quote.includes('文首白翼黄足'));
assert.ok(index.get('water-beishan-li-danzhang').quote.includes('南流'));
assert.deepEqual(index.get('water-beishan-gang').source_passage_ids,['passage-beishan-bianchun','passage-beishan-danzhang']);
assert.ok(index.get('water-beishan-gang').context_place_ids.includes('place-beishan-danzhang'));
assert.notEqual(index.get('water-beishan-youze').id,index.get('water-beishan-you-danhu').id);
console.log('PASS data: Northern 12 passages, 80 cards, 52 source blocks, 5 page corrections, 15 reviewed images and retained Zhujian and 3 documented placeholders');
if (process.env.ATLAS_DATA_ONLY === '1') process.exit(0);

const root = resolve(process.env.ATLAS_STATIC_DIR || 'dist');
const base = 'https://atlas.test/mythmap/';
const sizes = [{ width: 320, height: 700 }, { width: 390, height: 844 }, { width: 844, height: 390 }, { width: 1440, height: 1000 }];
for (const engine of (process.env.ATLAS_BROWSERS || 'chromium,webkit').split(',')) {
  const browser = await ({ chromium, webkit }[engine]).launch();
  try {
    const context = await browser.newContext({ viewport: sizes[1], reducedMotion: 'reduce' });
    await mockTianditu(context);
    await context.route('https://atlas.test/**', async route => {
      const url = new URL(route.request().url());
      if (!url.pathname.startsWith('/mythmap/')) return route.fulfill({ status: 404, body: 'Wrong base' });
      const file = resolve(root, decodeURIComponent(url.pathname.slice('/mythmap/'.length)) || 'index.html');
      if (!file.startsWith(root + sep) || !(await stat(file).catch(() => null))?.isFile()) return route.fulfill({ status: 404, body: 'Missing file' });
      return route.fulfill({ path: file });
    });
    await context.addInitScript(() => {
      if (location.origin === 'https://atlas.test') localStorage.setItem('shanhai-onboarding-v1', '1');
    });
    const page = await context.newPage(), errors = [], missing = [];
    page.on('pageerror', e => errors.push(e.message));
    page.on('response', r => { if (r.status() >= 400 && r.url().startsWith(base)) missing.push(r.url()); });
    async function ready(id) {
      await page.waitForFunction(id => {
        const d = document.querySelector('.detail-drawer');
        return d?.dataset.entryId === id && d.dataset.readingRestoring === 'false';
      }, id);
      await page.evaluate(() => document.fonts.ready);
      return page.locator('.detail-drawer');
    }
    async function open(id, lang = 'zh') {
      await page.goto(`${base}?chapter=03&item=${id}&lang=${lang}`);
      return ready(id);
    }
    for (const lang of ['zh', 'en']) {
      for (const e of browserEntries) {
        const d = await open(e.id, lang);
        assert.equal(await d.locator('h2').innerText(), lang === 'en' ? english[e.id].name : e.name);
        assert.equal(await d.locator('.detail-description').innerText(), lang === 'en' ? english[e.id].description : e.description);
        assert.equal(await d.locator(':scope > blockquote').innerText(), lang === 'en' ? english[e.id].quote : e.quote);
        assert.ok(!await d.evaluate(n=>n.scrollWidth>n.clientWidth),e.id+' 390px overflow');
        assert.ok(!await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth));
        assert.equal(await d.locator('.drawer-art').count(), e.artwork || e.appearance_unknown ? 1 : 0);
        if (e.artwork) {
          await d.locator('.drawer-art').evaluate(i => i.decode());
          assert.ok((await d.locator('.drawer-art').getAttribute('src')).includes(e.id === 'beast-zhu-jian' ? '/beasts/beast-zhu-jian.webp' : '/beishan/'));
        }
        if(e.appearance_unknown){await d.locator('.drawer-art').evaluate(i=>i.decode());assert.ok((await d.locator('.drawer-art').getAttribute('src')).includes('unknown-creature-v4'));}
        if (lang === 'en') assert.deepEqual(await d.evaluate(n => [...n.querySelectorAll('*')].filter(e => !e.children.length && e.getClientRects().length && !e.closest('.original-text,[lang="zh-CN"]') && /[\u3400-\u9fff]/u.test(e.textContent)).map(e => e.textContent)), []);
      }
      for (const size of sizes.filter(s=>s.width!==390)) {
        await page.setViewportSize(size);
        for (const e of size.width === 320 ? browserEntries : layoutEntries) {
          const d = await open(e.id, lang);
          assert.ok(!await d.evaluate(n => n.scrollWidth > n.clientWidth), `${e.id} ${lang} ${size.width}`);
          assert.ok(!await page.evaluate(() => document.documentElement.scrollWidth > innerWidth));
        }
      }
      await page.setViewportSize(sizes[1]);
      const currentPlace = index.get(activePassages[0].id.replace('passage-','place-'));
      let d = await open(currentPlace.id, lang);
      const contents=selected.filter(e=>e.context_place_id===currentPlace.id||e.context_place_ids?.includes(currentPlace.id));
      assert.equal(await d.locator('.detail-place-contents [data-related-id]').count(), contents.length);
      for (const card of contents) {
        await d.locator(`.detail-place-contents [data-related-id="${card.id}"]`).click();
        await ready(card.id);
        await page.locator('.return-related').click();
        d = await ready(currentPlace.id);
      }
      d = await open('water-beishan-feng-danhu', lang);
      await d.locator('[data-related-id="water-beishan-you-danhu"]').click();
      await ready('water-beishan-you-danhu');
      await page.goto(`${base}?chapter=03&lang=${lang}`);
      await page.locator('.global-search-trigger').click();
      await page.locator('.global-search-input').fill('诸犍');
      await page.locator('.search-result[data-result-id="beast-zhu-jian"]').click();
      await ready('beast-zhu-jian');
      await page.goto(`${base}?chapter=03&lang=${lang}`);
      await page.locator('.mobile-explore-nav button').nth(1).click();
      const northern = page.locator('[data-source-book="3"]');
      await northern.locator(':scope > summary').click();
      await northern.locator('.passage-range > summary').click();
      assert.equal(await northern.locator('[data-entry-id^="passage-beishan-"]').count(), 12);
      await northern.locator(`[data-entry-id="${activePassages[0].id}"]`).click();
      await ready(activePassages[0].id);
      await page.goto(`${base}?chapter=03&lang=${lang}`);
      await page.locator('.global-search-trigger').click();
      await page.locator('.global-search-input').fill(lang === 'zh' ? currentPlace.name : english[currentPlace.id].name);
      await page.locator(`.search-result[data-result-id="${currentPlace.id}"]`).click();
      await ready(currentPlace.id);
      console.log(`PASS ${engine} ${lang}: ${browserEntries.length} current/shared records, 4 viewports, ${contents.length} object round trips, images, water link, 12 catalog passages and search`);
    }
    const readingPassage=activePassages[0];
    let d = await open(readingPassage.id);
    await d.getByRole('button', { name: '收藏条目', exact: true }).click();
    await d.getByRole('button', { name: '标为已读', exact: true }).click();
    await page.reload(); d = await ready(readingPassage.id);
    assert.equal(await d.getByRole('button', { name: '已收藏 · 取消', exact: true }).getAttribute('aria-pressed'), 'true');
    assert.equal(await d.getByRole('button', { name: '已读 · 撤销', exact: true }).getAttribute('aria-pressed'), 'true');
    await d.locator('[data-reading-anchor="source"]').scrollIntoViewIfNeeded();
    await page.waitForFunction(id => {
      const s = JSON.parse(localStorage.getItem('shanhai-last-reading-v1'));
      return s?.id === id && s.position?.anchor !== 'start';
    }, readingPassage.id);
    await page.goto(base + '?lang=zh');
    await page.waitForFunction(()=>window.history.state?.shanhai?.stageIndex===0&&document.querySelector('.world-layout')?.dataset.chapter==='00');
    await page.evaluate(async()=>{
      await document.fonts.ready;
      await Promise.all([...document.images].filter(i=>i.loading!=='lazy'&&i.getClientRects().length).map(i=>i.decode().catch(()=>{})));
    });
    await page.locator('.resume-reading[aria-label]').click();
    d = await ready(readingPassage.id);
    assert.ok(await d.evaluate(n => n.scrollTop > 0));
    await page.evaluate(async () => {
      for (const w of [400, 600]) await document.fonts.load(`${w} 20px "Shanhai Title"`, '單狐机木華草漨求䑏䟽何儵孟寓帶彭栢椐橐虢譙駝鰼䑕');
    });
    assert.deepEqual(errors, []);
    assert.deepEqual(missing, []);
    await context.close();
    console.log(`PASS ${engine}: read/favorite refresh, resume, title face loading; zero page/resource errors`);
  } finally {
    await browser.close();
  }
}
