"""Maintain the reviewed first Nanshan batch and its English content without replacing other entries."""
import json
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
WORLD = ROOT / 'frontend/public/data/myth-world.json'
ENGLISH = ROOT / 'frontend/src/locale-content-en.json'
SOURCE = '《山海经·南山经》（《四部丛刊》景明成化本，郭璞传）'
SOURCE_EN = 'Shanhaijing · Nanshan Jing (Sibu Congkan facsimile of the Ming Chenghua edition; Guo Pu commentary)'
PAGE = 'https://zh.wikisource.org/wiki/Page:Sibu_Congkan0465-郭璞-山海經-2-1.djvu/'
ART = 'nanshan/'
NOTE = '引文据所列影印页作简体转写，标点为项目所加。经文、郭注与白话整理分别呈现；古籍中的功效记述不作为现实使用建议。'
NOTE_EN = 'The quotation is transcribed into simplified Chinese from the cited scan; punctuation is editorial. The ancient text, Guo Pu’s commentary and the project paraphrase are distinguished. Reported effects are ancient textual claims, not advice for use.'
SCENE = '地点场景示意 · 山形、植被和水流画法为艺术解释。'
SCENE_EN = 'Place scene · Mountain shape, vegetation and the depiction of water are artistic interpretations.'


def metadata(page, last=None):
    pages = list(range(page, (last or page) + 1))
    return {'source': SOURCE, 'source_chapter': '《南山经》', 'region': '南山经',
            'url': PAGE + str(page), 'source_locator': '卷第一 · 影印页 ' + '、'.join(map(str, pages)),
            'source_pages': [PAGE + str(number) for number in pages],
            'editorial_note': NOTE, 'content_batch': 'nanshan-first-three'}


def english_meta(record):
    return {'source': SOURCE_EN, 'source_chapter': 'Nanshan Jing', 'region': 'Nanshan Jing',
            'source_locator': record['source_locator'].replace('卷第一 · 影印页 ', 'Volume 1 · scan page ').replace('、', ', '),
            'editorial_note': NOTE_EN}


