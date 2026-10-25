import assert from 'node:assert/strict';
import {createHash} from 'node:crypto';
import {readFile,stat} from 'node:fs/promises';
import {resolve,sep} from 'node:path';
import {chromium,webkit} from 'playwright';
import {worldEntries} from '../src/entries.js';
import {readExploration} from '../src/exploration.js';
import {mockTianditu} from './mock-tianditu.mjs';

const json=async path=>JSON.parse(await readFile(new URL(path,import.meta.url),'utf8'));
const [world,english,inventory,review,scans,snapshot,catalog,generation]=await Promise.all([
'../public/data/myth-world.json','../src/locale-content-en.json','../../data/shanhaijing-inventory.json',
'../../data/dongshan-edition-review.json','../../data/reference-scans/dongshan/sources.json',
'../../data/shanhaijing-reference.json','../public/data/atlas/catalog.json','../artwork-source/dongshan/entities-generation.json'].map(json));
const entries=worldEntries(world),index=new Map(entries.map(e=>[e.id,e]));
const selected=entries.filter(e=>e.content_batch?.startsWith('dongshan-'));
const newBatches=['suzhu','leishan','xunzhuang','boqi','fantiao'].map(s=>'dongshan-'+s);
const commonChecks=process.env.ATLAS_COMMON_CHECKS!=='0';
const activeBatches=process.env.ATLAS_BATCH?[process.env.ATLAS_BATCH]:newBatches;
assert.ok(activeBatches.every(b=>newBatches.includes(b)));
const sharedBatches={'water-dongshan-shi':['leishan'],'water-dongshan-hu':['xunzhuang'],'water-dongshan-sea':['fantiao']};
const browserEntries=selected.filter(e=>activeBatches.includes(e.content_batch)||sharedBatches[e.id]?.some(s=>activeBatches.includes('dongshan-'+s)));
const activePassages=world.passages.filter(p=>activeBatches.includes(p.content_batch));
const layoutEntries=[...activePassages,...browserEntries.filter(e=>e.artwork)];
assert.equal(index.size,entries.length);
assert.equal(selected.length,28);assert.equal(review.entry_ids.length,23);
assert.deepEqual([1,2,3,4].map(b=>world.passages.filter(p=>(p.source_book||1)===b).length),[43,82,92,5]);
assert.equal(review.implemented_stages,5);assert.equal(review.remaining_stages,46);assert.equal(review.planned_stages,51);
assert.equal(review.next.name,'姑兒之山');assert.deepEqual(review.next.source_units,[16,17]);
assert.equal(inventory.chapters[3].explained_blocks,13);assert.equal(inventory.chapters[3].semantic_passages,5);
assert.equal(inventory.chapters[3].semantic_review,'partial');assert.equal(inventory.chapters[3].pending_candidate_passages,37);
const unitIndex=new Map(inventory.units.map(u=>[u.id,u]));
for(const id of review.heading_unit_ids)assert.equal(unitIndex.get(id).status,'heading_metadata');
assert.equal(unitIndex.get('source-04-0016').status,'pending_review');
assert.ok(unitIndex.get('source-04-0009').page_url.endsWith('/109'));
assert.ok(unitIndex.get('source-04-0009').captured_page_url.endsWith('/110'));
const covered=new Set(world.passages.filter(p=>p.source_book===4).flatMap(p=>p.source_unit_ids));
assert.deepEqual([...covered],Array.from({length:13},(_,i)=>'source-04-'+String(i+3).padStart(4,'0')));
for(const p of world.passages.filter(p=>p.source_book===4)){
 const raw=p.source_unit_ids.map(id=>snapshot.chapters[3].lines[Number(id.slice(-4))-1].text).join('');
 assert.equal(p.quote,raw);assert.equal(p.captured_text,raw);
 assert.deepEqual(p.captured_commentary.map(c=>c.annotations),p.source_unit_ids.map(id=>snapshot.chapters[3].lines[Number(id.slice(-4))-1].annotations));
 assert.equal(p.range,1);
}
assert.equal(createHash('sha256').update(await readFile(new URL('../../data/shanhaijing-reference.json',import.meta.url))).digest('hex'),review.snapshot_sha256);
for(const s of scans)assert.equal(createHash('sha256').update(await readFile(new URL('../../'+s.local_path,import.meta.url))).digest('hex'),s.sha256);
assert.equal(scans.length,16);
for(const f of review.font_supplements)assert.equal(createHash('sha256').update(await readFile(new URL('../../'+f.path,import.meta.url))).digest('hex'),f.sha256);
assert.equal(generation.assets.length,5);
for(const a of generation.assets){
 assert.equal(a.status,'reviewed');
 assert.equal(createHash('sha256').update(await readFile(new URL('../artwork-source/dongshan/'+a.source_file,import.meta.url))).digest('hex'),a.sha256);
 assert.equal(createHash('sha256').update(await readFile(a.original_path)).digest('hex'),a.sha256);
 assert.equal(index.get(a.entry_id).artwork,'dongshan/'+a.name+'-v1.webp');
}
for(const e of selected){
 assert.ok(english[e.id]?.name&&english[e.id]?.quote&&english[e.id]?.description,e.id);
 assert.ok(!/[\u3400-\u9fff\u{20000}-\u{323af}]/u.test(english[e.id].quote),e.id);
 assert.equal(e.review_status,'facsimile_reviewed');
 assert.equal(e.reveal_chapter,'04');
 assert.equal(readExploration('?chapter=04&item='+e.id,world,catalog).item,e.id);
 for(const id of [...e.related_entry_ids,...(e.source_passage_ids||[])])assert.ok(index.has(id),id);
 if(e.kind==='beast')assert.ok(e.artwork||e.appearance_unknown,e.id);
 else assert.ok(!e.artwork,e.id+' has no borrowed artwork');
 if(e.source_passage_ids?.length===1)assert.deepEqual(e.source_unit_ids,index.get(e.source_passage_ids[0]).source_unit_ids);
}
for(const id of ['water-dongshan-shi','water-dongshan-hu','water-dongshan-sea']){
 const e=index.get(id),ps=e.source_passage_ids.map(id=>index.get(id));assert.equal(ps.length,2);
 assert.deepEqual(new Set(e.source_unit_ids),new Set(ps.flatMap(p=>p.source_unit_ids)));
 assert.deepEqual(new Set(e.source_pages),new Set(ps.flatMap(p=>p.source_pages)));
 for(const q of e.quote.split('；'))assert.ok(ps.some(p=>p.quote.includes(q)));
}
assert.ok(english['beast-dongshan-yongyong-suzhu'].commentary_quote.includes('rong as the pronunciation'));
assert.ok(index.get('beast-dongshan-congcong-xunzhuang').quote.includes('如犬六足'));
assert.ok(index.get('beast-dongshan-zishu-xunzhuang').quote.includes('如鷄而䑕毛'));
assert.ok(index.get('beast-dongshan-zhen-xunzhuang').quote.includes('其喙如箴'));
assert.equal(index.get('beast-dongshan-huoshi-leishan').commentary_quote,'科斗也爾雅謂之活東');
assert.equal(index.get('place-dongshan-qianmei-suzhu').commentary_quote,'亦山名也音妺');
assert.equal(index.get('water-dongshan-jian-fantiao').commentary_quote,'音同减損之减');
assert.equal(index.get('material-dongshan-qingbistone-xunzhuang').quote,'其下多青碧石');
assert.equal(selected.filter(e=>e.appearance_unknown).length,1);
assert.ok(index.get('beast-dongshan-gan-fantiao').appearance_unknown&&!index.get('beast-dongshan-gan-fantiao').artwork);
for(const id of review.stable_existing_ids)assert.ok(index.has(id));
assert.equal(index.get('beast-dangkang').artwork,'beasts/beast-dangkang.webp');
assert.equal(index.get('beast-fei').artwork,'beasts/beast-fei.webp');
assert.equal(index.get('beast-heyu').artwork,'beasts/beast-heyu.webp');
console.log('PASS data: Eastern 5 passages, 23 cards, 13 source blocks; 5 reviewed images and 1 documented placeholder; retained legacy IDs');
if(process.env.ATLAS_DATA_ONLY==='1')process.exit(0);

