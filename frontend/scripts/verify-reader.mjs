import assert from 'node:assert/strict';
import { mkdir, readFile } from 'node:fs/promises';
import { chromium, firefox, webkit } from 'playwright';
import { worldEntries } from '../src/entries.js';
import { searchIndex, searchEntries } from '../src/search.js';
import { relatedEntries } from '../src/entry-relations.js';
import { mockTianditu } from './mock-tianditu.mjs';

const base = process.env.ATLAS_URL;
if (!base) throw new Error('Run through with-preview.mjs');
const json = async path => JSON.parse(await readFile(new URL(path, import.meta.url), 'utf8'));
const [world, catalog, en, inventory, review] = await Promise.all(['../public/data/myth-world.json','../public/data/atlas/catalog.json','../src/locale-content-en.json','../../data/shanhaijing-inventory.json','../../data/nanshan-edition-review.json'].map(json));
assert.equal(inventory.chapters.length,18);
assert.equal(inventory.units.length,2437);
const southern = world.passages.filter(p => p.id.startsWith('passage-nanshan-'));
assert.equal(southern.length,43);
assert.equal(review.counts.mountain_passages,39);
assert.deepEqual(southern.map(p=>p.order),Array.from({length:43},(_,i)=>i+1));
for (let i=1;i<43;i++) assert.equal(southern[i-1].source_span[1],southern[i].source_span[0], 'No source gaps between passages');
assert.ok(inventory.units.filter(u=>u.chapter===1).every(u=>u.status==='heading_metadata'||u.confirmed_passage_ids.length));
assert.ok(inventory.units.filter(u=>u.chapter!==1 && u.status==='explained_in_reader').every(u=>u.confirmed_passage_ids.length && u.confirmed_passage_ids.every(id=>world.passages.some(p=>p.id===id && p.review_status==='facsimile_reviewed'))), 'Other chapters require explicit reviewed passages, not automatic matching');
assert.equal(world.passages.filter(p=>p.source_pages.some(url=>url.endsWith('/26'))).length,3);
assert.ok(world.passages.find(p=>p.id==='passage-nanshan-range1').quote.includes('二千九百五十里'));
assert.deepEqual(review.counts.printed_range_counts,[10,17,14]);
assert.equal(review.counts.printed_closing_count,40);
const index = new Map(worldEntries(world).map(item=>[item.id,item]));
const search=searchIndex(world,catalog,world,catalog);
for (const passage of world.passages) {
  assert.ok(en[passage.id]?.quote && en[passage.id]?.description && !/[\u3400-\u9fff]/.test(en[passage.id].description));
  assert.ok(!('x' in passage || 'y' in passage));
  assert.ok(searchEntries(search,passage.name,'passage').some(p=>p.id===passage.id));
  assert.ok(passage.source_unit_ids.every(id=>inventory.units.some(u=>u.id===id)));
  for (const id of passage.related_entry_ids) assert.ok(relatedEntries(passage.id,index).some(p=>p.id===id));
}
await mkdir(new URL('../../output/qa/',import.meta.url),{recursive:true});
for (const name of (process.env.ATLAS_BROWSERS||'chromium,webkit').split(',')) {
  const browser=await ({chromium,firefox,webkit}[name]).launch();
  try {
    const context=await browser.newContext({viewport:{width:390,height:844},reducedMotion:'reduce'});
    await mockTianditu(context);
    const page=await context.newPage(),errors=[],failed=[],requested=[];
    page.on('pageerror',e=>errors.push(e.message));
    page.on('request',r=>requested.push(r.url()));
    page.on('response',r=>{if(r.status()>=400 && !r.url().includes('/api/'))failed.push(r.url());});
    await page.goto(`${base}?chapter=02&lang=zh`);
    assert.ok(!requested.some(url=>/nanshan\/(tangting|xun|danxue)-v1\.webp/.test(url)), 'Directory does not preload full scenes');
    await page.evaluate(()=>localStorage.setItem('shanhai-reading-v1',JSON.stringify({version:1,read:['beast-guan'],favorites:['beast-guan']})));
    await page.reload();
    await page.locator('.mobile-explore-nav button').nth(1).click();
    const directory=page.locator('.chapter-text-entries:visible');
    await directory.locator('>summary').click();
    await directory.locator('.passage-range>summary').nth(1).click();
    await directory.locator('[data-entry-id="passage-nanshan-xun"]').click();
    const drawer=page.locator('.detail-drawer');
    const ready=async id=>page.waitForFunction(id=>{
      const node=document.querySelector('.detail-drawer');
      return node?.dataset.entryId===id && node.dataset.readingRestoring==='false';
    },id);
    await ready('passage-nanshan-xun');
    assert.ok((await drawer.locator('.detail-description').innerText()).includes('第26页'));
    await drawer.locator('.detail-reading-actions button').nth(0).click();
    await drawer.locator('.detail-reading-actions button').nth(1).click();
    await page.reload();await ready('passage-nanshan-xun');
    assert.ok(await drawer.locator('.detail-reading-actions button').evaluateAll(nodes=>nodes.every(n=>n.getAttribute('aria-pressed')==='true')));
    const marks=await page.evaluate(()=>JSON.parse(localStorage.getItem('shanhai-reading-v1')));
    assert.ok(marks.read.includes('beast-guan') && marks.favorites.includes('beast-guan'),'Old marks retained');
    await drawer.locator('[data-reading-anchor="source"]').scrollIntoViewIfNeeded();
    await page.waitForTimeout(250);
    await page.goto(`${base}?lang=zh`);
    await page.locator('.resume-reading').click();await ready('passage-nanshan-xun');
    assert.ok(await drawer.evaluate(node=>node.scrollTop>0));
    await page.goto(`${base}?chapter=02&lang=en`);
    await page.locator('.global-search-trigger').click();
    await page.locator('.global-search-tools select').selectOption('passage');
    await page.locator('.global-search-input').fill('洵山');
    await page.locator('.search-result[data-result-id="passage-nanshan-xun"]').click();await ready('passage-nanshan-xun');
    assert.equal(await drawer.locator('.detail-description').innerText(),en['passage-nanshan-xun'].description);
    await drawer.locator('.return-search').click();
    assert.equal(await page.locator('.global-search-input').inputValue(),'洵山');
    for (const passage of southern) {
      await page.goto(`${base}?chapter=02&item=${passage.id}&lang=zh`);await ready(passage.id);
      assert.equal(await drawer.locator('>.content-origin').getAttribute('data-origin'),'shanhaijing');
      assert.equal(await drawer.evaluate(node=>node.scrollWidth>node.clientWidth),false,passage.id);
      assert.equal(await drawer.locator('[data-reading-anchor="quote"]+blockquote').innerText(),passage.quote);
    }
    await page.goto(`${base}?chapter=02&item=passage-nanshan-niuyang&lang=en`);await ready('passage-nanshan-niuyang');
    await drawer.locator('[data-related-id="water-guai"]').click();await ready('water-guai');
    await page.goBack();await ready('passage-nanshan-niuyang');
    assert.equal(new URL(page.url()).searchParams.get('chapter'),'02');
    assert.equal(await page.locator('.myth-map-wrap').getAttribute('data-map-mode'),'woodcut');
    for(const id of ['passage-nanshan-tangting','passage-nanshan-xun','passage-nanshan-danxue']) {
      await page.goto(`${base}?chapter=02&item=${id}&lang=en`);await ready(id);
      await drawer.locator('.drawer-art').scrollIntoViewIfNeeded();
      await drawer.locator('.drawer-art').evaluate(img=>img.decode());
      assert.ok(await drawer.locator('.drawer-art').evaluate(img=>img.naturalWidth>0),'New scene is actually used');
      assert.ok((await drawer.locator('.artwork-caption').innerText()).startsWith('Place scene'));
      if(name==='chromium')await drawer.screenshot({path:new URL(`../../output/qa/${id}-art.png`,import.meta.url).pathname.replace(/^\/([A-Za-z]:)/,'$1')});
    }
    for(const [width,height] of [[320,700],[390,844],[844,390],[1440,1000]])for(const lang of ['zh','en']) {
      await page.setViewportSize({width,height});
      await page.goto(`${base}?chapter=02&item=passage-nanshan-daoguo&lang=${lang}`);await ready('passage-nanshan-daoguo');
      assert.equal(await drawer.evaluate(node=>node.scrollWidth>node.clientWidth),false);
      await drawer.locator('.commentary-section>summary').click();
      assert.equal(await drawer.evaluate(node=>node.scrollWidth>node.clientWidth),false,'Expanded commentary fits');
      if(name==='chromium' && width===390)await drawer.screenshot({path:new URL(`../../output/qa/reader-${lang}.png`,import.meta.url).pathname.replace(/^\/([A-Za-z]:)/,'$1')});
    }
    assert.deepEqual(errors,[]);assert.deepEqual(failed,[]);
    await page.route('**/terrain/*.webp',route=>route.abort());
    await page.goto(`${base}?chapter=02&item=passage-nanshan-xun&lang=en`);await ready('passage-nanshan-xun');
    await page.waitForTimeout(500);
    assert.equal(await drawer.locator('.detail-description').innerText(),en['passage-nanshan-xun'].description);
    assert.deepEqual(errors,[],'Interrupted map images must not throw during reading');
    await context.close();
    console.log(`PASS ${name}: 43 passages, restored page, directory/search, old/new marks, resume/history/context and 8 layouts`);
  } finally {await browser.close();}
}
