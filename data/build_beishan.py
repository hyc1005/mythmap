"""Merge facsimile-reviewed Northern Mountain passages without replacing other books."""
import hashlib
import json
from pathlib import Path
from beishan_first_range import extend as extend_first_range

ROOT = Path(__file__).resolve().parents[1]
BATCH = 'beishan-danhu'
PASSAGE = 'passage-beishan-danhu'
PLACE = 'place-beishan-danhu'
SOURCE = '《山海经·北山经》（《四部丛刊》景明成化本，郭璞传）'
EN_SOURCE = 'Shanhaijing · Beishan Jing (Sibu Congkan facsimile; Guo Pu commentary)'
DESCRIPTION = '北山经首山为單狐，多机木，山上多華草。漨水从山中流出，向西注入泑水，随后水文列出芘石、文石。机木似榆、可烧以粪稻田等说明来自郭注；華草与两种石物不强定现代种类。此处泑水按北山上下文建档，不与西山同名水域自动合并。'
EN_DESCRIPTION = 'Danhu opens the Northern Mountains. Ji trees and flowering herbs are abundant. The Feng rises here and flows west into the You; pi stones and patterned stones follow in the water account. The elm comparison and agricultural use of ji come from Guo Pu’s commentary. No modern species or locality is assigned, and the You is kept separate from its Western namesake.'
EN_QUOTE = 'The Northern Mountains begin with Mount Danhu, where ji trees are abundant. Flowering herbs grow on its heights. The Feng River rises here and flows west into the You River; pi stones and patterned stones are abundant in this water account.'
NOTE = 'source-03-0002—0004全见影印76页，0001为篇题与郭氏传元信息，0005起求如山另段。机木郭注“音”与下一行“飢”连读；“音逢”只释漨水。芘字照底本保留，不擅改成芭或砒；“其中”承接水文，不强定两类石物只在漨水或泑水。正文、捕获快照和郭注分存，不宣称多版本逐字校勘。'
EN_NOTE = 'Units 2–4 are on scan 76. Unit 1 is heading metadata; unit 5 begins Qiuru. The pronunciation note for ji continues across the captured line break, while the Feng pronunciation belongs to the river. The edition’s pi character is retained. The stones belong to the water account without assigning them exclusively to either river. Text, captured transcription and commentary remain separate, without claiming a critical edition.'

ENTITIES = [
    ('plant-beishan-ji-danhu', 'plant', '机木', 'Ji trees (Danhu)', '多机木',
     '單狐山多机木。郭注比作榆木，记可烧以粪稻田、出蜀中，并注音飢；这些均为注文，不据此认定现代树种或产地坐标。',
     'Ji trees are abundant at Danhu. Guo Pu compares them to elm, records burning them to manure rice fields and an origin in Shu, and supplies a pronunciation gloss. These are commentary, not a modern botanical identification or coordinate.',
     'Ji trees are abundant.', '机木似榆可燒以糞稲田出蜀中音飢',
     'Guo Pu: ji resembles elm, can be burned to manure rice fields, and comes from Shu; its name is glossed with the pronunciation ji.'),
    ('plant-beishan-huacao-danhu', 'plant', '華草（單狐）', 'Flowering herbs (Danhu)', '其上多華草',
     '單狐山上多華草。经文没有展开花色、叶形、果实或功效，保留为本山草类记述，不补造专名物种。',
     'Flowering herbs are recorded on Danhu’s heights. The text gives no flower color, leaf shape, fruit or special use; this remains a local plant account without an invented species.',
     'Flowering herbs are abundant on its heights.', '', ''),
    ('water-beishan-feng-danhu', 'water', '漨水（單狐）', 'Feng River (Danhu)', '漨水出焉而西流注于泑水',
     '漨水出于單狐山，向西流入泑水。漨的音逢来自郭注；只保留篇内流向，不画出现代河道、汇流点或实测距离。',
     'The Feng rises at Danhu and flows west into the You. Its pronunciation follows Guo Pu’s gloss. The textual direction supplies no modern river course, confluence or measured distance.',
     'The Feng River rises here and flows west into the You River.', '音逢',
     'Guo Pu supplies the pronunciation feng.'),
    ('water-beishan-you-danhu', 'water', '泑水（北山经）', 'You River (Northern Mountains)', '西流注于泑水',
     '泑水在單狐段承接向西流来的漨水。本段未交代其源头或后续去向；与西山泑水、泑澤分别保存，不凭同名认定同一水系。',
     'The You receives the west-flowing Feng in the Danhu passage. Its source and onward course are unstated here. It remains separate from the Western You River and You Marsh rather than being merged by name.',
     'It flows west into the You River.', '', ''),
    ('material-beishan-pishi-danhu', 'material', '芘石（單狐水文）', 'Pi stones (Danhu water account)', '其中多芘石文石',
     '單狐段漨水注泑水的水文后列芘石、文石，芘石单独建卡。“芘”保留底本字形；没有矿物成分或功效说明，不强释为现代矿种。',
     'Pi stones and patterned stones follow the Feng-to-You water account; pi stones have a separate record. The edition’s character is retained, without an asserted mineral composition or special use.',
     'Pi stones and patterned stones are abundant in this water account.', '', ''),
    ('material-beishan-wenshi-danhu', 'material', '文石（單狐水文）', 'Patterned stones (Danhu water account)', '其中多芘石文石',
     '文石与芘石并列于單狐段水文，按本段上下文独立记录。不借其他山段的颜色、纹理或矿物解释补造本段形貌。',
     'Patterned stones occur alongside pi stones in Danhu’s water account. This record adds no colors, patterns or mineral identification borrowed from another mountain.',
     'Pi stones and patterned stones are abundant in this water account.', '', ''),
]