const root = resolve(process.env.ATLAS_STATIC_DIR || 'dist');
for(const d of review.font_supplements)assert.equal(createHash('sha256').update(await readFile(resolve(root,'fonts',d.path.split('/').at(-1)))).digest('hex'),d.sha256,'Published font bytes: '+d.family);
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
      await page.goto(`${base}?chapter=04&item=${id}&lang=${lang}`);
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
          assert.ok((await d.locator('.drawer-art').getAttribute('src')).includes(e.artwork));
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
      const currentPlace = index.get(activePassages[0].related_entry_ids[0]);
      let d, roundTrips=0;
      const contextPlaces=selected.filter(e=>activeBatches.includes(e.content_batch)&&(e.kind==='place'||e.id===currentPlace.id));
      for(const contextPlace of contextPlaces){
        d=await open(contextPlace.id,lang);
        const contents=selected.filter(e=>e.context_place_id===contextPlace.id||e.context_place_ids?.includes(contextPlace.id)||contextPlace.kind==='rite'&&contextPlace.related_entry_ids.includes(e.id)&&e.kind!=='passage');
        assert.equal(await d.locator('.detail-place-contents [data-related-id]').count(),contextPlace.kind==='rite'?0:contents.length);
        for(const card of contents){
          await d.locator(`[data-related-id="${card.id}"]`).click();await ready(card.id);
          await page.locator('.return-related').click();d=await ready(contextPlace.id);roundTrips++;
        }
      }
      if(commonChecks){
        for(const [query,id] of [['当康','beast-dangkang'],['蜚','beast-fei'],['合窳','beast-heyu']]){
          await page.goto(base+'?chapter=04&lang='+lang);
          await page.locator('.global-search-trigger').click();
          await page.locator('.global-search-input').fill(query);
          await page.locator('.search-result[data-result-kind="beast"][data-result-id="'+id+'"]').click();await ready(id);
        }
        await page.goto(base+'?chapter=04&lang='+lang);
        await page.locator('.mobile-explore-nav button').nth(1).click();
        for(const [book,count] of [[1,43],[2,82],[3,92],[4,5]])assert.equal(await page.locator('[data-source-book="'+book+'"] [data-entry-id]').count(),count);
        const eastern=page.locator('[data-source-book="4"]');
        await eastern.locator(':scope > summary').click();
        assert.equal(await eastern.locator('.passage-range').count(),1,'Hide empty future ranges');
        await eastern.locator('.passage-range > summary').click();
        for(const p of activePassages)assert.equal(await eastern.locator('[data-entry-id="'+p.id+'"]').count(),1);
        await eastern.locator('[data-entry-id="'+activePassages[0].id+'"]').click();await ready(activePassages[0].id);
      }
      await page.goto(`${base}?chapter=04&lang=${lang}`);
      await page.locator('.global-search-trigger').click();
      await page.locator('.global-search-input').fill(lang === 'zh' ? currentPlace.name : english[currentPlace.id].name);
      await page.locator(`.search-result[data-result-kind="place"][data-result-id="${currentPlace.id}"]`).click();
      await ready(currentPlace.id);
      console.log(`PASS ${engine} ${lang}: ${browserEntries.length} current/shared records, 4 viewports, ${roundTrips} nested/context round trips, images, ${commonChecks?'Eastern 5 and previous 217 catalog passages, retained legacy links; ':''}current search`);
    }
    const readingPassage=activePassages[0];
    let d = await open(readingPassage.id);
    await d.getByRole('button', { name: '收藏条目', exact: true }).click();
    await d.getByRole('button', { name: '标为已读', exact: true }).click();
    await page.reload(); d = await ready(readingPassage.id);
    assert.equal(await d.getByRole('button', { name: '已收藏 · 取消', exact: true }).getAttribute('aria-pressed'), 'true');
    assert.equal(await d.getByRole('button', { name: '已读 · 撤销', exact: true }).getAttribute('aria-pressed'), 'true');
    const scrollable = await d.evaluate(n => n.scrollHeight > n.clientHeight);
    await d.locator('[data-reading-anchor="source"]').evaluate(n => n.scrollIntoView({ block: 'start' }));
    if (scrollable) await d.evaluate(n => { n.scrollTop = Math.max(n.scrollTop, Math.min(100, n.scrollHeight - n.clientHeight)); });
    await page.waitForFunction(({id,scrollable}) => {
      const s = JSON.parse(localStorage.getItem('shanhai-last-reading-v1'));
      return s?.id === id && (!scrollable || s.position?.anchor !== 'start' || s.position?.fraction > 0);
    }, {id:readingPassage.id,scrollable});
    await page.goto(base + '?lang=zh');
    await page.waitForFunction(()=>window.history.state?.shanhai?.stageIndex===0&&document.querySelector('.world-layout')?.dataset.chapter==='00');
    await page.evaluate(async()=>{
      await document.fonts.ready;
      await Promise.all([...document.images].filter(i=>i.loading!=='lazy'&&i.getClientRects().length).map(i=>i.decode().catch(()=>{})));
    });
    await page.locator('.resume-reading[aria-label]').click();
    d = await ready(readingPassage.id);
    assert.equal(await d.evaluate(n => n.scrollTop > 0), scrollable);
    await page.evaluate(async characters => {
      for(const family of ['Atlas Eastern Rare'])for(const w of [400,600])await document.fonts.load(w+' 20px "'+family+'"',characters);
      for (const w of [400, 600]) await document.fonts.load(`${w} 20px "Shanhai Title"`, characters);
    }, review.font_supplements.map(f=>f.characters).join(''));
    assert.deepEqual(errors, []);
    assert.deepEqual(missing, []);
    await context.close();
    console.log(`PASS ${engine}: read/favorite refresh, resume, title face loading; zero page/resource errors`);
  } finally {
    await browser.close();
  }
}
