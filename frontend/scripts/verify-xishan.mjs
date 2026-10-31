import { openSourceLibrary } from './ui-controls.mjs';
import assert from 'node:assert/strict';
import { mkdir, readFile, stat } from 'node:fs/promises';
import { chromium, webkit } from 'playwright';
import { worldEntries } from '../src/entries.js';
import { searchEntries, searchIndex } from '../src/search.js';
import { entryRelations, relatedEntries } from '../src/entry-relations.js';
import { readExploration } from '../src/exploration.js';
import { mockTianditu } from './mock-tianditu.mjs';
import { resolve, sep } from 'node:path';

if (JSON.parse(await readFile(new URL('../public/data/myth-world.json', import.meta.url), 'utf8')).passages.filter(p => p.source_book === 2).length === 82) {
  await import('./verify-xishan-complete.mjs');
  process.exit(0);
}

const base = process.env.ATLAS_URL;
if (!base) throw new Error('Set ATLAS_URL; use ATLAS_STATIC_DIR for browser checks without a listening port.');
const json = async path => JSON.parse(await readFile(new URL(path, import.meta.url), 'utf8'));
const [world, catalog, english, inventory, review, generation, artwork, labels] = await Promise.all([
  '../public/data/myth-world.json', '../public/data/atlas/catalog.json', '../src/locale-content-en.json',
  '../../data/shanhaijing-inventory.json', '../../data/xishan-edition-review.json',
  '../artwork-source/xishan/generation.json', '../public/data/atlas/artwork-manifest.json', '../src/locale-en.json',
].map(json));
const index = new Map(worldEntries(world).map(item => [item.id, item]));
const range2FinishBatches = ['xishan-xunwu','xishan-quyang','xishan-zhongshou','xishan-huangren','xishan-zhonghuang','xishan-xihuang','xishan-laishan','xishan-range2-summary'];
const entries = [...index.values()].filter(item => ['xishan-first-three', 'xishan-second-three', 'xishan-third-three', 'xishan-yuci', 'xishan-shishan', 'xishan-nanshan-west', 'xishan-dashi', 'xishan-bozhong', 'xishan-tiandi', 'xishan-gaotu', 'xishan-huangshan', 'xishan-cuishan', 'xishan-guishan', 'xishan-range1-summary', 'xishan-qianshan', 'xishan-taimao', 'xishan-shuli', 'xishan-gaoshan', 'xishan-nvchuang', 'xishan-longshou', 'xishan-lutai', 'xishan-niaowei', 'xishan-xiaoci', 'xishan-daci', ...range2FinishBatches, 'xishan-chongwu', 'xishan-changsha', 'xishan-buzhou', 'xishan-mishan', 'xishan-zhongshan', 'xishan-taiqi', 'xishan-huaijiang'].includes(item.content_batch));
const browserEntries = process.env.ATLAS_BATCH ? entries.filter(item => item.content_batch === process.env.ATLAS_BATCH || process.env.ATLAS_BATCH === 'xishan-huaijiang' && ['water-xishan-you-changsha','place-xishan-zhupi-buzhou'].includes(item.id) || process.env.ATLAS_BATCH === 'xishan-taiqi' && item.id === 'water-xishan-westsea-guishan' || ['xishan-chongwu','xishan-buzhou'].includes(process.env.ATLAS_BATCH) && item.id === 'water-xishan-he-taimao' || process.env.ATLAS_BATCH === 'xishan-range2-finish' && (range2FinishBatches.includes(item.content_batch) || item.id === 'water-xishan-chi-huangshan') || process.env.ATLAS_BATCH === 'xishan-bozhong' && item.id === 'water-xishan-han-dashi' || ['xishan-shuli', 'xishan-gaoshan'].includes(process.env.ATLAS_BATCH) && item.id === 'water-xishan-wei' || process.env.ATLAS_BATCH === 'xishan-longshou' && item.id === 'water-xishan-jing-gaoshan' || process.env.ATLAS_BATCH === 'xishan-niaowei' && item.id === 'water-xishan-chi-huangshan') : entries;
assert.ok(browserEntries.length, 'ATLAS_BATCH must select an existing Western batch');
const passages = world.passages.filter(item => item.source_book === 2);
assert.equal(entries.length, 338);
assert.equal(entries.filter(item => item.content_batch === 'xishan-first-three').length, 11);
assert.equal(entries.filter(item => item.content_batch === 'xishan-second-three').length, 18);
assert.equal(entries.filter(item => item.content_batch === 'xishan-third-three').length, 21);
assert.equal(passages.length, 45);
assert.deepEqual(passages.map(item => item.order), Array.from({ length: 45 }, (_, i) => i + 1));
assert.equal(world.passages.filter(item => item.id.startsWith('passage-nanshan-')).length, 43);
assert.equal(inventory.chapters[1].semantic_review, 'partial');
assert.equal(inventory.chapters[1].pending_candidate_passages, 36);
assert.equal(inventory.units.find(item => item.id === 'source-02-0009').page_url.endsWith('/34'), true);
assert.equal(inventory.units.find(item => item.id === 'source-02-0009').captured_page_url.endsWith('/35'), true);
assert.equal(review.entry_ids.length, 293);
assert.ok(inventory.units.find(item => item.id === 'source-02-0018').page_url.endsWith('/35'));
assert.ok(inventory.units.find(item => item.id === 'source-02-0027').page_url.endsWith('/36'));
assert.ok(index.get('passage-xishan-xiaohua').commentary_quote.includes('〔录文缺字待核〕'));
assert.ok(index.get('plant-xishan-tiao-fuyu').quote.includes('赤花黄實'));
assert.ok(index.get('plant-xishan-tiao-shicui').quote.includes('白華黑實'));
assert.notEqual(index.get('plant-xishan-tiao-fuyu').artwork, index.get('plant-xishan-tiao-shicui').artwork);
assert.deepEqual(index.get('water-xishan-wei').source_passage_ids, ['passage-xishan-songguo', 'passage-xishan-fuyu', 'passage-xishan-zhushan', 'passage-xishan-yuci', 'passage-xishan-shishan', 'passage-xishan-nanshan-west', 'passage-xishan-dashi', 'passage-xishan-shuli', 'passage-xishan-gaoshan']);
assert.ok(inventory.units.find(item => item.id === 'source-02-0036').page_url.endsWith('/37'));
assert.ok(inventory.units.find(item => item.id === 'source-02-0045').page_url.endsWith('/38'));
assert.ok(index.get('passage-xishan-zhushan').captured_text.includes('⟦缺字图:南⟧'));
assert.ok(index.get('passage-xishan-zhushan').quote.includes('東南流注于洛水'));
assert.ok(!index.get('passage-xishan-zhushan').quote.includes('缺字图'));
assert.notEqual(index.get('beast-xishan-feiyi-ying').artwork, index.get('beast-xishan-feiyi-taihua').artwork);
assert.ok(index.get('beast-xishan-feiyi-ying').quote.includes('如鶉黄身而赤喙'));
assert.ok(!index.get('beast-xishan-renyu-zhushan').quote.includes('四脚'));
assert.ok(index.get('beast-xishan-renyu-zhushan').commentary_quote.includes('四脚'));
assert.ok(index.get('beast-xishan-bangyu-ying').quote.includes('其音如羊'));
assert.ok(index.get('water-xishan-zhao-ying').commentary_quote.includes('音韶'));
assert.ok(english['water-xishan-zhao-ying'].name.startsWith('Shao'));
assert.ok(index.get('animal-xishan-zuoniu-ying').artwork_caption.includes('仅列名'));
assert.ok(index.get('beast-xishan-qianyang-ying').artwork_caption.includes('钱来'));
assert.notEqual(index.get('water-xishan-yu-ying').id, index.get('water-xishan-yu-shicui').id);
assert.ok(index.get('plant-xishan-xuncao').quote.includes('方莖赤華而黑實'));
assert.equal(index.get('beast-guan').name, '讙');
assert.equal(index.get('beast-guanguan').name, '灌灌');
assert.equal(index.get('beast-xishan-tongqu').relation_scope, undefined, 'No invented aquatic habitat');
assert.ok(index.get('beast-xishan-feiyi-taihua').quote.includes('六足四翼'));
assert.equal(entries.filter(item => item.content_batch === 'xishan-yuci').length, 6);
assert.ok(index.get('beast-xishan-xiao-yuci').quote.includes('如禺而長臂善投'));
assert.ok(index.get('beast-xishan-tuofei-yuci').quote.includes('人面而一足'));
assert.ok(index.get('beast-xishan-tuofei-yuci').commentary_quote.includes('著其毛羽'));
assert.ok(index.get('passage-xishan-yuci').source_unit_ids.includes('source-02-0060'));
assert.ok(!index.get('passage-xishan-yuci').quote.includes('時山'));
assert.ok(index.get('passage-xishan-yuci').commentary_quote.includes('天雷也或作灾'));
assert.ok(inventory.units.find(item => item.id === 'source-02-0054').page_url.endsWith('/39'));
assert.equal(entries.filter(item => item.content_batch === 'xishan-shishan').length, 4);
assert.ok(index.get('passage-xishan-shishan').quote.includes('時山無草木'));
assert.deepEqual(index.get('passage-xishan-shishan').source_unit_ids, ['source-02-0061', 'source-02-0062']);
assert.ok(!index.get('passage-xishan-shishan').commentary_quote.includes('天雷'));
assert.equal(index.get('water-xishan-zhu-shishan').commentary_quote, '或作遂');
assert.notEqual(index.get('water-xishan-zhu-shishan').id, index.get('water-xishan-zhu').id);
assert.notEqual(index.get('material-xishan-shuiyu-shishan').context_place_id, index.get('material-xishan-shuiyu-zhushan').context_place_id);
assert.equal(entries.filter(item => item.content_batch === 'xishan-nanshan-west').length, 6);
assert.ok(inventory.units.find(item => item.id === 'source-02-0063').page_url.endsWith('/40'));
assert.ok(inventory.units.find(item => item.id === 'source-02-0063').captured_page_url.endsWith('/41'));
assert.deepEqual(index.get('passage-xishan-nanshan-west').source_unit_ids, ['source-02-0063', 'source-02-0064', 'source-02-0065']);
assert.equal(index.get('place-xishan-nanshan-west').source_book, 2);
assert.ok(index.get('water-xishan-dan-nanshan').quote.includes('北流注于渭'));
assert.ok(index.get('water-xishan-dan-zhushan').quote.includes('東南流注于洛水'));
assert.equal(index.get('beast-xishan-mengbao-nanshan').quote, '獸多猛豹');
assert.ok(index.get('beast-xishan-mengbao-nanshan').commentary_quote.includes('似熊而小'));
assert.ok(index.get('beast-xishan-mengbao-nanshan').artwork_caption.includes('郭注'));
assert.ok(index.get('beast-xishan-shijiu-nanshan').commentary_quote.includes('或曰鶘鸇'));
assert.ok(index.get('beast-xishan-shijiu-nanshan').artwork_caption.includes('异说'));
assert.equal(entries.filter(item => item.content_batch === 'xishan-dashi').length, 7);
assert.deepEqual(index.get('passage-xishan-dashi').source_unit_ids, ['source-02-0066', 'source-02-0067', 'source-02-0068']);
assert.ok(index.get('passage-xishan-dashi').quote.includes('上多榖柞下多杻橿'));
assert.ok(!index.get('passage-xishan-dashi').quote.includes('穀'));
assert.ok(index.get('water-xishan-qian-dashi').quote.includes('北流注于渭'));
assert.equal(index.get('water-xishan-qian-dashi').commentary_quote, '音潜');
assert.ok(english['water-xishan-qian-dashi'].name.startsWith('Qian'));
assert.ok(index.get('water-xishan-qing-dashi').quote.includes('南流注于漢水'));
assert.notEqual(index.get('water-xishan-qian-dashi').id, index.get('water-xishan-qing-dashi').id);
assert.ok(index.get('material-xishan-white-jade-dashi').quote.includes('陽多白玉'));
assert.ok(index.get('passage-xishan-dashi').content_note.includes('电子快照未收'));
assert.equal(entries.filter(item => item.content_batch === 'xishan-bozhong').length, 14);
assert.deepEqual(index.get('passage-xishan-bozhong').source_unit_ids, Array.from({ length: 8 }, (_, i) => 'source-02-' + String(i + 69).padStart(4, '0')));
assert.ok(index.get('passage-xishan-bozhong').captured_text.includes('⟦缺字图:囂⟧'));
assert.ok(index.get('passage-xishan-bozhong').quote.includes('沔囂水出焉北流注于湯水'));
assert.ok(!index.get('passage-xishan-bozhong').quote.includes('缺字图'));
assert.ok(inventory.units.find(item => item.id === 'source-02-0072').page_url.endsWith('/41'));
assert.ok(inventory.units.find(item => item.id === 'source-02-0072').captured_page_url.endsWith('/42'));
assert.deepEqual(index.get('water-xishan-han-dashi').source_passage_ids, ['passage-xishan-dashi', 'passage-xishan-bozhong']);
assert.ok(index.get('water-xishan-mian-bozhong').quote.includes('東南流注于沔'));
assert.equal(index.get('water-xishan-tang-bozhong').commentary_quote, '或作陽');
assert.ok(!index.get('animal-xishan-pi-bozhong').quote.includes('黄白'));
assert.ok(index.get('animal-xishan-pi-bozhong').commentary_quote.includes('黄白色'));
assert.ok(index.get('bird-xishan-baihan-bozhong').commentary_quote.includes('白雉'));
assert.equal(index.get('bird-xishan-chibie-bozhong').artwork, index.get('beast-xishan-chibie').artwork);
assert.ok(index.get('bird-xishan-chibie-bozhong').artwork_caption.includes('小华'));
assert.ok(index.get('plant-xishan-gurong-bozhong').quote.includes('黑華而不實'));
assert.ok(index.get('plant-xishan-gurong-bozhong').commentary_quote.includes('本根也'));
assert.equal(entries.filter(item => item.content_batch === 'xishan-tiandi').length, 5);
assert.deepEqual(index.get('passage-xishan-tiandi').source_unit_ids, Array.from({ length: 6 }, (_, i) => 'source-02-' + String(i + 77).padStart(4, '0')));
assert.ok(index.get('passage-xishan-tiandi').quote.includes('上多㯶柟下多菅蕙'));
assert.ok(inventory.units.find(item => item.id === 'source-02-0081').page_url.endsWith('/42'));
assert.ok(inventory.units.find(item => item.id === 'source-02-0081').captured_page_url.endsWith('/43'));
assert.ok(index.get('beast-xishan-xibian-tiandi').quote.includes('其状如狗'));
assert.ok(index.get('beast-xishan-li-tiandi').quote.includes('黑文而赤翁'));
assert.ok(index.get('beast-xishan-li-tiandi').commentary_quote.includes('翁頭下毛'));
assert.ok(index.get('plant-xishan-duheng-tiandi').quote.includes('其臭如蘼蕪'));
assert.ok(index.get('plant-xishan-duheng-tiandi').commentary_quote.includes('或曰馬得之而徤走'));
assert.equal(entries.filter(item => item.content_batch === 'xishan-tiandi' && item.kind === 'water').length, 0);
assert.equal(entries.filter(item => item.content_batch === 'xishan-gaotu').length, 14);
assert.deepEqual(index.get('passage-xishan-gaotu').source_unit_ids, Array.from({ length: 8 }, (_, i) => 'source-02-' + String(i + 83).padStart(4, '0')));
assert.ok(inventory.units.find(item => item.id === 'source-02-0090').page_url.endsWith('/43'));
assert.ok(inventory.units.find(item => item.id === 'source-02-0090').captured_page_url.endsWith('/44'));
assert.equal(index.get('passage-xishan-gaotu').source_pages.length, 1);
assert.ok(index.get('water-xishan-se-gaotu').commentary_quote.includes('音色'));
assert.ok(index.get('water-xishan-se-gaotu').quote.includes('西流注于諸資之水'));
assert.ok(index.get('water-xishan-tu-gaotu').quote.includes('南流注于集獲之水'));
assert.ok(index.get('material-xishan-yu-gaotu').quote.includes('白石'));
assert.ok(index.get('plant-xishan-wutiao-gaotu').quote.includes('其葉如葵而赤背'));
assert.ok(index.get('beast-xishan-yingru-gaotu').quote.includes('白尾馬足人手而四角'));
assert.ok(index.get('beast-xishan-yingru-gaotu').commentary_quote.includes('前两脚似人手'));
assert.ok(index.get('beast-xishan-shusi-gaotu').quote.includes('其状如鴟而人足'));
assert.equal(index.get('beast-xishan-shusi-gaotu').commentary_quote, '或作癎');
assert.equal(entries.filter(item => item.content_batch === 'xishan-huangshan').length, 8);
assert.deepEqual(index.get('passage-xishan-huangshan').source_unit_ids, Array.from({ length: 5 }, (_, i) => 'source-02-' + String(i + 91).padStart(4, '0')));
assert.ok(index.get('passage-xishan-huangshan').captured_text.includes('⟦缺字图:能⟧'));
assert.ok(index.get('passage-xishan-huangshan').quote.includes('人舌能言'));
assert.ok(!index.get('passage-xishan-huangshan').quote.includes('缺字图'));
assert.ok(index.get('plant-xishan-zhujian-huangshan').quote.includes('無草木多竹箭'));
assert.ok(index.get('water-xishan-pan-huangshan').commentary_quote.includes('眄'));
assert.notEqual(index.get('water-xishan-chi-huangshan').id, index.get('water-nanshan-chishui-gui').id);
assert.equal(index.get('beast-xishan-min-huangshan').commentary_quote, '音敏');
assert.ok(index.get('beast-xishan-yingmu-huangshan').commentary_quote.includes('脚指前後各兩'));
assert.ok(!index.get('beast-xishan-yingmu-huangshan').commentary_quote.includes('音敏'));
assert.equal(generation.style_direction.primary_reference, 'frontend/artwork-source/xishan/bird-yingmu-huangshan-v3.png');
assert.equal(entries.filter(item => item.content_batch === 'xishan-cuishan').length, 11);
assert.deepEqual(index.get('passage-xishan-cuishan').source_unit_ids, Array.from({ length: 4 }, (_, i) => 'source-02-' + String(i + 96).padStart(4, '0')));
assert.ok(inventory.units.find(item => item.id === 'source-02-0099').page_url.endsWith('/44'));
assert.ok(inventory.units.find(item => item.id === 'source-02-0099').captured_page_url.endsWith('/45'));
assert.equal(index.get('passage-xishan-cuishan').source_pages.length, 1);
assert.ok(index.get('passage-xishan-cuishan').quote.includes('西首四足可以禦火'));
assert.ok(index.get('bird-xishan-lei-cuishan').quote.includes('西首四足'));
assert.ok(index.get('bird-xishan-lei-cuishan').artwork_caption.includes('异文'));
assert.ok(index.get('animal-xishan-she-cuishan').commentary_quote.endsWith('有香'));
assert.equal(index.get('bird-xishan-lei-cuishan').commentary_quote, '音壘');
assert.equal(entries.filter(item => item.content_batch === 'xishan-cuishan' && item.kind === 'water').length, 0);
assert.equal(entries.filter(item => item.content_batch === 'xishan-guishan').length, 8);
assert.deepEqual(index.get('passage-xishan-guishan').source_unit_ids, Array.from({ length: 3 }, (_, i) => 'source-02-' + String(i + 100).padStart(4, '0')));
assert.equal(index.get('passage-xishan-guishan').source_pages.length, 1);
assert.ok(index.get('passage-xishan-guishan').source_pages[0].endsWith('/45'));
assert.ok(!index.get('passage-xishan-guishan').quote.includes('凡西經之首'));
assert.ok(index.get('water-xishan-qi-guishan').quote.includes('淒水出焉西流注于海'));
assert.equal(index.get('water-xishan-qi-guishan').commentary_quote, '或作浽');
assert.equal(index.get('material-xishan-gold-guishan').relation_scope, 'water');
assert.ok(index.get('material-xishan-caishi-guishan').commentary_quote.includes('石有采色者'));
assert.ok(index.get('material-xishan-jade-guishan').quote.includes('無草木多玉'));
assert.equal(entries.filter(item => item.content_batch === 'xishan-guishan' && ['兽','鸟'].includes(item.kind)).length, 0);
assert.equal(passages.filter(item => item.range === 1 && !item.is_summary).length, 19);
assert.equal(passages.filter(item => item.range === 2).length, 18);
assert.equal(entries.filter(item => item.content_batch === 'xishan-range1-summary').length, 4);
assert.ok(!index.has('place-xishan-range1-summary'));
assert.deepEqual(index.get('passage-xishan-range1-summary').source_unit_ids, Array.from({ length: 9 }, (_, i) => 'source-02-' + String(i + 103).padStart(4, '0')));
assert.ok(inventory.units.find(item => item.id === 'source-02-0108').page_url.endsWith('/45'));
assert.ok(inventory.units.find(item => item.id === 'source-02-0108').captured_page_url.endsWith('/46'));
assert.equal(index.get('passage-xishan-range1-summary').source_pages.length, 2);
assert.ok(index.get('passage-xishan-range1-summary').quote.includes('白蒂采等純之'));
assert.ok(!index.get('passage-xishan-range1-summary').quote.includes('西次二經'));
const qian = index.get('passage-xishan-qianshan');
assert.equal(entries.filter(item => item.content_batch === 'xishan-qianshan').length, 6);
assert.equal(qian.range, 2);
assert.deepEqual(qian.source_unit_ids, ['source-02-0112', 'source-02-0113']);
assert.equal(qian.quote, '西次二經之首曰鈐山其上多銅其下多玉其木多杻橿');
assert.equal(qian.source_pages.length, 1);
assert.ok(qian.source_pages[0].endsWith('/46'));
assert.equal(qian.commentary_quote, '〔影印页46〕音髠鉗之鉗或作冷又作塗');
assert.ok(!qian.quote.includes('西二百里'));
assert.ok(!index.has('passage-xishan-kunlun'));
assert.equal(passages.filter(item => item.range === 2 && !item.is_summary).length, 17);
assert.equal(index.get('material-xishan-copper-qianshan').quote, '其上多銅');
assert.equal(index.get('material-xishan-jade-qianshan').quote, '其下多玉');
assert.notEqual(index.get('plant-xishan-niu-qianshan').id, index.get('plant-xishan-jiang-qianshan').id);
assert.equal(entries.filter(item => item.content_batch === 'xishan-qianshan' && ['兽','鸟','water'].includes(item.kind)).length, 0);
const taimao = index.get('passage-xishan-taimao');
assert.equal(entries.filter(item => item.content_batch === 'xishan-taimao').length, 8);
assert.deepEqual(taimao.source_unit_ids, ['source-02-0114', 'source-02-0115', 'source-02-0116']);
assert.equal(taimao.range, 2);
assert.equal(taimao.quote, '西二百里曰㤗冐之山其陽多金其隂多鐡浴水出焉東流注于河其中多藻玉多白蛇');
assert.ok(taimao.source_pages[0].endsWith('/46'));
assert.ok(!taimao.quote.includes('數歴'));
assert.equal(index.get('beast-xishan-white-snake-taimao').commentary_quote, '水蛇');
assert.equal(index.get('beast-xishan-white-snake-taimao').relation_scope, 'water');
assert.equal(index.get('material-xishan-zaoyu-taimao').commentary_quote, '藻玉玉有符彩者或作柬音練');
assert.ok(!index.get('material-xishan-jin-taimao').quote.includes('黄金'));
assert.notEqual(index.get('water-xishan-yu-taimao').id, index.get('water-xishan-yu-ying').id);
const shuli = index.get('passage-xishan-shuli');
assert.equal(entries.filter(item => item.content_batch === 'xishan-shuli').length, 9);
assert.deepEqual(shuli.source_unit_ids, ['source-02-0117', 'source-02-0118', 'source-02-0119']);
assert.equal(shuli.quote, '又西一百七十里曰數歴之山其上多黄金其下多銀其木多杻橿其鳥多鸚䳇楚水出焉而南流注于渭其中多珠');
assert.equal(shuli.source_pages.length, 2);
assert.ok(inventory.units.find(r => r.id === 'source-02-0117').page_url.endsWith('/46'));
assert.ok(inventory.units.find(r => r.id === 'source-02-0117').captured_page_url.endsWith('/47'));
assert.ok(!shuli.quote.includes('曰髙山'));
assert.equal(index.get('beast-xishan-yingmu-shuli').appearance_unknown, true);
assert.ok(!index.get('beast-xishan-yingmu-shuli').quote.includes('青羽'));
assert.notEqual(index.get('beast-xishan-yingmu-shuli').id, index.get('beast-xishan-yingmu-huangshan').id);
assert.ok(index.get('water-xishan-chu-shuli').quote.includes('南流注于渭'));
assert.ok(index.get('water-xishan-wei').quote.includes('楚水出焉而南流注于渭'));
assert.equal(index.get('water-xishan-wei').source_passage_ids.length, 9);
assert.ok(index.get('water-xishan-wei').description.includes('七段') && index.get('water-xishan-wei').description.includes('南流'));
assert.equal(index.get('material-xishan-pearl-shuli').relation_scope, 'water');
const gao = index.get('passage-xishan-gaoshan');
assert.equal(entries.filter(item => item.content_batch === 'xishan-gaoshan').length, 10);
assert.deepEqual(gao.source_unit_ids, ['source-02-0120','source-02-0121','source-02-0122','source-02-0123']);
assert.equal(gao.quote, '又西百五十里曰髙山其上多銀其下多青碧雄黄其木多㯶其草多竹涇水出焉而東流注于渭其中多磬石青碧');
assert.equal(gao.source_pages.length, 1);
assert.ok(gao.source_pages[0].endsWith('/47'));
assert.ok(!gao.quote.includes('女牀'));
assert.equal(index.get('material-xishan-qingbi-gaoshan').relation_scope, undefined);
assert.equal(index.get('material-xishan-qingbi-water-gaoshan').relation_scope, 'water');
assert.notEqual(index.get('material-xishan-qingbi-gaoshan').id, index.get('material-xishan-qingbi-water-gaoshan').id);
assert.ok(index.get('material-xishan-qingbi-gaoshan').commentary_quote.startsWith('碧亦玉𩔗也'));
assert.ok(index.get('water-xishan-jing-gaoshan').commentary_quote.includes('今涇水出安定朝那縣西井頭山'));
assert.equal(index.get('material-xishan-qingshi-gaoshan').commentary_quote, '書曰泗濵浮磬是也');
assert.ok(index.get('water-xishan-wei').quote.endsWith('涇水出焉而東流注于渭'));
assert.ok(index.get('water-xishan-wei').description.includes('七北一南一东'));
assert.equal(entries.filter(item => item.content_batch === 'xishan-gaoshan' && ['兽','鸟','蛇'].includes(item.kind)).length, 0);
const nvchuang = index.get('passage-xishan-nvchuang');
assert.equal(entries.filter(item => item.content_batch === 'xishan-nvchuang').length, 9);
assert.deepEqual(nvchuang.source_unit_ids, ['source-02-0124','source-02-0125','source-02-0126','source-02-0127']);
assert.equal(nvchuang.quote, '西南三百里曰女牀之山其陽多赤銅其隂多石𣵀其獸多虎豹犀兕有鳥焉其状如翟而五彩文名曰鸞鳥見則天下安寧');
assert.equal(nvchuang.source_pages.length, 2);
assert.ok(!nvchuang.quote.includes('龍首'));
assert.ok(inventory.units.find(r => r.id === 'source-02-0126').page_url.endsWith('/47'));
assert.ok(inventory.units.find(r => r.id === 'source-02-0126').captured_page_url.endsWith('/48'));
for (const id of ['tiger','leopard','xi','si']) assert.equal(index.get('animal-xishan-' + id + '-nvchuang').appearance_unknown, true);
assert.ok(index.get('material-xishan-shinie-nvchuang').commentary_quote.startsWith('即楚石也'));
assert.ok(index.get('beast-xishan-luan-nvchuang').quote.includes('其状如翟而五彩文'));
assert.ok(!index.get('beast-xishan-luan-nvchuang').quote.includes('似鷄'));
assert.ok(index.get('beast-xishan-luan-nvchuang').content_note.includes('省字'));
const longshou = index.get('passage-xishan-longshou');
assert.equal(entries.filter(item => item.content_batch === 'xishan-longshou').length, 6);
assert.deepEqual(longshou.source_unit_ids, ['source-02-0128','source-02-0129']);
assert.equal(longshou.quote, '又西二百里曰龍首之山其陽多黄金其隂多鐡苕水出焉東南流注于涇水其中多羙玉');
assert.equal(longshou.source_pages.length, 1);
assert.ok(longshou.source_pages[0].endsWith('/48'));
assert.equal(longshou.commentary_quote, '');
assert.ok(!longshou.quote.includes('鹿臺'));
assert.equal(index.get('material-xishan-gold-longshou').quote, '其陽多黄金');
assert.equal(index.get('material-xishan-iron-longshou').quote, '其隂多鐡');
assert.equal(index.get('material-xishan-fine-jade-longshou').relation_scope, 'water');
assert.equal(index.get('water-xishan-tiao-longshou').quote, '苕水出焉東南流注于涇水');
assert.deepEqual(index.get('water-xishan-jing-gaoshan').source_passage_ids, ['passage-xishan-gaoshan','passage-xishan-longshou']);
assert.deepEqual(index.get('water-xishan-jing-gaoshan').context_place_ids, ['place-xishan-gaoshan','place-xishan-longshou']);
assert.ok(index.get('water-xishan-jing-gaoshan').quote.startsWith('涇水出焉而東流注于渭'));
assert.ok(index.get('water-xishan-jing-gaoshan').quote.endsWith('；苕水出焉東南流注于涇水'));
assert.equal(entries.filter(item => item.content_batch === 'xishan-longshou' && ['兽','鸟','蛇'].includes(item.kind)).length, 0);
const lutai = index.get('passage-xishan-lutai');
assert.equal(entries.filter(item => item.content_batch === 'xishan-lutai').length, 8);
assert.deepEqual(lutai.source_unit_ids, ['source-02-0130','source-02-0131','source-02-0132']);
assert.equal(lutai.quote, '又西二百里曰鹿臺之山其上多白玉其下多銀其獸多㸲牛羬羊白豪有鳥焉其状如雄雞而人面名曰鳬徯其名自呌也見則有兵');
assert.equal(lutai.source_pages.length, 1);
assert.ok(lutai.source_pages[0].endsWith('/48'));
assert.equal(lutai.commentary_quote, '〔影印页48〕今在上郡\n〔影印页48〕豪貆猪也');
assert.ok(!lutai.quote.includes('鳥危'));
assert.equal(index.get('material-xishan-white-jade-lutai').quote, '其上多白玉');
assert.equal(index.get('material-xishan-silver-lutai').quote, '其下多銀');
for (const id of ['animal-xishan-zuoniu-lutai','beast-xishan-qianyang-lutai','animal-xishan-baihao-lutai']) {
  assert.equal(index.get(id).appearance_unknown, true);
  assert.equal(index.get(id).quote, '其獸多㸲牛羬羊白豪');
  assert.ok(!index.get(id).quote.includes('馬尾'));
}
assert.equal(index.get('animal-xishan-baihao-lutai').commentary_quote, '豪貆猪也');
assert.equal(index.get('animal-xishan-zuoniu-lutai').commentary_quote, '');
assert.equal(index.get('beast-xishan-qianyang-lutai').commentary_quote, '');
assert.equal(index.get('beast-xishan-fuxi-lutai').quote, '有鳥焉其状如雄雞而人面名曰鳬徯其名自呌也見則有兵');
assert.ok(!index.get('beast-xishan-fuxi-lutai').appearance_unknown);
assert.equal(entries.filter(item => item.content_batch === 'xishan-lutai' && item.kind === 'water').length, 0);
const niaowei = index.get('passage-xishan-niaowei');
assert.equal(entries.filter(item => item.content_batch === 'xishan-niaowei').length, 8);
assert.deepEqual(niaowei.source_unit_ids, ['source-02-0133','source-02-0134','source-02-0135']);
assert.equal(niaowei.quote, '西南二百里曰鳥危之山其陽多磬石其隂多檀楮其中多女牀鳥危之水出焉西流注于赤水其中多丹粟');
assert.equal(niaowei.source_pages.length, 1);
assert.ok(niaowei.source_pages[0].endsWith('/48'));
assert.ok(inventory.units.find(item => item.id === 'source-02-0135').page_url.endsWith('/48'));
assert.ok(inventory.units.find(item => item.id === 'source-02-0135').captured_page_url.endsWith('/49'));
assert.equal(niaowei.commentary_quote, '〔影印页48〕楮即榖木；未詳');
assert.ok(!niaowei.quote.includes('小次'));
assert.equal(index.get('material-xishan-qingshi-niaowei').quote, '其陽多磬石');
assert.equal(index.get('plant-xishan-chu-niaowei').commentary_quote, '楮即榖木');
assert.equal(index.get('plant-xishan-tan-niaowei').commentary_quote, '');
assert.equal(index.get('material-xishan-nvchuang-niaowei').commentary_quote, '未詳');
assert.equal(index.get('material-xishan-nvchuang-niaowei').kind, 'material');
assert.ok(!index.get('material-xishan-nvchuang-niaowei').appearance_unknown);
assert.equal(index.get('material-xishan-dansu-niaowei').relation_scope, 'water');
assert.equal(index.get('water-xishan-niaowei').quote, '鳥危之水出焉西流注于赤水');
assert.deepEqual(index.get('water-xishan-chi-huangshan').source_passage_ids, ['passage-xishan-huangshan','passage-xishan-niaowei','passage-xishan-huangren']);
assert.deepEqual(index.get('water-xishan-chi-huangshan').context_place_ids, ['place-xishan-huangshan','place-xishan-niaowei','place-xishan-huangren']);
assert.equal(index.get('water-xishan-chi-huangshan').quote, '盼水出焉西流注于赤水；鳥危之水出焉西流注于赤水；皇水出焉西流注于赤水');
assert.equal(index.get('water-xishan-chi-huangshan').artwork, 'xishan/scene-huangshan-v1.webp');
assert.equal(entries.filter(item => item.content_batch === 'xishan-niaowei' && item.kind === 'beast').length, 0);
const xiaoci = index.get('passage-xishan-xiaoci');
assert.equal(entries.filter(item => item.content_batch === 'xishan-xiaoci').length, 5);
assert.deepEqual(xiaoci.source_unit_ids, ['source-02-0136','source-02-0137','source-02-0138']);
assert.equal(xiaoci.quote, '又西四百里曰小次之山其上多白玉其下多赤銅有獸焉其状如猨而白首赤足名曰朱厭見則大兵');
assert.ok(xiaoci.captured_text.includes('其状如猿'));
assert.ok(xiaoci.quote.includes('其状如猨'));
assert.equal(xiaoci.source_pages.length, 1);
assert.ok(xiaoci.source_pages[0].endsWith('/49'));
assert.equal(xiaoci.commentary_quote, '〔影印页49〕一作見則有兵起焉一作見則為兵');
assert.ok(!xiaoci.quote.includes('大次'));
assert.ok(inventory.units.find(item => item.id === 'source-02-0138').confirmed_passage_ids.includes(xiaoci.id));
assert.equal(index.get('material-xishan-white-jade-xiaoci').quote, '其上多白玉');
assert.equal(index.get('material-xishan-red-copper-xiaoci').quote, '其下多赤銅');
assert.equal(index.get('beast-xishan-zhuyan-xiaoci').quote, '有獸焉其状如猨而白首赤足名曰朱厭見則大兵');
assert.equal(index.get('beast-xishan-zhuyan-xiaoci').commentary_quote, '一作見則有兵起焉一作見則為兵');
assert.ok(!index.get('beast-xishan-zhuyan-xiaoci').appearance_unknown);
assert.equal(entries.filter(item => item.content_batch === 'xishan-xiaoci' && item.kind === 'water').length, 0);
const daci = index.get('passage-xishan-daci');
assert.equal(entries.filter(item => item.content_batch === 'xishan-daci').length, 6);
assert.deepEqual(daci.source_unit_ids, ['source-02-0139','source-02-0140']);
assert.equal(daci.quote, '又西三百里曰大次之山其陽多堊其隂多碧其獸多㸲牛麢羊');
assert.equal(daci.source_pages.length, 1);
assert.ok(daci.source_pages[0].endsWith('/49'));
assert.equal(daci.commentary_quote, '〔影印页49〕堊似土色甚白音惡');
assert.ok(!daci.quote.includes('薰吳'));
assert.equal(index.get('material-xishan-e-daci').quote, '其陽多堊');
assert.equal(index.get('material-xishan-e-daci').commentary_quote, '堊似土色甚白音惡');
assert.equal(index.get('material-xishan-bi-daci').quote, '其隂多碧');
assert.equal(index.get('material-xishan-bi-daci').commentary_quote, '');
for (const id of ['animal-xishan-zuoniu-daci','animal-xishan-lingyang-daci']) {
  assert.equal(index.get(id).quote, '其獸多㸲牛麢羊');
  assert.equal(index.get(id).appearance_unknown, true);
  assert.equal(index.get(id).commentary_quote, '');
}
assert.equal(entries.filter(item => item.content_batch === 'xishan-daci' && item.kind === 'water').length, 0);
for (const [batch, count] of range2FinishBatches.map((batch,i) => [batch,[4,10,8,7,4,7,5,5][i]])) assert.equal(entries.filter(item => item.content_batch === batch).length, count, batch);
const xunwu = index.get('passage-xishan-xunwu');
assert.equal(xunwu.quote, '又西四百里曰薰吳之山無草木多金玉');
assert.ok(!xunwu.quote.includes('黄金'));
const quyang = index.get('passage-xishan-quyang');
assert.deepEqual(quyang.source_unit_ids, ['source-02-0142','source-02-0143','source-02-0144']);
assert.equal(quyang.source_pages.length, 1);
assert.ok(quyang.source_pages[0].endsWith('/49'));
assert.ok(quyang.captured_text.includes('虎豹㸲牛') && quyang.quote.includes('虎犳㸲牛'));
assert.ok(index.get('animal-xishan-zhuo-quyang').commentary_quote.includes('犳音之樂反'));
assert.equal(index.get('plant-xishan-ji-quyang').commentary_quote, '稷似松有剌細理音即');
assert.ok(index.get('plant-xishan-yuzhang-quyang').commentary_quote.startsWith('豫章大木'));
assert.equal(index.get('plant-xishan-nan-quyang').commentary_quote, '');
assert.ok(inventory.units.find(u => u.id === 'source-02-0144').page_url.endsWith('/49'));
assert.ok(inventory.units.find(u => u.id === 'source-02-0144').captured_page_url.endsWith('/50'));
const huangren = index.get('passage-xishan-huangren');
assert.deepEqual(huangren.source_unit_ids, ['source-02-0147','source-02-0148','source-02-0149']);
assert.equal(index.get('material-xishan-qingxionghuang-huangren').commentary_quote, '即雌黄也或曰空青曽青之属');
assert.equal(index.get('water-xishan-huang-huangren').quote, '皇水出焉西流注于赤水');
assert.equal(index.get('material-xishan-dansu-huangren').relation_scope, 'water');
assert.equal(index.get('water-xishan-chi-huangshan').source_unit_ids.length, 11);
const zhonghuang = index.get('passage-xishan-zhonghuang');
assert.deepEqual(zhonghuang.source_unit_ids, ['source-02-0150','source-02-0151']);
assert.ok(zhonghuang.captured_text.includes('⟦缺字图:蕙⟧') && zhonghuang.quote.includes('蕙棠') && !zhonghuang.quote.includes('缺字图'));
assert.equal(index.get('plant-xishan-huitang-zhonghuang').commentary_quote, '彤棠之属也或作羔');
assert.ok(inventory.units.find(u => u.id === 'source-02-0153').page_url.endsWith('/50'));
assert.ok(inventory.units.find(u => u.id === 'source-02-0153').captured_page_url.endsWith('/51'));
assert.equal(index.get('animal-xishan-mi-xihuang').commentary_quote, '麋大如小牛鹿属也');
assert.equal(index.get('animal-xishan-deer-xihuang').commentary_quote, '');
assert.equal(index.get('animal-xishan-zuoniu-xihuang').commentary_quote, '');
assert.equal(index.get('bird-xishan-luoluo-laishan').appearance_unknown, true);
assert.equal(index.get('bird-xishan-luoluo-laishan').commentary_quote, '羅羅之鳥所未詳也');
const summary2 = index.get('passage-xishan-range2-summary');
assert.equal(summary2.is_summary, true);
assert.equal(summary2.range, 2);
assert.deepEqual(summary2.source_unit_ids, Array.from({length:6},(_,i)=>'source-02-'+String(156+i).padStart(4,'0')));
assert.equal(summary2.source_pages.length, 1);
assert.ok(summary2.source_pages[0].endsWith('/51'));
assert.ok(summary2.quote.includes('凡十七山四千一百四十里') && summary2.quote.endsWith('鈐而不糈毛采') && !summary2.quote.includes('崇吾'));
assert.ok(!index.has('place-xishan-range2-summary'));
assert.ok(!index.get('deity-xishan-horse-range2').quote.includes('四足'));
assert.ok(index.get('deity-xishan-ox-range2').quote.includes('四足而一臂操杖以行'));
assert.equal(index.get('rite-xishan-shaolao-range2').commentary_quote, '羊猪為少牢也');
assert.ok(index.get('rite-xishan-rooster-range2').commentary_quote.includes('所未詳也'));
assert.ok(!summary2.content_note.includes('首列十九山'));
assert.equal(world.beasts.length, 114);
assert.equal([...index.values()].filter(item=>item.appearance_unknown).length, 39);
const chongwu = index.get('passage-xishan-chongwu');
assert.equal(chongwu.range, 3);
assert.equal(chongwu.order, 39);
assert.equal(entries.filter(item => item.content_batch === 'xishan-chongwu').length, 9);
assert.equal(passages.filter(item => item.range === 3).length, 7);
assert.deepEqual(chongwu.source_unit_ids, Array.from({length:7},(_,i) => 'source-02-' + String(162+i).padStart(4,'0')));
assert.deepEqual(chongwu.source_pages.map(p => p.split('/').at(-1)), ['51','52']);
assert.ok(inventory.units.find(u => u.id === 'source-02-0162').page_url.endsWith('/51'));
assert.ok(inventory.units.find(u => u.id === 'source-02-0162').captured_page_url.endsWith('/52'));
assert.ok(chongwu.captured_text.includes('⟦缺字图:搏⟧'));
assert.ok(chongwu.quote.includes('帝之摶獸之丘'));
assert.ok(!chongwu.quote.includes('缺字图'));
assert.equal(index.get('water-xishan-yanyuan-chongwu').commentary_quote, '音於然反');
assert.equal(index.get('place-xishan-zhongsui-chongwu').commentary_quote, '山名');
assert.equal(index.get('water-xishan-yaoze-chongwu').commentary_quote, '音遥');
assert.ok(index.get('plant-xishan-unnamed-chongwu').quote.includes('員葉而白柎赤華而黒理'));
assert.ok(index.get('plant-xishan-unnamed-chongwu').commentary_quote.includes('丈夫字或作柎音符'));
assert.ok(index.get('beast-xishan-jufu-chongwu').quote.includes('文臂豹虎而善投'));
assert.equal(index.get('beast-xishan-jufu-chongwu').commentary_quote, '或作夸父');
assert.ok(!index.get('bird-xishan-manman-chongwu').quote.includes('色青赤'));
assert.ok(index.get('bird-xishan-manman-chongwu').commentary_quote.includes('色青赤'));
for (const id of ['beast-xishan-jufu-chongwu','bird-xishan-manman-chongwu']) assert.ok(!index.get(id).appearance_unknown && index.get(id).artwork_pending);
assert.deepEqual(index.get('water-xishan-he-taimao').source_passage_ids, ['passage-xishan-taimao','passage-xishan-chongwu','passage-xishan-buzhou']);
assert.ok(index.get('water-xishan-he-taimao').quote.includes('；崇吾之山在河之南'));
assert.ok(!entryRelations.some(r => r.ids.includes('place-xishan-laishan') && r.ids.includes('place-xishan-chongwu')));
const changsha = index.get('passage-xishan-changsha');
assert.equal(changsha.range, 3);
assert.equal(changsha.order, 40);
assert.equal(entries.filter(item => item.content_batch === 'xishan-changsha').length, 5);
assert.deepEqual(changsha.source_unit_ids, ['source-02-0169','source-02-0170']);
assert.deepEqual(changsha.source_pages.map(p => p.split('/').at(-1)), ['52']);
assert.equal(changsha.quote, '西北三百里曰長沙之山泚水出焉北流注于泑水無草木多青雄黄');
assert.equal(index.get('water-xishan-ci-changsha').commentary_quote, '音紫');
assert.ok(english['water-xishan-ci-changsha'].name.startsWith('Zi'));
assert.equal(index.get('water-xishan-you-changsha').commentary_quote, '烏交反又音黝水色黑也');
assert.ok(!index.get('material-xishan-qingxionghuang-changsha').commentary_quote);
assert.notEqual(index.get('material-xishan-qingxionghuang-changsha').id, index.get('material-xishan-qingxionghuang-huangren').id);
for (const entry of entries.filter(e => e.content_batch === 'xishan-changsha')) assert.ok(entry.artwork_pending && !entry.artwork && !entry.appearance_unknown);
assert.ok(entryRelations.some(r => r.ids.includes('place-xishan-chongwu') && r.ids.includes('place-xishan-changsha') && r.quote === '西北三百里曰長沙之山'));
assert.ok(entryRelations.some(r => r.ids.includes('water-xishan-ci-changsha') && r.ids.includes('water-xishan-you-changsha') && r.quote === '泚水出焉北流注于泑水'));
const buzhou = index.get('passage-xishan-buzhou');
assert.equal(buzhou.range, 3);
assert.equal(buzhou.order, 41);
assert.equal(entries.filter(e => e.content_batch === 'xishan-buzhou').length,6);
assert.deepEqual(buzhou.source_unit_ids,Array.from({length:7},(_,i)=>'source-02-'+String(171+i).padStart(4,'0')));
assert.deepEqual(buzhou.source_pages.map(p=>p.split('/').at(-1)),['52','53']);
assert.ok(inventory.units.find(u=>u.id==='source-02-0171').page_url.endsWith('/52'));
assert.ok(inventory.units.find(u=>u.id==='source-02-0171').captured_page_url.endsWith('/53'));
assert.ok(buzhou.commentary_quote.includes('流歧出合而東流注泑澤'));
assert.ok(buzhou.commentary_quote.includes('百里其水停冬夏不增减'));
assert.ok(buzhou.quote.endsWith('𬃷黄華而赤柎食之不勞'));
assert.ok(!buzhou.quote.includes('峚山'));
assert.ok(!buzhou.quote.includes('不周風'));
assert.ok(!index.has('wind-xishan-buzhou'));
assert.ok(index.get('water-xishan-youze-buzhou').commentary_quote.endsWith('衮咆二音'));
assert.ok(!index.get('plant-xishan-jia-guo-buzhou').commentary_quote);
assert.notEqual(index.get('water-xishan-youze-buzhou').id,index.get('water-xishan-you-changsha').id);
assert.equal(index.get('water-xishan-he-taimao').source_passage_ids.length,3);
assert.deepEqual(index.get('water-xishan-he-taimao').source_pages.map(p=>p.split('/').at(-1)),['46','51','52','53']);
for(const entry of entries.filter(e=>e.content_batch==='xishan-buzhou')) assert.ok(entry.artwork_pending && !entry.artwork && !entry.appearance_unknown);
const mishan=index.get('passage-xishan-mishan');
assert.equal(mishan.range,3);assert.equal(mishan.order,42);
assert.equal(entries.filter(e=>e.content_batch==='xishan-mishan').length,16);
assert.deepEqual(mishan.source_unit_ids,Array.from({length:15},(_,i)=>'source-02-'+String(178+i).padStart(4,'0')));
assert.deepEqual(mishan.source_pages.map(p=>p.split('/').at(-1)),['53','54','55']);
for(const [unit,page,captured] of [[180,53,54],[189,54,55]]) {const u=inventory.units.find(u=>u.id==='source-02-'+String(unit).padStart(4,'0'));assert.ok(u.page_url.endsWith('/'+page));assert.ok(u.captured_page_url.endsWith('/'+captured));}
assert.ok(mishan.captured_text.includes('⟦缺字图:鬼⟧'));assert.ok(mishan.quote.includes('天地鬼神是食是饗'));assert.ok(!mishan.quote.includes('缺字图'));
assert.ok(mishan.quote.endsWith('其間盡澤也是多竒鳥怪獸竒魚皆異物焉'));
assert.equal(index.get('material-xishan-xuanyu-mishan').commentary_quote,'言玉膏中又出黑玉也');
assert.ok(index.get('material-xishan-yugao-mishan').commentary_quote.endsWith('沸音拂'));
assert.equal(index.get('water-xishan-jize-mishan').commentary_quote,'后稷神所馮因名云');
assert.ok(index.get('material-xishan-yurong-mishan').commentary_quote.includes('之華英又曰登崑崙𠔃食玉英'));
assert.ok(!mishan.quote.includes('金剛石') && mishan.commentary_quote.includes('金剛石'));
assert.ok(!index.has('material-xishan-diamond-mishan'));
assert.equal(index.get('place-xishan-zhongshan').source_passage_ids[0],mishan.id);
assert.equal(index.get('place-xishan-zhongshan').content_batch,'xishan-zhongshan');
assert.ok(!index.has('passage-xishan-kunlun'));
assert.notEqual(index.get('water-xishan-dan-mishan').id,index.get('water-xishan-dan-nanshan').id);
const miPlaceholders=['deity-xishan-huangdi-mishan','deity-xishan-heaven-earth-mishan','bird-xishan-birds-mi-zhong','beast-xishan-beasts-mi-zhong','beast-xishan-fish-mi-zhong'];
for(const id of miPlaceholders)assert.ok(index.get(id).appearance_unknown && index.get(id).artwork_pending);
for(const e of entries.filter(e=>e.content_batch==='xishan-mishan'))assert.ok(!e.artwork && e.artwork_pending);
assert.equal(entries.filter(e=>e.content_batch==='xishan-mishan' && e.appearance_unknown).length,5);
const zhongshan=index.get('passage-xishan-zhongshan');
assert.equal(zhongshan.range,3);assert.equal(zhongshan.order,43);
assert.equal(entries.filter(e=>e.content_batch==='xishan-zhongshan').length,10);
assert.deepEqual(zhongshan.source_unit_ids,Array.from({length:10},(_,i)=>'source-02-'+String(193+i).padStart(4,'0')));
assert.deepEqual(zhongshan.source_pages.map(p=>p.split('/').at(-1)),['55','56']);
assert.ok(inventory.units.find(u=>u.id==='source-02-0198').page_url.endsWith('/55'));
assert.ok(inventory.units.find(u=>u.id==='source-02-0198').captured_page_url.endsWith('/56'));
assert.ok(zhongshan.quote.endsWith('邑大旱'));
assert.ok(zhongshan.commentary_quote.includes('百獸之所聚飛鳥之栖也'));
assert.ok(zhongshan.commentary_quote.includes('圃之上以詔後世'));
assert.ok(!zhongshan.quote.includes('赤豹白虎'));
const zhongPlace=index.get('place-xishan-zhongshan');
assert.deepEqual(zhongPlace.source_passage_ids,['passage-xishan-mishan','passage-xishan-zhongshan']);
assert.deepEqual(zhongPlace.source_pages.map(p=>p.split('/').at(-1)),['53','54','55','56']);
assert.ok(zhongPlace.quote.includes('自峚山至于鍾山四百六十里'));
assert.ok(zhongPlace.quote.includes('又西北四百二十里曰鍾山'));
assert.equal(zhongPlace.source_unit_ids.length,25);
assert.ok(mishan.related_entry_ids.includes(zhongPlace.id));
assert.ok(index.get('deity-xishan-gu-zhongshan').quote.includes('人靣而龍身'));
assert.ok(!index.get('deity-xishan-gu-zhongshan').quote.includes('馬身'));
assert.ok(index.get('deity-xishan-gu-zhongshan').commentary_quote.includes('人靣馬身'));
assert.equal(index.get('deity-xishan-baojiang-zhongshan').commentary_quote,'葆或作祖');
assert.ok(index.get('deity-xishan-di-zhongshan').appearance_unknown);
assert.notEqual(index.get('deity-xishan-di-zhongshan').id,index.get('deity-xishan-huangdi-mishan').id);
assert.ok(index.get('bird-xishan-qinpi-e-zhongshan').quote.includes('虎𤓰'));
assert.ok(index.get('bird-xishan-gu-jun-zhongshan').quote.includes('其邑大旱'));
const zhongCreatureIds=['deity-xishan-gu-zhongshan','deity-xishan-qinpi-zhongshan','deity-xishan-baojiang-zhongshan','deity-xishan-di-zhongshan','bird-xishan-qinpi-e-zhongshan','bird-xishan-gu-jun-zhongshan'];
assert.equal(entries.filter(e=>e.content_batch==='xishan-zhongshan'&&e.appearance_unknown).length,3);
for(const e of entries.filter(e=>e.content_batch==='xishan-zhongshan'))assert.ok(e.artwork_pending&&!e.artwork);
const taiqi=index.get('passage-xishan-taiqi');
assert.equal(taiqi.range,3);assert.equal(taiqi.order,44);
assert.equal(entries.filter(e=>e.content_batch==='xishan-taiqi').length,6);
assert.deepEqual(taiqi.source_unit_ids,Array.from({length:5},(_,i)=>'source-02-'+String(203+i).padStart(4,'0')));
assert.deepEqual(taiqi.source_pages.map(p=>p.split('/').at(-1)),['56']);
assert.ok(inventory.units.find(u=>u.id==='source-02-0207').page_url.endsWith('/56'));
assert.ok(inventory.units.find(u=>u.id==='source-02-0207').captured_page_url.endsWith('/57'));
assert.ok(taiqi.quote.endsWith('見則天下大穰'));
assert.ok(taiqi.commentary_quote.includes('也韓子曰穰嵗之秋'));
assert.equal(index.get('beast-xishan-wenyao-taiqi').commentary_quote,'音遥；鸞雞鳥名未詳也或作欒；豐穰收熟也韓子曰穰嵗之秋');
assert.ok(!index.get('beast-xishan-wenyao-taiqi').appearance_unknown);
assert.ok(index.get('beast-xishan-wenyao-taiqi').quote.includes('魚身而鳥翼蒼文而白首赤喙'));
assert.ok(!index.has('bird-xishan-luanji-taiqi'));
assert.equal(index.get('place-xishan-liusha').kind,'place');
assert.equal(index.get('water-xishan-guan-taiqi').quote,'𮗚水出焉西流注于流沙');
const westernSea=index.get('water-xishan-westsea-guishan');
assert.deepEqual(westernSea.source_passage_ids,['passage-xishan-guishan','passage-xishan-taiqi']);
assert.deepEqual(westernSea.source_pages.map(p=>p.split('/').at(-1)),['45','56']);
assert.equal(westernSea.source_unit_ids.length,8);
assert.ok(westernSea.artwork.endsWith('scene-guishan-v1.webp'));
assert.ok(westernSea.artwork_caption.includes('不代指文鰩魚'));
assert.ok(taiqi.related_entry_ids.includes(westernSea.id));
assert.notEqual(index.get('water-xishan-eastsea-taiqi').id,index.get('water-nanshan-east-sea').id);
for(const e of entries.filter(e=>e.content_batch==='xishan-taiqi'))assert.ok(e.artwork_pending&&!e.artwork);
const huaijiang=index.get('passage-xishan-huaijiang');
assert.equal(huaijiang.range,3);assert.equal(huaijiang.order,45);
assert.equal(entries.filter(e=>e.content_batch==='xishan-huaijiang').length,24);
assert.deepEqual(huaijiang.source_unit_ids,Array.from({length:15},(_,i)=>'source-02-'+String(208+i).padStart(4,'0')));
assert.deepEqual(huaijiang.source_pages.map(p=>p.split('/').at(-1)),['57','58']);
assert.ok(inventory.units.find(u=>u.id==='source-02-0216').page_url.endsWith('/57'));
assert.ok(inventory.units.find(u=>u.id==='source-02-0216').captured_page_url.endsWith('/58'));
for(const glyph of ['鬼','搏','滛'])assert.ok(huaijiang.captured_text.includes('⟦缺字图:'+glyph+'⟧'));
assert.ok(!huaijiang.quote.includes('缺字图'));
assert.ok(huaijiang.quote.includes('各在一摶爰有滛水'));
assert.ok(huaijiang.quote.endsWith('其音如勃皇見則其邑有兵'));
assert.equal(index.get('beast-xishan-luomu-huaijiang').commentary_quote,'即䗱螺也');
assert.ok(index.get('deity-xishan-yingzhao-huaijiang').commentary_quote.endsWith('此所未詳也'));
assert.ok(index.get('deity-xishan-houji-huaijiang').commentary_quote.endsWith('箕尾也'));
assert.ok(index.get('plant-xishan-yaomu-ruo-huaijiang').commentary_quote.includes('大木之竒靈者為若'));
assert.ok(index.get('bird-xishan-zhan-huaijiang').commentary_quote.includes('白鳥青雕'));
assert.ok(index.get('deity-xishan-yingzhao-huaijiang').quote.includes('馬身而人靣虎文而鳥翼'));
assert.ok(index.get('deity-xishan-ox-eight-huaijiang').quote.includes('八足二首馬尾'));
assert.deepEqual(index.get('water-xishan-you-changsha').source_passage_ids,['passage-xishan-changsha','passage-xishan-huaijiang']);
assert.deepEqual(index.get('place-xishan-zhupi-buzhou').source_passage_ids,['passage-xishan-buzhou','passage-xishan-huaijiang']);
assert.equal(index.get('water-xishan-you-changsha').source_unit_ids.length,17);
assert.equal(index.get('place-xishan-zhupi-buzhou').source_unit_ids.length,22);
assert.ok(huaijiang.related_entry_ids.includes('water-xishan-you-changsha'));
assert.ok(huaijiang.related_entry_ids.includes('place-xishan-zhupi-buzhou'));
assert.equal(index.get('place-xishan-kunlun').content_batch,'xishan-huaijiang');
assert.ok(!index.has('passage-xishan-kunlun'));
const huaiCreatureIds=['beast-xishan-luomu-huaijiang','deity-xishan-yingzhao-huaijiang','deity-xishan-houji-huaijiang','deity-xishan-lilun-huaijiang','bird-xishan-ying-huaijiang','bird-xishan-zhan-huaijiang','deity-xishan-youqiong-huaijiang','deity-xishan-ox-eight-huaijiang'];
assert.equal(entries.filter(e=>e.content_batch==='xishan-huaijiang'&&e.appearance_unknown).length,6);
for(const e of entries.filter(e=>e.content_batch==='xishan-huaijiang'))assert.ok(e.artwork_pending&&!e.artwork);
const hasArtwork = entry => Boolean(entry.artwork || entry.appearance_unknown || entry.kind === 'deity' || /^(beast|animal|bird)-/.test(entry.id));
const search = searchIndex(world, catalog, world, catalog);
for (const id of ['water-xishan-chi-huangshan','water-nanshan-chishui-gui']) assert.ok(searchEntries(search, '赤水', 'water').some(item => item.id === id));
for (const id of ['place-xishan-nvchuang','material-xishan-nvchuang-niaowei']) assert.ok(searchEntries(search, '女牀').some(item => item.id === id));
for (const id of ['beast-xishan-qianyang','beast-xishan-qianyang-ying','beast-xishan-qianyang-lutai']) assert.ok(searchEntries(search, '羬羊', 'beast').some(item => item.id === id));
for (const id of ['animal-xishan-zuoniu','animal-xishan-zuoniu-ying','animal-xishan-zuoniu-lutai','animal-xishan-zuoniu-daci']) assert.ok(searchEntries(search, '㸲牛').some(item => item.id === id));
for (const id of ['material-xishan-dansu-gaotu', 'material-xishan-dansu-nanshan', 'material-xishan-dansu-guishan']) assert.ok(searchEntries(search, '丹粟', 'material').some(item => item.id === id));
for (const id of ['water-xishan-dan-nanshan', 'water-xishan-dan-zhushan', 'water-nanshan-dan']) assert.ok(searchEntries(search, '丹水', 'water').some(item => item.id === id), id + ': same-name Dan waters remain discoverable');
for (const id of ['beast-xishan-feiyi-ying', 'beast-xishan-feiyi-taihua']) assert.ok(searchEntries(search, '肥遗', 'beast').some(item => item.id === id), `${id}: shared-name discovery keeps distinct records`);
for (const entry of entries) {
  assert.ok(!('x' in entry || 'y' in entry || 'place_id' in entry), 'New content does not invent mapped positions');
  assert.equal(entry.review_status, 'facsimile_reviewed');
  assert.ok(english[entry.id]?.description && english[entry.id]?.quote);
  assert.equal(readExploration(`?chapter=03&item=${entry.id}`, world, catalog).item, entry.id);
  assert.equal(readExploration(`?chapter=02&item=${entry.id}`, world, catalog).item, null);
  assert.ok(searchEntries(search, entry.name, entry.kind).some(item => item.id === entry.id));
  assert.ok(entry.source_unit_ids.every(id => inventory.units.some(u => u.id === id && u.confirmed_passage_ids.length)));
  if (['xishan-range1-summary', 'xishan-qianshan', 'xishan-taimao', 'xishan-shuli', 'xishan-gaoshan', 'xishan-nvchuang', 'xishan-longshou', 'xishan-lutai', 'xishan-niaowei', 'xishan-xiaoci', 'xishan-daci', ...range2FinishBatches, 'xishan-chongwu', 'xishan-changsha', 'xishan-buzhou', 'xishan-mishan', 'xishan-zhongshan', 'xishan-taiqi', 'xishan-huaijiang'].includes(entry.content_batch)) {
    assert.ok(!entry.artwork && entry.artwork_pending);
  } else assert.ok(entry.artwork && !entry.artwork_pending);
}
for (const relation of entryRelations.filter(item => item.source === '《西山经》')) {
  for (const label of relation.labels) assert.ok(labels[label] && !/\p{Script=Han}/u.test(labels[label]), `English relationship label: ${label}`);
  const sources = relation.ids.flatMap(id => [index.get(id), ...(index.get(id).source_passage_ids || []).map(id => index.get(id))]);
  assert.ok(sources.some(item => item.quote.includes(relation.quote)), `${relation.ids}: exact source evidence`);
  for (const id of relation.ids) assert.ok(relatedEntries(id, index).some(item => item.id === relation.ids.find(other => other !== id)));
}
assert.equal(generation.assets.length, 56);
for (const asset of generation.assets) {
  assert.equal(asset.status, 'reviewed');
  const published = artwork.assets.find(item => item.id === `xishan-${asset.name}-v1`);
  assert.ok(published.source_copy.endsWith(asset.source_file));
  for (const [name, variant] of Object.entries(published.variants)) {
    assert.equal((await stat(new URL('../public' + variant.path, import.meta.url))).size, variant.bytes);
    assert.ok(Math.max(...variant.dimensions) <= ({ full: 1280, card: 320, preview: 480 }[name]));
  }
}
const output = new URL('../../output/qa/', import.meta.url);
await mkdir(output, { recursive: true });
for (const name of (process.env.ATLAS_BROWSERS || 'chromium,webkit').split(',')) {
  const browser = await ({ chromium, webkit }[name]).launch();
  try {
    const context = await browser.newContext({ viewport: { width: 390, height: 844 }, reducedMotion: 'reduce' });
    await mockTianditu(context);
    if (process.env.ATLAS_STATIC_DIR) {
      const root = resolve(process.env.ATLAS_STATIC_DIR);
      const address = new URL(base);
      await context.route(`${address.origin}/**`, async route => {
        const requested = new URL(route.request().url());
        if (!requested.pathname.startsWith(address.pathname)) return route.fulfill({ status: 404, body: 'Not found' });
        const target = resolve(root, decodeURIComponent(requested.pathname.slice(address.pathname.length)) || 'index.html');
        if (!target.startsWith(root + sep)) return route.fulfill({ status: 403, body: 'Forbidden' });
        if (!(await stat(target).catch(() => null))?.isFile()) return route.fulfill({ status: 404, body: 'Not found' });
        await route.fulfill({ path: target });
      });
    }
    await context.addInitScript(() => localStorage.setItem('shanhai-onboarding-v1', '1'));
    const page = await context.newPage(), errors = [], failed = [], requested = [];
    page.on('pageerror', error => errors.push(error.message));
    page.on('request', request => requested.push(request.url()));
    page.on('response', response => { if (response.status() >= 400 && response.url().startsWith(base)) failed.push(response.url()); });
    const drawer = page.locator('.detail-drawer');
    const ready = async id => {
      try {
        await page.waitForFunction(id => {
          const node = document.querySelector('.detail-drawer');
          return node?.dataset.entryId === id && node.dataset.readingRestoring === 'false';
        }, id);
        if (name === 'webkit') await page.waitForTimeout(200);
      } catch (error) {
        console.error('Drawer readiness failure', JSON.stringify({ expected: id, url: page.url(), errors, failed,
          state: await page.evaluate(() => ({ id: document.querySelector('.detail-drawer')?.dataset.entryId,
            restoring: document.querySelector('.detail-drawer')?.dataset.readingRestoring,
            searchOpen: Boolean(document.querySelector('.global-search-input')) })) }));
        throw error;
      }
    };
    const decode = async () => {
      await drawer.locator('.drawer-art').scrollIntoViewIfNeeded();
      await page.waitForFunction(() => {
        const img = document.querySelector('.detail-drawer .drawer-art');
        return img?.complete && img.naturalWidth > 0;
      });
      await drawer.locator('.drawer-art').evaluate(img => img.decode());
    };
    await page.goto(`${base}?chapter=00&lang=zh`);
    assert.equal(requested.some(url => /xishan\/.*-v1\.webp/.test(url)), false, 'No full batch download at startup');
    for (const lang of ['zh', 'en']) {
      await page.goto(`${base}?chapter=03&lang=${lang}`);
      await page.locator('.mobile-explore-nav button').nth(1).click();
      await openSourceLibrary(page);
      const directory = page.locator('.chapter-text-entries[data-source-book="2"]:visible');
      await directory.locator('>summary').click();
      for (const summary of await directory.locator('.passage-range>summary').all()) await summary.click();
      assert.equal(await directory.locator('[data-entry-id]').count(), passages.length);
      await directory.locator('[data-entry-id="passage-xishan-qianlai"]').click();
      await ready('passage-xishan-qianlai');
      assert.equal(await drawer.locator('.detail-entry-position').innerText(), `1 / ${passages.length}`);
      await drawer.locator('.detail-entry-nav button').nth(1).click();
      await ready('passage-xishan-songguo');
      assert.equal(await drawer.locator('.detail-entry-position').innerText(), `2 / ${passages.length}`);
      for (const entry of browserEntries) {
        await page.goto(`${base}?chapter=03&item=${entry.id}&lang=${lang}`); await ready(entry.id);
        assert.equal(await drawer.locator('>.content-origin').getAttribute('data-origin'), 'shanhaijing');
        assert.equal(await drawer.locator('.detail-description').innerText(), lang === 'en' ? english[entry.id].description : entry.description);
        assert.equal(await drawer.evaluate(node => node.scrollWidth > node.clientWidth), false);
        if (hasArtwork(entry)) await decode();
        else {
          assert.equal(await drawer.locator('.drawer-art, .artwork-pending').count(), 0);
        }
        await drawer.locator('.detail-reading-actions button').nth(0).click();
        await drawer.locator('.detail-reading-actions button').nth(1).click();
        await page.reload(); await ready(entry.id);
        assert.ok(await drawer.locator('.detail-reading-actions button').evaluateAll(nodes => nodes.every(node => node.getAttribute('aria-pressed') === (document.documentElement.lang === 'en' ? 'false' : 'true'))));
      }
      await page.goto(`${base}?chapter=03&item=place-xishan-songguo&lang=${lang}`); await ready('place-xishan-songguo');
      await drawer.locator('[data-related-id="water-xishan-huo"]').click(); await ready('water-xishan-huo');
      await drawer.locator('[data-related-id="water-xishan-wei"]').click(); await ready('water-xishan-wei');
      await page.goBack(); await ready('water-xishan-huo');
      await page.goBack(); await ready('place-xishan-songguo');
      await drawer.locator('[data-related-id="passage-xishan-songguo"]').click(); await ready('passage-xishan-songguo');
      assert.equal(new URL(page.url()).searchParams.get('chapter'), '03');
      await page.goto(`${base}?chapter=03&item=place-xishan-fuyu&lang=${lang}`); await ready('place-xishan-fuyu');
      await drawer.locator('[data-related-id="water-xishan-fuyu"]').click(); await ready('water-xishan-fuyu');
      await drawer.locator('[data-related-id="water-xishan-wei"]').click(); await ready('water-xishan-wei');
      assert.ok(await drawer.locator('[data-related-id="passage-xishan-songguo"]').count());
      assert.ok(await drawer.locator('[data-related-id="passage-xishan-fuyu"]').count());
      await page.goto(`${base}?chapter=03&item=water-xishan-guan&lang=${lang}`); await ready('water-xishan-guan');
      await drawer.locator('[data-related-id="material-xishan-liuzhe"]').click(); await ready('material-xishan-liuzhe');
      await page.goBack(); await ready('water-xishan-guan');
      await drawer.locator('[data-related-id="water-xishan-yu-shicui"]').click(); await ready('water-xishan-yu-shicui');
      await page.goto(`${base}?chapter=03&item=place-xishan-taihua&lang=${lang}`); await ready('place-xishan-taihua');
      await drawer.locator('[data-related-id="place-xishan-xiaohua"]').click(); await ready('place-xishan-xiaohua');
      await drawer.locator('[data-related-id="place-xishan-fuyu"]').click(); await ready('place-xishan-fuyu');
      await drawer.locator('[data-related-id="place-xishan-shicui"]').click(); await ready('place-xishan-shicui');
      await drawer.locator('[data-related-id="place-xishan-ying"]').click(); await ready('place-xishan-ying');
      await drawer.locator('[data-related-id="water-xishan-yu-ying"]').click(); await ready('water-xishan-yu-ying');
      await drawer.locator('[data-related-id="beast-xishan-bangyu-ying"]').click(); await ready('beast-xishan-bangyu-ying');
      await page.goBack(); await ready('water-xishan-yu-ying');
      await drawer.locator('[data-related-id="water-xishan-zhao-ying"]').click(); await ready('water-xishan-zhao-ying');
      await page.goto(`${base}?chapter=03&item=place-xishan-zhushan&lang=${lang}`); await ready('place-xishan-zhushan');
      await drawer.locator('[data-related-id="water-xishan-zhu"]').click(); await ready('water-xishan-zhu');
      await drawer.locator('[data-related-id="water-xishan-wei"]').click(); await ready('water-xishan-wei');
      for (const id of ['songguo', 'fuyu', 'zhushan', 'yuci', 'shishan', 'nanshan-west', 'dashi', 'shuli', 'gaoshan']) assert.equal(await drawer.locator(`[data-related-id="passage-xishan-${id}"]`).count(), 1);
      await page.goto(`${base}?chapter=03&item=water-xishan-dan-zhushan&lang=${lang}`); await ready('water-xishan-dan-zhushan');
      await drawer.locator('[data-related-id="beast-xishan-renyu-zhushan"]').click(); await ready('beast-xishan-renyu-zhushan');
      await page.goBack(); await ready('water-xishan-dan-zhushan');
      await drawer.locator('[data-related-id="water-xishan-luo-zhushan"]').click(); await ready('water-xishan-luo-zhushan');
      await page.goto(`${base}?chapter=03&item=place-xishan-zhushan&lang=${lang}`); await ready('place-xishan-zhushan');
      await drawer.locator('[data-related-id="place-xishan-fushan"]').click(); await ready('place-xishan-fushan');
      await drawer.locator('[data-related-id="plant-xishan-xuncao"]').click(); await ready('plant-xishan-xuncao');
      await page.goto(base + '?chapter=03&item=place-xishan-fushan&lang=' + lang); await ready('place-xishan-fushan');
      await drawer.locator('[data-related-id="place-xishan-yuci"]').click(); await ready('place-xishan-yuci');
      await drawer.locator('[data-related-id="water-xishan-qi-yuci"]').click(); await ready('water-xishan-qi-yuci');
      await drawer.locator('[data-related-id="water-xishan-wei"]').click(); await ready('water-xishan-wei');
      await drawer.locator('[data-related-id="passage-xishan-yuci"]').click(); await ready('passage-xishan-yuci');
      await page.goto(base + '?chapter=03&item=place-xishan-yuci&lang=' + lang); await ready('place-xishan-yuci');
      await drawer.locator('[data-related-id="place-xishan-shishan"]').click(); await ready('place-xishan-shishan');
      await drawer.locator('[data-related-id="water-xishan-zhu-shishan"]').click(); await ready('water-xishan-zhu-shishan');
      await drawer.locator('[data-related-id="material-xishan-shuiyu-shishan"]').click(); await ready('material-xishan-shuiyu-shishan');
      await page.goBack(); await ready('water-xishan-zhu-shishan');
      await drawer.locator('[data-related-id="water-xishan-wei"]').click(); await ready('water-xishan-wei');
      await drawer.locator('[data-related-id="passage-xishan-shishan"]').click(); await ready('passage-xishan-shishan');
      await page.goto(base + '?chapter=03&item=place-xishan-shishan&lang=' + lang); await ready('place-xishan-shishan');
      await drawer.locator('[data-related-id="place-xishan-nanshan-west"]').click(); await ready('place-xishan-nanshan-west');
      await drawer.locator('[data-related-id="water-xishan-dan-nanshan"]').click(); await ready('water-xishan-dan-nanshan');
      await drawer.locator('[data-related-id="water-xishan-wei"]').click(); await ready('water-xishan-wei');
      await drawer.locator('[data-related-id="passage-xishan-nanshan-west"]').click(); await ready('passage-xishan-nanshan-west');
      await page.goto(base + '?chapter=03&item=place-xishan-nanshan-west&lang=' + lang); await ready('place-xishan-nanshan-west');
      await drawer.locator('[data-related-id="place-xishan-dashi"]').click(); await ready('place-xishan-dashi');
      await drawer.locator('[data-related-id="water-xishan-qian-dashi"]').click(); await ready('water-xishan-qian-dashi');
      await drawer.locator('[data-related-id="water-xishan-wei"]').click(); await ready('water-xishan-wei');
      await drawer.locator('[data-related-id="passage-xishan-dashi"]').click(); await ready('passage-xishan-dashi');
      await page.goto(base + '?chapter=03&item=water-xishan-qing-dashi&lang=' + lang); await ready('water-xishan-qing-dashi');
      await drawer.locator('[data-related-id="water-xishan-han-dashi"]').click(); await ready('water-xishan-han-dashi');
      await page.goBack(); await ready('water-xishan-qing-dashi');
      await page.goto(base + '?chapter=03&item=place-xishan-dashi&lang=' + lang); await ready('place-xishan-dashi');
      await drawer.locator('[data-related-id="place-xishan-bozhong"]').click(); await ready('place-xishan-bozhong');
      await drawer.locator('[data-related-id="water-xishan-han-dashi"]').click(); await ready('water-xishan-han-dashi');
      for (const id of ['passage-xishan-dashi', 'passage-xishan-bozhong']) assert.equal(await drawer.locator('[data-related-id="' + id + '"]').count(), 1);
      await drawer.locator('[data-related-id="water-xishan-mian-bozhong"]').click(); await ready('water-xishan-mian-bozhong');
      await page.goBack(); await ready('water-xishan-han-dashi');
      await page.goto(base + '?chapter=03&item=water-xishan-xiao-bozhong&lang=' + lang); await ready('water-xishan-xiao-bozhong');
      await drawer.locator('[data-related-id="water-xishan-tang-bozhong"]').click(); await ready('water-xishan-tang-bozhong');
      await page.goto(`${base}?chapter=03&lang=${lang}`);
      await page.locator('.global-search-trigger').click();
      await page.locator('.global-search-input').fill('䳋渠');
      await page.locator('.global-search-tools select').selectOption('beast');
      await page.locator('.search-result[data-result-id="beast-xishan-tongqu"]').click(); await ready('beast-xishan-tongqu');
      await drawer.locator('.return-search').click();
      assert.equal(await page.locator('.global-search-input').inputValue(), '䳋渠');
      await page.goto(base + '?chapter=03&item=place-xishan-bozhong&lang=' + lang); await ready('place-xishan-bozhong');
      await drawer.locator('[data-related-id="place-xishan-tiandi"]').click(); await ready('place-xishan-tiandi');
      for (const id of ['beast-xishan-xibian-tiandi', 'beast-xishan-li-tiandi', 'plant-xishan-duheng-tiandi']) {
        await drawer.locator('[data-related-id="' + id + '"]').click(); await ready(id);
        await drawer.locator('[data-related-id="passage-xishan-tiandi"]').click(); await ready('passage-xishan-tiandi');
        await drawer.locator('[data-related-id="place-xishan-tiandi"]').click(); await ready('place-xishan-tiandi');
      }
      await page.goto(base + '?chapter=03&item=place-xishan-tiandi&lang=' + lang); await ready('place-xishan-tiandi');
      await drawer.locator('[data-related-id="place-xishan-gaotu"]').click(); await ready('place-xishan-gaotu');
      for (const [river, receiver] of [['water-xishan-se-gaotu', 'water-xishan-zhuzi-gaotu'], ['water-xishan-tu-gaotu', 'water-xishan-jihuo-gaotu']]) {
        await drawer.locator('[data-related-id="' + river + '"]').click(); await ready(river);
        await drawer.locator('[data-related-id="' + receiver + '"]').click(); await ready(receiver);
        await drawer.locator('[data-related-id="passage-xishan-gaotu"]').click(); await ready('passage-xishan-gaotu');
        await drawer.locator('[data-related-id="place-xishan-gaotu"]').click(); await ready('place-xishan-gaotu');
      }
      for (const id of ['material-xishan-yu-gaotu', 'plant-xishan-wutiao-gaotu', 'beast-xishan-yingru-gaotu', 'beast-xishan-shusi-gaotu']) {
        await drawer.locator('[data-related-id="' + id + '"]').click(); await ready(id);
        await drawer.locator('[data-related-id="passage-xishan-gaotu"]').click(); await ready('passage-xishan-gaotu');
        await drawer.locator('[data-related-id="place-xishan-gaotu"]').click(); await ready('place-xishan-gaotu');
      }
      await page.goto(base + '?chapter=03&item=place-xishan-gaotu&lang=' + lang); await ready('place-xishan-gaotu');
      await drawer.locator('[data-related-id="place-xishan-huangshan"]').click(); await ready('place-xishan-huangshan');
      for (const id of ['plant-xishan-zhujian-huangshan', 'beast-xishan-min-huangshan', 'beast-xishan-yingmu-huangshan']) {
        await drawer.locator('[data-related-id="' + id + '"]').click(); await ready(id);
        await decode();
        await drawer.locator('[data-related-id="passage-xishan-huangshan"]').click(); await ready('passage-xishan-huangshan');
        await drawer.locator('[data-related-id="place-xishan-huangshan"]').click(); await ready('place-xishan-huangshan');
      }
      await drawer.locator('[data-related-id="water-xishan-pan-huangshan"]').click(); await ready('water-xishan-pan-huangshan');
      await drawer.locator('[data-related-id="water-xishan-chi-huangshan"]').click(); await ready('water-xishan-chi-huangshan');
      await page.goBack(); await ready('water-xishan-pan-huangshan');
      await drawer.locator('[data-related-id="material-xishan-jade-huangshan"]').click(); await ready('material-xishan-jade-huangshan');
      await page.goto(base + '?chapter=03&item=place-xishan-huangshan&lang=' + lang); await ready('place-xishan-huangshan');
      await drawer.locator('[data-related-id="place-xishan-cuishan"]').click(); await ready('place-xishan-cuishan');
      for (const id of ['animal-xishan-maoniu-cuishan', 'animal-xishan-ling-cuishan', 'animal-xishan-she-cuishan', 'bird-xishan-lei-cuishan']) {
        await drawer.locator('[data-related-id="' + id + '"]').click(); await ready(id); await decode();
        await drawer.locator('[data-related-id="passage-xishan-cuishan"]').click(); await ready('passage-xishan-cuishan');
        await drawer.locator('[data-related-id="place-xishan-cuishan"]').click(); await ready('place-xishan-cuishan');
      }
      await page.goto(base + '?chapter=03&item=place-xishan-cuishan&lang=' + lang); await ready('place-xishan-cuishan');
      await drawer.locator('[data-related-id="place-xishan-guishan"]').click(); await ready('place-xishan-guishan');
      await drawer.locator('[data-related-id="water-xishan-qi-guishan"]').click(); await ready('water-xishan-qi-guishan');
      await drawer.locator('[data-related-id="water-xishan-westsea-guishan"]').click(); await ready('water-xishan-westsea-guishan');
      await page.goBack(); await ready('water-xishan-qi-guishan');
      for (const id of ['material-xishan-caishi-guishan','material-xishan-gold-guishan']) {
        await drawer.locator('[data-related-id="' + id + '"]').click(); await ready(id);
        await drawer.locator('[data-related-id="water-xishan-qi-guishan"]').click(); await ready('water-xishan-qi-guishan');
      }
      await drawer.locator('[data-related-id="passage-xishan-guishan"]').click(); await ready('passage-xishan-guishan');
      await drawer.locator('[data-related-id="place-xishan-guishan"]').click(); await ready('place-xishan-guishan');
      await page.goto(base + '?chapter=03&item=passage-xishan-guishan&lang=' + lang); await ready('passage-xishan-guishan');
      await drawer.locator('[data-related-id="passage-xishan-range1-summary"]').click(); await ready('passage-xishan-range1-summary');
      for (const id of ['rite-xishan-hua-range1','rite-xishan-yu-range1','rite-xishan-seventeen-range1']) {
        await drawer.locator('[data-related-id="' + id + '"]').click(); await ready(id);
        assert.equal(await drawer.locator('.drawer-art, .artwork-pending').count(), 0);
        await drawer.locator('[data-related-id="passage-xishan-range1-summary"]').click(); await ready('passage-xishan-range1-summary');
      }
      await drawer.locator('[data-related-id="passage-xishan-qianshan"]').click(); await ready('passage-xishan-qianshan');
      assert.equal(await drawer.locator('.drawer-art, .artwork-pending').count(), 0);
      for (const id of ['material-xishan-copper-qianshan','material-xishan-jade-qianshan','plant-xishan-niu-qianshan','plant-xishan-jiang-qianshan']) {
        await drawer.locator('[data-related-id="' + id + '"]').click(); await ready(id);
        assert.equal(await drawer.locator('.drawer-art, .artwork-pending').count(), 0);
        await drawer.locator('[data-related-id="place-xishan-qianshan"]').click(); await ready('place-xishan-qianshan');
        await drawer.locator('[data-related-id="passage-xishan-qianshan"]').click(); await ready('passage-xishan-qianshan');
      }
      await drawer.locator('[data-related-id="place-xishan-qianshan"]').click(); await ready('place-xishan-qianshan');
      await drawer.locator('[data-related-id="place-xishan-taimao"]').click(); await ready('place-xishan-taimao');
      await drawer.locator('[data-related-id="water-xishan-yu-taimao"]').click(); await ready('water-xishan-yu-taimao');
      await drawer.locator('[data-related-id="water-xishan-he-taimao"]').click(); await ready('water-xishan-he-taimao');
      await page.goBack(); await ready('water-xishan-yu-taimao');
      for (const id of ['material-xishan-zaoyu-taimao','beast-xishan-white-snake-taimao']) {
        await drawer.locator('[data-related-id="' + id + '"]').click(); await ready(id);
        if (id.startsWith('beast-')) {
          await decode();
          assert.ok((await drawer.locator('.drawer-art').getAttribute('src')).includes('unknown-creature-v4-full.webp'));
        }
        await drawer.locator('[data-related-id="water-xishan-yu-taimao"]').click(); await ready('water-xishan-yu-taimao');
      }
      await drawer.locator('[data-related-id="place-xishan-taimao"]').click(); await ready('place-xishan-taimao');
      await drawer.locator('[data-related-id="place-xishan-shuli"]').click(); await ready('place-xishan-shuli');
      await drawer.locator('[data-related-id="beast-xishan-yingmu-shuli"]').click(); await ready('beast-xishan-yingmu-shuli');
      await decode();
      assert.ok((await drawer.locator('.drawer-art').getAttribute('src')).includes('unknown-creature-v4-full.webp'));
      await drawer.locator('[data-related-id="passage-xishan-shuli"]').click(); await ready('passage-xishan-shuli');
      await drawer.locator('[data-related-id="water-xishan-chu-shuli"]').click(); await ready('water-xishan-chu-shuli');
      await drawer.locator('[data-related-id="water-xishan-wei"]').click(); await ready('water-xishan-wei');
      assert.equal(await drawer.locator('[data-related-id="passage-xishan-shuli"]').count(), 1);
      await page.goBack(); await ready('water-xishan-chu-shuli');
      await drawer.locator('[data-related-id="material-xishan-pearl-shuli"]').click(); await ready('material-xishan-pearl-shuli');
      await drawer.locator('[data-related-id="water-xishan-chu-shuli"]').click(); await ready('water-xishan-chu-shuli');
      await drawer.locator('[data-related-id="place-xishan-shuli"]').click(); await ready('place-xishan-shuli');
      await drawer.locator('[data-related-id="place-xishan-gaoshan"]').click(); await ready('place-xishan-gaoshan');
      await drawer.locator('[data-related-id="water-xishan-jing-gaoshan"]').click(); await ready('water-xishan-jing-gaoshan');
      await drawer.locator('[data-related-id="water-xishan-wei"]').click(); await ready('water-xishan-wei');
      assert.equal(await drawer.locator('[data-related-id="passage-xishan-gaoshan"]').count(), 1);
      await page.goBack(); await ready('water-xishan-jing-gaoshan');
      for (const id of ['material-xishan-qingshi-gaoshan','material-xishan-qingbi-water-gaoshan']) {
        await drawer.locator('[data-related-id="' + id + '"]').click(); await ready(id);
        assert.equal(await drawer.locator('.drawer-art, .artwork-pending').count(), 0);
        await drawer.locator('[data-related-id="water-xishan-jing-gaoshan"]').click(); await ready('water-xishan-jing-gaoshan');
      }
      await drawer.locator('[data-related-id="place-xishan-gaoshan"]').click(); await ready('place-xishan-gaoshan');
      await drawer.locator('[data-related-id="place-xishan-nvchuang"]').click(); await ready('place-xishan-nvchuang');
      for (const id of ['animal-xishan-tiger-nvchuang','animal-xishan-leopard-nvchuang','animal-xishan-xi-nvchuang','animal-xishan-si-nvchuang','beast-xishan-luan-nvchuang']) {
        await drawer.locator('[data-related-id="' + id + '"]').click(); await ready(id);
        await decode();
        assert.ok((await drawer.locator('.drawer-art').getAttribute('src')).includes('unknown-creature-v4-full.webp'));
        assert.ok((await drawer.locator('.return-related').innerText()).includes(lang === 'zh' ? index.get('place-xishan-nvchuang').name : english['place-xishan-nvchuang'].name));
        await drawer.locator('.return-related').click(); await ready('place-xishan-nvchuang');
      }
      await page.goto(`${base}?chapter=03&item=place-xishan-nvchuang&lang=${lang}`); await ready('place-xishan-nvchuang');
      await drawer.locator('[data-related-id="place-xishan-longshou"]').click(); await ready('place-xishan-longshou');
      await drawer.locator('[data-related-id="water-xishan-tiao-longshou"]').click(); await ready('water-xishan-tiao-longshou');
      await drawer.locator('[data-related-id="water-xishan-jing-gaoshan"]').click(); await ready('water-xishan-jing-gaoshan');
      await drawer.locator('[data-related-id="water-xishan-wei"]').click(); await ready('water-xishan-wei');
      await page.goto(`${base}?chapter=03&item=place-xishan-longshou&lang=${lang}`); await ready('place-xishan-longshou');
      await drawer.locator('[data-related-id="place-xishan-lutai"]').click(); await ready('place-xishan-lutai');
      for (const id of ['animal-xishan-zuoniu-lutai','beast-xishan-qianyang-lutai','animal-xishan-baihao-lutai','beast-xishan-fuxi-lutai']) {
        await drawer.locator('[data-related-id="' + id + '"]').click(); await ready(id);
        await decode();
        assert.ok((await drawer.locator('.drawer-art').getAttribute('src')).includes('unknown-creature-v4-full.webp'));
        assert.ok((await drawer.locator('.return-related').innerText()).includes(lang === 'zh' ? index.get('place-xishan-lutai').name : english['place-xishan-lutai'].name));
        await drawer.locator('.return-related').click(); await ready('place-xishan-lutai');
      }
      await page.goto(`${base}?chapter=03&item=place-xishan-lutai&lang=${lang}`); await ready('place-xishan-lutai');
      await drawer.locator('[data-related-id="place-xishan-niaowei"]').click(); await ready('place-xishan-niaowei');
      await drawer.locator('[data-related-id="material-xishan-nvchuang-niaowei"]').click(); await ready('material-xishan-nvchuang-niaowei');
      assert.equal(await drawer.locator('.drawer-art, .artwork-pending').count(), 0);
      await drawer.locator('.commentary-section>summary').click();
      assert.equal(await drawer.locator('.commentary-section blockquote').innerText(), '未詳');
      await drawer.locator('.return-related').click(); await ready('place-xishan-niaowei');
      await drawer.locator('[data-related-id="water-xishan-niaowei"]').click(); await ready('water-xishan-niaowei');
      await drawer.locator('[data-related-id="material-xishan-dansu-niaowei"]').click(); await ready('material-xishan-dansu-niaowei');
      await drawer.locator('.return-related').click(); await ready('water-xishan-niaowei');
      await drawer.locator('[data-related-id="water-xishan-chi-huangshan"]').click(); await ready('water-xishan-chi-huangshan');
      for (const id of ['passage-xishan-huangshan','passage-xishan-niaowei']) assert.equal(await drawer.locator('[data-related-id="' + id + '"]').count(), 1);
      await page.goto(`${base}?chapter=03&item=place-xishan-niaowei&lang=${lang}`); await ready('place-xishan-niaowei');
      await drawer.locator('[data-related-id="place-xishan-xiaoci"]').click(); await ready('place-xishan-xiaoci');
      await drawer.locator('[data-related-id="beast-xishan-zhuyan-xiaoci"]').click(); await ready('beast-xishan-zhuyan-xiaoci');
      await decode();
      assert.ok((await drawer.locator('.drawer-art').getAttribute('src')).includes('unknown-creature-v4-full.webp'));
      await drawer.locator('.commentary-section>summary').click();
      assert.equal(await drawer.locator('.commentary-section blockquote').innerText(), '一作見則有兵起焉一作見則為兵');
      await drawer.locator('.return-related').click(); await ready('place-xishan-xiaoci');
      await page.goto(`${base}?chapter=03&item=place-xishan-xiaoci&lang=${lang}`); await ready('place-xishan-xiaoci');
      await drawer.locator('[data-related-id="place-xishan-daci"]').click(); await ready('place-xishan-daci');
      for (const id of ['animal-xishan-zuoniu-daci','animal-xishan-lingyang-daci']) {
        await drawer.locator('[data-related-id="' + id + '"]').click(); await ready(id);
        await decode();
        assert.ok((await drawer.locator('.drawer-art').getAttribute('src')).includes('unknown-creature-v4-full.webp'));
        assert.equal(await drawer.locator('.commentary-section').count(), 0);
        await drawer.locator('.return-related').click(); await ready('place-xishan-daci');
      }
      await drawer.locator('[data-related-id="material-xishan-e-daci"]').click(); await ready('material-xishan-e-daci');
      await drawer.locator('.commentary-section>summary').click();
      assert.equal(await drawer.locator('.commentary-section blockquote').innerText(), '堊似土色甚白音惡');
      await page.goto(`${base}?chapter=03&item=place-xishan-daci&lang=${lang}`); await ready('place-xishan-daci');
      for (const slug of ['xunwu','quyang','zhongshou','huangren','zhonghuang','xihuang','laishan']) {
        await drawer.locator('[data-related-id="place-xishan-' + slug + '"]').click(); await ready('place-xishan-' + slug);
      }
      await drawer.locator('[data-related-id="passage-xishan-laishan"]').click(); await ready('passage-xishan-laishan');
      await drawer.locator('[data-related-id="passage-xishan-range2-summary"]').click(); await ready('passage-xishan-range2-summary');
      for (const id of ['deity-xishan-horse-range2','deity-xishan-ox-range2','rite-xishan-shaolao-range2','rite-xishan-rooster-range2']) {
        await drawer.locator('[data-related-id="' + id + '"]').click(); await ready(id);
        if (id.startsWith('deity-')) {
          await decode();
          assert.ok((await drawer.locator('.drawer-art').getAttribute('src')).includes('unknown-creature-v4-full.webp'));
        }
        await drawer.locator('.return-related').click(); await ready('passage-xishan-range2-summary');
      }
      await page.goto(`${base}?chapter=03&item=water-xishan-huang-huangren&lang=${lang}`); await ready('water-xishan-huang-huangren');
      await drawer.locator('[data-related-id="water-xishan-chi-huangshan"]').click(); await ready('water-xishan-chi-huangshan');
      for (const id of ['passage-xishan-huangshan','passage-xishan-niaowei','passage-xishan-huangren']) assert.equal(await drawer.locator('[data-related-id="' + id + '"]').count(), 1);
      const allSearchCases = ['material-xishan-e-daci', 'material-xishan-bi-daci', 'animal-xishan-zuoniu-daci', 'animal-xishan-lingyang-daci', 'beast-xishan-zhuyan-xiaoci', 'material-xishan-white-jade-xiaoci', 'material-xishan-red-copper-xiaoci', 'material-xishan-nvchuang-niaowei', 'plant-xishan-chu-niaowei', 'water-xishan-niaowei', 'material-xishan-dansu-niaowei', 'animal-xishan-zuoniu-lutai', 'beast-xishan-qianyang-lutai', 'animal-xishan-baihao-lutai', 'beast-xishan-fuxi-lutai', 'water-xishan-tiao-longshou', 'material-xishan-fine-jade-longshou', 'plant-xishan-tiao-fuyu', 'plant-xishan-tiao-shicui', 'animal-xishan-zuoniu', 'beast-xishan-feiyi-ying', 'beast-xishan-feiyi-taihua', 'beast-xishan-renyu-zhushan', 'plant-xishan-xuncao', 'beast-xishan-xiao-yuci', 'beast-xishan-tuofei-yuci', 'water-xishan-zhu-shishan', 'material-xishan-shuiyu-shishan', 'beast-xishan-mengbao-nanshan', 'beast-xishan-shijiu-nanshan', 'water-xishan-dan-nanshan', 'water-xishan-qian-dashi', 'water-xishan-qing-dashi', 'water-xishan-han-dashi', 'material-xishan-silver-dashi', 'material-xishan-white-jade-dashi', 'animal-xishan-pi-bozhong', 'bird-xishan-baihan-bozhong', 'plant-xishan-gurong-bozhong', 'water-xishan-xiao-bozhong', 'beast-xishan-xibian-tiandi', 'beast-xishan-li-tiandi', 'plant-xishan-duheng-tiandi', 'water-xishan-se-gaotu', 'water-xishan-tu-gaotu', 'material-xishan-yu-gaotu', 'plant-xishan-wutiao-gaotu', 'beast-xishan-yingru-gaotu', 'beast-xishan-shusi-gaotu', 'beast-xishan-min-huangshan', 'beast-xishan-yingmu-huangshan', 'water-xishan-pan-huangshan', 'animal-xishan-ling-cuishan', 'bird-xishan-lei-cuishan', 'water-xishan-qi-guishan', 'rite-xishan-yu-range1', 'plant-xishan-niu-qianshan', 'plant-xishan-jiang-qianshan', 'material-xishan-zaoyu-taimao', 'beast-xishan-white-snake-taimao', 'water-xishan-yu-taimao', 'water-xishan-chu-shuli', 'beast-xishan-yingmu-shuli', 'material-xishan-pearl-shuli', 'water-xishan-jing-gaoshan', 'material-xishan-qingbi-gaoshan', 'material-xishan-qingbi-water-gaoshan', 'beast-xishan-luan-nvchuang', 'material-xishan-shinie-nvchuang', 'animal-xishan-xi-nvchuang'];
      await page.goto(`${base}?chapter=03&item=place-xishan-chongwu&lang=${lang}`); await ready('place-xishan-chongwu');
      for (const id of ['place-xishan-zhongsui-chongwu','water-xishan-yaoze-chongwu','place-xishan-tuan-shou-qiu-chongwu','water-xishan-yanyuan-chongwu','plant-xishan-unnamed-chongwu','beast-xishan-jufu-chongwu','bird-xishan-manman-chongwu']) {
        await drawer.locator(`[data-related-id="${id}"]`).click(); await ready(id);
        if (/^(beast|bird)-/.test(id)) { await decode(); assert.ok((await drawer.locator('.drawer-art').getAttribute('src')).includes('unknown-creature-v4')); }
        assert.ok((await drawer.locator('.return-related').innerText()).includes(lang === 'zh' ? '崇吾' : 'Chongwu'));
        await drawer.locator('.return-related').click(); await ready('place-xishan-chongwu');
      }
      await drawer.locator('[data-related-id="water-xishan-he-taimao"]').click(); await ready('water-xishan-he-taimao');
      for (const id of ['passage-xishan-taimao','passage-xishan-chongwu']) assert.equal(await drawer.locator(`[data-related-id="${id}"]`).count(),1);
      await page.goto(`${base}?chapter=03&item=place-xishan-chongwu&lang=${lang}`); await ready('place-xishan-chongwu');
      await drawer.locator('[data-related-id="place-xishan-changsha"]').click(); await ready('place-xishan-changsha');
      for (const id of ['water-xishan-ci-changsha','water-xishan-you-changsha','material-xishan-qingxionghuang-changsha']) {
        await drawer.locator(`[data-related-id="${id}"]`).click(); await ready(id);
        assert.equal(await drawer.locator('.drawer-art, .artwork-pending').count(),0);
        assert.ok((await drawer.locator('.return-related').innerText()).includes(lang === 'zh' ? '長沙' : 'Changsha'));
        await drawer.locator('.return-related').click(); await ready('place-xishan-changsha');
      }
      await drawer.locator('[data-related-id="water-xishan-ci-changsha"]').click(); await ready('water-xishan-ci-changsha');
      await drawer.locator('[data-related-id="water-xishan-you-changsha"]').click(); await ready('water-xishan-you-changsha');
      assert.ok((await drawer.locator('.detail-description').innerText()).includes(lang === 'zh' ? '水色黑' : 'dark-water'));
      await page.goto(`${base}?chapter=03&item=place-xishan-changsha&lang=${lang}`); await ready('place-xishan-changsha');
      await drawer.locator('[data-related-id="place-xishan-buzhou"]').click(); await ready('place-xishan-buzhou');
      for(const id of ['place-xishan-zhupi-buzhou','place-xishan-yuechong-buzhou','water-xishan-youze-buzhou','plant-xishan-jia-guo-buzhou']) {
        await drawer.locator(`[data-related-id="${id}"]`).click();await ready(id);
        assert.equal(await drawer.locator('.drawer-art,.artwork-pending').count(),0);
        assert.ok((await drawer.locator('.return-related').innerText()).includes(lang==='zh'?'不周':'Buzhou'));
        await drawer.locator('.return-related').click();await ready('place-xishan-buzhou');
      }
      await drawer.locator('[data-related-id="water-xishan-youze-buzhou"]').click();await ready('water-xishan-youze-buzhou');
      await drawer.locator('[data-related-id="water-xishan-he-taimao"]').click();await ready('water-xishan-he-taimao');
      for(const id of ['passage-xishan-taimao','passage-xishan-chongwu','passage-xishan-buzhou']) assert.equal(await drawer.locator(`[data-related-id="${id}"]`).count(),1);
      await page.goto(`${base}?chapter=03&item=place-xishan-buzhou&lang=${lang}`);await ready('place-xishan-buzhou');
      await drawer.locator('[data-related-id="place-xishan-mishan"]').click();await ready('place-xishan-mishan');
      for(const id of ['plant-xishan-danmu-mishan','water-xishan-dan-mishan','water-xishan-jize-mishan','material-xishan-yugao-mishan','material-xishan-xuanyu-mishan','material-xishan-yurong-mishan','material-xishan-jinyu-mishan','place-xishan-zhongshan',...miPlaceholders]){
        await drawer.locator(`[data-related-id="${id}"]`).click();await ready(id);
        if(miPlaceholders.includes(id)){await decode();assert.ok((await drawer.locator('.drawer-art').getAttribute('src')).includes('unknown-creature-v4'));}
        else assert.equal(await drawer.locator('.drawer-art,.artwork-pending').count(),0);
        assert.ok((await drawer.locator('.return-related').innerText()).includes(lang==='zh'?'峚':'Mi'));
        await drawer.locator('.return-related').click();await ready('place-xishan-mishan');
      }
      await drawer.locator('[data-related-id="water-xishan-dan-mishan"]').click();await ready('water-xishan-dan-mishan');
      await drawer.locator('[data-related-id="water-xishan-jize-mishan"]').click();await ready('water-xishan-jize-mishan');
      await page.goto(`${base}?chapter=03&item=material-xishan-yugao-mishan&lang=${lang}`);await ready('material-xishan-yugao-mishan');
      await drawer.locator('[data-related-id="plant-xishan-danmu-mishan"]').click();await ready('plant-xishan-danmu-mishan');
      await page.goto(`${base}?chapter=03&item=material-xishan-yurong-mishan&lang=${lang}`);await ready('material-xishan-yurong-mishan');
      await drawer.locator('[data-related-id="place-xishan-zhongshan"]').click();await ready('place-xishan-zhongshan');
      await page.goto(`${base}?chapter=03&item=place-xishan-mishan&lang=${lang}`);await ready('place-xishan-mishan');
      await drawer.locator('[data-related-id="place-xishan-zhongshan"]').click();await ready('place-xishan-zhongshan');
      for(const id of [...zhongCreatureIds,'place-xishan-kunlun-yang-zhongshan','place-xishan-yaoya-zhongshan']){
        await drawer.locator(`[data-related-id="${id}"]`).click();await ready(id);
        if(zhongCreatureIds.includes(id)){await decode();assert.ok((await drawer.locator('.drawer-art').getAttribute('src')).includes('unknown-creature-v4'));}
        else assert.equal(await drawer.locator('.drawer-art,.artwork-pending').count(),0);
        await drawer.locator('.return-related').click();await ready('place-xishan-zhongshan');
      }
      for(const id of ['passage-xishan-mishan','passage-xishan-zhongshan'])assert.equal(await drawer.locator(`[data-related-id="${id}"]`).count(),1);
      for(const [from,to] of [['deity-xishan-gu-zhongshan','bird-xishan-gu-jun-zhongshan'],['deity-xishan-qinpi-zhongshan','bird-xishan-qinpi-e-zhongshan']]){
        await page.goto(`${base}?chapter=03&item=${from}&lang=${lang}`);await ready(from);
        await drawer.locator(`[data-related-id="${to}"]`).click();await ready(to);await decode();
        await drawer.locator('.return-related').click();await ready(from);
      }
      await page.goto(`${base}?chapter=03&item=place-xishan-zhongshan&lang=${lang}`);await ready('place-xishan-zhongshan');
      await drawer.locator('[data-related-id="place-xishan-taiqi"]').click();await ready('place-xishan-taiqi');
      for(const id of ['water-xishan-guan-taiqi','place-xishan-liusha','beast-xishan-wenyao-taiqi','water-xishan-eastsea-taiqi']){
        await drawer.locator(`[data-related-id="${id}"]`).click();await ready(id);
        if(id==='beast-xishan-wenyao-taiqi'){await decode();assert.ok((await drawer.locator('.drawer-art').getAttribute('src')).includes('unknown-creature-v4'));}
        else assert.equal(await drawer.locator('.drawer-art,.artwork-pending').count(),0);
        await drawer.locator('.return-related').click();await ready('place-xishan-taiqi');
      }
      await drawer.locator('[data-related-id="water-xishan-guan-taiqi"]').click();await ready('water-xishan-guan-taiqi');
      await drawer.locator('[data-related-id="place-xishan-liusha"]').click();await ready('place-xishan-liusha');
      await page.goto(`${base}?chapter=03&item=beast-xishan-wenyao-taiqi&lang=${lang}`);await ready('beast-xishan-wenyao-taiqi');
      await drawer.locator('[data-related-id="water-xishan-westsea-guishan"]').click();await ready('water-xishan-westsea-guishan');await decode();
      for(const id of ['passage-xishan-guishan','passage-xishan-taiqi'])assert.equal(await drawer.locator(`[data-related-id="${id}"]`).count(),1);
      await page.goto(`${base}?chapter=03&item=beast-xishan-wenyao-taiqi&lang=${lang}`);await ready('beast-xishan-wenyao-taiqi');
      await drawer.locator('[data-related-id="water-xishan-eastsea-taiqi"]').click();await ready('water-xishan-eastsea-taiqi');
      await page.goto(`${base}?chapter=03&item=place-xishan-taiqi&lang=${lang}`);await ready('place-xishan-taiqi');
      await drawer.locator('[data-related-id="place-xishan-huaijiang"]').click();await ready('place-xishan-huaijiang');
      for(const id of [...huaiCreatureIds,'water-xishan-qiushi-huaijiang','place-xishan-pingpu-huaijiang','place-xishan-kunlun','water-xishan-daze-huaijiang','plant-xishan-yaomu-ruo-huaijiang','place-xishan-danshan-huaijiang','water-xishan-flowing-huaijiang']){
        await drawer.locator(`[data-related-id="${id}"]`).click();await ready(id);
        if(huaiCreatureIds.includes(id)){await decode();assert.ok((await drawer.locator('.drawer-art').getAttribute('src')).includes('unknown-creature-v4'));}
        else assert.equal(await drawer.locator('.drawer-art,.artwork-pending').count(),0);
        await drawer.locator('.return-related').click();await ready('place-xishan-huaijiang');
      }
      await drawer.locator('[data-related-id="water-xishan-qiushi-huaijiang"]').click();await ready('water-xishan-qiushi-huaijiang');
      await drawer.locator('[data-related-id="water-xishan-you-changsha"]').click();await ready('water-xishan-you-changsha');
      for(const id of ['passage-xishan-changsha','passage-xishan-huaijiang'])assert.equal(await drawer.locator(`[data-related-id="${id}"]`).count(),1);
      await page.goto(`${base}?chapter=03&item=place-xishan-zhupi-buzhou&lang=${lang}`);await ready('place-xishan-zhupi-buzhou');
      for(const id of ['passage-xishan-buzhou','passage-xishan-huaijiang'])assert.equal(await drawer.locator(`[data-related-id="${id}"]`).count(),1);
      const searchCases = process.env.ATLAS_BATCH === 'xishan-range2-finish' ? [
        'material-xishan-jin-xunwu','material-xishan-jade-xunwu','plant-xishan-ji-quyang','plant-xishan-yuzhang-quyang','animal-xishan-zhuo-quyang','animal-xishan-zuoniu-quyang',
        'material-xishan-tufu-zhongshou','animal-xishan-xi-zhongshou','material-xishan-qingxionghuang-huangren','water-xishan-huang-huangren','material-xishan-dansu-huangren','water-xishan-chi-huangshan',
        'plant-xishan-huitang-zhonghuang','animal-xishan-mi-xihuang','animal-xishan-deer-xihuang','bird-xishan-luoluo-laishan',
        'deity-xishan-horse-range2','deity-xishan-ox-range2','rite-xishan-shaolao-range2','rite-xishan-rooster-range2',
        'material-xishan-nvchuang-niaowei','water-xishan-jing-gaoshan','water-xishan-wei','beast-xishan-qianyang-lutai',
      ] : ['xishan-chongwu','xishan-changsha','xishan-buzhou','xishan-mishan','xishan-zhongshan','xishan-taiqi','xishan-huaijiang'].includes(process.env.ATLAS_BATCH) ? [...browserEntries.map(item => item.id), 'beast-xishan-xiao-yuci', 'water-xishan-wei', 'water-xishan-chi-huangshan', 'material-xishan-qingxionghuang-huangren', 'material-xishan-qingxionghuang-changsha'] : allSearchCases;
      for (const [caseIndex, id] of searchCases.entries()) {
        // Start a fresh document per five cases to stay within WebKit's History API write quota.
        if (caseIndex % 5 === 0) {
          await page.goto(base + '?chapter=03&lang=' + lang);
          await page.locator('.global-search-trigger').click();
        }
        const item = index.get(id);
        await page.locator('.global-search-tools select').selectOption(item.kind);
        await page.locator('.global-search-input').fill(item.name);
        await page.locator(`.search-result[data-result-id="${id}"]`).click(); await ready(id);
        await drawer.locator('.return-search').click();
      }
      await page.locator('.global-search-tools select').selectOption('all');
      await page.locator('.global-search-input').fill('囂');
      for (const id of ['beast-xishan-xiao-yuci', 'water-xishan-xiao-bozhong']) assert.equal(await page.locator('.search-result[data-result-id="' + id + '"]').count(), 1);
      await page.locator('.global-search-tools select').selectOption('water');
      await page.locator('.global-search-input').fill('丹水');
      for (const id of ['water-xishan-dan-nanshan', 'water-xishan-dan-zhushan', 'water-nanshan-dan']) assert.equal(await page.locator('.search-result[data-result-id="' + id + '"]').count(), 1);
      await page.locator('.global-search-tools select').selectOption('beast');
      await page.locator('.global-search-input').fill('肥遗');
      for (const id of ['beast-xishan-feiyi-ying', 'beast-xishan-feiyi-taihua']) assert.equal(await page.locator(`.search-result[data-result-id="${id}"]`).count(), 1);
      await page.locator('.search-result[data-result-id="beast-xishan-feiyi-ying"]').click(); await ready('beast-xishan-feiyi-ying');
      await drawer.locator('.return-search').click();
      await page.locator('.search-result[data-result-id="beast-xishan-feiyi-taihua"]').click(); await ready('beast-xishan-feiyi-taihua');
      await drawer.locator('[data-reading-anchor="source"]').scrollIntoViewIfNeeded();
      await page.waitForFunction(() => {
        const saved = JSON.parse(localStorage.getItem('shanhai-last-reading-v1'));
        return saved?.id === 'beast-xishan-feiyi-taihua' && saved.chapter === '03' && saved.position?.anchor !== 'start';
      });
      await page.goto(`${base}?lang=${lang}`);
      await page.waitForFunction(() => window.history.state?.shanhai?.stageIndex === 0);
      assert.ok((await page.locator('.resume-reading[aria-label]').getAttribute('aria-label')).includes(lang === 'zh' ? index.get('beast-xishan-feiyi-taihua').name : english['beast-xishan-feiyi-taihua'].name));
      await page.locator('.resume-reading[aria-label]').click(); await ready('beast-xishan-feiyi-taihua');
      assert.ok(await drawer.evaluate(node => node.scrollTop > 0));
      console.log(`PASS ${name} ${lang}: ${browserEntries.length} browser records, bird/snake Feiyi separation, 9 Wei sources, southeast glyph and reading state`);
    }
    for (const [width, height] of [[320, 700], [390, 844], [844, 390], [1440, 1000]]) for (const lang of ['zh', 'en']) {
      await page.setViewportSize({ width, height });
      await page.goto(`${base}?chapter=03&item=passage-xishan-huaijiang&lang=${lang}`); await ready('passage-xishan-huaijiang');
      if (width === 390 && lang === 'zh') {
        const loaded = await page.evaluate(async () => {
          for (const weight of [400,600]) await document.fonts.load(weight + ' 16px ShanhaiRare', '𢇨𭥍𣈆㤗𣵀𪇱䍃䗡𨵿𬃷𡺯𤓰𫟍䲹㱕𮗚䗱𨼆𮪍𠕂');
          return [...document.fonts].filter(f => f.family.replaceAll('\"', '') === 'ShanhaiRare' && ['221E8','2D94D','23206','3917','23D40','2A1F1','4343','45E1','28D7F','21EAF','244F0','2B7CD','4CB9','3C55','2E5DA','45F1','28F06','2EA8D','20542'].some(code => f.unicodeRange.toUpperCase().includes(code))).map(f => ({range:f.unicodeRange.toUpperCase(),status:f.status}));
        });
        for (const code of ['221E8','2D94D','23206','3917','23D40','2A1F1','4343','45E1','28D7F','21EAF','244F0','2B7CD','4CB9','3C55','2E5DA','45F1','28F06','2EA8D','20542']) assert.ok(loaded.some(f => f.range.includes(code) && f.status === 'loaded'), code + ': correct rare-character face loaded');
      }
      await drawer.locator('.commentary-section>summary').click();
      assert.equal(await drawer.evaluate(node => node.scrollWidth > node.clientWidth), false);
      assert.ok(await drawer.locator('.detail-related button').evaluateAll(nodes => nodes.every(node => node.getBoundingClientRect().height >= 44)));
      if (name === 'chromium' && width === 390) await page.screenshot({ type: 'jpeg', quality: 70, path: new URL(`xishan-${lang}.jpg`, output).pathname.replace(/^\/([A-Za-z]:)/, '$1') });
    }
    assert.deepEqual(errors, []);
    assert.deepEqual(failed, []);
    await context.close();
    console.log(`PASS ${name}: Western 43 mountains + two range summaries/293 cards, ${browserEntries.length} browser records, exact relations, 56 artworks, bilingual search/marks/resume and 8 layouts`);
  } finally { await browser.close(); }
}