def read(path):
    return json.loads((ROOT / path).read_text(encoding='utf-8'))


def write(path, value):
    (ROOT / path).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def extend_qiuru(world, english, chapter, review, scans):
    batch, pid, place = 'beishan-qiuru', 'passage-beishan-qiuru', 'place-beishan-qiuru'
    lines = chapter['lines']
    refs = lines[4:10]
    raw = ''.join(l['text'] for l in refs)
    pages = [s['url'] for s in scans if s['page'] in [76, 77]]
    common = dict(source=SOURCE, source_chapter='《北山经》', source_book=3, region='北山经',
                  source_locator='卷第三 · 影印页 76、77', source_pages=pages, url=pages[0],
                  source_unit_ids=[f'source-03-{i:04}' for i in range(5, 11)], reveal_chapter='03',
                  content_batch=batch, review_status='facsimile_reviewed', artwork_pending=True,
                  direction='單狐向北二百五十里至求如，滑水向西注諸毗水；均为篇内方位，不作现代定位。',
                  editorial_note='正文、郭注与项目说明分列；食用与治病为古籍记述，不作为现实建议。')
    translation = dict(source=EN_SOURCE, source_chapter='Beishan Jing', region='Beishan Jing',
                       source_locator='Volume 3 · scan pages 76, 77',
                       direction='Qiuru lies 250 textual li north of Danhu; the Hua flows west into the Zhupi. These are textual directions, not modern locations.',
                       editorial_note='Text, commentary and editorial notes are separate; eating and healing claims are ancient accounts, not present-day advice.')
    desc = '單狐向北二百五十里为求如山，上多铜、下多玉，无草木。滑水出于此，向西流入諸毗之水；水中记滑魚与水馬。滑魚形如鱓而赤背，水馬形如马、文臂牛尾。郭注释臂为前脚，并引旧籍与汉代故事作比拟，不能据注文给它另加人臂或神异器官。'
    en_desc = 'Qiuru lies 250 li north of Danhu, with copper above and jade below but no vegetation. The Hua rises here and flows west into the Zhupi. Huayu resembles an eel with a red back; Shuima is horse-shaped, with patterned forelegs and an ox tail. The foreleg reading comes from Guo Pu, whose older quotations and Han account remain commentary rather than additional anatomy.'
    en_quote = 'Two hundred and fifty li north is Mount Qiuru, with copper above, jade below, and no grasses or trees. The Hua River rises here and flows west into the Zhupi. Huayu is eel-shaped with a red back and a sound compared to wu; eating it is said to relieve warts. Shuima is horse-shaped, with patterned forelegs and an ox tail; its sound resembles a call.'
    note = '0005—0009均见76页，0009牛尾及水马郭注捕获为77页，按影印校回76；0010其音如呼及注见77页，0011帶山另段。0008音吾子之吾回释前句梧，不归水馬；疣贅也释滑魚食用句。諸毗山只在郭注出现，单独作注文地点，不与西山同名山合并。周禮马黑脊等引文为比拟，不追加本段黑背特征；水马注录文省字或异写保留，非逐字校勘定本。'
    en_note = 'Units 5–9 are on scan 76; unit 9 was captured as 77 and is corrected only in the reading page index. Unit 10 continues the call on 77; unit 11 begins Dai. The wu pronunciation in unit 8 belongs to the preceding fish sound, and the wart gloss to its eating claim. Mount Zhupi appears only in commentary and remains separate from its Western namesake. The Zhouli black-spine comparison does not add a black back to Shuima; incomplete or variant captured commentary is retained without claiming a critical edition.'
    passage = {**common, 'id': pid, 'kind': 'passage', 'name': '求如之山', 'range': 1, 'order': 2,
               'description': desc, 'quote': raw, 'captured_text': raw,
               'captured_commentary': [{'source_unit_id': f'source-03-{i+5:04}', 'annotations': l['annotations']} for i,l in enumerate(refs)],
               'commentary_quote': '\n'.join(f'〔影印页{77 if i == 5 else 76}〕' + '；'.join(l['annotations']) for i,l in enumerate(refs) if l['annotations']),
               'content_note': note, 'subjects': ['求如之山', '铜', '玉', '滑水', '諸毗之水', '諸毗山', '滑魚', '水馬'],
               'source_span': [sum(len(l['text']) for l in lines[:4]), sum(len(l['text']) for l in lines[:10])],
               'related_entry_ids': []}
    english[pid] = {**translation, 'name': 'Mount Qiuru', 'description': en_desc, 'quote': en_quote, 'content_note': en_note,
                    'commentary_quote': 'Guo Pu says that the receiving river rises at Mount Zhupi; the eel resembles a snake; wu resembles the sound of people resisting one another, with a pronunciation gloss. Warts are glossed separately. For Shuima, bi means forelegs; the commentary quotes older horse wording and a Han-era account. Its call is compared to a human shout.'}
    specs = [
        (place, 'place', '求如之山', 'Mount Qiuru', raw, desc, en_desc, en_quote, '', ''),
        ('material-beishan-copper-qiuru', 'material', '铜（求如）', 'Copper (Qiuru)', '其上多銅', '求如山上多铜；只保留经文所记位置，不推定现代矿床、冶炼技术或年代。', 'Copper is abundant above on Qiuru; no modern deposit, smelting technology or date is inferred.', 'Copper is abundant above.', '', ''),
        ('material-beishan-jade-qiuru', 'material', '玉（求如）', 'Jade (Qiuru)', '其下多玉', '求如山下多玉，正文没有细分颜色、品种或功效。', 'Jade is abundant below Qiuru; the text gives no color, specific type or special use.', 'Jade is abundant below.', '', ''),
        ('water-beishan-hua-qiuru', 'water', '滑水（求如）', 'Hua River (Qiuru)', '滑水出焉而西流注于諸毗之水', '滑水出于求如山，向西注入諸毗之水；滑魚、水馬均见其后水文，流向不换算现代河道。', 'The Hua rises at Qiuru and flows west into the Zhupi. Huayu and Shuima follow in its water account; no modern river course is reconstructed.', 'The Hua rises here and flows west into the Zhupi River.', '', ''),
        ('water-beishan-zhupi-qiuru', 'water', '諸毗之水（北山经）', 'Zhupi River (Northern Mountains)', '西流注于諸毗之水', '諸毗之水承接西流的滑水。郭注另说水出諸毗山；不据同名合并西山諸毗山，也不臆定现代汇流点。', 'The Zhupi receives the west-flowing Hua. Guo Pu says that this water rises at Mount Zhupi. It is not merged with the Western namesake mountain or assigned a modern confluence.', 'It flows west into the Zhupi River.', '水出諸毗山也', 'Guo Pu: the water rises at Mount Zhupi.'),
        ('place-beishan-zhupi-qiuru', 'place', '諸毗山（北山郭注）', 'Mount Zhupi (Northern commentary)', '滑水出焉而西流注于諸毗之水', '諸毗山见于本段郭注水出諸毗山也，是对承接水域的来源说明，不是求如之后的新主线山段。与西山同名山分开，不借西山居民或形貌。', 'Mount Zhupi occurs in Guo Pu’s explanation of the receiving water’s source. It is not a new route stage after Qiuru and is kept separate from the Western namesake and its residents.', 'The Hua rises here and flows west into the Zhupi River.', '水出諸毗山也', 'Guo Pu: the water rises at Mount Zhupi.'),
        ('beast-beishan-huayu-qiuru', 'beast', '滑魚（求如）', 'Huayu (Qiuru)', '其中多滑魚其状如鱓赤背其音如梧食之已疣', '求如水文中的滑魚形如鱓、背赤，声音比作梧，食用治疣为古籍说法。郭注释鱓似蛇，声音如人相枝梧，并另注梧音；不借西山同名滑魚的蛇状四足。', 'Huayu in Qiuru’s water account is eel-shaped with a red back. Its sound is compared to wu, and its eating claim concerns warts. Guo Pu compares the eel to a snake and the sound to people resisting one another; no four feet are borrowed from the Western namesake.', 'Huayu is abundant in the water, eel-shaped with a red back. Its sound is compared to wu; eating it is said to relieve warts.', '鱓魚似蛇音善；如人相枝梧聲；音吾子之吾；疣贅也', 'Guo Pu compares the eel to a snake, glosses its pronunciation, compares the sound to people resisting one another, supplies the wu pronunciation, and explains warts separately.'),
        ('beast-beishan-shuima-qiuru', 'beast', '水馬（求如）', 'Shuima (Qiuru)', '其中多水馬其状如馬文臂牛尾其音如呼', '求如水文中的水馬形如马，文臂、牛尾，声音如呼。郭注释臂为前脚，故配图将文饰集中前腿；引周禮及汉代渥洼水故事另列，不增加黑背、人臂、鱼尾或角。', 'Shuima is horse-shaped, with patterned forelegs, an ox tail and a call-like sound. Guo Pu explains bi as forelegs, guiding the illustration’s front-leg markings. The Zhouli quotation and Han-era Wowa account remain commentary; no black back, human arms, fish tail or horns are added.', 'Shuima is abundant in the water, horse-shaped with patterned forelegs and an ox tail. Its sound resembles a call.', refs[4]['annotations'][0]+'；如人呌呼', 'Guo Pu explains bi as forelegs, quotes older horse wording and a Han-era account associated with Wowa, and compares the sound to a human shout.'),
    ]
    cards = []
    jobs = {a['entry_id']: a for a in read('frontend/artwork-source/beishan/generation.json')['assets']}
    for id, kind, name, en_name, excerpt, description, en_description, eq, cq, ecq in specs:
        assert excerpt in raw, id
        c = {**common, 'id': id, 'kind': kind, 'name': name, 'quote': excerpt, 'description': description,
             'commentary_quote': cq, 'source_passage_ids': [pid], 'related_entry_ids': [pid]}
        english[id] = {**translation, 'name': en_name, 'description': en_description, 'quote': eq, 'commentary_quote': ecq}
        if id != place:
            c['context_place_id'] = place
        if kind in {'water','beast'} or id == 'place-beishan-zhupi-qiuru':
            c['relation_scope'] = 'water'
        if id == place:
            c.update(content_note=note, commentary_quote=passage['commentary_quote'])
            english[id].update(content_note=en_note, commentary_quote=english[pid]['commentary_quote'])
        if id in jobs and jobs[id]['status'] == 'reviewed':
            c.update(artwork='beishan/'+jobs[id]['name']+'-v1.webp', artwork_pending=False,
                     artwork_caption='经文形貌与木刻演绎 · 刻纹、配色和姿态为艺术解释；水馬前脚释义来自郭注。' if 'shuima' in id else '经文赤背鱓状与木刻演绎 · 刻纹、配色和姿态为艺术解释，不借西山四足。')
            english[id]['artwork_caption'] = 'Textual form in woodcut interpretation; patterns, colors and pose are artistic. Shuima’s foreleg reading follows commentary.' if 'shuima' in id else 'The red-backed eel-like form in woodcut interpretation; patterns and pose are artistic, without the Western namesake’s four feet.'
        cards.append(c)
    passage['related_entry_ids'] = [c['id'] for c in cards]
    ids = {c['id']: c for c in cards}
    for a,b in [('water-beishan-hua-qiuru','water-beishan-zhupi-qiuru'),('water-beishan-zhupi-qiuru','place-beishan-zhupi-qiuru'),('water-beishan-hua-qiuru','beast-beishan-huayu-qiuru'),('water-beishan-hua-qiuru','beast-beishan-shuima-qiuru')]:
        ids[a]['related_entry_ids'].append(b); ids[b]['related_entry_ids'].append(a)
    for group, additions in [('passages',[passage]), ('text_entities',[c for c in cards if c['kind']=='place']), ('natural_features',[c for c in cards if c['kind'] in {'water','material'}]), ('beasts',[c for c in cards if c['kind']=='beast'])]:
        world[group] = [r for r in world[group] if r.get('content_batch') != batch] + additions
    previous = next(p for p in world['passages'] if p['id'] == PASSAGE)
    previous['related_entry_ids'] += [pid]
    passage['related_entry_ids'].append(PASSAGE)
    world['revision'] = 'myth-world-2026-10-24-beishan-qiuru-v1'
    review.update(scope='北山经單狐、求如：2阅读段、15独立卡；其余仅录文结构盘点待逐页校核。', scan_pages=[76,77],
                  source_unit_page_corrections={'source-03-0009':76})
    review['entry_ids'] += [c['id'] for c in cards]
    review['passages'].append({'id':pid,'source_unit_ids':passage['source_unit_ids'],'source_span':passage['source_span'],'status':'facsimile_reviewed'})
    review['commentary_alignment'].append({'source_unit_ids':['source-03-0007','source-03-0008','source-03-0009','source-03-0010'], 'basis':note})
    review['limits'] = '單狐與求如已对照76—77页，经文、捕获层、逐行郭注与整理说明分存；不宣称北山全篇或多版本逐字校勘完成。求如两幅生物图已审，非生物均留空。'
    review['next'] = {'name':'帶山','source_units':[11,16],'captured_pages':[77], 'status':'pending_facsimile_review', 'notes':'复用77页；䑏䟽马状一角有错、北山鵸䳜乌状五彩赤文与西山三首六尾分开，儵魚如鸡赤毛三尾六足四首；0017譙明另段，0018的实际页界待核。'}


