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
const newBatches = ['shishan','tongrong','gaoshi','lushan','yishan','yanshan','raoshan','ganshan','lunshan','jieshi','yanmenshan','taize-didu','mufeng','range3-summary','book-total'].map(s => 'beishan-'+s);
const commonChecks = process.env.ATLAS_COMMON_CHECKS !== '0';
const activeBatches = process.env.ATLAS_BATCH ? [process.env.ATLAS_BATCH] : newBatches;
assert.ok(activeBatches.every(b => newBatches.includes(b)));
const sharedBatches = {'water-beishan-he':['gaoshi','lushan','yishan','yanshan','raoshan','lunshan','jieshi'],'water-beishan-huchi-taitou':['shishan','gaoshi']};
const browserEntries = selected.filter(e => activeBatches.includes(e.content_batch) || sharedBatches[e.id]?.some(s=>activeBatches.includes('beishan-'+s)));
const activePassages = world.passages.filter(p => activeBatches.includes(p.content_batch));
const layoutEntries = [...activePassages, ...activePassages.map(p => {
  const creatures=browserEntries.filter(e=>e.content_batch===p.content_batch&&e.artwork&&['beast','deity','plant'].includes(e.kind));
  return creatures.find(e=>/youyu|heluo|xixi/.test(e.id))||creatures[0];
}).filter(Boolean)];
const passage = index.get('passage-beishan-danhu');
const place = index.get('place-beishan-danhu');
assert.equal(index.size, entries.length);
assert.equal(selected.length, 599);
assert.equal(review.entry_ids.length, 507);
assert.equal(world.passages.filter(p => p.id.startsWith('passage-nanshan-')).length, 43);
assert.equal(world.passages.filter(p => p.source_book === 2).length, 82);
assert.equal(world.passages.filter(p => p.source_book === 3).length, 92);
assert.deepEqual(passage.source_unit_ids, ['source-03-0002', 'source-03-0003', 'source-03-0004']);
assert.equal(passage.quote, snapshot.chapters[2].lines.slice(1, 4).map(l => l.text).join(''));
assert.equal(passage.captured_text, passage.quote);
assert.ok(!passage.quote.includes('求如'));
assert.ok(passage.commentary_quote.includes('出蜀中音\n〔影印页76〕飢；音逢'));
assert.ok(index.get('plant-beishan-ji-danhu').commentary_quote.endsWith('音飢'));
assert.deepEqual(passage.captured_commentary.map(r => r.annotations), snapshot.chapters[2].lines.slice(1, 4).map(l => l.annotations));
assert.equal(inventory.chapters[2].explained_blocks, 296);
assert.equal(inventory.chapters[2].semantic_review, 'reviewed');
assert.equal(inventory.chapters[2].pending_candidate_passages, 0);
assert.equal(inventory.units.find(u => u.id === 'source-03-0001').status, 'heading_metadata');
assert.equal(inventory.units.find(u => u.id === 'source-03-0259').status, 'explained_in_reader');
for (const [id,page,captured] of [['source-03-0018',77,78],['source-03-0027',78,79],['source-03-0036',79,80],['source-03-0045',80,81],['source-03-0054',81,82],['source-03-0063',82,83],['source-03-0072',83,84],['source-03-0081',84,85],['source-03-0090',85,86],['source-03-0099',86,87],['source-03-0108',87,88],['source-03-0117',88,89],['source-03-0126',89,90],['source-03-0135',90,91],['source-03-0144',91,92],['source-03-0153',92,93],['source-03-0162',93,94],['source-03-0171',94,95],['source-03-0180',95,96],['source-03-0189',96,97],['source-03-0198',97,98],['source-03-0207',98,99],['source-03-0216',99,100],['source-03-0225',100,101],['source-03-0234',101,102],['source-03-0243',102,103],['source-03-0252',103,104],['source-03-0261',104,105],['source-03-0270',105,106],['source-03-0279',106,107],['source-03-0288',107,108]]) {
  const u=inventory.units.find(u=>u.id===id); assert.ok(u.page_url.endsWith('/'+page)); assert.ok(u.captured_page_url.endsWith('/'+captured));
}
assert.deepEqual(world.passages.filter(p=>p.source_book===3).map(p=>p.order),Array.from({length:92},(_,i)=>i+1));
const covered=new Set(world.passages.filter(p=>p.source_book===3).flatMap(p=>p.source_unit_ids));
assert.equal(covered.size,296);
for(let i=2;i<=297;i++)assert.ok(covered.has('source-03-'+String(i).padStart(4,'0')));
for(const p of world.passages.filter(p=>p.source_book===3)) {
  const raw=p.source_unit_ids.map(id=>snapshot.chapters[2].lines[Number(id.slice(-4))-1].text).join('');
  let restored=raw;for(const c of review.text_corrections.filter(c=>p.source_unit_ids.includes(c.source_unit_id)))restored=restored.replace(c.captured,c.replacement);
  assert.equal(p.captured_text,raw,p.id+' captured boundary');assert.equal(p.quote,restored,p.id+' restored boundary');
}
assert.deepEqual(index.get('passage-beishan-bianchun').source_unit_ids,['source-03-0040','source-03-0041','source-03-0042','source-03-0043']);
assert.deepEqual(index.get('plant-beishan-kui-bianchun').source_unit_ids,index.get('passage-beishan-bianchun').source_unit_ids);
assert.ok(index.get('beast-beishan-youyu-daishan').quote.includes('三尾六足四首'));
assert.ok(index.get('beast-beishan-heluo-qiaoming').quote.includes('一首而十身'));
assert.ok(index.get('beast-beishan-xixi-zhuoguang').quote.includes('十翼鱗皆在羽端'));
assert.ok(index.get('beast-beishan-qitu-daishan').quote.includes('如烏五彩而赤文'));
assert.equal(index.get('water-beishan-he').source_passage_ids.length,25);
assert.ok(inventory.units.find(u => u.id === 'source-03-0009').page_url.endsWith('/76'));
assert.ok(inventory.units.find(u => u.id === 'source-03-0009').captured_page_url.endsWith('/77'));
assert.ok(index.get('beast-beishan-huayu-qiuru').quote.includes('如鱓赤背'));
assert.ok(index.get('beast-beishan-shuima-qiuru').quote.includes('文臂牛尾'));
assert.equal(index.get('place-beishan-zhupi-qiuru').commentary_quote, '水出諸毗山也');
for (const e of selected) {
  assert.ok(english[e.id]?.name && english[e.id]?.description && english[e.id]?.quote, e.id);
  assert.ok(!/[\u3400-\u9fff]/u.test(english[e.id].quote), e.id + ' English quote');
  assert.equal(e.review_status, 'facsimile_reviewed');
  if (['beast','deity'].includes(e.kind)) assert.ok(e.artwork?.startsWith('beishan/') || e.id === 'beast-zhu-jian' && e.artwork === 'beasts/beast-zhu-jian.webp' || e.id === 'beast-jingwei' && e.artwork === 'jingwei.webp' || e.appearance_unknown, e.id);
  else if(e.artwork) assert.ok(['plant-beishan-redgrain-huguan','plant-beishan-sansang-huan'].includes(e.id),'Only text-supported tree artwork');
  else assert.equal(e.artwork, undefined, 'No borrowed or invented illustrations');
  assert.equal(readExploration(`?chapter=03&item=${e.id}`, world, catalog).item, e.id);
  for (const id of [...e.related_entry_ids, ...(e.source_passage_ids || [])]) assert.ok(index.has(id), id);
  if (e.source_passage_ids?.length === 1) {
    assert.deepEqual(e.source_unit_ids,index.get(e.source_passage_ids[0]).source_unit_ids,e.id+' isolated source units');
  }
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
assert.equal(generation.assets.length,57);
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
assert.deepEqual(index.get('passage-beishan-xiaoxian').source_unit_ids,['source-03-0063']);
assert.deepEqual(index.get('passage-beishan-daxian').source_unit_ids,['source-03-0064','source-03-0065','source-03-0066','source-03-0067']);
assert.ok(index.get('beast-beishan-nafu-guanti').quote.includes('如牛而白尾'));
assert.ok(index.get('beast-beishan-songsi-guanti').quote.includes('如雌雉而人靣'));
assert.ok(index.get('beast-beishan-maoniu-panhou').quote.includes('四節生毛'));
assert.ok(index.get('beast-beishan-changshe-daxian').quote.includes('其毛如彘豪'));
assert.ok(index.get('water-beishan-bian-panhou').quote.includes('南流'));
assert.notEqual(index.get('water-beishan-lize-panhou').id,index.get('water-beishan-li-danzhang').id);
assert.equal(index.get('water-beishan-youze').source_passage_ids.length,3);
for(const id of ['chigui','si','maoniu','shijiu'].map(s=>'beast-beishan-'+s+'-dunhong'))assert.ok(index.get(id).appearance_unknown&&!index.get(id).artwork);
assert.equal(review.text_corrections.length,9);
assert.ok(index.get('beast-beishan-zhuhuai-beiyue').quote.includes('四角人目彘耳'));
assert.ok(index.get('passage-beishan-beiyue').captured_text.includes('⟦缺字图:'));
assert.ok(!index.get('passage-beishan-beiyue').quote.includes('⟦缺字图:'));
assert.deepEqual(index.get('water-beishan-xiao-beiyue-hunxi').source_passage_ids,['passage-beishan-beiyue','passage-beishan-hunxi']);
assert.notEqual(index.get('water-beishan-xiao-beiyue-hunxi').id,index.get('water-beishan-xiao-zhuoguang').id);
assert.ok(index.get('beast-beishan-peipei-shaoxian').appearance_unknown);
assert.ok(index.get('beast-beishan-feiyi-hunxi').quote.includes('一首兩身'));
assert.equal(snapshot.chapters[2].lines[87].text,'');
assert.deepEqual(inventory.units.find(u=>u.id==='source-03-0088').confirmed_passage_ids,['passage-beishan-hunxi']);
assert.equal(createHash('sha256').update(await readFile(new URL('../../'+review.extb_font_supplement.path,import.meta.url))).digest('hex'),review.extb_font_supplement.sha256);
assert.equal(world.passages.filter(p=>p.source_book===3&&p.range===1&&p.id!=='passage-beishan-range1-summary').length,25);
assert.equal(index.get('passage-beishan-guancen').range,2);
assert.equal(index.get('rite-beishan-range1-summary').kind,'rite');
assert.deepEqual(index.get('water-beishan-taize').source_passage_ids,['passage-beishan-yufa','passage-beishan-dishan','passage-beishan-wangwu']);
assert.ok(index.get('water-beishan-di-dishan').quote.includes('東流'));
assert.ok(index.get('water-beishan-xian-beixian').quote.includes('西北流'));
assert.ok(index.get('beast-beishan-yao-dishan').quote.includes('如豹而文首'));
assert.ok(index.get('deity-beishan-human-serpent-range1-summary').quote.includes('人靣蛇身'));
assert.ok(index.get('passage-beishan-range1-summary').quote.includes('二十五山五千四百九十里'));
for(const id of ['beast-beishan-ma-beixian','beast-beishan-ma-dishan','beast-beishan-longgui-dishan'])assert.ok(index.get(id).appearance_unknown&&!index.get(id).artwork);
assert.deepEqual(index.get('passage-beishan-guancen').source_unit_ids,['source-03-0100','source-03-0101','source-03-0102']);
assert.deepEqual(inventory.units.find(u=>u.id==='source-03-0099').confirmed_passage_ids,['passage-beishan-range1-summary']);
assert.deepEqual(index.get('water-beishan-fen-guancen').source_passage_ids,['passage-beishan-guancen','passage-beishan-shaoyang','passage-beishan-xianyong','passage-beishan-huqi']);
assert.equal(world.passages.filter(p=>p.source_book===3&&p.range===2).length,17);
assert.equal(snapshot.chapters[2].lines[104].text,'');
assert.deepEqual(inventory.units.find(u=>u.id==='source-03-0105').confirmed_passage_ids,['passage-beishan-shaoyang']);
assert.ok(index.get('material-beishan-ochre-shaoyang').commentary_quote.includes('管子曰山上有赭者其下有鐵'));
assert.ok(index.get('beast-beishan-lv-xianyong').commentary_quote.includes('似馿而岐蹄角如麢羊'));
assert.ok(index.get('beast-beishan-lv-xianyong').commentary_quote.includes('北唐以閭'));
assert.equal(index.get('beast-beishan-white-di-xianyong').commentary_quote,'');
assert.ok(index.get('beast-beishan-white-you-xianyong').commentary_quote.includes('白𪂂'));
assert.ok(index.get('beast-beishan-ci-xianyong').quote.includes('如儵而赤麟'));
assert.ok(index.get('water-beishan-suan-shaoyang').quote.includes('東流'));
assert.ok(index.get('water-beishan-jin-xianyong').quote.includes('東南流'));
assert.ok(index.get('water-beishan-sheng-huqi').quote.includes('東北流'));
assert.ok(index.get('water-beishan-wei-baisha').quote.includes('出于其上潜于其下'));
assert.ok(index.get('passage-beishan-baisha').quote.includes('無草木鳥獸'));
assert.equal(index.get('passage-beishan-ershi').source_unit_ids.length,1);
assert.ok(!index.get('water-beishan-fen-guancen').source_unit_ids.includes('source-03-0113'));
for(const id of ['mi','white-di','white-you'].map(s=>'beast-beishan-'+s+'-xianyong'))assert.ok(index.get(id).appearance_unknown&&!index.get(id).artwork);
assert.deepEqual(index.get('water-beishan-mao').source_passage_ids,['passage-beishan-zhuyu','passage-beishan-duntou']);
assert.ok(index.get('water-beishan-kuang').quote.includes('西流'));
assert.ok(index.get('beast-beishan-boma-duntou').quote.includes('牛尾而白身一角'));
assert.ok(index.get('beast-beishan-paoxiao-gouwu').quote.includes('其目在腋下虎齒人𤓰'));
assert.equal(snapshot.chapters[2].lines[126].text,'');
assert.deepEqual(inventory.units.find(u=>u.id==='source-03-0127').confirmed_passage_ids,['passage-beishan-gouwu']);
assert.ok(index.get('passage-beishan-beixiao').captured_text.includes('⟦缺字图:囂⟧'));
assert.ok(!index.get('passage-beishan-beixiao').quote.includes('⟦缺字图:'));
assert.ok(index.get('beast-beishan-dugu-beixiao').quote.includes('犬首馬尾彘鬛'));
assert.equal(index.get('beast-beishan-dugu-beixiao').commentary_quote,'音谷');
assert.ok(index.get('beast-beishan-banmao-beixiao').commentary_quote.startsWith('般冐'));
assert.ok(index.get('water-beishan-cen-beixiao').quote.includes('東流注于卭澤'));
assert.equal([...review.extb_font_supplement.characters].length,17);
assert.equal(review.batch_size,15);assert.equal(review.stage_plan.length,15);
assert.equal(review.second_range_summary.reported_mountains,17);assert.equal(review.second_range_summary.named_mountains,16);
assert.equal(world.passages.filter(p=>p.source_book===3&&p.range===3).length,48);
for(const [unit,pid] of [['source-03-0150','passage-beishan-range2-summary'],['source-03-0181','passage-beishan-wangwu']])assert.deepEqual(inventory.units.find(u=>u.id===unit).confirmed_passage_ids,[pid]);
assert.ok(index.get('beast-beishan-hui-guishan').quote.includes('四角馬尾而有距'));
assert.ok(index.get('beast-beishan-fen-guishan').quote.includes('白身赤尾六足'));
assert.equal(index.get('beast-beishan-hui-guishan').context_place_id,'place-beishan-guishan');
assert.equal(index.get('material-beishan-gold-fawan').context_place_id,'place-beishan-fawan');
assert.ok(index.get('water-beishan-jiao-jiaoshan').aliases.includes('乾河'));
assert.ok(index.get('beast-beishan-tianma-macheng').quote.includes('如白犬而黑頭'));
assert.ok(index.get('beast-beishan-feishu-tianchi').quote.includes('如兎而䑕首以其背飛'));
assert.ok(index.get('beast-beishan-xianfu-yangshan').quote.includes('魚首而彘身'));
assert.ok(index.get('rite-beishan-jade-casting-range2').commentary_quote.includes('不埋'));
assert.equal(index.get('water-beishan-yanmen-liangqu').commentary_quote,'水名');
assert.notEqual(index.get('water-beishan-yanmen-liangqu').id,index.get('water-beishan-yanmen-shaoxian').id);
for(const id of ['beast-beishan-xiao-liangqu','beast-beishan-ma-huguan','beast-beishan-shan-huguan','beast-beishan-strange-snakes-huan'])assert.ok(index.get(id).appearance_unknown&&!index.get(id).artwork);
assert.equal(index.get('material-beishan-qisuan-xianshan').kind,'material');
assert.equal(review.next.status,'beishan_complete');
assert.notEqual(index.get('place-beishan-jingshan').id,index.get('place-beishan-jingshan-east').id);
assert.ok(index.get('beast-beishan-suanyu-jingshan').quote.includes('如蛇而四翼六目三足'));
assert.ok(index.get('plant-beishan-zhuyu-jingshan').commentary_quote.includes('根似羊蹄'));
assert.ok(index.get('plant-beishan-qinjiao-jingshan').commentary_quote.includes('子似椒而細'));
assert.ok(index.get('water-beishan-yanfan-jingshan').commentary_quote.includes('或無販字'));
assert.ok(index.get('material-beishan-xuansu-jingshan-east').commentary_quote.includes('黒砥'));
assert.ok(index.get('water-beishan-bo-chongwei').commentary_quote.includes('鮮于山'));
assert.ok(index.get('water-beishan-ping-pingshan').quote.includes('潜于其下'));
for(const id of ['water-beishan-gao-jingshan-east','water-beishan-dan-chongwei'])assert.ok(index.get(id).related_entry_ids.includes('water-beishan-he'));
assert.equal(index.get('place-fajiu').content_batch,'beishan-fajiu');
assert.equal(world.places.filter(p=>p.id==='place-fajiu').length,1);
assert.equal(index.get('place-fajiu').x,540);assert.equal(index.get('place-fajiu').y,175);
assert.equal(index.get('beast-jingwei').place_id,'place-fajiu');
assert.equal(index.get('beast-jingwei').context_place_id,'place-fajiu');
assert.equal(index.get('beast-jingwei').artwork,'jingwei.webp');
assert.ok(index.get('beast-jingwei').aliases.includes('精卫'));
assert.ok(index.get('beast-jingwei').quote.includes('名曰女娃'));
assert.ok(index.get('beast-jingwei').legacy_quote);
assert.equal(index.get('water-beishan-huangze-chongwei').source_passage_ids.length,2);
for(const id of ['water-beishan-zhang-fajiu','water-beishan-fu-shenqun'])assert.equal(index.get(id).source_passage_ids.length,2);
assert.equal(index.get('water-beishan-danlin-yeli').context_place_id,'place-beishan-danlin-forest-yeli');
for(const [u,p] of [[222,'shenqun'],[228,'fajiu'],[231,'shaoshan']]){
 const id='source-03-'+String(u).padStart(4,'0');assert.equal(snapshot.chapters[2].lines[u-1].text,'');
 assert.deepEqual(inventory.units.find(x=>x.id===id).confirmed_passage_ids,['passage-beishan-'+p]);
}
for(const id of ['beast-beishan-feiyi-pengpi','beast-beishan-white-snakes-shenqun','beast-beishan-flying-insects-shenqun'])assert.ok(index.get(id).appearance_unknown&&!index.get(id).artwork);
assert.ok(index.get('beast-beishan-guxi-xiaohou').quote.includes('如烏而白文'));
assert.ok(index.get('beast-beishan-huangniao-xuanyuan').quote.includes('如梟而白首'));
assert.ok(index.get('water-beishan-fu-shenqun').quote.includes('滏水'));
assert.ok(index.get('water-beishan-niushou-xishan-north').quote.endsWith('滏水'));
assert.equal(review.remaining_stage_estimate.before_this_batch,15);
assert.equal(review.remaining_stage_estimate.count,0);
assert.equal(review.remaining_stage_estimate.stages.length,0);
assert.deepEqual(review.next.source_units,[]);
for(const id of ['place-beishan-jingshan','place-beishan-jingshan-east','place-beishan-jingshan-after-xi'])assert.ok(index.has(id));
assert.equal(index.get('passage-beishan-jingshan-after-xi').source_pages[0].split('/').at(-1),'101');
assert.ok(index.get('passage-beishan-dunyu').source_pages[0].endsWith('/102'));
assert.equal(index.get('water-beishan-yang-songshan').quote,'陽水出焉東北流注于河');
assert.notEqual(index.get('water-beishan-peng-dunyu').id,index.get('water-beishan-peng-daishan').id);
assert.ok(index.get('water-beishan-tailu-dunyu').commentary_quote.endsWith('平澤即其水'));
assert.ok(index.get('water-beishan-zhi-dunyu').commentary_quote.includes('中丘縣西窮泉谷'));
assert.equal(index.get('water-beishan-huai-dunyu').commentary_quote,'');
assert.ok(index.get('beast-beishan-huomin-xiushan').appearance_unknown&&!index.get('beast-beishan-huomin-xiushan').artwork);
assert.ok(index.get('beast-beishan-huomin-xiushan').commentary_quote.includes('或曰蠖黽一物名'));
assert.ok(index.get('plant-beishan-shaoyao-xiushan').commentary_quote.includes('一名辛夷'));
assert.equal(review.remaining_stage_estimate.mountain_passages,0);
assert.equal(index.get('water-beishan-wei-xiushan').source_passage_ids.length,2);
assert.equal(index.get('water-beishan-qin-yeli').source_passage_ids.length,2);
assert.equal(index.get('water-beishan-huchi-taitou').source_passage_ids.length,6);
assert.ok(index.get('water-beishan-huchi-taitou').aliases.includes('虖池'));
assert.ok(index.get('water-beishan-huchi-taitou').aliases.includes('虖沱'));
assert.ok(index.get('beast-beishan-dongdong-taixi').quote.includes('一角一目目在耳後'));
assert.ok(index.get('beast-beishan-dongdong-taixi').artwork);
assert.ok(!index.get('beast-beishan-dongdong-taixi').appearance_unknown);
assert.ok(index.get('material-beishan-leishi-weilong').commentary_quote.startsWith('未詳也'));
assert.ok(index.get('material-beishan-leishi-weilong').commentary_quote.includes('或曰石名'));
assert.notEqual(index.get('water-beishan-fei-weilong').id,index.get('water-beishan-fei-pengpi').id);
assert.notEqual(index.get('water-beishan-daze-weilong').id,index.get('water-beishan-taize').id);
assert.equal(index.get('water-beishan-muma-baima').quote,'木馬之水出焉而東北流注于虖沱');
assert.equal(index.get('water-beishan-lou-taixi').quote,'東流注于漊水');
assert.equal(index.get('water-beishan-yenu-taixi').commentary_quote,'液音恱懌之懌');

assert.equal(review.scan_pages.length,33);
for(const id of ['plant-beishan-zao-range3','plant-beishan-zhi-range3','plant-beishan-tu-range3','material-beishan-jade-carried-range3','material-beishan-rice-range3']){assert.ok(world.text_entities.some(e=>e.id===id));assert.ok(!index.get(id).context_place_id);}
assert.equal(selected.filter(e=>e.appearance_unknown).length,26);
assert.deepEqual(review.chapter_completion.catalog_counts,[26,17,48,1]);
assert.equal(review.third_range_summary.named_mountains,47);
assert.equal(review.third_range_summary.reported_mountains,46);
assert.deepEqual(review.third_range_summary.deity_groups,[20,14,10]);
assert.equal(review.closing_total.range_mountain_sum,88);
assert.equal(review.closing_total.reported_mountains,87);
assert.equal(review.closing_total.range_li_sum,23530);
assert.equal(review.closing_total.reported_li,23230);
assert.equal(review.closing_total.mountain_difference,1);
assert.equal(review.closing_total.li_difference,300);
assert.equal(index.get('passage-beishan-book-total').range,4);
assert.ok(index.get('passage-beishan-mufeng').quote.includes('錞于母逢'));
assert.ok(index.get('passage-beishan-range3-summary').quote.includes('無逢'));
assert.equal(index.get('water-beishan-yu-youdu-mufeng').context_place_id,'place-beishan-youdu-mufeng');
for(const id of ['material-beishan-jade-didu','material-beishan-gold-didu'])assert.equal(index.get(id).context_place_id,'place-beishan-didu');
assert.notEqual(index.get('water-beishan-taize-didu').id,index.get('water-beishan-taize').id);
assert.equal(index.get('wind-beishan-li-mufeng').kind,'wind');
assert.ok(index.get('rite-beishan-jade-not-buried-range3').commentary_quote.includes('不埋所用玉也'));
assert.equal(snapshot.chapters[2].lines[283].text,'');
assert.deepEqual(inventory.units.find(u=>u.id==='source-03-0284').confirmed_passage_ids,['passage-beishan-yanmenshan']);
for(const id of ['tuotuo-raoshan','liuli-raoshan','shiyu-raoshan','puyi-jieshi'].map(s=>'beast-beishan-'+s))assert.ok(index.get(id).appearance_unknown&&!index.get(id).artwork);
for(const [id,q] of [['beast-beishan-yuan-ganshan','如牛而三足'],['beast-beishan-pi-lunshan','川在尾上'],['deity-beishan-horse-human-range3','馬身而人靣'],['deity-beishan-pig-eight-snake-range3','八足蛇尾'],['beast-beishan-redhead-snake-mufeng','赤首白身']])assert.ok(index.get(id).quote.includes(q)&&index.get(id).artwork);
for(const slug of ['range1-summary','range2-summary','range3-summary'])assert.ok(index.get('rite-beishan-book-total').related_entry_ids.includes('rite-beishan-'+slug));

console.log('PASS data: Northern 92 passages, 507 cards, 296 source blocks, 32 page corrections, 57 reviewed images, retained Jingwei/Fajiu/Zhujian and 26 documented placeholders');
if (process.env.ATLAS_DATA_ONLY === '1') process.exit(0);

const root = resolve(process.env.ATLAS_STATIC_DIR || 'dist');
for(const d of [review.title_font_supplement,review.extb_font_supplement,review.edition_tan_font])assert.equal(createHash('sha256').update(await readFile(resolve(root,'fonts',d.path.split('/').at(-1)))).digest('hex'),d.sha256,'Published font bytes: '+d.family);
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
    const page = await context.newPage(), errors = [], missing = [], pending = new Set();
    page.on('pageerror', e => errors.push(e.message));
    page.on('response', r => { if (r.status() >= 400 && r.url().startsWith(base)) missing.push(r.url()); });
    page.on('request', request => { if (request.url().startsWith(base)) pending.add(request); });
    for (const event of ['requestfinished', 'requestfailed']) page.on(event, request => pending.delete(request));
    async function ready(id) {
      await page.waitForFunction(id => {
        const d = document.querySelector('.detail-drawer');
        return d?.dataset.entryId === id && d.dataset.readingRestoring === 'false';
      }, id);
      await page.evaluate(() => document.fonts.ready);
      return page.locator('.detail-drawer');
    }
    async function open(id, lang = 'zh') {
      try {
        await page.goto(`${base}?chapter=03&item=${id}&lang=${lang}`, { waitUntil: 'domcontentloaded' });
        return await ready(id);
      } catch (error) {
        const state = await page.evaluate(() => ({ document: document.readyState,
          entry: document.querySelector('.detail-drawer')?.dataset,
          fonts: [...document.fonts].filter(font => font.status === 'loading').map(font => font.family) })).catch(() => null);
        console.error('Northern navigation failed', JSON.stringify({ id, lang, pending: [...pending].map(request => request.url()), state }));
        throw error;
      }
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
      d = await open('water-beishan-feng-danhu', lang);
      await d.locator('[data-related-id="water-beishan-you-danhu"]').click();
      await ready('water-beishan-you-danhu');
      await page.goto(`${base}?chapter=03&lang=${lang}`);
      await page.locator('.global-search-trigger').click();
      await page.locator('.global-search-input').fill('诸犍');
      await page.locator('.search-result[data-result-id="beast-zhu-jian"]').click();
      await ready('beast-zhu-jian');
      for(const [query,id] of [['精卫','beast-jingwei'],['发鸠','place-fajiu']]){
        await page.goto(base+'?chapter=03&lang='+lang);
        await page.locator('.global-search-trigger').click();await page.locator('.global-search-input').fill(query);
        await page.locator('.search-result[data-result-id="'+id+'"]').click();await ready(id);
      }
      await page.goto(`${base}?chapter=03&lang=${lang}`);
      await page.locator('.mobile-explore-nav button').nth(1).click();
      const northern = page.locator('[data-source-book="3"]');
      await northern.locator(':scope > summary').click();
      for (const summary of await northern.locator('.passage-range > summary').all()) await summary.click();
      assert.equal(await northern.locator('.passage-range').count(),4);
      assert.equal(await northern.locator('.passage-range').nth(0).locator('[data-entry-id]').count(),26);
      assert.equal(await northern.locator('.passage-range').nth(1).locator('[data-entry-id]').count(),17);
      assert.equal(await northern.locator('.passage-range').nth(2).locator('[data-entry-id]').count(),48);
      assert.equal(await northern.locator('.passage-range').nth(3).locator('[data-entry-id]').count(),1);
      assert.equal(await northern.locator('[data-entry-id^="passage-beishan-"]').count(), 92);
      await northern.locator(`[data-entry-id="${activePassages[0].id}"]`).click();
      await ready(activePassages[0].id);
      }
      await page.goto(`${base}?chapter=03&lang=${lang}`);
      await page.locator('.global-search-trigger').click();
      await page.locator('.global-search-input').fill(lang === 'zh' ? currentPlace.name : english[currentPlace.id].name);
      await page.locator(`.search-result[data-result-id="${currentPlace.id}"]`).click();
      await ready(currentPlace.id);
      console.log(`PASS ${engine} ${lang}: ${browserEntries.length} current/shared records, 4 viewports, ${roundTrips} nested/context round trips, images, ${commonChecks?'92 catalog passages and legacy links; ':''}current search`);
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
      for(const family of ['Atlas Northern Tan','Atlas Northern ExtB'])for(const w of [400,600])await document.fonts.load(w+' 20px "'+family+'"',characters);
      for (const w of [400, 600]) await document.fonts.load(`${w} 20px "Shanhai Title"`, characters);
    }, review.title_font_supplement.characters + review.extb_font_supplement.characters + review.edition_tan_font.characters);
    assert.deepEqual(errors, []);
    assert.deepEqual(missing, []);
    await context.close();
    console.log(`PASS ${engine}: read/favorite refresh, resume, title face loading; zero page/resource errors`);
  } finally {
    await browser.close();
  }
}
