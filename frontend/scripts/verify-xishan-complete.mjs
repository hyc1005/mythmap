import assert from 'node:assert/strict';
import { browserDiagnostics } from './browser-diagnostics.mjs';
import { readFile, stat } from 'node:fs/promises';
import { resolve, sep } from 'node:path';
import { chromium, webkit } from 'playwright';
import { worldEntries } from '../src/entries.js';
import { searchEntries, searchIndex } from '../src/search.js';
import { mockTianditu } from './mock-tianditu.mjs';

const json = async path => JSON.parse(await readFile(new URL(path, import.meta.url), 'utf8'));
const [world, english, inventory, review, relations, generation] = await Promise.all([
  '../public/data/myth-world.json', '../src/locale-content-en.json', '../../data/shanhaijing-inventory.json',
  '../../data/xishan-edition-review.json', '../src/xishan-relations.json', '../artwork-source/xishan/generation.json',
].map(json));
const entries = worldEntries(world), index = new Map(entries.map(e => [e.id, e]));
assert.equal(index.size, entries.length, 'Unique global IDs');
const passages = world.passages.filter(p => p.source_book === 2);
const cards = entries.filter(e => e.content_batch?.startsWith('xishan-') && e.kind !== 'passage');
assert.equal(passages.length, 82);
assert.equal(cards.length, 508);
assert.deepEqual(passages.map(p => p.order), Array.from({ length: 82 }, (_, i) => i + 1));
assert.deepEqual([1, 2, 3, 4].map(n => passages.filter(p => p.range === n && !p.is_summary).length), [19, 17, 22, 19]);
assert.equal(passages.filter(p => p.is_summary).length, 5);
assert.equal(world.passages.filter(p => p.id.startsWith('passage-nanshan-')).length, 43);
const westernUnits = inventory.units.filter(u => u.chapter === 2);
assert.equal(westernUnits.length, 378);
assert.equal(inventory.chapters[1].pending_candidate_passages, 0);
assert.equal(inventory.chapters[1].semantic_review, 'reviewed');
const covered = new Set(passages.flatMap(p => p.source_unit_ids));
for (let i = 3; i <= 378; i++) assert.ok(covered.has(`source-02-${String(i).padStart(4, '0')}`));
assert.equal(covered.size, 376);
assert.equal(review.entry_ids.length, cards.length);
assert.ok(english['passage-xishan-futang'].description.includes('Fuyang'));
assert.ok(english['passage-xishan-futang'].quote.includes('Fuyang'));
assert.deepEqual(review.scan_pages, Array.from({ length: 42 }, (_, i) => i + 34));
for (const relation of relations) for (const id of relation.ids) assert.ok(index.has(id), `Relation target ${id}`);
for (const e of [...passages, ...cards]) {
  assert.ok(english[e.id]?.name && english[e.id]?.description && english[e.id]?.quote, e.id);
  assert.ok(e.source_pages.length && e.source_unit_ids.length, e.id);
  for (const id of [...(e.related_entry_ids || []), ...(e.source_passage_ids || [])]) assert.ok(index.has(id), `${e.id} -> ${id}`);
  if (e.context_place_id) assert.ok(index.has(e.context_place_id));
}
const kunlun = index.get('place-xishan-kunlun');
assert.deepEqual(kunlun.source_passage_ids, ['passage-xishan-huaijiang', 'passage-xishan-kunlun']);
assert.ok(index.get('passage-xishan-huaijiang').related_entry_ids.includes(kunlun.id));
assert.deepEqual(index.get('place-xishan-liusha').source_passage_ids,['passage-xishan-taiqi','passage-xishan-luomushan']);
assert.ok(index.has('place-xishan-kunlun-yang-zhongshan'));
for(const id of ['place-xishan-kunlun','place-xishan-zhongshan'])assert.ok(!index.get(id).context_place_ids.includes(id),'A shared mountain must not list itself as a resident');
assert.ok(index.get('beast-luwu').quote.includes('九尾人面而虎𤓰'));
assert.ok(index.get('beast-qiongqi-xishan').quote.includes('如牛蝟毛'));
assert.ok(index.get('beast-qiongqi-hainei').quote.includes('如虎'));
assert.ok(index.get('beast-bo').quote.includes('一角虎牙爪'));
assert.ok(index.get('beast-xishan-manman-gangwei').quote.includes('鼠身而鼈首'));
assert.ok(index.get('bird-xishan-manman-chongwu').quote.includes('一翼一目'));
assert.notEqual(index.get('place-xishan-yinshan3').id, index.get('place-xishan-yinshan4').id);
assert.ok(index.get('passage-xishan-range3-summary').quote.includes('二十三山'));
assert.ok(index.get('passage-xishan-western-total').quote.includes('一萬七千五百一十七里'));
for(const [id,cn] of [['range1-summary','二千九百五十七里'],['range2-summary','四千一百四十里'],['range3-summary','六千七百四十四里'],['range4-summary','三千六百八十里']])assert.ok(index.get('passage-xishan-'+id).quote.includes(cn));
assert.equal(2957+4140+6744+3680,17521);
assert.ok(index.get('passage-xishan-western-total').description.includes('17521'));
const newPassages = passages.slice(45), batches = new Set(newPassages.map(p => p.content_batch));
assert.equal(generation.assets.length,90);
assert.ok(generation.assets.every(a=>a.status==='reviewed'));
assert.equal(generation.assets.filter(a=>a.entry_id).length,34);
for(const a of generation.assets.filter(a=>a.entry_id))assert.equal(index.get(a.entry_id)?.artwork,`xishan/${a.name}-v1.webp`,a.name);
const changedArt = generation.assets.filter(a => a.entry_id).map(a => a.entry_id);
const imageOnly=process.env.ATLAS_IMAGES_ONLY==='1';
const selected = [...new Map([...entries.filter(e => !imageOnly&&batches.has(e.content_batch)),
  ...changedArt.map(id => index.get(id)), index.get('passage-xishan-huaijiang'), index.get('place-xishan-liusha'),
  ...(imageOnly?['passage-xishan-sanwei','place-xishan-sanwei','place-xishan-zhongqu','passage-xishan-zhongqu','plant-xishan-huai-zhongqu','bird-xishan-xiao-baiyu','place-xishan-huaijiang','place-xishan-kunlun','place-xishan-zhongshan','passage-xishan-futang','place-xishan-futang','plant-xishan-zong-futang','plant-xishan-nan-futang'].map(id=>index.get(id)):[]),
  index.get('beast-xishan-zhuyan-xiaoci'), index.get('deity-xishan-yingzhao-huaijiang'),
  index.get('beast-xishan-wenyao-taiqi')].filter(Boolean).map(e => [e.id,e])).values()];
