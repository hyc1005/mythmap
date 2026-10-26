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
'../../data/zhongshan-edition-review.json','../../data/reference-scans/zhongshan/sources.json',
'../../data/shanhaijing-reference.json','../public/data/atlas/catalog.json','../artwork-source/zhongshan/entities-generation.json'].map(json));
const entries=worldEntries(world),index=new Map(entries.map(e=>[e.id,e]));
const selected=entries.filter(e=>e.content_batch?.startsWith('zhongshan-'));
const newBatches=review.stage_plan.slice(112,127).map(s=>'zhongshan-'+s.slug);
const commonChecks=process.env.ATLAS_COMMON_CHECKS!=='0';
const activeBatches=process.env.ATLAS_BATCH?[process.env.ATLAS_BATCH]:newBatches;
assert.ok(activeBatches.every(b=>newBatches.includes(b)));
const activeIds=new Set(world.passages.filter(p=>activeBatches.includes(p.content_batch)).map(p=>p.id));
const browserEntries=selected.filter(e=>activeBatches.includes(e.content_batch)||e.source_passage_ids?.some(id=>activeIds.has(id)));
const activePassages=world.passages.filter(p=>activeBatches.includes(p.content_batch));
const layoutEntries=[...activePassages,...browserEntries.filter(e=>e.artwork)];
assert.equal(index.size,entries.length);assert.equal(selected.length,868);assert.equal(review.entry_ids.length,741);
assert.deepEqual([1,2,3,4,5].map(b=>world.passages.filter(p=>(p.source_book||1)===b).length),[43,82,92,51,127]);
assert.equal(review.implemented_stages,127);assert.equal(review.remaining_stages,85);assert.equal(review.planned_stages,212);
assert.equal(review.status,'partially_implemented');assert.equal(review.next.name,'風雨之山');
assert.equal(inventory.chapters[4].explained_blocks,388);assert.equal(inventory.chapters[4].semantic_passages,127);
assert.equal(inventory.chapters[4].semantic_review,'partial');
const unitIndex=new Map(inventory.units.map(u=>[u.id,u]));
assert.equal(unitIndex.get('source-05-0001').status,'heading_metadata');
for(let i=2;i<=389;i++)assert.equal(unitIndex.get('source-05-'+String(i).padStart(4,'0')).status,'explained_in_reader');
assert.equal(unitIndex.get('source-05-0390').status,'pending_review');
assert.ok(unitIndex.get('source-05-0009').page_url.endsWith('/2'));
assert.ok(unitIndex.get('source-05-0009').captured_page_url.endsWith('/3'));
for(const p of world.passages.filter(p=>p.source_book===5)){
 const refs=p.source_unit_ids.map(id=>snapshot.chapters[4].lines[Number(id.slice(-4))-1]);
 const raw=refs.map(l=>l.text).join('');
 assert.equal(p.quote,refs.map((l,i)=>p.source_unit_ids[i]==='source-05-0308'?l.text.replaceAll('�','鴆'):p.source_unit_ids[i]==='source-05-0334'?l.text.replace('寓不','寓木'):l.text).join('').replaceAll('⟦缺字图:鬼⟧','鬼').replaceAll('⟦缺字图:冢⟧','冢'));assert.equal(p.captured_text,raw);
 assert.deepEqual(p.captured_commentary.map(c=>c.annotations),refs.map(l=>l.annotations));
 assert.ok(p.range>=1&&p.range<=9);
}
assert.equal(createHash('sha256').update(await readFile(new URL('../../data/shanhaijing-reference.json',import.meta.url))).digest('hex'),review.snapshot_sha256);
assert.equal(scans.length,69);
for(const s of scans)assert.equal(createHash('sha256').update(await readFile(new URL('../../'+s.local_path,import.meta.url))).digest('hex'),s.sha256);
assert.equal(review.font_supplements.length,3);
for(const f of review.font_supplements)assert.equal(createHash('sha256').update(await readFile(new URL('../../'+f.path,import.meta.url))).digest('hex'),f.sha256);
assert.equal(review.font_preflight.implemented_batch_missing_characters,'');
assert.equal(generation.assets.length,49);
for(const a of generation.assets){
 assert.equal(a.status,'reviewed');
 assert.equal(createHash('sha256').update(await readFile(new URL('../artwork-source/zhongshan/'+a.source_file,import.meta.url))).digest('hex'),a.sha256);
 assert.equal(createHash('sha256').update(await readFile(a.original_path)).digest('hex'),a.sha256);
 assert.equal(index.get(a.entry_id).artwork,'zhongshan/'+a.name+'-v1.webp');
}
for(const e of selected){
 assert.ok(english[e.id]?.name&&english[e.id]?.quote&&english[e.id]?.description,e.id);
 assert.ok(!/[\u3400-\u9fff\u{20000}-\u{323af}]/u.test(english[e.id].quote),e.id);
 assert.equal(e.review_status,'facsimile_reviewed');assert.equal(e.reveal_chapter,'04');assert.equal(e.source_book,5);
 assert.equal(readExploration('?chapter=04&item='+e.id,world,catalog).item,e.id);
 for(const id of [...e.related_entry_ids,...(e.source_passage_ids||[])])assert.ok(index.has(id),id);
 if(e.kind==='beast')assert.ok(e.artwork||e.appearance_unknown,e.id);

 if(e.source_passage_ids?.length===1)assert.deepEqual(e.source_unit_ids,index.get(e.source_passage_ids[0]).source_unit_ids);
}
assert.equal(selected.filter(e=>e.appearance_unknown).length,75);
assert.ok(index.get('beast-zhongshan-nuo-gancao').appearance_unknown);
assert.equal(english['place-zhongshan-r01-gancao'].name,'Mount Ganzao');
assert.ok(!index.get('beast-zhongshan-nuo-gancao').artwork);
assert.equal(index.get('beast-zhongshan-nuo-gancao').commentary_quote,'𤠢䑕所未詳音虺字亦或作虺；音那或作熊也');
assert.ok(index.get('beast-zhongshan-hao-quzhu').quote.includes('赤喙尾赤羽'));
assert.equal(index.get('beast-zhongshan-hao-quzhu').commentary_quote,'鮪似鱣也');
assert.equal(index.get('plant-zhongshan-li-lier').commentary_quote,'音厲');
assert.equal(index.get('plant-zhongshan-jian-comparison-lier').commentary_quote,'揀木名子如指頭白而粘可以；浣衣也音練或作簡');
assert.ok(index.get('plant-zhongshan-jian-comparison-lier').comparison_only);
assert.ok(!index.get('plant-zhongshan-jian-comparison-lier').context_place_id);
assert.ok(index.get('plant-zhongshan-jiang-lier').description.includes('不移给'));
assert.ok(!index.get('plant-zhongshan-jiang-lier').quote.includes('方莖'));
const river=index.get('water-zhongshan-he');
assert.equal(river.source_passage_ids.length,14);assert.equal(river.context_place_ids.length,14);
assert.deepEqual(river.source_unit_ids,river.source_passage_ids.flatMap(id=>index.get(id).source_unit_ids));
assert.ok(river.quote.includes('西流注于河')&&river.quote.includes('而南流注于河'));
for(const [a,b] of [['water-zhongshan-gong-gancao',river.id],['water-zhongshan-quzhu',river.id],['water-zhongshan-quzhu','beast-zhongshan-hao-quzhu']]){
 assert.ok(index.get(a).related_entry_ids.includes(b));assert.ok(index.get(b).related_entry_ids.includes(a));
}

