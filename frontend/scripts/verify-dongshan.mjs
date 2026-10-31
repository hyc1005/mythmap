import { openSourceLibrary } from './ui-controls.mjs';
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
const newBatches=review.stage_plan.slice(20).map(s=>'dongshan-'+s.slug);
const commonChecks=process.env.ATLAS_COMMON_CHECKS!=='0';
const activeBatches=process.env.ATLAS_BATCH?[process.env.ATLAS_BATCH]:newBatches;
assert.ok(activeBatches.every(b=>newBatches.includes(b)));
const sharedBatches={'water-dongshan-shi':['beihao'],'water-dongshan-sea':['beihao','dongshi'],'beast-dongshan-large-snake':['bishan','qizhong'],'beast-dongshan-qiu-maoshan':['qinshan','taishan-range4']};
const browserEntries=selected.filter(e=>activeBatches.includes(e.content_batch)||sharedBatches[e.id]?.some(s=>activeBatches.includes('dongshan-'+s)));
const activePassages=world.passages.filter(p=>activeBatches.includes(p.content_batch));
const layoutEntries=[...activePassages,...browserEntries.filter(e=>e.artwork)];
assert.equal(index.size,entries.length);
assert.equal(selected.length,288);assert.equal(review.entry_ids.length,237);
assert.deepEqual([1,2,3,4].map(b=>world.passages.filter(p=>(p.source_book||1)===b).length),[43,82,92,51]);
assert.equal(review.implemented_stages,51);assert.equal(review.remaining_stages,0);assert.equal(review.planned_stages,51);
assert.equal(review.next,null);assert.equal(review.status,'complete');
assert.equal(inventory.chapters[3].explained_blocks,139);assert.equal(inventory.chapters[3].semantic_passages,51);
assert.equal(inventory.chapters[3].semantic_review,'reviewed');assert.equal(inventory.chapters[3].pending_candidate_passages,0);
const unitIndex=new Map(inventory.units.map(u=>[u.id,u]));
for(const id of review.heading_unit_ids)assert.equal(unitIndex.get(id).status,'heading_metadata');
for(const u of inventory.units.filter(u=>u.chapter===4))assert.ok(u.status==='heading_metadata'||u.status==='explained_in_reader',u.id);
assert.ok(unitIndex.get('source-04-0009').page_url.endsWith('/109'));
assert.ok(unitIndex.get('source-04-0009').captured_page_url.endsWith('/110'));
const covered=new Set(world.passages.filter(p=>p.source_book===4).flatMap(p=>p.source_unit_ids));
assert.deepEqual([...covered],Array.from({length:139},(_,i)=>'source-04-'+String(i+3).padStart(4,'0')));
for(const p of world.passages.filter(p=>p.source_book===4)){
 const raw=p.source_unit_ids.map(id=>snapshot.chapters[3].lines[Number(id.slice(-4))-1].text).join('');
 assert.equal(p.quote,raw.replace(/⟦缺字图:([^⟧]+)⟧/g,'$1'));assert.equal(p.captured_text,raw);
 assert.deepEqual(p.captured_commentary.map(c=>c.annotations),p.source_unit_ids.map(id=>snapshot.chapters[3].lines[Number(id.slice(-4))-1].annotations));
 assert.equal(p.range,review.stage_plan.find(s=>s.slug===p.content_batch.slice(9)).range);
}
assert.equal(createHash('sha256').update(await readFile(new URL('../../data/shanhaijing-reference.json',import.meta.url))).digest('hex'),review.snapshot_sha256);
for(const s of scans)assert.equal(createHash('sha256').update(await readFile(new URL('../../'+s.local_path,import.meta.url))).digest('hex'),s.sha256);
assert.equal(scans.length,16);
for(const f of review.font_supplements)assert.equal(createHash('sha256').update(await readFile(new URL('../../'+f.path,import.meta.url))).digest('hex'),f.sha256);
assert.equal(generation.assets.length,34);
for(const a of generation.assets){
 assert.equal(a.status,'reviewed');
 for(const old of a.revision_history||[]){assert.ok(['rejected','superseded'].includes(old.status));assert.equal(createHash('sha256').update(await readFile(new URL('../artwork-source/dongshan/'+old.source_file,import.meta.url))).digest('hex'),old.sha256);assert.equal(createHash('sha256').update(await readFile(old.original_path)).digest('hex'),old.sha256);}
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
 if(['beast','deity'].includes(e.kind))assert.ok(e.artwork||e.appearance_unknown,e.id);
 else assert.ok(!e.artwork,e.id+' has no borrowed artwork');
 if(e.source_passage_ids?.length===1)assert.deepEqual(e.source_unit_ids,index.get(e.source_passage_ids[0]).source_unit_ids);
}
for(const [id,count] of [['water-dongshan-shi',4],['water-dongshan-hu',2],['water-dongshan-sea',5],['beast-dongshan-gan-fantiao',2],['water-dongshan-jiang',2],['beast-dongshan-large-snake',3],['beast-dongshan-qiu-maoshan',3]]){
 const e=index.get(id),ps=e.source_passage_ids.map(id=>index.get(id));assert.equal(ps.length,count);
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
assert.equal(selected.filter(e=>e.appearance_unknown).length,14);
assert.ok(index.get('beast-dongshan-gan-fantiao').appearance_unknown&&!index.get('beast-dongshan-gan-fantiao').artwork);
for(const id of review.stable_existing_ids)assert.ok(index.has(id));
assert.equal(index.get('beast-dangkang').artwork,'beasts/beast-dangkang.webp');
assert.equal(index.get('beast-fei').artwork,'dongshan/creature-fei-taishan-v1.webp');
assert.equal(index.get('beast-heyu').artwork,'dongshan/creature-heyu-yanshan-v1.webp');
assert.equal(index.get('material-dongshan-zhenstone-gaoshi').commentary_quote,'可以；為砥針治癰腫者');
assert.equal(index.get('water-dongshan-jiang').commentary_quote,'一作海');
assert.equal(index.get('beast-dongshan-kanyu-chai').commentary_quote,'未詳音序');
assert.equal(english['beast-dongshan-kanyu-chai'].name,'Kanxu fish');
assert.equal(index.get('rite-dongshan-range1-summary').kind,'rite');
assert.ok(!index.get('deity-dongshan-human-dragon-range1').context_place_id);
assert.ok(index.get('rite-dongshan-range1-summary').related_entry_ids.includes('deity-dongshan-human-dragon-range1'));
assert.ok(index.get('plant-dongshan-gu-caoxi').quote.includes('榖'));
assert.ok(index.get('place-dongshan-caoxi').quote.includes('而無水'));
assert.notEqual(index.get('water-dongshan-ze-gaoshi').id,index.get('water-dongshan-ze-yue').id);
assert.equal(index.get('beast-dongshan-shen-yigao').commentary_quote,'蜃蚌也');
assert.equal(index.get('beast-dongshan-yao-yigao').commentary_quote,'珧玉珧亦蚌屬');
const head=index.get('passage-dongshan-geshan-head'),tail=index.get('passage-dongshan-geshan-tail');
for(const p of [head,tail]){assert.ok(p.captured_text.includes('⟦缺字图:葛⟧'));assert.ok(!p.quote.includes('⟦'));assert.ok(p.quote.includes('葛山'));}
assert.equal(head.captured_commentary.at(-1).source_unit_id,'source-04-0050');
assert.deepEqual(head.captured_commentary.at(-1).annotations,['朱蟞六足有珠魚之羙也']);
assert.ok(index.get('beast-dongshan-zhubie-geshan-head').commentary_quote.endsWith('朱蟞六足有珠魚之羙也'));
assert.ok(index.get('beast-dongshan-zhubie-geshan-head').quote.includes('如肺而有目六足有珠'));
assert.ok(index.get('beast-dongshan-qiuyu-yue').quote.includes('莬而鳥喙䲭目蛇尾'));
assert.equal(index.get('beast-dongshan-qiuyu-yue').commentary_quote,'言佯死也；仇餘二音');
assert.equal(index.get('animal-dongshan-zhong-yue').commentary_quote,'螽蝗𩔗也言傷敗田苗音終');
assert.ok(!index.get('animal-dongshan-zhong-yue').artwork);
for(const id of ['animal-dongshan-zhong-yue','animal-dongshan-huang-insects-yue'])assert.equal(index.get(id).appearance_unknown,true);
assert.equal(english['plant-dongshan-qi-yue'].name,'Qi (Yu-e)');
assert.ok(!english['plant-dongshan-ji-yue']);
for(const [a,b] of [["water-dongshan-yigao", "water-dongshan-jinv"], ["water-dongshan-yigao", "beast-dongshan-shen-yigao"], ["water-dongshan-yigao", "beast-dongshan-yao-yigao"], ["water-dongshan-li-geshan-head", "water-dongshan-yu-marsh"], ["water-dongshan-li-geshan-head", "beast-dongshan-zhubie-geshan-head"], ["water-dongshan-zayu", "water-dongshan-huang-yue"], ["beast-dongshan-qiuyu-yue", "animal-dongshan-zhong-yue"], ["beast-dongshan-qiuyu-yue", "animal-dongshan-huang-insects-yue"]]){assert.ok(index.get(a).related_entry_ids.includes(b));assert.ok(index.get(b).related_entry_ids.includes(a));}

assert.ok(tail.quote.includes('水行五百里流沙三百里'));
for(const g of review.glyph_issues.slice(0,2)){assert.equal(g.status,'restored_in_reading_layer');assert.ok(index.get(g.passage_id).captured_text.includes(g.captured));}
assert.ok(unitIndex.get('source-04-0045').page_url.endsWith('/113'));
assert.ok(unitIndex.get('source-04-0054').page_url.endsWith('/114'));
const easternPassages=world.passages.filter(p=>p.source_book===4);
assert.deepEqual([1,2,3,4,5].map(r=>easternPassages.filter(p=>p.range===r).length),[13,18,10,9,1]);
for(let i=1;i<easternPassages.length;i++)assert.equal(easternPassages[i-1].source_span[1],easternPassages[i].source_span[0]);
assert.deepEqual([1,2,3,4].map(r=>review.stage_plan.filter(s=>s.range===r&&s.kind==='mountain').length),[12,17,9,8]);
assert.ok(index.get('passage-dongshan-range3-summary').quote.includes('十九山'));
assert.ok(index.get('passage-dongshan-book-total').quote.includes('四十六山萬八千八百六十里'));
assert.equal(index.get('rite-dongshan-book-total').kind,'rite');
assert.ok(!index.get('plant-dongshan-fu-wood-wugao').context_place_id);
assert.equal(index.get('material-dongshan-millet-range3').quote,'米用𮮐');
assert.equal(index.get('beast-dongshan-wei-mengzi').commentary_quote,'鮪即鱏也似鱣而長；鼻體無鱗甲别名䱎䲛一名鱑也');
assert.deepEqual(index.get('passage-dongshan-mengzi').captured_commentary.at(-1).annotations,['鼻體無鱗甲别名䱎䲛一名鱑也']);
assert.ok(index.get('passage-dongshan-mengzi').captured_commentary.find(c=>c.source_unit_id==='source-04-0091').annotations[0].includes('�'));
assert.equal(review.glyph_issues.find(g=>g.source_unit_id==='source-04-0091').status,'facsimile_checked_uncertain_codepoints');
for(const scan of scans.filter(s=>s.detail_local_path))assert.equal(createHash('sha256').update(await readFile(new URL('../../'+scan.detail_local_path,import.meta.url))).digest('hex'),scan.detail_sha256);
for(const [id,q] of [['beast-dongshan-longzhi-fuli','九尾九首虎爪'],['beast-dongshan-youyou-zhenshan','羊目四角牛尾'],['beast-dongshan-gege-qizhong','六足鳥尾'],['beast-dongshan-zi-dongshi','一首而十身'],['beast-fei','白首一目而蛇尾'],['beast-heyu','人面黄身而赤尾']])assert.ok(index.get(id).quote.includes(q),id);
assert.equal(index.get('beast-dangkang').name,'当康');
assert.equal(english['plant-dongshan-junpu-mengzi'].name,'Junpu (Mengzi)');
console.log('PASS data: Eastern complete: 51 passages, 237 cards, 139 source blocks; 34 selected images plus retained Dangkang and 14 documented placeholders; retained legacy IDs');
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
        for(const [book,count] of [[1,43],[2,82],[3,92],[4,51]])assert.equal(await page.locator('[data-source-book="'+book+'"] [data-entry-id]').count(),count);
        await openSourceLibrary(page);
        const eastern=page.locator('[data-source-book="4"]');
        await eastern.locator(':scope > summary').click();
        assert.equal(await eastern.locator('.passage-range').count(),5,'All ranges and closing total visible');
        assert.equal(await eastern.locator('.passage-range').nth(0).locator('[data-entry-id]').count(),13);
        for(const [i,n] of [[1,18],[2,10],[3,9],[4,1]])assert.equal(await eastern.locator('.passage-range').nth(i).locator('[data-entry-id]').count(),n);
        for(const group of await eastern.locator('.passage-range > summary').all())await group.click();
        for(const p of activePassages)assert.equal(await eastern.locator('[data-entry-id="'+p.id+'"]').count(),1);
        await eastern.locator('[data-entry-id="'+activePassages[0].id+'"]').click();await ready(activePassages[0].id);
      }
      await page.goto(`${base}?chapter=04&lang=${lang}`);
      await page.locator('.global-search-trigger').click();
      await page.locator('.global-search-input').fill(lang === 'zh' ? currentPlace.name : english[currentPlace.id].name);
      await page.locator(`.search-result[data-result-kind="${currentPlace.kind}"][data-result-id="${currentPlace.id}"]`).click();
      await ready(currentPlace.id);
      console.log(`PASS ${engine} ${lang}: ${browserEntries.length} current/shared records, 4 viewports, ${roundTrips} nested/context round trips, images, ${commonChecks?'Eastern 51 and previous 217 catalog passages, retained legacy links; ':''}current search`);
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