def build():
    chapter = read('data/shanhaijing-reference.json')['chapters'][2]
    lines = chapter['lines']
    world = read('frontend/public/data/myth-world.json')
    english = read('frontend/src/locale-content-en.json')
    scans = read('data/reference-scans/beishan/sources.json')
    for scan in scans:
        assert hashlib.sha256((ROOT / scan['local_path']).read_bytes()).hexdigest() == scan['sha256']
    refs = lines[1:4]
    quote = ''.join(line['text'] for line in refs)
    assert quote == '北山經之首曰單狐之山多机木其上多華草漨水出焉而西流注于泑水其中多芘石文石'
    common = dict(source=SOURCE, source_chapter='《北山经》', source_book=3, region='北山经',
                  source_locator='卷第三 · 影印页 76', source_pages=[scans[0]['url']], url=scans[0]['url'],
                  source_unit_ids=[f'source-03-{i:04}' for i in range(2, 5)], reveal_chapter='03',
                  content_batch=BATCH, review_status='facsimile_reviewed', artwork_pending=True,
                  direction='按《北山经》篇内次序与原文方位阅读；不换算现代坐标或实测里程。',
                  editorial_note='经文据影印核对，保留底本字形与未标点形式；白话和英文为项目整理，郭注分列。')
    en_common = dict(source=EN_SOURCE, source_chapter='Beishan Jing', region='Beishan Jing',
                     source_locator='Volume 3 · scan page 76',
                     direction='Read the textual sequence and directions; these are not modern coordinates or measured distances.',
                     editorial_note='The Chinese was compared with the facsimile; edition characters and unpunctuated form are retained. Explanations and English are editorial; commentary is separate.')
    commentary = '机木似榆可燒以糞稲田出蜀中音飢；漨水：音逢'
    en_commentary = 'Guo Pu compares ji to elm, records burning it to manure rice fields and an origin in Shu, and glosses its pronunciation ji. The river name is glossed feng.'
    cards = [{**common, 'id': PLACE, 'kind': 'place', 'name': '單狐之山', 'description': DESCRIPTION,
              'quote': quote, 'commentary_quote': commentary, 'source_passage_ids': [PASSAGE],
              'content_note': NOTE, 'related_entry_ids': [PASSAGE]}]
    english[PLACE] = {**en_common, 'name': 'Mount Danhu', 'description': EN_DESCRIPTION,
                      'quote': EN_QUOTE, 'commentary_quote': en_commentary, 'content_note': EN_NOTE}
    for id, kind, name, en_name, excerpt, desc, en_desc, en_quote, note, en_note in ENTITIES:
        assert excerpt in quote
        card = {**common, 'id': id, 'kind': kind, 'name': name, 'description': desc, 'quote': excerpt,
                'commentary_quote': note, 'source_passage_ids': [PASSAGE], 'context_place_id': PLACE,
                'related_entry_ids': [PASSAGE]}
        if kind in {'water', 'material'}:
            card['relation_scope'] = 'water'
        cards.append(card)
        english[id] = {**en_common, 'name': en_name, 'description': en_desc,
                       'quote': en_quote, 'commentary_quote': en_note}
    feng, you, pi, wen = [next(c for c in cards if c['id'] == id) for id in
                         ['water-beishan-feng-danhu', 'water-beishan-you-danhu',
                          'material-beishan-pishi-danhu', 'material-beishan-wenshi-danhu']]
    feng['related_entry_ids'].append(you['id'])
    you['related_entry_ids'].append(feng['id'])
    for stone in [pi, wen]:
        stone['related_entry_ids'] += [feng['id'], you['id']]
    passage = {**common, 'id': PASSAGE, 'kind': 'passage', 'name': '單狐之山', 'range': 1, 'order': 1,
               'description': DESCRIPTION, 'quote': quote, 'captured_text': quote,
               'captured_commentary': [{'source_unit_id': f'source-03-{i+2:04}', 'annotations': line['annotations']} for i, line in enumerate(refs)],
               'commentary_quote': '\n'.join('〔影印页76〕' + '；'.join(line['annotations']) for line in refs if line['annotations']), 'content_note': NOTE,
               'source_span': [len(lines[0]['text']), sum(len(l['text']) for l in lines[:4])],
               'subjects': ['單狐之山', '单狐之山', '机木', '華草', '漨水', '泑水', '芘石', '文石'],
               'related_entry_ids': [c['id'] for c in cards]}
    english[PASSAGE] = {**english[PLACE]}
    for group, additions in [('passages', [passage]), ('text_entities', [cards[0]]), ('natural_features', cards[1:])]:
        world[group] = [r for r in world[group] if r.get('content_batch') != BATCH] + additions
    world['revision'] = 'myth-world-2026-10-24-beishan-danhu-v1'
    review = {
        'scope': '北山经首山單狐：1阅读段、7独立卡；全篇仅盘点录文结构，其他段落尚未逐页校核。',
        'snapshot_sha256': hashlib.sha256((ROOT / 'data/shanhaijing-reference.json').read_bytes()).hexdigest(),
        'revision_url': chapter['revision_url'], 'scan_pages': [76], 'heading_unit_ids': ['source-03-0001'],
        'source_unit_page_corrections': {}, 'entry_ids': [c['id'] for c in cards],
        'passages': [{'id': PASSAGE, 'source_unit_ids': passage['source_unit_ids'], 'source_span': passage['source_span'], 'status': 'facsimile_reviewed'}],
        'commentary_alignment': [{'source_unit_ids': ['source-03-0002', 'source-03-0003'],
                                 'reading': '机木似榆可燒以糞稲田出蜀中音飢', 'basis': '76页机木双行小注的音与飢连读；音逢另属漨水，捕获快照不改。'}],
        'structure_inventory': {
            'status': 'transcription_only_pending_facsimile_review', 'source_blocks': len(lines),
            'captured_pages': [76, 108], 'structural_candidates': 90,
            'ranges': [
                {'range': 1, 'source_units': [2, 99], 'summary_units': [96, 99], 'reported_mountains': 25, 'reported_li': 5490},
                {'range': 2, 'source_units': [100, 150], 'summary_units': [147, 150], 'reported_mountains': 17, 'reported_li': 5690},
                {'range': 3, 'source_units': [151, 296], 'summary_units': [290, 296], 'reported_mountains': 46, 'reported_li': 12350}],
            'closing_total_unit': 297, 'reported_total_mountains': 87, 'reported_total_li': 23230,
            'limits': '以上段界与数字仅据本地录文定位，未核全篇影印；列数25+17+46=88与篇末87、里程5490+5690+12350=23530与篇末23230暂存差异，后续须逐页复核，不改原数字。90结构候选不是最终山数或阅读段数。',
            'candidate_boundary_risks': [
                {'source_units': [96, 102], 'note': '候选重复切分首列总括，并把管涔首山并入；应分别核96—99及100—102。'},
                {'source_units': [147, 155], 'note': '候选重复切分次二总括，并把太行/歸山并入；应分别核147—150及151—155。'},
                {'source_units': [270, 274], 'note': '燕山与山行水行至饒山未分；须逐页核270—271及272—274。'},
                {'source_units': [280, 286], 'note': '碣石、鴈門、泰澤中帝都被同候选合并；须分别核280—282、283—284、285—286。'},
                {'source_units': [290, 297], 'note': '次三总括与篇末总计被重复切分；须核290—296及297。'}]},
        'stable_existing_ids': ['03-04', 'beast-jingwei', 'beast-zhu-jian', 'place-fajiu', 'place-north-ranges'],
        'title_font_supplement': {
            'family': 'Noto Serif SC', 'characters': '單机華漨求䑏䟽何儵孟寓帶彭栢椐橐虢譙駝鰼䑕幽張杠極樗熏聮葵蔓薤訾雘韭鴳鵁鵺䐆㗸侯匠柘潘磁竦薨那韓題鮭鳲䰽䲃刚夕懐枳渾瀤獄窫鮨鴈埋牲狕珪瘗隄鮮䧑䳑勝岐晉爾縣蒼酸閭雍鮪卭狂狍獨鉤頭餘㶌䮝䱇䴅丸乾决姑屋教暨梁歸洹澠璧發聞胡賁領飛鶋鶌糈树脩䃤京椒秦與薄藇藷販囷戾歐沁沮泰洳滏漳濝蚤蟲衛謁錫鴣䵸栒泜洧溹繡芍藥鱯黽䍶戱敞歷液漊礨維䬅倫千師戎滋燕獂碣稌繩般茝萬載逢邻錞饒鶹', 'weights': [400, 700],
            'path': 'frontend/public/fonts/shanhai-title-beishan.woff2',
            'source_url': 'https://fonts.googleapis.com/css2?family=Noto+Serif+SC%3Awght%40400..700&text=%E5%96%AE%E6%9C%BA%E8%8F%AF%E6%BC%A8%E6%B1%82%E4%91%8F%E4%9F%BD%E4%BD%95%E5%84%B5%E5%AD%9F%E5%AF%93%E5%B8%B6%E5%BD%AD%E6%A0%A2%E6%A4%90%E6%A9%90%E8%99%A2%E8%AD%99%E9%A7%9D%E9%B0%BC%E4%91%95%E5%B9%BD%E5%BC%B5%E6%9D%A0%E6%A5%B5%E6%A8%97%E7%86%8F%E8%81%AE%E8%91%B5%E8%94%93%E8%96%A4%E8%A8%BE%E9%9B%98%E9%9F%AD%E9%B4%B3%E9%B5%81%E9%B5%BA%E4%90%86%E3%97%B8%E4%BE%AF%E5%8C%A0%E6%9F%98%E6%BD%98%E7%A3%81%E7%AB%A6%E8%96%A8%E9%82%A3%E9%9F%93%E9%A1%8C%E9%AE%AD%E9%B3%B2%E4%B0%BD%E4%B2%83%E5%88%9A%E5%A4%95%E6%87%90%E6%9E%B3%E6%B8%BE%E7%80%A4%E7%8D%84%E7%AA%AB%E9%AE%A8%E9%B4%88%E5%9F%8B%E7%89%B2%E7%8B%95%E7%8F%AA%E7%98%97%E9%9A%84%E9%AE%AE%E4%A7%91%E4%B3%91%E5%8B%9D%E5%B2%90%E6%99%89%E7%88%BE%E7%B8%A3%E8%92%BC%E9%85%B8%E9%96%AD%E9%9B%8D%E9%AE%AA%E5%8D%AD%E7%8B%82%E7%8B%8D%E7%8D%A8%E9%89%A4%E9%A0%AD%E9%A4%98%E3%B6%8C%E4%AE%9D%E4%B1%87%E4%B4%85%E4%B8%B8%E4%B9%BE%E5%86%B3%E5%A7%91%E5%B1%8B%E6%95%99%E6%9A%A8%E6%A2%81%E6%AD%B8%E6%B4%B9%E6%BE%A0%E7%92%A7%E7%99%BC%E8%81%9E%E8%83%A1%E8%B3%81%E9%A0%98%E9%A3%9B%E9%B6%8B%E9%B6%8C%E7%B3%88%E6%A0%91%E8%84%A9%E4%83%A4%E4%BA%AC%E6%A4%92%E7%A7%A6%E8%88%87%E8%96%84%E8%97%87%E8%97%B7%E8%B2%A9%E5%9B%B7%E6%88%BE%E6%AD%90%E6%B2%81%E6%B2%AE%E6%B3%B0%E6%B4%B3%E6%BB%8F%E6%BC%B3%E6%BF%9D%E8%9A%A4%E8%9F%B2%E8%A1%9B%E8%AC%81%E9%8C%AB%E9%B4%A3%E4%B5%B8%E6%A0%92%E6%B3%9C%E6%B4%A7%E6%BA%B9%E7%B9%A1%E8%8A%8D%E8%97%A5%E9%B1%AF%E9%BB%BD%E4%8D%B6%E6%88%B1%E6%95%9E%E6%AD%B7%E6%B6%B2%E6%BC%8A%E7%A4%A8%E7%B6%AD%E4%AC%85%E5%80%AB%E5%8D%83%E5%B8%AB%E6%88%8E%E6%BB%8B%E7%87%95%E7%8D%82%E7%A2%A3%E7%A8%8C%E7%B9%A9%E8%88%AC%E8%8C%9D%E8%90%AC%E8%BC%89%E9%80%A2%E9%82%BB%E9%8C%9E%E9%A5%92%E9%B6%B9&display=swap',
            'sha256': 'a11eaffdb07c0468882bb3e46a1d641c147b9b9e8ac94b28883d2aed0de2de7d',
            'license': 'frontend/public/fonts/noto-serif-sc-LICENSE.txt',
            'rebuild': 'python frontend/scripts/fonts/supplement-title-font.py',
            'limits': '179字小子集随站点发布，不在运行时请求Google；原标题与罕字字库不改，既有30字本机依赖累计补6，另有24字限制，见独立ExtB子集记录。'},
        'limits': NOTE + '本批没有生物插画任务，7卡及阅读段均无图；不把西山同名水域或其他山的植物图用于本段。',
        'next': {'name': '求如之山', 'source_units': [5, 10], 'captured_pages': [76, 77],
                 'status': 'pending_facsimile_review', 'notes': '复用76页，首次核存77页；0009牛尾及水马注的实际页界须核。北山滑魚如鱓赤背，不借西山滑魚蛇状四足；水馬文臂牛尾与郭注前脚释义分开。'}}
    extend_qiuru(world, english, chapter, review, scans)
    extend_first_range(world, english, chapter, review)
    write('frontend/public/data/myth-world.json', world)
    write('frontend/src/locale-content-en.json', english)
    write('data/beishan-edition-review.json', review)
    print('Built the complete Northern reading: 92 passages, 507 cards; original numerical differences retained')


if __name__ == '__main__':
    build()