for(const [unit,page] of [[54,7],[63,8],[72,9],[81,10],[90,11],[99,12]])assert.ok(unitIndex.get('source-05-'+String(unit).padStart(4,'0')).page_url.endsWith('/'+page));
for(const [id,count] of [['water-zhongshan-yi',9],['water-zhongshan-luo',18],['water-zhongshan-gu',5]])assert.equal(index.get(id).source_passage_ids.length,count);
assert.ok(index.get('water-zhongshan-shao-yin').quote.includes('少水出焉'));
assert.ok(index.get('passage-zhongshan-r01-niushou').captured_text.includes('⟦缺字图:鬼⟧'));
assert.ok(!index.get('passage-zhongshan-r01-niushou').quote.includes('⟦'));
assert.ok(index.get('beast-zhongshan-mingshe-xian').quote.includes('四翼'));
assert.ok(index.get('beast-zhongshan-fuzhu-aoan').quote.includes('四角'));
assert.ok(index.get('beast-zhongshan-feiyu-niushou').quote.includes('如鮒'));
assert.ok(index.get('beast-zhongshan-feiyu-gui').quote.includes('如豚而赤文'));
assert.ok(index.get('beast-zhongshan-huashe-yang').description.includes('不画蛇尾'));
for(const id of ['deity-zhongshan-taifeng-he','deity-zhongshan-xunchi-aoan','deity-zhongshan-wuluo-qingyao']){
 assert.equal(index.get(id).source_passage_ids.length,2);
 assert.ok(index.get('rite-zhongshan-r03-summary').related_entry_ids.includes(id));
}
assert.ok(index.get('beast-zhongshan-linggui-yangxu').commentary_only);
assert.ok(index.get('deity-zhongshan-jiaochong-pingfeng').quote.includes('二首'));
assert.ok(index.get('beast-zhongshan-jue-shou').quote.includes('三目有耳'));
assert.ok(index.get('rite-zhongshan-rooster-pingfeng').quote.includes('勿殺'));

