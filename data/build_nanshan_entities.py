"""Complete independent Southern cards without adding invented map coordinates."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
def read(path): return json.loads((ROOT/path).read_text(encoding='utf-8'))
def write(path,value): (ROOT/path).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

BEASTS=[
('lu','鯥','di','有魚焉','食之無腫疾','鱼状被列为鯥，却有牛形、蛇尾和胁下的翼，居于陆地。经文写它冬死夏生，郭注以蛰伏解释。','Lu','An ox-shaped fish with a serpent tail and wings beneath its flanks, dwelling on land. Winter death and summer life are explained by the commentary as dormancy.','A fish resembles an ox, lives on land, has a serpent tail and wings beneath the flanks, and a bovine-like cry with an unresolved comparison glyph. Called Lu, it is said to die in winter and live in summer; eating it is said to prevent swelling.','An ox-shaped creature with four bovine legs, a long serpent tail, and exactly two feathered wings emerging below the left and right ribs. No fish head; no fins replacing the legs. Full body, three-quarter view.'),
('lei','𩔗','danyuan','有獸焉','食者不妬','亶爰山的𩔗像狸而有髦，原文又写自为牝牡。郭注保存异写与解释，不据此补出繁殖情节。','Mane-bearing creature','A wildcat-like creature with a mane, described as both female and male. Its name retains the edition glyph.','A creature resembles a wildcat with a mane, named 𩔗. It is described as both female and male; eating it is said to prevent jealousy.','One wildcat-like quadruped with a conspicuous mane around the neck. Ordinary external anatomy, no sexual organs, no extra heads or limbs. Full body.'),
('changfu','𪁺𩿧','jishan','有鳥焉','食之無卧','基山之鸟像鸡，有三首、六目、六足、三翼。经文记食之无卧；形貌按这些数量保留，不另添其他异能。','Three-headed bird','A chicken-like bird described with three heads, six eyes, six feet and three wings.','A bird resembles a chicken but has three heads, six eyes, six feet and three wings. Named 𪁺𩿧, eating it is said to prevent sleep.','An anatomically deliberate chicken-like mythical bird, EXACTLY THREE separate heads, each head with TWO visible eyes (six eyes total), EXACTLY SIX separate legs and feet, EXACTLY THREE feathered wings. Frontal three-quarter symmetrical display, the third wing rises behind the back; keep every head, foot and wing separated and countable. One body, no extra parts.'),
('lili','狸力','gui','有獸焉','多土功','柜山的狸力像豚而有距，叫声像犬。经文把它的出现与土功相连，没有描写它挖山造城的过程。','Lili','A pig-like creature with spurs and a dog-like cry, associated in the text with earthworks.','A creature resembles a pig with spurs and barks like a dog. Called Lili, its appearance is said to accompany earthworks in the district.','A single pig-like quadruped with pig snout, hoofed feet and conspicuous small rooster-like spurs behind the lower legs. No canine head, no digging tools, no human hands. Full body.'),
('zhu','鴸','gui','有鳥焉','多放士','鴸像鸱，足似人手，鸣声自呼其名。它出现时多放士的记述，属于经文的征兆表达。','Zhu','A kite-like bird with feet compared to human hands, calling its own name.','A bird resembles a kite with human-hand-like feet. Its sound is compared to bi, and it calls its own name. Called Zhu, its appearance is said to accompany dismissed officials.','One kite-like raptor with a feathered bird body, wings and normal bird head, but exactly two feet anatomically shaped like human hands with five fingers each. Hands attach only at the two legs; no extra human arms. Full body.'),
('changyou','长右','changyou','有獸焉','見則郡縣大水','长右山中之兽像禺而有四耳，鸣声如吟。原文以它的出现联系大水，不据此描写它主动引洪水。','Changyou','An ape-like creature with four ears and a moaning cry.','An ape-like creature has four ears and a moaning cry. Named Changyou, its appearance is said to foretell great floods.','One ape-like full-body creature with exactly FOUR distinct external ears, two on each side of its head. Ordinary ape face and limbs, no horns, no wings, no magic water.'),
('huahuai','猾褢','yaoguang','有獸焉','見則縣有大繇','猾褢像人而有猪鬣，穴居、冬蛰，声音如斵木。它与大繇的联系依经文保留，不补造劳役场面。','Huahuai','A human-like cave-dwelling creature with pig bristles, dormant in winter.','A human-like creature has pig bristles, lives in caves and is dormant in winter. Named Huahuai, it sounds like chopping wood and is associated with great labor levies.','One non-sexual human-like mythical figure with modest dense coarse pig bristles covering the shoulders, spine and torso, seated in a neutral crouch near a small rock. Human-like face, not a pig head; no clothes, tools or exposed genitals. Full body.'),
('zhi','彘','fuyu','有獸焉','是食人','浮玉山的彘像虎而有牛尾，声音如吠犬。经文写它食人，图像只呈其形，不画捕食情节。','Zhi','A tiger-like creature with an ox tail and a dog-like cry.','A creature resembles a tiger with an ox tail and barks like a dog. Called Zhi, it eats people.','One tiger-like quadruped with striped coat and a bovine ox tail ending in a dark tuft instead of a tiger tail. Neutral standing pose, full body, no prey or violence.'),
('huan-xun','䍺','xun','有獸焉','其名曰䍺','洵山的䍺像羊而无口，经文又写不可杀。这里保留这两项记述，不解释它如何饮食，也不补造额外器官。','Mouthless Huan','A sheep-like creature with no mouth; the text says it is not to be killed.','A creature resembles a sheep but has no mouth. It is described as not to be killed and is named 䍺.','One sheep-like quadruped whose face has eyes and nostrils but absolutely NO mouth opening, lips or mouth line. Calm full-body three-quarter pose. Normal wool, no wounds, no sealed stitches, no extra organs. Make the mouthless face clearly visible.'),
('quru','瞿如','daoguo','有鳥焉','其鳴自號也','瞿如像鵁，有白首、三足、人面，鸣声自呼其名。三足与人面均见经文，羽色的其他部分不作定论。','Quru','A waterbird-like creature with a white head, three feet and a human face.','A bird resembles a jiao waterbird, with a white head, three feet and a human face. Called Quru, it calls its own name.','One waterbird-like bird with a white feathered head framing a clearly human face, exactly THREE separate legs and feet. Exactly two normal feathered wings. Full body, all three feet clearly separated on the ground, no additional heads.'),
('hujiao','虎蛟','daoguo','其中有虎蛟','可以已痔','泿水中的虎蛟是鱼身、蛇尾，声音如鸳鸯。名称虽有虎字，经文没有写虎头或虎爪，图像依鱼身蛇尾处理。','Hujiao','A fish-bodied water creature with a serpent tail; a tiger head is not specified.','Hujiao has a fish body and a serpent tail, with a mandarin-duck-like cry. Eating it is said to prevent swelling and treat hemorrhoids.','One aquatic mythical creature with a true FISH head and scaled fish torso with fins, transitioning into a long tapering SERPENT tail. NO tiger head, no tiger markings, no legs, no wings, no horns. Full body gently curved.'),
('zhuan','鱄鱼','ji','其中有鱄','見則天下大旱','鱄鱼像鲋，身有猪毛，声音像豚。经文记其出现与大旱相关；这里只画鱼与毛的形貌，不把旱灾画成它主动施为。','Zhuan fish','A crucian-carp-like fish with pig bristles and a pig-like cry.','A fish resembles a crucian carp with pig bristles and a pig-like cry. Called Zhuan, its appearance is said to foretell great drought.','One crucian-carp-shaped fish with fins, scales and patches of coarse pig bristles along the body. A normal fish head, NOT a pig snout. Full body side profile, no limbs or wings.'),
('yulingqiu','𪃍','lingqiu','有鳥焉','見則天下大旱','令丘之鸟像枭，有人面、四目与耳，鸣声自呼其名。它的名字保留底本用字，不补写未核定的读音。','Four-eyed owl-like bird','An owl-like bird with a human face, four eyes and ears, retaining its edition name.','A bird resembles an owl with a human face, four eyes and ears. Named 𪃍, it calls its own name; its appearance is said to foretell great drought.','One owl-like bird with a human face, exactly FOUR clearly visible eyes arranged in two pairs, and two external ears. Feathered body, two wings, two bird feet. Frontal full-body pose, no additional faces or heads.'),
('yuanchu','鵷鶵','nanyu','有鳯皇鵷鶵','有鳯皇鵷鶵','南禺山末尾并记凤皇与鵷鶵。郭注说鵷鶵亦凤属，经文没有另写它的形貌，因此使用统一留空剪影，不另画一只确定的神鸟。','Yuanchu','Named at Nanyu with Fenghuang; its separate appearance is not described.','Fenghuang and Yuanchu are present.',''),
]

WATERS=[
('west-sea','西海 · 南山经','zhaoyao','臨于西海之上','招摇山临于西海之上。这里保留原书的方位海名，不确定其现代对应。','Western Sea · Southern text','Zhaoyao overlooks the Western Sea; a modern identification is not asserted.'),
('east-sea','东海 · 南山经','jiwei','其尾踆于東海','箕尾山尾临着东海。图面海岸仅是篇内场景，不作为现代海岸复原。','Eastern Sea · Southern text','The tail of Jiwei sits above the Eastern Sea. The scene does not reconstruct a modern coastline.'),
('fang','汸水','jiwei','汸水出焉而南流注于淯其中多白玉','汸水从箕尾山流出，向南汇入淯，水中多白玉。','Fang River','The Fang River rises at Jiwei and flows south into Yu, with much white jade.'),
('yu-receiver','淯','jiwei','汸水出焉而南流注于淯','淯承接南流的汸水。本段没有另写它的源头与全程。','Yu · receiving water','Yu receives the southward Fang River; its own source is not specified here.'),
('ying-gui','英水 · 柜山','gui','英水出焉西南流注于赤水其中多白玉多丹粟','柜山英水向西南流入赤水，水中多白玉与丹粟。它与青丘英水按不同山段分别建卡。','Ying River · Gui','This Ying River rises at Gui and flows southwest into Red Water, with white jade and cinnabar grains. It is kept separate from Qingqiu’s Ying.'),
('chishui-gui','赤水 · 柜山段','gui','英水出焉西南流注于赤水','本段赤水承接柜山英水。不与《大荒北经》的同名赤水自动合并。','Red Water · Gui passage','This Red Water receives Gui’s Ying River. It is not automatically equated with Red Water in Dahuang Beijing.'),
('tiao','苕水','fuyu','苕水出于其隂北流注于具區其中多鮆魚','苕水从浮玉山阴流出，向北注入具区，水中多鮆鱼。','Tiao River','The Tiao rises on Fuyu’s shaded side and flows north into Juqu, with many ji fish.'),
('juqu','具区','fuyu','北望具區','浮玉山北望具区，苕水也向北流入其中。郭注另以太湖解释该名，现代地望不在本卡定论。','Juqu','Fuyu looks north to Juqu, which also receives the northward Tiao River. The commentary offers a later identification; no modern coordinates are assigned.'),
('zhupi-fuyu','诸毗 · 浮玉段','fuyu','東望諸毗','浮玉山向东望诸毗，本段郭注称其为水名；与柜山段注文所说的山名分开记录。','Zhupi · Fuyu water reference','Fuyu looks east to Zhupi, identified here as a water name in the commentary. The mountain reference in the Gui passage is kept separate.'),
('shu','䦠水','cheng','䦠水出焉而南流注于虖勺其中多黄金','䦠水从成山流出，向南注入虖勺，水中多黄金。水名保留底本字形。','River from Cheng','The river rises at Cheng and flows south into Hushao, with much gold.'),
('hushao-receiver','虖勺 · 成山流入对象','cheng','䦠水出焉而南流注于虖勺','这里的虖勺是成山䦠水的流入对象。不因同名就改写为虖勺山。','Hushao · receiving water','Hushao is the receiving water named after the river from Cheng. Its name alone does not establish identity with Mount Hushao.'),
('shao','勺水','kuaiji','勺水出焉而南流注于湨','勺水从会稽山流出，向南汇入湨。','Shao River','The Shao rises at Kuaiji and flows south into Ju.'),
('ju','湨','yi','湨水出焉而南流注于列塗','湨在会稽段承接勺水，在夷山段又记为出水并南注列涂。两处文字分别保留，不据此推绘完整河道。','Ju River','Ju receives Shao in the Kuaiji passage; at Yi it is said to rise and flow south into Lietu. Both statements are retained without reconstructing a full channel.'),
('lietu','列涂','yi','湨水出焉而南流注于列塗','列涂是夷山湨水南流的去处。本段没有另写它的形状与尺度。','Lietu','Lietu receives the southward Ju River from Yi; its form and scale are not independently described.'),
('xun','洵水','xun','洵水出焉而南流注于閼之澤其中多芘蠃','洵水从洵山流出，向南汇入阏之泽，水中多芘蠃。','Xun River','The Xun rises at Mount Xun and flows south into Yan Marsh, with many piluo.'),
('yan-marsh','阏之泽','xun','洵水出焉而南流注于閼之澤','阏之泽承接南流的洵水；泽地边界与水面形状未详。','Yan Marsh','Yan Marsh receives the southward Xun River. Its boundaries and shape are unspecified.'),
('pang','滂水','hushao','滂水出焉而東流注于海','虖勺段写滂水东流入海，区吴、鹿吴两段又分别记鹿水、泽更之水南流注入。这里只保留这些文字关系。','Pang River','Pang flows east to the sea in the Hushao passage. Lu and Zegeng flow south into Pang in the Quwu and Luwu passages.'),
('lu','鹿水','quwu','鹿水出焉而南流注于滂水','鹿水从区吴山流出，向南汇入滂水。','Lu River','The Lu rises at Quwu and flows south into Pang.'),
('zegeng','泽更之水','luwu','澤更之水出焉而南流注于滂水','泽更之水从鹿吴山流出，向南注入滂水；随后水中记述引出蛊雕。','Zegeng Water','Zegeng rises at Luwu and flows south into Pang. Gudiao follows in the water description.'),
('yin','泿水','daoguo','泿水出焉而南流注于海其中有虎蛟','泿水从祷过山流出，向南入海，其中记有鱼身蛇尾的虎蛟。','Yin Water','Yin rises at Daoguo and flows south into the sea, with the fish-bodied, serpent-tailed Hujiao.'),
('dan','丹水','danxue','丹水出焉而南流注于㴾海','丹水从丹穴山流出，向南汇入本段所写的㴾海。','Dan Water','Dan rises at Danxue and flows south into the sea named in this passage.'),
('bohai-south','㴾海 · 南山经','danxue','南流注于㴾海','丹穴段的丹水与发爽段的汎水，都向南注入㴾海。本卡不自动将它等同于现代渤海。','Bohai · Southern text','Dan and Fan flow south into the sea named in this passage. Identity with the modern Bohai is not assumed.'),
('fan','汎水','fashuang','汎水出焉而南流注于㴾海','汎水从发爽山流出，向南注入㴾海。','Fan Water','Fan rises at Fashuang and flows south into the sea named in the text.'),
('hei','黑水 · 鸡山','ji','黒水出焉而南流注于海其中有鱄魚','鸡山黑水向南流入海中，水中有形如鲋而身带猪毛的鱄鱼。','Black Water · Chicken Mountain','Black Water rises at Chicken Mountain and flows south into the sea, with bristled Zhuan fish.'),
('zuo','佐水','nanyu','佐水出焉而東南流注于海','佐水从南禺山流出，向东南入海。山穴季节性进出水另见同段，不据此改写为佐水的水文机制。','Zuo Water','Zuo rises at Nanyu and flows southeast into the sea. The cave’s seasonal water statement is retained separately.'),
]

def build():
    world,en=read('frontend/public/data/myth-world.json'),read('frontend/src/locale-content-en.json')
    passages={p['id'].removeprefix('passage-nanshan-'):p for p in world['passages'] if p['id'].startswith('passage-nanshan-')}
    existing_scenes={'zhaoyao','niuyang','qingqiu','tangting','xun','danxue'}
    mountain_ids={s:('place-'+s if s in {'zhaoyao','niuyang','qingqiu'} else 'place-nanshan-'+s) for s in passages if s not in {'range1','range2','range3','total'}}
    scene=lambda s: f'nanshan/{s if s in existing_scenes else "scene-"+s}-v1.webp'
    records={x['id']:x for x in world.get('text_entities',[]) if x.get('content_batch')!='nanshan-entities'}
    jobs=[]; by_passage={p['id']:[] for p in passages.values()}
    full={x['id']:x for group in ['beasts','places','natural_features'] for x in world[group]}
    def upsert(group,record):
        rows=world[group]; old=next((x for x in rows if x['id']==record['id']),None)
        if old: old.update(record)
        else: rows.append(record)
    def add(id,kind,name,slug,desc,en_name,en_desc,quote=None,en_quote=None,art=None,chapter='02',group='text_entities',context=True):
        p=passages[slug]
        r={k:p[k] for k in ['source','source_chapter','region','source_locator','source_pages','url','editorial_note','commentary_quote']}
        r.update(id=id,kind=kind,name=name,description=desc,quote=quote or p['quote'],reveal_chapter=chapter,
            direction='据所引山段阅读；不表示现代坐标、实测距离或未经原文说明的栖居范围。',
            source_passage_ids=[p['id']],source_unit_ids=p['source_unit_ids'],content_batch='nanshan-entities',
            related_entry_ids=[p['id']],artwork=art or scene(slug),
            artwork_caption='场景示意 · 依据所引山段组织，画中地貌、植被和未明示细节为艺术解释。')
        if context and slug in mountain_ids and id!=mountain_ids[slug]:r['context_place_id']=mountain_ids[slug]
        if group=='text_entities':records[id]=r
        else:upsert(group,r)
        english_parent=en[p['id']]
        rendered_quote=(en_quote or english_parent['quote']).replace('The tree Bai䓘','The tree named here').replace('Bai䓘','the tree named here')
        for before,after in [('The 䦠 River','A river'),('and is named 䍺','and is named Huan'),('named 𩔗','retaining its edition name'),('Named 𪁺𩿧, eating it','Eating it'),('Named 𪃍, it calls','It calls')]:rendered_quote=rendered_quote.replace(before,after)
        en[id]={**{k:english_parent[k] for k in ['source','source_chapter','region','source_locator','editorial_note']},
            'name':en_name,'description':en_desc,'quote':rendered_quote,
            'direction':'Read through the cited passage; no modern coordinates, measured distances or unsupported habitat boundaries are assigned.',
            'artwork_caption':'Scene illustration · Landforms, vegetation and unspecified details are artistic interpretations of the cited passage.'}
        by_passage[p['id']].append(id)
        return r
    for slug,id in mountain_ids.items():
        p=passages[slug]; ep=en[p['id']]
        if id not in full:
            add(id,'place',p['name'],slug,p['description'],ep['name'],ep['description'],context=False)
        else:by_passage[p['id']].append(id)
        if slug not in existing_scenes:
            jobs.append({'name':'scene-'+slug,'entry_ids':[id],'subject':ep['quote'], 'category':'scene'})
    for slug,name,parent,start,end,desc,en_name,en_desc,en_quote,visual in BEASTS:
        p=passages[parent]; a=p['quote'].index(start); b=p['quote'].index(end,a)+len(end); q=p['quote'][a:b]
        r=add('beast-nanshan-'+slug,'兽',name,parent,desc,en_name,en_desc,q,en_quote,
            art=f'nanshan/creature-{slug}-v1.webp' if visual else scene(parent),chapter='03',group='beasts')
        r['reveal_stage']=3; r['place_basis']='经文山段关联，未添加独立地图点。'
        if not visual:
            r['appearance_unknown']=True
            r['artwork_caption']='形貌未详 · 灰白问号剪影为统一占位，不代表该生物的形态。'
            en[r['id']]['artwork_caption']='Appearance unspecified · The gray question-mark silhouette is a shared placeholder, not a depiction of this creature.'
            upsert('beasts',r)
        en[r['id']]['kind']='Creature'; en[r['id']]['place_basis']='Associated by the passage; no separate map marker.'
        if visual:
            r['artwork_caption']='形貌示意 · 经文明示的身体结构保留；颜色、姿态和未明示细节为艺术解释。'
            en[r['id']]['artwork_caption']='Form illustration · Explicit body structures follow the text; color, pose and unspecified details are artistic interpretations.'
            jobs.append({'name':'creature-'+slug,'entry_ids':[r['id']],'subject':visual,'category':'creature'})
    for slug,name,parent,q,desc,en_name,en_desc in WATERS:
        assert q in passages[parent]['quote'],name
        add('water-nanshan-'+slug,'water',name,parent,desc,en_name,en_desc,q,en_desc,group='natural_features')
    for slug,name,parent,desc,en_name,en_desc,visual in [
        ('yan','棪木','tangting','堂庭山多棪木。郭注说它的果实似柰而赤，可食；树叶与树形不是经文逐项给出的特征。','Yan tree','Yan trees occur at Tangting. The commentary describes red, apple-like fruit; the text does not fully specify leaves or tree form.','One complete fruit-bearing tree with modest red apple-like fruits. The tree silhouette and leaves are illustrative, not a botanical identification. No glowing magic effects.'),
        ('baigao','白䓘','lunzhe','白䓘像榖而有赤理，汁液如漆，味如饴。经文记食之不饥、释劳，郭注又释血玉为染玉；不以这些说法给出现代植物鉴定。','Tree of Lunzhe','A gu-like tree with red grain, lacquer-like sap and a sweet taste. Ancient uses are recorded without identifying a modern plant.','One complete paper-mulberry-like tree with subtle red grain visible on a natural exposed trunk patch and a small dark sap bead. No chopped logs, utensils, glowing fruit, human figures or exaggerated red foliage.')]:
        r=add('plant-nanshan-'+slug,'plant',name,parent,desc,en_name,en_desc,art=f'nanshan/plant-{slug}-v1.webp',group='natural_features')
        jobs.append({'name':'plant-'+slug,'entry_ids':[r['id']],'subject':visual,'category':'plant'})
    for slug,name,parent,desc,en_name,en_desc in [
        ('yuyi','育遗','maowei','旄山之尾南有育遗谷，多怪鸟，凯风从这里出来。谷地边界与形状没有另写。','Yuyi Valley','A valley south of Mount Mao’s tail, with strange birds, from which the Kai wind emerges.'),
        ('zhonggu','中谷','lingqiu','中谷在令丘山南，条风从这里出来。这里保留山南之谷与风源的文字关系。','Middle Valley','A valley south of Lingqiu from which the Tiao wind emerges.')]:
        add('valley-nanshan-'+slug,'valley',name,parent,desc,en_name,en_desc)
    for slug,name,parent,desc,en_name,en_desc in [
        ('kai','凯风','maowei','经文说凯风从育遗谷出来。郭注释为南风；图中云气仅用于场景示意。','Kai wind','The Kai wind emerges from Yuyi Valley; the commentary explains it as a southerly wind.'),
        ('tiao','条风','lingqiu','条风从令丘山南的中谷出来，郭注以东北风解释。这里记录古籍所述的风源。','Tiao wind','The Tiao wind emerges from Middle Valley; the commentary explains it as a northeasterly wind.')]:
        add('wind-nanshan-'+slug,'wind',name,parent,desc,en_name,en_desc)
    for slug,name,parent,desc,en_name,en_desc in [
        ('liuhuang','流黄','gui','柜山段写西临流黄，郭注把相关名称解释为山名；本段没有另述流黄的山形。','Liuhuang reference','Gui faces Liuhuang to the west; the commentary calls it a mountain name, without a separate form description.'),
        ('zhupi','诸毗 · 柜山段','gui','柜山北望诸毗，郭注在这里将其列为山名。与浮玉段被注为水名的诸毗分别保留。','Zhupi · Gui mountain reference','Gui looks north to Zhupi, treated as a mountain name here. The water reference at Fuyu is kept separate.'),
        ('qiushan','丘山','qiwu','漆吴山向东望丘山，原文继而写其光载出载入。不据这几句补造天文坐标或确定山形。','Qiushan reference','Qiwu looks east to Qiushan, followed by a description of appearing and disappearing light. No definite landform or astronomical coordinates are inferred.')]:
        r=add('place-nanshan-reference-'+slug,'place',name,parent,desc,en_name,en_desc)
        r['artwork_caption']='来源山段场景示意 · 不表示本参照地点的确定山形。'; en[r['id']]['artwork_caption']='Source-passage scene · This does not depict a confirmed form of the reference place.'
    for slug,name,parents,desc,en_name,en_desc in [
        ('white-ape','白猿',['tangting','fashuang'],'白猿见于堂庭与发爽两段，经文只记其多，没有另立特殊形貌或功效。','White apes','White apes occur at Tangting and Fashuang; no distinct supernatural structure or effect is specified.'),
        ('fu','蝮虫',['yuanyi','yu','feitou'],'蝮虫多见于猨翼、羽山与非山之首。郭注另有形貌解释，这里不据古名确定为某一现代毒蛇。','Fu creatures','Venomous creatures occur in several mountain passages. A modern species is not identified from the old name.'),
        ('ji-fish','鮆鱼',['fuyu'],'鮆鱼见于浮玉山苕水记述。郭注说其狭薄而长，又称刀鱼；这些解释与经文分开保存。','Ji fish','Ji fish occur in the Tiao River passage. The commentary describes a narrow, thin, elongated fish and another name.'),
        ('piluo','芘蠃',['xun'],'洵水中多芘蠃，郭注解释为紫色螺。配图复用水域场景，不作为现代物种鉴定图。','Piluo',['Piluo occur in Xun Water; the commentary describes purple snails. The shared water scene does not establish a modern species.'][0]),
        ('xi','犀',['daoguo'],'祷过山下多犀。郭注另描述其形貌，经文这一句没有列出角数；不以现代物种形态覆盖古注。','Xi','Xi are recorded below Daoguo. Horn numbers are not specified in this main-text statement.'),
        ('si','兕',['daoguo'],'兕与犀、象并记于祷过山下。郭注有似水牛、一角等解释，卡片保留这些层次而不作现代鉴定。','Si','Si occur below Daoguo with xi and elephants; the commentary compares them to water buffalo and mentions one horn.'),
        ('elephant','象',['daoguo'],'象见于祷过山下，底本正文用𧰼字。它与犀、兕同段出现，不据此补出共同行动的故事。','Elephants','Elephants occur below Daoguo, written with the edition glyph 𧰼. No joint action with the other animals is implied.')]:
        r=add('animal-nanshan-'+slug,'animal',name,parents[0],desc,en_name,en_desc)
        r['context_place_ids']=[mountain_ids[parent] for parent in parents]
        for parent in parents[1:]:
            r['source_passage_ids'].append(passages[parent]['id']); r['related_entry_ids'].append(passages[parent]['id']); by_passage[passages[parent]['id']].append(r['id'])
    for number,visual,cn,enform in [(1,'A bird body with exactly two wings and two bird feet, topped by one traditional dragon head.','鸟身龙首','bird bodies and dragon heads'),(2,'A long serpentine dragon body with one clear bird head, no human face.','龙身鸟首','dragon bodies and bird heads'),(3,'A long serpentine dragon body with one human face, no bird head.','龙身人面','dragon bodies and human faces')]:
        slug='range'+str(number); title=['','䧿山','南次二经','南次三经'][number]
        r=add('deity-nanshan-'+str(number),'deity',title+'诸神',slug,'本列山神的共同形貌为'+cn+'。这是山列总述，没有给出各神的独立名字。',f'Range {number} deities','The deities of this range have '+enform+'. Individual names are not supplied.',art=f'nanshan/deity-{number}-v1.webp',context=False)
        r['artwork_caption']='山神共同形貌示意 · 不代表某位有独立名字的神。'; en[r['id']]['artwork_caption']='Shared divine form · This is not a separately named deity.'
        jobs.append({'name':'deity-'+str(number),'entry_ids':[r['id']],'subject':visual+' A schematic image of the shared form of a range of deities, not a newly invented named god.','category':'deity'})
        add('rite-nanshan-'+str(number),'rite',title+'祭礼',slug,passages[slug]['description'],f'Range {number} rites',en[passages[slug]['id']]['description'],art=r['artwork'],context=False)
    world['text_entities']=list(records.values())
    for p in passages.values():
        p['related_entry_ids']=list(dict.fromkeys([*p.get('related_entry_ids',[]),*by_passage[p['id']]]))
    # Existing Southern creatures remain stable, now linked to their precise mountain cards.
    for beast_id,slug in [('beast-boyi','jishan'),('beast-gudiao','luwu'),('beast-phoenix','danxue')]:
        beast=next(b for b in world['beasts'] if b['id']==beast_id); beast['context_place_id']=mountain_ids[slug]
    phoenix=next(b for b in world['beasts'] if b['id']=='beast-phoenix')
    phoenix['context_place_ids']=[mountain_ids['danxue'],mountain_ids['nanyu']]
    passages['nanyu']['related_entry_ids']=list(dict.fromkeys([*passages['nanyu']['related_entry_ids'],'beast-phoenix']))
    for id,parents in [('water-nanshan-ju',['yi','kuaiji']),('water-nanshan-pang',['hushao','quwu','luwu']),('water-nanshan-bohai-south',['danxue','fashuang'])]:
        r=next(x for x in world['natural_features'] if x['id']==id)
        r['context_place_ids']=[mountain_ids[parent] for parent in parents]
        for parent in parents:
            p=passages[parent]
            p['related_entry_ids']=list(dict.fromkeys([*p['related_entry_ids'],id]))
            r['related_entry_ids']=list(dict.fromkeys([*r['related_entry_ids'],p['id']]))
    for b in world['beasts']:
        if b['id'] in ['beast-gudiao','beast-xuangui','beast-chiru','beast-nanshan-hujiao','beast-nanshan-zhuan']:b['relation_scope']='water'
    relations=[]
    for a,b,parent,quote in [
        ('fang','yu-receiver','jiwei','汸水出焉而南流注于淯'),('ying-gui','chishui-gui','gui','英水出焉西南流注于赤水'),
        ('tiao','juqu','fuyu','苕水出于其隂北流注于具區'),('shu','hushao-receiver','cheng','䦠水出焉而南流注于虖勺'),
        ('shao','ju','kuaiji','勺水出焉而南流注于湨'),('ju','lietu','yi','湨水出焉而南流注于列塗'),
        ('xun','yan-marsh','xun','洵水出焉而南流注于閼之澤'),('lu','pang','quwu','鹿水出焉而南流注于滂水'),
        ('zegeng','pang','luwu','澤更之水出焉而南流注于滂水'),('dan','bohai-south','danxue','丹水出焉而南流注于㴾海'),
        ('fan','bohai-south','fashuang','汎水出焉而南流注于㴾海')]:
        assert quote in passages[parent]['quote']
        relations.append({'ids':['water-nanshan-'+a,'water-nanshan-'+b],'source':'《南山经》','quote':quote,'labels':['流入此水','承接来水']})
    for water,id,parent,quote in [('yin','beast-nanshan-hujiao','daoguo','泿水出焉而南流注于海其中有虎蛟'),('hei','beast-nanshan-zhuan','ji','黒水出焉而南流注于海其中有鱄魚'),('zegeng','beast-gudiao','luwu','水有獸焉名曰蠱雕'),('tiao','animal-nanshan-ji-fish','fuyu','其中多鮆魚'),('xun','animal-nanshan-piluo','xun','其中多芘蠃')]:
        assert quote in passages[parent]['quote']
        relations.append({'ids':['water-nanshan-'+water,id],'source':'《南山经》','quote':quote,'labels':['水段所见','本段水域']})
    write('frontend/src/nanshan-entity-relations.json',relations)
    destination='frontend/artwork-source/nanshan/entities-generation.json'
    previous=read(destination) if (ROOT/destination).exists() else {'assets':[]}
    oldjobs={a['name']:a for a in previous['assets']}
    for r in [*world['beasts'],*world['natural_features'],*world['text_entities']]:
        if r.get('content_batch')!='nanshan-entities':continue
        art=r.get('artwork')
        job=oldjobs.get(Path(art).stem.removesuffix('-v1')) if art else None
        source=(ROOT/'frontend/artwork-source/nanshan'/job.get('source_file',Path(art).stem+'.png')) if job else (ROOT/'frontend/artwork-source'/art.replace('.webp','.png')) if art else None
        if art and art.startswith('nanshan/') and (not source.exists() or (job and job['status']!='reviewed')):
            r['planned_artwork']=art;r['artwork_pending']=True;r.pop('artwork',None)
        else:r.pop('planned_artwork',None);r.pop('artwork_pending',None)
    world['revision']='myth-world-2026-10-19-nanshan-entities-v4'
    write('frontend/public/data/myth-world.json',world); write('frontend/src/locale-content-en.json',en)
    style='Use case: illustration-story. A single antique Chinese woodcut illustration for a Shanhaijing atlas, matching carved charcoal knife lines, warm ivory forms, restrained ochre and muted celadon. Genuine transparent background outside irregular carved edges; no opaque rectangle, checkerboard, text, lettering, labels, seals, arrows, watermarks or modern objects. '
    for job in jobs:
        if job['category']=='scene': job['prompt']=style+'Wide landscape vignette. Illustrate the land and water description in this passage: '+job['subject']+' Focus on the mountain, water and recorded vegetation or its absence. DO NOT include animals, people, gods, rituals or literal magical effects. Mineral abundance is suggested subtly in rock texture. No extra modern geographic landmarks. Landform shape is artistic, not a reconstruction.'
        else: job['prompt']=style+job['subject']+' '+('Vertical composition, entire tree visible.' if job['category']=='plant' else 'Square composition, entire subject visible with generous margin; precise readable anatomy. No landscape or decorative halo.')
        job['reference_images']=[];job['review_note']='Pending visual review';job['status']='planned'
    for job in jobs:
        if job['name'] in oldjobs:job.update(oldjobs[job['name']])
    write(destination,{'tool':'built-in image_gen','transparent_background':True,'assets':jobs})
    write('data/nanshan-entity-coverage.json',{'scope':'南山经；常见草木物产留在山概况，泛称怪兽/怪鱼/怪木不虚构独立物种。', 'mountain_ids':list(mountain_ids.values()),'new_beast_ids':['beast-nanshan-'+b[0] for b in BEASTS], 'new_water_ids':['water-nanshan-'+r[0] for r in WATERS], 'text_entity_ids':[id for id,r in records.items() if r.get('content_batch')=='nanshan-entities'], 'artwork_jobs':[j['name'] for j in jobs], 'passage_links':by_passage})
    print('Southern mountain cards:',len(mountain_ids),'; new named creatures:',len(BEASTS),'; new waters:',len(WATERS),'; new artwork:',len(jobs))

if __name__=='__main__':build()