def build():
    world = json.loads(WORLD.read_text(encoding='utf-8'))
    english = json.loads(ENGLISH.read_text(encoding='utf-8'))

    def put(group, record, en, page, last=None):
        record = {**metadata(page, last), **record}
        rows = world.setdefault(group, [])
        old = next((item for item in rows if item['id'] == record['id']), None)
        if old is None:
            rows.append(record)
        else:
            old.update(record)
        english[record['id']] = {**english.get(record['id'], {}), **english_meta(record), **en}
        return record

    def mountain(id, name, x, y, art, description, quote_text, commentary, en, page, last):
        return put('places', {'id': id, 'kind': 'place', 'name': name, 'x': x, 'y': y,
            'group': 'south', 'reveal_stage': 2, 'reveal_chapter': '02', 'artwork': ART + art + '-v1.webp',
            'artwork_caption': SCENE, 'description': description, 'quote': quote_text,
            'commentary_quote': commentary, 'direction': '《南山经》篇内地点锚点；图面位置不表示真实坐标、里程或连续游览路线。'},
            {**en, 'artwork_caption': SCENE_EN, 'direction': 'A textual place anchor within Nanshan Jing. Its diagram position does not represent modern coordinates, scaled distances or a continuous visitor route.'}, page, last)

    mountain('place-zhaoyao', '招摇之山', 545, 625, 'zhaoyao',
        '西海之上，招摇山是《南山经》开篇的一座山。山间多桂木与金玉，祝余像韭草，开着青色的花；迷谷有黑色的纹理，花光四照。白耳的狌狌伏行其间。丽𪊨之水从这里流出，向西入海，水中又记有育沛。草木、异兽与流水，在这段经文中相次展开。',
        '其首曰招摇之山，临于西海之上，多桂，多金玉。有草焉，其状如韭而青花，其名曰祝余，食之不饥。有木焉，其状如榖而黑理，其花四照，其名曰迷谷，佩之不迷。有兽焉，其状如禺而白耳，伏行人走，其名曰狌狌，食之善走。丽𪊨之水出焉，而西流注于海，其中多育沛，佩之无瘕疾。',
        '「桂葉似枇杷」；釋榖為「榖，楮也，皮作紙」；育沛下注「未詳」。',
        {'name': 'Mount Zhaoyao', 'description': 'Above the Western Sea, Mount Zhaoyao opens the Nanshan Jing. Cassia trees, metals and jade occur here. Zhuyu resembles chives and bears blue-green flowers; Migu has dark grain and shining blossoms. White-eared Shengsheng move low to the ground. The Li𪊨 River rises here and flows west to the sea, with an object called Yupei recorded in its waters.',
         'quote': 'Its first mountain is Zhaoyao, overlooking the Western Sea, with abundant cassia, metals and jade. A chive-like herb with blue-green flowers is called Zhuyu; eating it is said to prevent hunger. A tree resembling gu has dark grain and shining flowers; it is called Migu, and carrying it is said to prevent losing one’s way. An ape-like creature with white ears crouches and walks as a person does: Shengsheng. Eating it is said to aid running. The Li𪊨 River rises here and flows west to the sea. Its waters contain much Yupei; wearing it is said to prevent abdominal affliction.'}, 16, 17)
    mountain('place-niuyang', '杻阳之山', 645, 635, 'niuyang',
        '杻阳山的两面，记着不同的物产：向阳一面多赤金，背阴一面多白金。山中有鹿蜀，白首、虎纹、赤尾，鸣声如歌。怪水从山间流出，向东汇入宪翼之水，旋龟便记在这段水域之中。山兽与水族各有形貌，随着水流，文字也从山中转向了下游。',
        '又东三百七十里，曰杻阳之山，其阳多赤金，其阴多白金。有兽焉，其状如马而白首，其文如虎而赤尾，其音如谣，其名曰鹿蜀，佩之宜子孙。怪水出焉，而东流注于宪翼之水。其中多玄龟，其状如龟而鸟首虺尾，其名曰旋龟，其音如判木，佩之不聋，可以为底。',
        '赤金下注「銅也」；白金下注「銀也」；郭注以「如破木聲」解「如判木」。',
        {'name': 'Mount Niuyang', 'description': 'The two faces of Mount Niuyang are described through their resources: red metal on the sunny side, white metal on the shaded side. Lushu has a white head, tiger markings, a red tail and a singing cry. The Guai River rises from the mountain and flows east into the Xianyi River. Xuangui is described in this water passage, as the account turns from the mountain toward its downstream waters.',
         'quote': 'Another 370 li east is Mount Niuyang. Its sunny side has red metal; its shaded side has white metal. A horse-like creature has a white head, tiger markings, a red tail and a singing cry. It is called Lushu; wearing it is said to favor descendants. The Guai River rises here and flows east into the Xianyi River. These waters contain many dark turtles with bird heads and serpent tails, called Xuangui. Their cry resembles splitting wood; wearing them is said to prevent deafness and treat ailments.'}, 18, 19)
    mountain('place-qingqiu', '青丘之山', 760, 570, 'qingqiu',
        '青丘山向阳处多玉，背阴处多青雘。这里的狐有九条尾，声音像婴儿；灌灌则是一种鸠状的鸟，鸣声仿佛人在相呼。英水自山中流出，向南注入即翼之泽，鱼身人面的赤鱬见于这段水中。山上的鸟兽与山下的流水相接，青丘的景象也由此铺开。',
        '又东三百里，曰青丘之山，其阳多玉，其阴多青䨼。有兽焉，其状如狐而九尾，其音如婴儿，能食人，食者不蛊。有鸟焉，其状如鸠，其音若呵，名曰灌灌，佩之不惑。英水出焉，南流注于即翼之泽。其中多赤鱬，其状如鱼而人面，其音如鸳鸯，食之不疥。',
        '郭注以「如人相呵呼聲」解灌灌之鸣，又记「或作濩濩」。底本「青䨼」保留于引文，白话采用通行写法「青雘」。',
        {'name': 'Mount Qingqiu', 'description': 'Jade occurs on Qingqiu’s sunny side, and a green mineral is recorded on its shaded side. Its fox has nine tails and an infant-like cry. Guanguan is a dove-like bird whose call is likened to people calling to one another. The Ying River rises here and flows south into Jiyi Marsh. Chiru, with fish bodies and human faces, are described in this water passage.',
         'quote': 'Another 300 li east is Mount Qingqiu. Its sunny side has jade; its shaded side has green mineral. A fox-like creature has nine tails and an infant-like cry. It can eat people; eating it is said to ward off gu. A dove-like bird calls as if calling out; its name is Guanguan, and wearing it is said to prevent bewilderment. The Ying River rises here and flows south into Jiyi Marsh. These waters contain Chiru, with fish bodies, human faces and mandarin-duck-like calls. Eating them is said to prevent skin disease.'}, 20, 21)

    def feature(id, kind, name, context, desc, text, en, page, last=None, art=None, commentary='', note=''):
        record = {'id': id, 'kind': kind, 'name': name, 'context_place_id': context,
                  'description': desc, 'quote': text, 'reveal_chapter': '02',
                  'direction': '按所引山段组织阅读；关联地点不表示现代位置。',
                  'commentary_quote': commentary, 'content_note': note}
        if art:
            record['artwork'] = ART + art + '-v1.webp'
            record['artwork_caption'] = SCENE if kind == 'water' else '依据经文的图像解释 · 未明示的细节为艺术表现。'
        return put('natural_features', record, {**en,
            'direction': 'Grouped by the cited mountain passage; the associated place is not a modern location.',
            **({'artwork_caption': SCENE_EN if kind == 'water' else 'An artistic interpretation of the text; unspecified details are illustrative.'} if art else {})}, page, last)

    feature('plant-zhuyu', 'plant', '祝余', 'place-zhaoyao',
        '招摇山有一种像韭草的植物，花呈青色，名叫祝余。它与桂木、迷谷一同见于开篇的山中草木记述。经文还说“食之不饥”；这里保留的是古人写下的名字与形貌，不能据此把它认作今天某一种可食植物。',
        '有草焉，其状如韭而青花，其名曰祝余，食之不饥。',
        {'name': 'Zhuyu', 'description': 'Zhuyu is a herb on Mount Zhaoyao, described as chive-like with blue-green flowers. It appears alongside cassia and Migu in the opening account of the mountain. The text says eating it prevents hunger; this records an ancient claim, not an identification of a present-day edible plant.',
         'quote': 'There is a chive-like herb with blue-green flowers, called Zhuyu. Eating it is said to prevent hunger.', 'content_note': 'Its modern botanical identity is not established here.'}, 16, art='zhuyu', commentary='「祝餘」下注「或作桂荼」。', note='不据古籍功效确定现代物种或食用方式。')
    feature('plant-migu', 'plant', '迷谷', 'place-zhaoyao',
        '迷谷也是招摇山中的木。经文用“如榖”描写它的形状，又写其纹理黑、花光四照。郭注将榖解释为楮。至于“佩之不迷”，是这株树在古籍中的特异记述；它的现代物种归属仍不在这里作定论。',
        '有木焉，其状如榖而黑理，其花四照，其名曰迷谷，佩之不迷。',
        {'name': 'Migu', 'description': 'Migu is a tree on Mount Zhaoyao. It resembles gu, has dark grain and flowers that shine all around. Guo Pu explains gu as paper mulberry. The claim that carrying Migu prevents losing one’s way belongs to the ancient account; no modern species identification is asserted here.',
         'quote': 'There is a gu-like tree with dark grain and flowers shining all around. Its name is Migu. Carrying it is said to prevent losing one’s way.', 'content_note': 'The illustration interprets its form; it does not identify a modern species.'}, 16, 17, 'migu', '「榖，楮也，皮作紙」；「其花四照」下注「言有光燄也」。', '图中叶形、花形与亮部均为艺术解释，不作为现代植物鉴定。')
    feature('water-liji', 'water', '丽𪊨之水', 'place-zhaoyao',
        '丽𪊨之水从招摇山流出，向西注入海中。水里记有育沛，却没有展开它的形貌。这个水名和向西入海的方向，是经文在招摇山段留下的线索。',
        '丽𪊨之水出焉，而西流注于海，其中多育沛，佩之无瘕疾。',
        {'name': 'Li𪊨 River', 'description': 'The Li𪊨 River rises on Mount Zhaoyao and flows west into the sea. Yupei is recorded in its waters, without an account of its appearance. The name and westward flow are the geographic clues preserved in this passage.',
         'quote': 'The Li𪊨 River rises here and flows west into the sea. It contains much Yupei; wearing it is said to prevent abdominal affliction.', 'content_note': 'The rare written character is retained; no unconfirmed modern reading or location is supplied.'}, 17, art='zhaoyao', note='保留底本水名用字；未确认的现代读音与地望不补写。')
    for id, name, desc, text, en in [
        ('water-guai', '怪水', '怪水出自杻阳山，向东汇入宪翼之水。随后，经文写到鸟首、虺尾的旋龟。山中鹿蜀的记述到此转入水域，旋龟的关联也由这段流水文字来说明。',
         '怪水出焉，而东流注于宪翼之水。其中多玄龟，其状如龟而鸟首虺尾，其名曰旋龟。',
         {'name': 'Guai River', 'description': 'The Guai River rises on Mount Niuyang and flows east into the Xianyi River. The account then describes Xuangui, turtles with bird heads and serpent tails. This water passage supplies the basis for their association.', 'quote': 'The Guai River rises here and flows east into the Xianyi River. These waters contain dark turtles with bird heads and serpent tails, called Xuangui.'}),
        ('water-xianyi', '宪翼之水', '在杻阳山段，宪翼之水是怪水向东汇入的水域。经文在这里没有另外交代它的源头、全程或所在山。顺着这条流入关系，可以回看怪水与旋龟的记述。',
         '怪水出焉，而东流注于宪翼之水。',
         {'name': 'Xianyi River', 'description': 'In the Mount Niuyang passage, Xianyi receives the eastward-flowing Guai River. Its own source, full course and mountain are not independently specified here. The recorded link leads back to Guai and the Xuangui passage.', 'quote': 'The Guai River rises here and flows east into the Xianyi River.'})]:
        feature(id, 'water', name, 'place-niuyang', desc, text, {**en, 'content_note': 'The flow relation is explicit; no modern coordinates or additional river course are inferred.'}, 18, 19, 'niuyang', note='只保留经文明示的流入关系，不补造源头、河道或现代坐标。')
    for id, name, desc, text, en in [
        ('water-ying-qingqiu', '英水', '青丘山的英水向南流去，注入即翼之泽。紧接着的水中记述里，有鱼身人面的赤鱬。同名水流在其他山段也有出现，本条只指青丘这一段。',
         '英水出焉，南流注于即翼之泽。其中多赤鱬，其状如鱼而人面，其音如鸳鸯，食之不疥。',
         {'name': 'Ying River · Qingqiu', 'description': 'The Ying River rises at Qingqiu and flows south into Jiyi Marsh. Chiru, with fish bodies and human faces, appear in the following water description. Rivers with the same name occur elsewhere; this entry concerns only the Qingqiu passage.', 'quote': 'The Ying River rises here and flows south into Jiyi Marsh. These waters contain Chiru, with fish bodies, human faces and mandarin-duck-like calls. Eating them is said to prevent skin disease.'}),
        ('water-jiyi', '即翼之泽', '即翼之泽在青丘山段承接南流的英水。经文没有为这片泽地另画边界，也没有写出它的尺度。这里依据的是水名和流入方向，场景中的湿地形状只是图像解释。',
         '英水出焉，南流注于即翼之泽。',
         {'name': 'Jiyi Marsh', 'description': 'Jiyi Marsh receives the southward-flowing Ying River in the Qingqiu passage. Its boundary and scale are not separately described. The entry preserves the name and flow relation; the illustrated wetland shape is an artistic interpretation.', 'quote': 'The Ying River rises here and flows south into Jiyi Marsh.'})]:
        feature(id, 'water', name, 'place-qingqiu', desc, text, {**en, 'content_note': 'This entry belongs to the Qingqiu passage. The illustration does not reconstruct the waterbody’s shape.'}, 21, art='qingqiu', note='按青丘山段区分同名水域；图片不复原泽地或河道的实际形状。')
    feature('material-yupei', 'material', '育沛', 'place-zhaoyao',
        '招摇山的丽𪊨之水中，记有一种叫育沛的物产。经文说它可以佩用，却没有描写它的样子，郭注也只写“未详”。因此这里保留其名与水域关系，不把它画成确定的动物、玉石或珠饰。',
        '其中多育沛，佩之无瘕疾。',
        {'name': 'Yupei', 'description': 'Yupei is recorded in the Li𪊨 River at Mount Zhaoyao. The text mentions wearing it but gives no appearance; Guo Pu’s note says it is unidentified. Its name and water association are retained without depicting it as a specific animal, mineral or ornament.',
         'quote': 'These waters contain much Yupei; wearing it is said to prevent abdominal affliction.', 'content_note': 'Appearance and identity are unspecified. No image is assigned.'}, 17, commentary='育沛下注「未詳」。', note='物产是阅读分类，不等于已确定其为矿物；形貌与本体未详。')

    put('beasts', {'id': 'beast-guanguan', 'name': '灌灌', 'kind': '鸟', 'reveal_stage': 3, 'reveal_chapter': '03',
        'description': '青丘山中的鸠状鸟，声音像人在相呼。经文名之为灌灌；它与《西山经》中一目三尾的讙，分别见于不同篇目。',
        'quote': '有鸟焉，其状如鸠，其音若呵，名曰灌灌，佩之不惑。',
        'commentary_quote': '郭注：「如人相呵呼聲」；又记「或作濩濩」。',
        'artwork': ART + 'guanguan-v1.webp', 'place_id': 'place-qingqiu', 'context_place_id': 'place-qingqiu',
        'place_basis': '《南山经》青丘山段明载；图标为篇内示意。',
        'content_note': '经文只明示鸠状与鸣声；插画羽色与姿态为艺术解释。'},
        {'name': 'Guanguan', 'kind': 'Bird', 'description': 'A dove-like bird at Mount Qingqiu, with a call likened to people calling to one another. Guanguan is distinct from the one-eyed, three-tailed Huan in the Xishan Jing.',
         'quote': 'There is a dove-like bird whose call is like calling out. Its name is Guanguan. Wearing it is said to prevent bewilderment.',
         'place_basis': 'Explicitly recorded in the Qingqiu passage of Nanshan Jing; the map icon is diagrammatic.',
         'content_note': 'Only a dove-like form and its call are specified. Plumage color and pose are illustrative.'}, 21)

    updates = [
        ('beast-shengsheng', 'place-zhaoyao', 17, '其状如禺而白耳，伏行人走，其名曰狌狌，食之善走。',
         '狌狌见于招摇山，像禺而有白耳，伏地行走，也写作如人走。原文没有另写人面；图中面部的处理属于艺术解释。',
         'Shengsheng is recorded on Mount Zhaoyao, resembling an ape with white ears. It crouches and walks as a person does. The text does not independently specify a human face; the face in the illustration is artistic interpretation.',
         'It resembles an ape with white ears, crouching and walking as a person does. It is called Shengsheng; eating it is said to aid running.'),
        ('beast-lushu', 'place-niuyang', 18, '其状如马而白首，其文如虎而赤尾，其音如谣，其名曰鹿蜀，佩之宜子孙。',
         '杻阳山中的鹿蜀，马状、白首，身有虎纹而尾呈赤色。它的鸣声被比作歌谣。经文在写过这只山兽后，转而记述从山中流出的怪水。',
         'Lushu at Mount Niuyang resembles a horse, with a white head, tiger markings and a red tail. Its cry is likened to singing. The passage turns from this mountain creature to the Guai River rising there.',
         'It resembles a horse with a white head, tiger markings and a red tail. Its cry is like singing. It is called Lushu; wearing it is said to favor descendants.'),
        ('beast-xuangui', 'place-niuyang', 19, '其中多玄龟，其状如龟而鸟首虺尾，其名曰旋龟，其音如判木，佩之不聋，可以为底。',
         '怪水向东流入宪翼之水，随后写到旋龟：龟身、鸟首、虺尾，鸣声如木被劈开。它属于这段水中记述，不能只因同见于杻阳山段就改写成陆上的山兽。',
         'After the Guai River flows east into the Xianyi River, the text describes Xuangui: turtles with bird heads, serpent tails and calls like splitting wood. This is a water passage, not a description of a land-dwelling mountain beast.',
         'These waters contain dark turtles with bird heads and serpent tails, called Xuangui. Their cry resembles splitting wood; wearing them is said to prevent deafness and treat ailments.'),
        ('beast-jiuweihu', 'place-qingqiu', 20, '有兽焉，其状如狐而九尾，其音如婴儿，能食人，食者不蛊。',
         '青丘山有狐状而九尾的兽，声音像婴儿。经文随后写灌灌与英水；这些是同一山段相次记下的鸟兽与流水，不据此补出它们之间的捕食或因果关系。',
         'The creature on Mount Qingqiu resembles a fox with nine tails and an infant-like cry. Guanguan and the Ying River follow in the passage. Their occurrence in one account does not establish feeding or causal relationships.',
         'There is a fox-like creature with nine tails and an infant-like cry. It can eat people; eating it is said to ward off gu.'),
        ('beast-chiru', 'place-qingqiu', 21, '其中多赤鱬，其状如鱼而人面，其音如鸳鸯，食之不疥。',
         '英水南流，注入即翼之泽，随后记有赤鱬。它鱼身人面，声音像鸳鸯，是青丘山段的水中异物。这里不将它和山上的九尾狐写成同一种栖居环境。',
         'After the Ying River flows south into Jiyi Marsh, the passage records Chiru: fish with human faces and mandarin-duck-like calls. This is a water creature in the Qingqiu passage, distinct from the fox described on the mountain.',
         'These waters contain Chiru, with fish bodies, human faces and mandarin-duck-like calls. Eating them is said to prevent skin disease.'),
    ]
    for id, context, page, text, description, en_desc, en_quote in updates:
        put('beasts', {'id': id, 'context_place_id': context, 'description': description, 'quote': text,
            'place_id': context if id in ['beast-shengsheng', 'beast-lushu', 'beast-jiuweihu'] else 'place-south-ranges',
            'place_basis': '据所引山段关联阅读；水族依据水中记述，不将其陆上定位。',
            'illustration_review': '已核对本段影印页与现有插画的核心形貌；未明示的面部、颜色和姿态为艺术解释。'},
            {'description': en_desc, 'quote': en_quote,
             'place_basis': 'Associated through the cited passage; water creatures are linked to the water description, without a land-habitat claim.',
             'illustration_review': 'The passage scan and the illustration’s core form were reviewed. Unspecified facial details, colors and poses are artistic interpretation.'}, page, 21 if id == 'beast-jiuweihu' else page)

    world['revision'] = 'myth-world-2026-10-19-nanshan-reader-v3' if world.get('passages') else 'myth-world-2026-10-19-nanshan-v2'
    relations = []
    def link(a, b, text, forward, backward):
        relations.append({'ids': [a, b], 'source': '《南山经》', 'quote': text, 'labels': [forward, backward]})
    link('place-zhaoyao', 'plant-zhuyu', '有草焉，其状如韭而青花，其名曰祝余', '山中所见', '见于此山')
    link('place-zhaoyao', 'plant-migu', '有木焉，其状如榖而黑理，其花四照，其名曰迷谷', '山中所见', '见于此山')
    link('place-zhaoyao', 'beast-shengsheng', '其名曰狌狌', '山中所见', '见于此山')
    link('place-zhaoyao', 'water-liji', '丽𪊨之水出焉', '水出此山', '水源记述')
    link('water-liji', 'material-yupei', '其中多育沛', '水中所记', '见于此水')
    link('place-niuyang', 'beast-lushu', '其名曰鹿蜀', '山中所见', '见于此山')
    link('place-niuyang', 'water-guai', '怪水出焉', '水出此山', '水源记述')
    link('water-guai', 'water-xianyi', '怪水出焉，而东流注于宪翼之水', '向东流入', '承接来水')
    link('water-guai', 'beast-xuangui', '其中多玄龟，其状如龟而鸟首虺尾，其名曰旋龟', '水段所见', '本段水域')
    link('place-qingqiu', 'beast-jiuweihu', '其状如狐而九尾', '山中所见', '见于此山')
    link('place-qingqiu', 'beast-guanguan', '有鸟焉，其状如鸠，其音若呵，名曰灌灌', '山中所见', '见于此山')
    link('place-qingqiu', 'water-ying-qingqiu', '英水出焉，南流注于即翼之泽', '水出此山', '水源记述')
    link('water-ying-qingqiu', 'water-jiyi', '南流注于即翼之泽', '向南流入', '承接来水')
    link('water-ying-qingqiu', 'beast-chiru', '其中多赤鱬，其状如鱼而人面', '水段所见', '本段水域')
    (ROOT / 'frontend/src/nanshan-relations.json').write_text(json.dumps(relations, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    WORLD.write_text(json.dumps(world, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    ENGLISH.write_text(json.dumps(english, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print('Updated 2 new mountains, 8 natural features, Guanguan and 6 existing entries; unrelated records preserved.')


if __name__ == '__main__':
    build()