for(const [unit,page] of [[189,22],[198,23],[207,24],[216,25],[225,26],[234,27],[243,28],[252,29],[261,30],[270,31],[279,32],[288,33]])assert.ok(unitIndex.get('source-05-'+String(unit).padStart(4,'0')).page_url.endsWith('/'+page));
for(const slug of ['r06-mountain-194','r07-summary']){const p=index.get('passage-zhongshan-'+slug);assert.ok(p.captured_text.includes('⟦缺字图:冢⟧'));assert.ok(p.quote.includes('冢'));assert.ok(!p.quote.includes('⟦'));}
const localTurtle=index.get('beast-zhongshan-threeleg-da241'), sixeye=index.get('beast-zhongshan-sixeye-comment-da241');
assert.ok(localTurtle.quote.includes('三足'));assert.ok(!localTurtle.quote.includes('六目'));
assert.ok(sixeye.comparison_only&&sixeye.commentary_only&&!sixeye.context_place_id);assert.ok(sixeye.quote.includes('六眼'));
assert.ok(index.get('beast-zhongshan-wenwen-fanggao').quote.includes('反舌'));
assert.ok(index.get('beast-zhongshan-xiubi-tuo').quote.includes('白喙'));
assert.ok(index.get('deity-zhongshan-threeheads-range7').description.includes('躯干'));
assert.ok(!index.get('deity-zhongshan-threeheads-range7').context_place_id);


assert.ok(unitIndex.get('source-05-0297').page_url.endsWith('/34'));
assert.ok(unitIndex.get('source-05-0297').captured_page_url.endsWith('/35'));
assert.equal(index.get('water-zhongshan-ju-range8').source_passage_ids.length,2);
assert.equal(index.get('water-zhongshan-ju-range8').context_place_ids.length,2);
assert.ok(index.get('water-zhongshan-zhang-jingshan8').related_entry_ids.includes('water-zhongshan-ju-range8'));
assert.ok(index.get('beast-zhongshan-li-cattle-jingshan8').commentary_quote.includes('黑色'));
assert.ok(index.get('beast-zhongshan-wenfish-jing8').appearance_unknown);
assert.ok(index.get('beast-zhongshan-jiao-zhang8').appearance_unknown);
assert.ok(index.get('beast-zhongshan-jiao-zhang8').commentary_quote.includes('尾長三四尺'));
assert.ok(index.get('animal-zhongshan-lvmi-jingshan8').appearance_unknown);
assert.deepEqual(index.get('passage-zhongshan-r08-jingshan').source_pages.map(p=>Number(p.split('/').at(-1))),[34,35]);


