"""Merge the reviewed Central passages, preserving all other books."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path):
    return json.loads((ROOT / path).read_text(encoding='utf-8'))


def write(path, value):
    (ROOT / path).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


ROWS = [
    dict(slug='r01-gancao', en_name='Mount Ganzao',
         description='中山经薄山首甘棗，共水西注河，上多杻木。蘀草葵本杏叶、黄华荚实；或作楛叶为异说。㔮如𤠢鼠而文题，郭注明言参照鼠形未詳，故留形貌占位，不据鼠字强定现代物种，也不把或作熊画成熊。医食功效均为古述。',
         en_quote='The Central account begins with Mount Ganzao in the Bo range. Gong water rises here and flows west into the He. Niu trees are abundant above. Tuo has a mallow-like base, apricot-like leaves, yellow flowers and podded fruit, and is said to relieve dim sight. Nuo resembles a named shu with a patterned forehead and is said to relieve swellings when eaten.',
         en_description='Ganzao opens the Bo range. Gong water flows west into the He. Tuo plant anatomy and ancient eating claims remain separate from the Nuo account. Guo Pu says the compared shu form is unknown, so Nuo retains a placeholder, without a modern rodent identification or a bear inferred from a variant character.',
         en_note='Units 2–6 are on scan 2. The chapter heading is metadata. Commentary gives an alternative leaf comparison and states uncertainty about the rodent comparison; ancient healing claims are not medical guidance.'),
    dict(slug='r01-lier', en_name='Mount Li-er',
         description='甘棗向东二十里为歴兒，上多橿与櫔木。方茎圆叶、黄华而毛、实如揀属于櫔木，不移给仅列名的橿。揀为果实比拟且郭注称木名，单列参照卡，不作为本山实生植物。揀木注文跨8—9连读，服之不忘为古述。',
         en_quote='Twenty li east is Mount Li-er, with many Jiang and Li trees above. The latter has square stems and round leaves, yellow flowers and hairiness; its fruit resembles jian, and taking it is said to prevent forgetfulness.',
         en_description='Li-er lies twenty li east of Ganzao. The square stems, round leaves, yellow flowers, hairiness and jian-like fruit describe Li, not the separately named Jiang tree. Jian is recorded as a comparison rather than an assertion that it grows here. Its commentary continues across units 8–9.',
         en_note='Units 7–9 are all on scan 2; unit 9 was captured as scan 3. The jian-tree gloss continues into unit 9 and does not belong to Quzhu. The memory claim is ancient.'),
    dict(slug='r01-quzhu', en_name='Mount Quzhu',
         description='歴兒向东十五里为渠豬，上多竹。渠豬水南注河，与甘棗共水西注河分别保留方向及出处，仅共享河的文本名目。豪鱼如鮪，郭注鮪似鱣；赤喙尾赤羽原词保留，图中红喙红羽尾是明确艺术解释，不把羽字擅定成对鸟翼。已白癣为古述。',
         en_quote='Fifteen li east is Mount Quzhu, with much bamboo above. Quzhu water rises here and flows south into the He. Hao fish resemble wei, with red beak/tail and red yu, and are said to relieve white skin lesions.',
         en_description='Quzhu lies fifteen li east of Li-er. Its water flows south into the He, separately from Gong water’s westward account. Guo Pu compares wei with zhan. The unpunctuated red-beak/tail/red-yu wording is retained; a red snout and red feather-like tail are an artistic interpretation, without paired bird wings or a modern species claim.',
         en_note='Units 10–12 are on scan 3. The fish comparison comes from commentary. Feather construction, body details, colors outside the stated red parts and pose are artistic; the eating claim is ancient.')
]


def E(slug, kind, key, name, en_name, quote, description, en_quote, en_description, **extra):
    return dict(slug=slug, kind=kind, id=f'{kind}-zhongshan-{key}', name=name, en_name=en_name, quote=quote, description=description, en_quote=en_quote, en_description=en_description, **extra)


ENTITIES = [
    E('r01-gancao', 'water', 'gong-gancao', '共水（甘棗）', 'Gong water (Ganzao)', '共水出焉而西流注于河', '共水从甘棗出，西注河；音恭属于水名，不按现代河道定位。', 'Gong water rises here and flows west into the He.', 'The westward source account and pronunciation remain textual, without a modern river identification.', commentary='音恭', en_commentary='Guo Pu compares the pronunciation with gong.'),
    E('r01-gancao', 'water', 'he', '河（中山首列文本索引）', 'He (Central first-range textual index)', '西流注于河', '河为甘棗共水西注与渠豬水南注的受水体文本名目，各段方向分别保留，不据此认定现代水系。', 'Gong water flows west into the He.', 'This recipient index preserves the separate Gong westward and Quzhu southward accounts, without a modern geographic merger.'),
    E('r01-gancao', 'plant', 'niu-gancao', '杻木（甘棗）', 'Niu trees (Ganzao)', '其上多杻木', '仅记山上多杻木，未载独立形貌，不借蘀草或櫔木的叶花特征。', 'Niu trees are abundant above.', 'Only the product name is given, without anatomy borrowed from Tuo or Li.'),
    E('r01-gancao', 'plant', 'tuo-gancao', '蘀（甘棗）', 'Tuo (Ganzao)', '其下有草焉葵本而杏葉黄華而莢實名曰蘀可以已瞢', '蘀草葵本、杏叶、黄华荚实；或作楛叶为郭注异说，不将两种比拟叶同时叠画。已瞢为古述，不作现代药效或种属认定。', 'Tuo has a mallow-like base, apricot-like leaves, yellow flowers and podded fruit, and is said to relieve dim sight.', 'The plant form follows the main text. The alternative leaf comparison is commentary, and the ancient claim does not identify a modern medicinal species.', commentary='或作楛葉；他落反；音盲', en_commentary='Guo Pu records hu-like leaves as a variant and supplies pronunciation glosses for the name and the ancient ailment.'),
    E('r01-gancao', 'beast', 'nuo-gancao', '㔮（甘棗）', 'Nuo (Ganzao)', '有獸焉其狀如𤠢鼠而文題其名曰㔮食之已癭', '㔮如𤠢鼠而文题；郭注明言参照鼠形未詳。保留文本与音注、暂用占位，不编成现代鼠种或把异字熊当熊形；食疗为古述。', 'Nuo resembles a named shu with a patterned forehead and is said to relieve swellings when eaten.', 'The compared shu form is explicitly unknown in commentary. The placeholder avoids inventing a modern rodent or a bear from an alternative character; the eating claim is ancient.', commentary='𤠢䑕所未詳音虺字亦或作虺；音那或作熊也', en_commentary='Guo Pu states that the compared shu is unknown and supplies hui comparisons for its character. Separately, the name has a na pronunciation gloss and xiong as a variant character.', unknown=True),
    E('r01-lier', 'plant', 'jiang-lier', '橿（歴兒）', 'Jiang trees (Li-er)', '其上多橿', '橿仅列名，方茎圆叶黄花等后文属于櫔木，不移给本卡。', 'Jiang trees are abundant above.', 'Jiang is only named; the following Li-tree anatomy is not transferred to this card.'),
    E('r01-lier', 'plant', 'li-lier', '櫔木（歴兒）', 'Li trees (Li-er)', '多櫔木是木也方莖而員葉黄華而毛其實如揀服之不忘', '櫔木方茎圆叶、黄华而毛、实如揀；具体毛生部位不超出原词强定。揀的白粘果注属于比拟树名，不反填櫔的果色；服之不忘为古述。', 'Li has square stems and round leaves, yellow flowers and hairiness; its fruit resembles jian, and taking it is said to prevent forgetfulness.', 'The main-text anatomy remains distinct from the jian comparison gloss, without inferring Li fruit color or modern pharmacology.', commentary='音厲', en_commentary='Guo Pu gives li pronunciation.'),
    E('r01-lier', 'plant', 'jian-comparison-lier', '揀（櫔实比拟）', 'Jian (Li fruit comparison)', '其實如揀', '揀是櫔果实的比拟对象，郭注称木名，子如指头、白粘、可浣衣；不把本卡列成本山实生木。音練及或作簡跨8—9连读。', 'Its fruit resembles jian.', 'Jian is a comparison object, not an assertion that this tree grows at Li-er. Commentary describes finger-sized white sticky fruit used for washing; the gloss continues across units 8–9.', commentary='揀木名子如指頭白而粘可以；浣衣也音練或作簡', en_commentary='Guo Pu identifies a tree with finger-sized white sticky fruit used for washing, gives lian pronunciation and records jian as a variant spelling.', comparison_only=True),
    E('r01-quzhu', 'plant', 'bamboo-quzhu', '竹（渠豬）', 'Bamboo (Quzhu)', '其上多竹', '渠豬山上多竹，仅记古物产名，不确定现代竹种。', 'Bamboo is abundant above.', 'The textual product term does not identify a modern bamboo species.'),
    E('r01-quzhu', 'water', 'quzhu', '渠豬之水', 'Quzhu water', '渠豬之水出焉而南流注于河', '渠豬水源出后南注河；不把山名与水名合卡，方向与共水西注河分别存录。', 'Quzhu water rises here and flows south into the He.', 'Mountain and water names remain distinct; this southward account stays separate from Gong water’s westward flow.'),
    E('r01-quzhu', 'beast', 'hao-quzhu', '豪魚（渠豬）', 'Hao fish (Quzhu)', '其中是多豪魚狀如鮪赤喙尾赤羽可以已白癬', '豪鱼如鮪，郭注鮪似鱣。赤喙尾赤羽无现代句读，图中红喙及红羽状尾作明确演绎，不断言羽必指成对飞翼；细长鱼体、鳞鳍细节、羽尾构造、其余体色与姿态均为艺术解释，不强定现代鲟鱼种。食疗为古述。', 'Hao fish resemble wei, with red beak/tail and red yu, and are said to relieve white skin lesions.', 'Guo Pu compares wei with zhan. The red snout and red feather-like tail explicitly interpret the unpunctuated wording; elongated body proportions, scales/fins, tail-feather construction, other colors and pose are artistic. No paired bird wings or modern species identification are asserted.', commentary='鮪似鱣也', en_commentary='Guo Pu compares wei with zhan.', water=True)
]

from zhongshan_next30 import ROWS as NEXT_ROWS, entities as next_entities, LINKS as NEXT_LINKS, SHARES as NEXT_SHARES
ROWS += NEXT_ROWS
ENTITIES += next_entities(E)
from zhongshan_stages34_63 import ROWS as B2_ROWS, entities as b2_entities, LINKS as B2_LINKS, SHARES as B2_SHARES, OVERRIDES
ROWS += B2_ROWS
ENTITIES += b2_entities(E)
NEXT_LINKS += B2_LINKS
NEXT_SHARES += B2_SHARES


def build():
    review = read('data/zhongshan-edition-review.json')
    chapter = read('data/shanhaijing-reference.json')['chapters'][4]
    assert hashlib.sha256((ROOT / 'data/shanhaijing-reference.json').read_bytes()).hexdigest() == review['snapshot_sha256']
    world = read('frontend/public/data/myth-world.json')
    english = read('frontend/src/locale-content-en.json')
    jobs = {a['entry_id']: a for a in read('frontend/artwork-source/zhongshan/entities-generation.json')['assets']}
    passages, cards = [], []
    for order, row in enumerate(ROWS, 1):
        stage = next(s for s in review['stage_plan'] if s['slug'] == row['slug'])
        first, last = stage['source_units']; refs = chapter['lines'][first - 1:last]
        captured = ''.join(l['text'] for l in refs); raw = captured.replace('⟦缺字图:鬼⟧', '鬼').replace('⟦缺字图:冢⟧', '冢'); pid = 'passage-zhongshan-' + row['slug']; root_kind = 'place' if stage['kind'] == 'mountain' else 'rite'; place = root_kind + '-zhongshan-' + row['slug']
        pages = stage['facsimile_pages']; urls = [f'https://zh.wikisource.org/wiki/Page:Sibu_Congkan0466-郭璞-山海經-2-2.djvu/{p}' for p in pages]
        common = dict(source='《山海经·中山经》（《四部丛刊》景明成化本，郭璞传）', source_chapter='《中山经》', source_book=5, region='中山经', source_locator='卷第五 · 影印页' + '、'.join(map(str, pages)), source_pages=urls, url=urls[0], source_unit_ids=stage['source_unit_ids'], reveal_chapter='04', content_batch='zhongshan-' + row['slug'], review_status='facsimile_reviewed', artwork_pending=True, direction='按中山经篇内顺序与古述方位阅读，不换算现代坐标或实测里程。', editorial_note='正文、捕获与郭注分存；解释与英文为项目整理。食疗及灾异属古籍记述。')
        encommon = dict(source='Shanhaijing · Central Mountains (Sibu Congkan edition, Guo Pu commentary)', source_chapter='Zhongshan Jing', region='Zhongshan Jing', source_locator='Volume 5 · scan pages ' + ', '.join(map(str, pages)), direction='Read the Central textual sequence and ancient directions, not modern coordinates or measured distances.', editorial_note='Text, captured transcription and commentary remain separate. English and explanations are editorial; healing and omen claims are ancient.')
        commentary = '\n'.join('〔影印页' + str(review['source_unit_page_corrections'].get(id, int(l['page'].rsplit('/', 1)[-1]))) + '〕' + '；'.join(l['annotations']) for id, l in zip(stage['source_unit_ids'], refs) if l['annotations'])
        p = {**common, 'id': pid, 'kind': 'passage', 'name': stage['name'], 'range': stage['range'], 'order': order, 'description': row['description'], 'quote': raw, 'captured_text': captured, 'commentary_quote': commentary, 'captured_commentary': [dict(source_unit_id=id, annotations=l['annotations']) for id, l in zip(stage['source_unit_ids'], refs)], 'content_note': stage['note'], 'source_span': stage['source_span'], 'subjects': [stage['name']], 'related_entry_ids': [place]}
        english[pid] = {**encommon, 'name': row['en_name'], 'description': row['en_description'], 'quote': row['en_quote'], 'content_note': row['en_note']}
        cards.append({**common, 'id': place, 'kind': root_kind, 'name': stage['name'], 'description': row['description'], 'quote': raw, 'commentary_quote': commentary, 'content_note': stage['note'], 'source_passage_ids': [pid], 'related_entry_ids': [pid]})
        english[place] = dict(english[pid]); comments = ''.join(a for l in refs for a in l['annotations'])
        for e in [e for e in ENTITIES if e['slug'] == row['slug']]:
            assert e['quote'] in (comments if e.get('commentary_only') else raw), e['id']
            assert all(not q or q in comments for q in e.get('commentary', '').split('；')), e['id']
            c = {**common, **{k: e[k] for k in ['id', 'kind', 'name', 'quote', 'description']}, 'commentary_quote': e.get('commentary', ''), 'context_place_id': place, 'source_passage_ids': [pid], 'related_entry_ids': [pid]}
            if e.get('commentary_only'): c['commentary_only'] = True
            english[c['id']] = {**encommon, 'name': e['en_name'], 'description': e['en_description'], 'quote': e['en_quote'], 'commentary_quote': e.get('en_commentary', '')}
            if e['kind'] == 'water' or e.get('water'): c['relation_scope'] = 'water'
            if e.get('unknown'):
                c.update(appearance_unknown=True, artwork_caption='参照形貌未详 · 统一问号占位不代表本生物形态。')
                english[c['id']]['artwork_caption'] = 'The comparison form is unknown; the shared question-mark placeholder is not a depiction.'
                if e['id'] != 'beast-zhongshan-nuo-gancao':
                    c['artwork_caption'] = '形貌未详或依据不足 · 问号占位不代表形态。'
                    english[c['id']]['artwork_caption'] = 'Insufficient independent form evidence; the question-mark placeholder is not a depiction.'
            elif (art := jobs.get(e['id'])) and art['status'] == 'reviewed':
                c.update(artwork='zhongshan/' + art['name'] + '-v1.webp', artwork_pending=False, artwork_caption='经文与郭注鱼形依据 · 红羽尾构造、比例和姿态为明确艺术解释。')
                english[c['id']]['artwork_caption'] = 'Fish-form evidence follows the text and commentary; the red feather-like tail construction, proportions and pose are explicitly artistic.'
                if e['id'] != 'beast-zhongshan-hao-quzhu':
                    c['artwork_caption'] = '经文/郭注形貌与木刻演绎 · 器官依据见说明，未定细节、配色及姿态为艺术解释。'
                    english[c['id']]['artwork_caption'] = 'Textual or commentary-based form in woodcut interpretation; unspecified details, colors and pose are artistic.'
            if e.get('comparison_only') or stage['kind'] != 'mountain':
                c.pop('context_place_id')
                if e.get('comparison_only'): c['comparison_only'] = True
                c['related_entry_ids'].append(place); next(x for x in cards if x['id'] == place)['related_entry_ids'].append(c['id'])
            cards.append(c); p['subjects'].append(c['name']); p['related_entry_ids'].append(c['id'])
        passages.append(p)
    index = {c['id']: c for c in cards + passages}
    river = index['water-zhongshan-he']; recipient = index['passage-zhongshan-r01-quzhu']
    river.update(context_place_ids=[river['context_place_id'], 'place-zhongshan-r01-quzhu'], source_passage_ids=[*river['source_passage_ids'], recipient['id']], source_unit_ids=[*river['source_unit_ids'], *recipient['source_unit_ids']], source_pages=list(dict.fromkeys([*river['source_pages'], *recipient['source_pages']])), source_locator='卷第五 · 影印页2、3', quote=river['quote'] + '；而南流注于河')
    river['related_entry_ids'].append(recipient['id']); recipient['related_entry_ids'].append(river['id'])
    english[river['id']].update(quote='Gong water flows west into the He. Separately, Quzhu water flows south into the He.', source_locator='Volume 5 · scan pages 2, 3')
    for id, slug, q, eq in NEXT_SHARES:
        c = index[id]; p = index['passage-zhongshan-' + slug]; stage = next(s for s in review['stage_plan'] if s['slug'] == slug)
        assert q in p['quote'], (id, q)
        root = ('place' if stage['kind'] == 'mountain' else 'rite') + '-zhongshan-' + slug
        c['source_passage_ids'] = list(dict.fromkeys([*c['source_passage_ids'], p['id']]))
        if stage['kind'] == 'mountain': c['context_place_ids'] = list(dict.fromkeys([c['context_place_id'], *c.get('context_place_ids', []), root]))
        c['source_unit_ids'] = list(dict.fromkeys([*c['source_unit_ids'], *p['source_unit_ids']]))
        c['source_pages'] = list(dict.fromkeys([*c['source_pages'], *p['source_pages']]))
        page_numbers = sorted({int(url.rsplit('/', 1)[-1]) for url in c['source_pages']})
        c['source_locator'] = '卷第五 · 影印页' + '、'.join(map(str, page_numbers)); english[id]['source_locator'] = 'Volume 5 · scan pages ' + ', '.join(map(str, page_numbers))
        c['quote'] += '；' + q; english[id]['quote'] += ' Separately, ' + eq
        c['related_entry_ids'] += [p['id'], root]; p['related_entry_ids'].append(id); index[root]['related_entry_ids'].append(id)
    river.update(name='河（中山水文文本索引）', description='河文本索引分别存甘棗共水西注、渠豬水南注及青要畛水、騩山正回水、冝蘇滽滽水、和山九水北注六出处，不认定现代水系同一性。')
    english[river['id']].update(name='He (Central textual index)', description='This textual index preserves separate recipient accounts at Ganzao, Quzhu, Qingyao, Wei, Yisu and He, without settling modern geographic identity.')
    for id, (name, en_name, description, en_description) in OVERRIDES.items():
        index[id].update(name=name, description=description)
        english[id].update(name=en_name, description=en_description)
    for a, b in [('water-zhongshan-gong-gancao', river['id']), ('water-zhongshan-quzhu', river['id']), ('water-zhongshan-quzhu', 'beast-zhongshan-hao-quzhu'), *NEXT_LINKS]:
        index[a]['related_entry_ids'].append(b); index[b]['related_entry_ids'].append(a)
    for a, b in zip(passages, passages[1:]):
        a['related_entry_ids'].append(b['id']); b['related_entry_ids'].append(a['id'])
    batches = {'zhongshan-' + r['slug'] for r in ROWS}
    for group, values in [('passages', passages), ('text_entities', [c for c in cards if c['kind'] in {'place', 'rite', 'deity', 'animal'} or c['kind'] in {'plant', 'material'} and not c.get('context_place_id')]), ('beasts', [c for c in cards if c['kind'] == 'beast']), ('natural_features', [c for c in cards if c['kind'] in {'plant', 'water', 'material'} and c.get('context_place_id')])]:
        world[group] = [c for c in world[group] if c.get('content_batch') not in batches] + values
    world['revision'] = 'myth-world-2026-10-25-zhongshan-sixtythree-v1'
    review.update(status='partially_implemented', implemented_stages=63, remaining_stages=149, scope='前63段正文、郭注、双语及实体接入；后149阶段仍待逐批核定。', batch_size=30, entry_ids=[c['id'] for c in cards], passages=[dict(id=p['id'], source_unit_ids=p['source_unit_ids'], source_span=p['source_span'], status='facsimile_reviewed') for p in passages], artwork_summary=dict(selected=sum(a['status'] == 'reviewed' for a in jobs.values()), appearance_unknown=sum(c.get('appearance_unknown', False) for c in cards)), next=dict(name=review['stage_plan'][63]['name'], source_units=review['stage_plan'][63]['source_units'], facsimile_pages=review['stage_plan'][63]['facsimile_pages'], status='pending_bilingual_entity_review'))
    review['limits'] = '212阶段中前63阶段已接入，余149；形貌不足、异说与数字差异明确保留。页面验收以本地逐阶段交接为准。快照及原始捕获不改。'
    for stage in review['stage_plan'][:63]:
        stage.update(content_status='facsimile_reviewed', browser_status='see local handoff acceptance', passage_id='passage-zhongshan-' + stage['slug'], new_cards=sum(c['content_batch'] == 'zhongshan-' + stage['slug'] for c in cards))
    write('frontend/public/data/myth-world.json', world); write('frontend/src/locale-content-en.json', english); write('data/zhongshan-edition-review.json', review)
    print(f'Built Central: {len(passages)} passages, {len(cards)} cards; 149 stages remain')


if __name__ == '__main__':
    build()