assert.equal(newPassages.length,37);
for(const id of ['beast-luwu','beast-tulou','beast-qinyuan','beast-zheng','beast-bifang','beast-tian-gou','beast-dijiang','beast-guan','beast-bo','beast-qiongqi-xishan','beast-luoyu']) {
 assert.ok(index.get(id).content_batch.startsWith('xishan-'));
 assert.equal(index.get(id).reveal_chapter,'05');
 assert.equal(index.get(id).place_id,'place-west-ranges');
}
console.log(`PASS data: all 378 Western source blocks classified, 82 passages, 77 named mountains, ${cards.length} cards, 37 completion stages and stable core IDs`);
if(process.env.ATLAS_DATA_ONLY==='1') process.exit(0);

const base=process.env.ATLAS_URL || 'https://atlas.test/mythmap/';
const root=resolve(process.env.ATLAS_STATIC_DIR || 'dist');
const engines=(process.env.ATLAS_BROWSERS || 'chromium,webkit').split(',');
const viewportSizes=[{width:320,height:740},{width:390,height:844},{width:844,height:390},{width:1440,height:1000}];
for(const engine of engines){
 const browser=await ({chromium,webkit}[engine]).launch();
 let captureFailure;
 try{
  const context=await browser.newContext({viewport:viewportSizes[1],reducedMotion:'reduce'});
  captureFailure = browserDiagnostics(context, `western-${engine}`);
  await mockTianditu(context);
  await context.route('https://atlas.test/**',async route=>{
   const u=new URL(route.request().url());
   if(!u.pathname.startsWith('/mythmap/'))return route.fulfill({status:404,body:'Wrong base'});
   const file=resolve(root,decodeURIComponent(u.pathname.slice('/mythmap/'.length))||'index.html');
   if(!file.startsWith(root+sep)||!(await stat(file).catch(()=>null))?.isFile())return route.fulfill({status:404,body:'Missing file'});
   await route.fulfill({path:file});
  });
  await context.addInitScript(()=>{
   if(location.origin==='https://atlas.test')localStorage.setItem('shanhai-onboarding-v1','1');
  });
  let page=await context.newPage();const errors=[],missing=[];
  context.on('page',p=>p.on('pageerror',e=>errors.push(e.message)));
  page.on('pageerror',e=>errors.push(e.message));
  context.on('response',r=>{if(r.status()>=400&&r.url().startsWith(base))missing.push(r.url());});
  async function open(e,lang){
   await page.goto(`${base}?chapter=03&item=${encodeURIComponent(e.id)}&lang=${lang}`);
   await page.waitForFunction(id=>{const d=document.querySelector('.detail-drawer');return d?.dataset.entryId===id&&d.dataset.readingRestoring==='false'},e.id);
   await page.evaluate(()=>document.fonts.ready);
   return page.locator('.detail-drawer');
  }
  for(const lang of ['zh','en']){
   let count=0;
   for(const e of selected){
    const d=await open(e,lang);
    assert.equal(await d.locator('h2').innerText(),lang==='en'?english[e.id].name:e.name,e.id);
    assert.equal(await d.locator('.detail-description').innerText(),lang==='en'?english[e.id].description:e.description,e.id);
    assert.ok(!await d.evaluate(n=>n.scrollWidth>n.clientWidth),e.id+' horizontal overflow');
    assert.equal(await d.locator(`.detail-place-contents [data-related-id="${e.id}"]`).count(),0,e.id+' should not list itself');
    const image=d.locator('.drawer-art');
    if(await image.count()){
     await image.evaluate(i=>i.decode());
     const src=await image.getAttribute('src');
     assert.ok(await image.evaluate(i=>i.naturalWidth>0),e.id);
     if(e.artwork)assert.ok(!src.includes('unknown-creature-v4'),e.id+' selected artwork');
     else assert.ok(src.includes('unknown-creature-v4'),e.id+' placeholder');
    }else assert.ok(!e.artwork,e.id+' missing selected artwork');
    for(const button of await d.locator('[data-related-id]').all()){
     const target=await button.getAttribute('data-related-id');assert.ok(index.has(target),`${e.id} link ${target}`);
    }
    if(!imageOnly&&e.kind==='passage'&&batches.has(e.content_batch)&&e.related_entry_ids.length){
     const child=e.related_entry_ids[0];
     await d.locator(`[data-related-id="${child}"]`).first().click();
     await page.waitForFunction(id=>document.querySelector('.detail-drawer')?.dataset.entryId===id,child);
     await page.locator('.detail-drawer .return-related').click();
     await page.waitForFunction(id=>document.querySelector('.detail-drawer')?.dataset.entryId===id,e.id);
    }
    count++;
    if(count%30===0){console.log(`PROGRESS ${engine} ${lang}: ${count}/${selected.length}`);await page.close();page=await context.newPage();}
   }
   console.log(`PASS ${engine} ${lang}: ${count} completion and image records`);
  }
  // Every stage is checked at each small and large viewport in both languages.
  const layoutPassages = ['kunlun','yushan','range3-summary','yingdi','yanzi','range4-summary','western-total'].map(slug=>index.get('passage-xishan-'+slug));
  for(const lang of ['zh','en'])for(const viewport of viewportSizes){
   await page.setViewportSize(viewport);
   for(const e of !imageOnly&&viewport.width===320?newPassages:layoutPassages){const d=await open(e,lang);assert.ok(!await d.evaluate(n=>n.scrollWidth>n.clientWidth),e.id);}
  }
  const rare=[...new Set([...passages,...cards].flatMap(e=>[e.name,e.quote,e.commentary_quote,e.description,e.content_note].filter(Boolean)).join(''))].filter(c=>{const n=c.codePointAt(0);return n>=0x3400&&n<=0x4DBF||n>=0x20000&&n<=0x323AF}).join('');
  await page.evaluate(async text=>{for(const w of [400,600])await document.fonts.load(`${w} 18px ShanhaiRare`,text)},rare);
  // Verify catalog reachability across all five Western groups, including the closing total.
  await page.goto(base+'?chapter=03&lang=zh');
  const western=page.locator('[data-source-book="2"]');await western.locator(':scope > summary').click();
  assert.equal(await western.locator('.passage-range').count(),5);
  assert.equal(await western.locator('[data-entry-id^="passage-xishan-"]').count(),82);
  for(const e of newPassages){assert.equal(await western.locator(`[data-entry-id="${e.id}"]`).count(),1);}
  const catalog=await json('../public/data/atlas/catalog.json');
  const search=searchIndex(world,catalog,world,catalog,'zh');
  for(const query of ['陸吾','欽原','𢕟𢓨','鵸䳜','冉遺','孰湖'])assert.ok(searchEntries(search,query).length,query);
  assert.ok(searchEntries(search,'陆吾').some(item=>item.id==='beast-luwu'),'Retained simplified name');
  if(!imageOnly){
   for(const lang of ['zh','en'])for(const id of ['beast-luwu','beast-xishan-manman-gangwei','beast-xishan-ranyi-yingdi']){
    await page.goto(base+'?chapter=03&lang='+lang);await page.locator('.global-search-trigger').click();
    await page.locator('.global-search-input').fill(lang==='zh'?index.get(id).name:english[id].name);
    await page.locator(`.search-result[data-result-id="${id}"]`).click();
    await page.waitForFunction(id=>document.querySelector('.detail-drawer')?.dataset.entryId===id,id);
    await page.locator('.return-search').click();
   }
   const id='passage-xishan-yanzi';let d=await open(index.get(id),'zh');
   await d.getByRole('button',{name:'收藏条目',exact:true}).click();await d.getByRole('button',{name:'标为已读',exact:true}).click();
   await page.reload();await page.waitForFunction(id=>document.querySelector('.detail-drawer')?.dataset.entryId===id,id);
   d=page.locator('.detail-drawer');assert.equal(await d.getByRole('button',{name:'已收藏 · 取消',exact:true}).getAttribute('aria-pressed'),'true');
   assert.equal(await d.getByRole('button',{name:'已读 · 撤销',exact:true}).getAttribute('aria-pressed'),'true');
   await d.locator('[data-reading-anchor="source"]').scrollIntoViewIfNeeded();
   await page.waitForFunction(id=>{const s=JSON.parse(localStorage.getItem('shanhai-last-reading-v1'));return s?.id===id&&s.position?.anchor!=='start'},id);
   await page.goto(base+'?lang=zh');await page.waitForFunction(()=>window.history.state?.shanhai?.stageIndex===0);
   await page.locator('.resume-reading[aria-label]').click();
   await page.waitForFunction(id=>{const d=document.querySelector('.detail-drawer');return d?.dataset.entryId===id&&d.dataset.readingRestoring==='false'},id);
   assert.ok(await page.locator('.detail-drawer').evaluate(n=>n.scrollTop>0));
  }
  assert.deepEqual(errors,[]);assert.deepEqual(missing,[]);
  await context.close();
  console.log(`PASS ${engine}: ${selected.length} records in both languages, ${imageOnly?'7 representative stages in 8 layouts':'all 37 stages at 320px plus 7 representative stages in 8 layouts'}, 5 catalog groups, artwork decoding, rare font load and zero page/resource errors`);
 } catch (error) {
    try { await captureFailure?.(error); } catch (captureError) { console.error('Failure capture failed:', captureError.message); }
    throw error;
  } finally { await browser.close(); }
}