assert.ok(unitIndex.get('source-05-0306').page_url.endsWith('/35'));
assert.ok(unitIndex.get('source-05-0306').captured_page_url.endsWith('/36'));
const nvji=index.get('passage-zhongshan-r08-nvji');
assert.ok(nvji.quote.includes('多鴆')&&!nvji.quote.includes('�'));
assert.ok(nvji.captured_text.includes('�'));
assert.ok(nvji.captured_commentary.some(c=>c.annotations.some(a=>a.includes('�'))));
assert.ok(nvji.commentary_quote.includes('鴆大如鵰')&&nvji.commentary_quote.includes('長頭')&&nvji.commentary_quote.includes('名運目'));
assert.ok(!nvji.commentary_quote.includes('�'));
assert.ok(index.get('deity-zhongshan-tuowei-jiao').description.includes('局部'));
assert.ok(index.get('beast-zhongshan-whitejiao-nvji').commentary_quote.includes('長尾'));
assert.ok(index.get('beast-zhongshan-zhen-nvji').commentary_quote.includes('紫綠色長頭赤喙'));
assert.deepEqual(nvji.source_pages.map(p=>Number(p.split('/').at(-1))),[35,36]);

for(const [unit,page] of [[315,36],[324,37],[333,38]]){
 const u=unitIndex.get('source-05-'+String(unit).padStart(4,'0'));
 assert.ok(u.page_url.endsWith('/'+page));assert.ok(u.captured_page_url.endsWith('/'+(page+1)));
}
assert.deepEqual(index.get('passage-zhongshan-r08-lun').source_pages.map(p=>Number(p.split('/').at(-1))),[36]);
assert.deepEqual(index.get('passage-zhongshan-r08-tong').source_pages.map(p=>Number(p.split('/').at(-1))),[37,38]);
assert.deepEqual(index.get('passage-zhongshan-r08-long').source_pages.map(p=>Number(p.split('/').at(-1))),[38]);
const heng=index.get('passage-zhongshan-r08-heng');
assert.ok(heng.captured_text.includes('寓不')&&heng.quote.includes('寓木')&&!heng.quote.includes('寓不'));
assert.equal(index.get('water-zhongshan-zhang-jingshan8').source_passage_ids.length,2);
assert.ok(index.get('water-zhongshan-zhang-jingshan8').quote.includes('南流注于漳'));
assert.ok(index.get('water-zhongshan-wei-yizhu8').related_entry_ids.includes('water-zhongshan-zhang-jingshan8'));
assert.ok(index.get('beast-zhongshan-chuo-lun8').commentary_quote.includes('鹿脚青色'));
assert.ok(index.get('beast-zhongshan-chuo-lun8').commentary_quote.endsWith('略反'));
assert.ok(index.get('animal-zhongshan-chuo-dayao8').appearance_unknown);
assert.ok(!index.get('animal-zhongshan-chuo-dayao8').artwork);
assert.ok(index.get('deity-zhongshan-jimeng-guang8').quote.includes('人身而龍首'));
assert.ok(index.get('deity-zhongshan-shetuo-qi8').quote.includes('方面三足'));
assert.ok(index.get('material-zhongshan-white-min-qi8').commentary_quote.includes('石似；玉者'));
assert.equal(index.get('material-zhongshan-gui-stone-ruo8').commentary_quote,'未詳');
assert.equal(index.get('plant-zhongshan-bai-yu8').commentary_quote,'一作楢');
assert.equal(selected.filter(e=>e.content_batch==='zhongshan-r08-zhi'&&e.kind==='animal').length,0);
for(const [unit,page] of [[342,39],[351,40],[360,41],[369,42],[378,43],[387,44]]){
 const u=unitIndex.get('source-05-'+String(unit).padStart(4,'0'));
 assert.ok(u.page_url.endsWith('/'+page));assert.ok(u.captured_page_url.endsWith('/'+(page+1)));
}
assert.deepEqual(index.get('passage-zhongshan-r08-huan').source_pages.map(p=>Number(p.split('/').at(-1))),[39,40]);
assert.deepEqual(index.get('passage-zhongshan-r08-summary').source_pages.map(p=>Number(p.split('/').at(-1))),[40,41]);
assert.deepEqual(index.get('passage-zhongshan-r09-min').source_pages.map(p=>Number(p.split('/').at(-1))),[41,42]);
assert.ok(index.get('deity-zhongshan-humanbird-summary8').quote.includes('鳥身而人面'));
const centralJiang=index.get('water-zhongshan-jiang-range9-nvfan9');
assert.equal(centralJiang.source_passage_ids.length,5);
assert.equal(index.get('water-zhongshan-luo').source_passage_ids.length,18);
assert.equal(index.get('water-zhongshan-luo-nvfan9').source_passage_ids.length,1);
assert.equal(index.get('water-zhongshan-great-jiang-lai9').source_passage_ids.length,2);
const hooked=index.get('beast-zhongshan-hooked-snake-ju9');
assert.ok(hooked.comparison_only&&hooked.commentary_only&&!hooked.context_place_id);
assert.ok(hooked.quote.includes('尾岐'));
assert.ok(index.get('beast-zhongshan-mo-lai9').commentary_only);
assert.ok(index.get('beast-zhongshan-tuo-min9').commentary_quote.includes('鱗彩'));
assert.ok(index.get('beast-zhongshan-kui-cattle-min9').commentary_quote.includes('大牛'));
assert.ok(index.get('beast-zhongshan-qiezhi-ju9').quote.includes('赤身白首'));
assert.ok(index.get('beast-zhongshan-balang-she9').quote.includes('白尾長耳'));
assert.ok(index.get('beast-zhongshan-wei-ge9').commentary_quote.includes('尾四五尺頭有岐'));
assert.ok(index.get('plant-zhongshan-mei-qi9').commentary_quote.includes('𱾗'));
console.log('PASS data: Central 127 passages /741 cards, 388 source blocks, 49 reviewed images and 75 documented placeholders; local anatomy, reading restoration and shared river contexts');
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
    let openedView;
    async function open(id, lang = 'zh') {
      const url=`${base}?chapter=04&item=${id}&lang=${lang}`;
      const view=lang+':'+page.viewportSize().width;
      if(openedView===view&&page.url().startsWith(base)){
        await page.evaluate(url=>{history.pushState(null,'',url);dispatchEvent(new PopStateEvent('popstate',{state:null}));},url);
      }else await page.goto(url);
      openedView=view;
      await page.waitForFunction(lang=>document.documentElement.lang===(lang==='en'?'en':'zh-CN'),lang);
      return ready(id);
    }
    for (const lang of (process.env.ATLAS_LANGUAGES || 'zh,en').split(',')) {
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
      if(activeBatches.includes('zhongshan-r01-lier')){
        d=await open('place-zhongshan-r01-lier',lang);
        assert.equal(await d.locator('.detail-place-contents [data-related-id="plant-zhongshan-jian-comparison-lier"]').count(),0);
        await d.locator('[data-related-id="plant-zhongshan-jian-comparison-lier"]').click();await ready('plant-zhongshan-jian-comparison-lier');
        await page.locator('.return-related').click();await ready('place-zhongshan-r01-lier');roundTrips++;
      }

      for(const card of browserEntries.filter(e=>e.comparison_only)){
        const root=index.get(index.get(card.source_passage_ids[0]).related_entry_ids[0]);
        d=await open(root.id,lang);
        assert.equal(await d.locator('.detail-place-contents [data-related-id="'+card.id+'"]').count(),0);
        await d.locator('[data-related-id="'+card.id+'"]').click();await ready(card.id);
        await page.locator('.return-related').click();await ready(root.id);roundTrips++;
      }
      for(const slug of ['r07-ku','r07-shaoshi','r07-taishi'])if(activeBatches.includes('zhongshan-'+slug)){
        const id='place-zhongshan-'+slug, target='deity-zhongshan-threeheads-range7';
        d=await open(id,lang);await d.locator('[data-related-id="'+target+'"]').click();await ready(target);
        await page.locator('.return-related').click();await ready(id);roundTrips++;
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
        for(const [book,count] of [[1,43],[2,82],[3,92],[4,51],[5,127]])assert.equal(await page.locator('[data-source-book="'+book+'"] [data-entry-id]').count(),count);
        const central=page.locator('[data-source-book="5"]');
        await central.locator(':scope > summary').click();
        assert.equal(await central.locator('.passage-range').count(),9);
        assert.equal(await central.locator('.passage-range').nth(0).locator('[data-entry-id]').count(),16);
        for(const range of await central.locator('.passage-range').all())await range.locator(':scope > summary').click();
        for(const p of activePassages)assert.equal(await central.locator('[data-entry-id="'+p.id+'"]').count(),1);
        await central.locator('[data-entry-id="'+activePassages[0].id+'"]').click();await ready(activePassages[0].id);
      }
      await page.goto(`${base}?chapter=04&lang=${lang}`);
      await page.locator('.global-search-trigger').click();
      await page.locator('.global-search-input').fill(lang === 'zh' ? currentPlace.name : english[currentPlace.id].name);
      await page.locator(`.search-result[data-result-kind="${currentPlace.kind}"][data-result-id="${currentPlace.id}"]`).click();
      await ready(currentPlace.id);
      console.log(`PASS ${engine} ${lang}: ${browserEntries.length} current/shared records, direct loads and client history, 4 viewports, ${roundTrips} nested/context round trips, images, ${commonChecks?'Central 127 and previous 268 catalog passages, retained legacy links; ':''}current search`);
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
      for(const family of ['Atlas Central Rare','Atlas Central ExtH'])for(const w of [400,600])await document.fonts.load(w+' 20px "'+family+'"',characters);
      for (const w of [400, 600]) await document.fonts.load(`${w} 20px "Shanhai Title"`, characters);
    }, review.font_supplements.map(f=>f.characters).join(''));
    if(engine==='chromium'){
      const cdp=await context.newCDPSession(page);await cdp.send('DOM.enable');await cdp.send('CSS.enable');
      for(const supplement of review.font_supplements.filter(f=>f.family.startsWith('Atlas Central'))){
      const {characters,family}=supplement;
      for(const weight of [400,600]){
        await page.evaluate(({characters,weight})=>{const h=document.querySelector('.detail-drawer h2');h.innerHTML='';const probe=document.createElement('span');probe.id='central-rare-probe';probe.textContent=characters;probe.style.fontWeight=weight;h.append(probe);return document.fonts.ready;},{characters,weight});
        const doc=await cdp.send('DOM.getDocument');const node=await cdp.send('DOM.querySelector',{nodeId:doc.root.nodeId,selector:'#central-rare-probe'});
        const {fonts}=await cdp.send('CSS.getPlatformFontsForNode',{nodeId:node.nodeId});
        assert.ok(fonts.length&&fonts.every(f=>f.isCustomFont&&f.familyName===family),JSON.stringify(fonts));
        assert.equal(fonts.reduce((n,f)=>n+f.glyphCount,0),Array.from(characters).length);
      }
      }
      await cdp.detach();
    }
    assert.deepEqual(errors, []);
    assert.deepEqual(missing, []);
    await context.close();
    console.log(`PASS ${engine}: read/favorite refresh, resume, title face loading; zero page/resource errors`);
  } finally {
    await browser.close();
  }
}
