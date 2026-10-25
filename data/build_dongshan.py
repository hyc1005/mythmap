"""Merge reviewed Eastern passages without rebuilding other books."""
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
def read(path):
    return json.loads((ROOT / path).read_text(encoding='utf-8'))
def write(path, value):
    (ROOT / path).write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')

ROWS = [
dict(slug='suzhu',en_name='Mount Suzhu',
 description='东山经首山樕𧑤，北临乾昧；乾昧为郭注所称另一山名。食水东北注海，水文中鱅鱅之鱼如犂牛、音如彘鸣；犂牛似虎文来自郭注，不因鱼名增鱼鳍或因猪音画猪首。',
 en_description='Suzhu opens the Eastern account and faces Qianmei to the north, identified as a mountain in commentary. The Shi flows northeast into the sea. Yongyong fish resemble li oxen and sound like pigs; the tiger-patterned ox comparison comes from commentary, without added fish fins or a pig head.',
 en_quote='The Eastern mountain account begins at Mount Suzhu, facing Qianmei to the north. The Shi rises here and flows northeast into the sea. Yongyong fish are abundant in the water account, resembling li oxen and sounding like pigs.',
 en_note='Units 3–5 are on scan 109; the chapter heading and attribution in 1–2 are metadata. Qianmei is a mountain in commentary. The tiger-patterned ox gloss is separate from the main text and supplies no fish fins or pig anatomy.'),
dict(slug='leishan',en_name='Mount Lei',
 description='樕𧑤向南三百里为藟山，上有玉、下有金。湖水东注食水，水中多活師；郭注科斗也及尔雅称谓独列。蝌蚪释义来自郭注，配图不画成年蛙；山名音注疑字保留捕获。',
 en_description='Lei lies 300 li south of Suzhu, with jade above and gold below. The Hu flows east into the Shi, with Huoshi in the water account. Guo Pu identifies Huoshi as tadpoles and records an Erya name. The illustration follows this commentary identification, without an adult frog; the difficult mountain-name gloss remains captured.',
 en_quote='Three hundred li south is Mount Lei, with jade above and gold below. The Hu rises here and flows east into the Shi, with abundant Huoshi.',
 en_note='Units 6–7 are on scan 109. The tadpole identification is commentary, not a main-text anatomical statement. The difficult captured mountain pronunciation remains unresolved; the Hu–Shi confluence does not establish modern geography.'),
dict(slug='xunzhuang',en_name='Mount Xunzhuang',
 description='藟山向南三百里为栒状，上多金玉、下多青碧石。從從犬状六足、鸣自詨；䖪䑕鸡状鼠毛，旱兆为古述。𣲵水北注湖水，其中箴魚如儵、喙如箴；不借北山鸡状四首儵魚补本段形貌。青碧石、从从及后续鸟鱼各自分卡。',
 en_description='Xunzhuang lies 300 li south of Lei, with gold and jade above and qingbi stone below. Congcong is dog-shaped with six feet and calls its own name. Zishu is chicken-shaped with mouse-like hair; its drought omen is an ancient account. The Zhi flows north into the Hu, with Zhen fish compared to shu and having needle-like beaks. This comparison adds none of the Northern Youyu’s chicken form or multiple heads.',
 en_quote='Three hundred li south is Mount Xunzhuang, with gold and jade above and qingbi stone below. Congcong resembles a dog with six feet and calls its name. Zishu resembles a chicken with mouse-like hair; its appearance is said to bring drought to the settlement. The Zhi rises here and flows north into the Hu. Zhen fish resemble shu, with needle-like beaks, and eating them is said to prevent epidemic illness.',
 en_note='Units 8–9 are on scan 109; 9 was captured as 110 and is corrected only in the reading page index. Units 10–12 are on 110. Qingbi stone spans 8–9. The shu comparison is kept apart from the Northern chicken-shaped Youyu; the ancient eating claim is not present medical guidance.'),
dict(slug='boqi',en_name='Mount Boqi',
 description='栒状向南三百里为勃亝之山，无草木、无水。保留底本亝字及两项否定，不补动物、矿物、水道或山景插画。',
 en_description='Boqi lies 300 li south of Xunzhuang, without grasses, trees or water. The edition spelling and both absences remain, without invented animals, minerals, waterways or scenery.',
 en_quote='Three hundred li south is Mount Boqi, without grasses, trees or water.',
 en_note='Unit 13 is on scan 110. Its short account is a separate reading passage; the spelling is not silently normalized to a different edition.'),
dict(slug='fantiao',en_name='Mount Fantiao',
 description='勃亝向南三百里为番條，无草木而多沙。減水北注海，其中多鱤魚。音同与减損之减跨行连读归減水；一名黄頰、音感归鱤魚。鱼形未详，保留占位，不据现代鱼种补图。',
 en_description='Fantiao lies 300 li south of Boqi, without vegetation and with much sand. The Jian flows north into the sea and has Gan fish. The cross-line pronunciation comparison belongs to Jian water; the Huangjia alternative and gan pronunciation belong to the fish. Its form stays unspecified, with a placeholder rather than an inferred modern species.',
 en_quote='Three hundred li south is Mount Fantiao, without grasses or trees and with much sand. The Jian rises here and flows north into the sea; Gan fish are abundant in its water account.',
 en_note='Units 14–15 are on scan 110; 16 begins Guer. The water pronunciation spans units, while the fish-name gloss is separate. The sea is a shared textual recipient index, not a modern coastline.')
]
def E(slug,kind,key,name,en_name,quote,description,en_description,en_quote,**extra):
    return dict(slug=slug,kind=kind,id=f'{kind}-dongshan-{key}',name=name,en_name=en_name,
                quote=quote,description=description,en_description=en_description,en_quote=en_quote,**extra)
ENTITIES = [
E('suzhu','place','qianmei-suzhu','乾昧之山（北临）','Mount Qianmei (northward reference)','北臨乾昧','乾昧为樕𧑤北临之名，郭注亦山名也；非新列名行程山段，不补现代坐标。','Qianmei is the northern reference at Suzhu, identified as a mountain in commentary; it is not an added route mountain or modern coordinate.','Suzhu faces Qianmei to the north.',commentary='亦山名也音妺',en_commentary='Guo Pu identifies it as a mountain and supplies a pronunciation gloss.'),
E('suzhu','water','shi','食水（东山文本索引）','Shi water (Eastern textual index)','食水出焉而東北流注于海','樕𧑤记食水源出东北注海；藟山湖水东注食水另存。同篇索引不定现代河道，也不先并未核北號另一出处。','Suzhu records the Shi source and northeastward flow into the sea; Lei separately names it as the east-flowing Hu’s recipient. This textual index supplies no modern course or premature merger with Beihao.','The Shi rises here and flows northeast into the sea.'),
E('suzhu','water','sea','海（东山首列水文）','Sea (Eastern first-range water accounts)','東北流注于海','樕𧑤食水东北注海，番條減水北注海，方向与出处逐段分存，不补现代岸线。','The Shi at Suzhu flows northeast into the sea; the Jian at Fantiao flows north into the sea. Each direction and context remain distinct, without a modern coastline.','It flows northeast into the sea.'),
E('suzhu','beast','yongyong-suzhu','鱅鱅之魚','Yongyong fish','其中多鱅鱅之魚其状如犂牛其音如彘鳴','鱅鱅如犂牛、音如彘。犂牛似虎文是郭注；插画牛状虎纹据此，不因鱼名添鳍，猪音不添猪首。无角、四裂蹄、体色与姿态为艺术解释。','Yongyong resembles a li ox and sounds like a pig. Tiger-patterned ox form follows commentary, without fish fins or a pig head. Hornless form, four cloven hooves, color and pose are artistic.','Yongyong fish resemble li oxen and sound like pigs.',commentary='音容；牛似虎文者',en_commentary='Guo Pu supplies rong as the pronunciation and describes the compared ox as tiger-patterned.',water=True),
E('leishan','material','jade-leishan','玉（藟山）','Jade (Lei)','其上有玉','藟山上有玉，颜色与现代成分未详。','Jade occurs above Lei; color and modern composition are unstated.','There is jade above.'),
E('leishan','material','gold-leishan','金（藟山）','Gold (Lei)','其下有金','藟山下有金，仅按古物产词存录。','Gold is recorded below Lei as a textual product term.','There is gold below.'),
E('leishan','water','hu','湖水（藟山、栒状文本索引）','Hu water (Lei and Xunzhuang index)','湖水出焉東流注于食水','藟山湖水出而东注食水；栒状𣲵水北注湖水另存。湖水为本段水名，不据湖字补湖岸。','Lei gives the Hu source and eastward flow into the Shi; Xunzhuang separately records north-flowing Zhi entering Hu. Its textual name supplies no lake shoreline.','The Hu rises here and flows east into the Shi.'),
E('leishan','beast','huoshi-leishan','活師（藟山）','Huoshi (Lei)','其中多活師','正文仅名活師，郭注科斗也并引尔雅称谓；据注蝌蚪形作图。圆体、双目、无可见足及尾膜弯姿为解释，不定现代蛙种。','The main text names Huoshi; commentary identifies it as a tadpole and gives an Erya name. Rounded body, two eyes, no visible developing legs, tail membrane and curve are artistic, without a modern frog species.','Huoshi are abundant in the water account.',commentary='科斗也爾雅謂之活東',en_commentary='Guo Pu identifies it as a tadpole and records the Erya name huodong.',water=True),
E('xunzhuang','material','gold-xunzhuang','金（栒状）','Gold (Xunzhuang)','其上多金玉','山上金玉并录，此卡分录金，不添矿带图。','Gold and jade are recorded above; this card isolates gold without invented mineral mapping.','Gold and jade are abundant above.'),
E('xunzhuang','material','jade-xunzhuang','玉（栒状）','Jade (Xunzhuang)','其上多金玉','本山玉与金并列，不借藟山物产图。','Jade stands beside gold in this context, without borrowed Lei imagery.','Gold and jade are abundant above.'),
E('xunzhuang','material','qingbistone-xunzhuang','青碧石（栒状）','Qingbi stone (Xunzhuang)','其下多青碧石','青碧石跨0008—0009连读，保留一项，不拆青、碧、石三矿。','Qingbi stone spans units 8–9 and remains one product, not three inferred minerals.','Qingbi stone is abundant below.'),
E('xunzhuang','beast','congcong-xunzhuang','從從','Congcong','有獸焉其状如犬六足其名曰從從其鳴自詨','從從犬状六足，鸣自詨。插画须六条足胫与六犬爪逐个可数；三对足位、毛色与低行姿为艺术解释，不添角翼或人面。','Congcong is dog-shaped with six feet and calls its name. Six independent legs and dog paws must be countable; the three-pair arrangement, coat color and low stance are artistic, without horns, wings or a human face.','Congcong resembles a dog with six feet and calls its own name.'),
E('xunzhuang','beast','zishu-xunzhuang','䖪䑕','Zishu','有鳥焉其状如鷄而䑕毛其名曰䖪䑕見則其邑大旱','䖪䑕鸡状鼠毛，旱兆为古述。插画保鸡首鸟体与鼠般短毛，不画鼠头、鼠耳或鼠尾；配色、收翼与两鸟足为艺术解释。','Zishu is chicken-shaped with mouse-like hair and an ancient drought omen. Its image retains a chicken head and bird body with short fur, without a mouse head, ears or tail. Color, folded wings and two bird feet are artistic.','Zishu resembles a chicken with mouse-like hair; its appearance is said to bring drought to the settlement.',commentary='音咨',en_commentary='Guo Pu supplies zi pronunciation.'),
E('xunzhuang','water','zhi-xunzhuang','𣲵水（栒状）','Zhi water (Xunzhuang)','𣲵水出焉而北流注于湖水','𣲵水从栒状出、北注湖水；音枳属水名。保留𣲵字，不与北山洧、滋或其他同音水合并。','The Zhi rises at Xunzhuang and flows north into the Hu; the zhi gloss belongs to this water name. Its edition character stays separate from other similarly pronounced waters.','The Zhi rises here and flows north into the Hu.',commentary='音枳',en_commentary='Guo Pu gives zhi pronunciation.'),
E('xunzhuang','beast','zhen-xunzhuang','箴魚（栒状）','Zhen fish (Xunzhuang)','其中多箴魚其状如儵其喙如箴食之無疫疾','箴魚如儵、喙如箴。图中概括细鱼体、针状长喙，身色、鳍尾与姿态为解释；儵之比拟不借北山鸡状多首儵魚，也不强定现代针鱼种。食用无疫为古述。','Zhen fish are compared to shu and have needle-like beaks. The generalized slim fish body, colors, fins, tail and pose are artistic, without a modern species claim or the Northern Youyu’s chicken form and multiple heads. The eating claim is ancient.','Zhen fish resemble shu, have needle-like beaks, and are said to prevent epidemic illness when eaten.',commentary='出東海今江東水中亦有之',en_commentary='Guo Pu reports them in the Eastern Sea and in the waters of Jiangdong in his time; these are ancient references.',water=True),
E('fantiao','material','sand-fantiao','沙（番條）','Sand (Fantiao)','多沙','番條多沙，只录物产，不据此推现代沙漠。','Sand is abundant, without a modern desert inference.','There is much sand.'),
E('fantiao','water','jian-fantiao','減水（番條）','Jian water (Fantiao)','減水出焉北流注于海','減水北注海，音同与减損之减跨行连读，非另一个同水。','The Jian flows north into the sea. Its cross-line pronunciation comparison does not create a separate Tong water.','The Jian rises here and flows north into the sea.',commentary='音同减損之减',en_commentary='The cross-unit gloss compares the pronunciation to jian in the phrase for reduction.'),
E('fantiao','beast','gan-fantiao','鱤魚（番條）','Gan fish (Fantiao)','其中多鱤魚','鱤魚正文只列名，郭注一名黄頰、音感，未详独立形貌；暂用占位，不按现代同名鱼补头身和鳍尾。','Gan fish are only named in the main text. Commentary gives Huangjia as another name and the pronunciation gan, without an independent anatomical description; the placeholder adds no modern namesake’s form.','Gan fish are abundant in the water account.',commentary='一名黄頰音感',en_commentary='Guo Pu gives Huangjia as another name and glosses gan.',water=True,unknown=True)
]

from dongshan_second_batch import ROWS as SECOND_ROWS, entities as second_entities
ROWS += SECOND_ROWS
ENTITIES += second_entities(E)
from dongshan_third_batch import ROWS as THIRD_ROWS, entities as third_entities
ROWS += THIRD_ROWS
ENTITIES += third_entities(E)

def build():
    review=read('data/dongshan-edition-review.json')
    chapter=read('data/shanhaijing-reference.json')['chapters'][3]
    world=read('frontend/public/data/myth-world.json');english=read('frontend/src/locale-content-en.json')
    stages={s['slug']:s for s in review['stage_plan']}
    jobs={a['entry_id']:a for a in read('frontend/artwork-source/dongshan/entities-generation.json')['assets']}
    passages=[];cards=[];corrections=review['source_unit_page_corrections']
    for order,row in enumerate(ROWS,1):
        slug=row['slug'];stage=stages[slug];a,b=stage['source_units'];refs=chapter['lines'][a-1:b]
        captured=''.join(l['text'] for l in refs);raw=re.sub(r'⟦缺字图:([^⟧]+)⟧',r'\1',captured);pid='passage-dongshan-'+slug;place=('rite' if stage['kind']=='summary' else 'place')+'-dongshan-'+slug
        pages=stage['facsimile_pages'];urls=[f'https://zh.wikisource.org/wiki/Page:Sibu_Congkan0465-郭璞-山海經-2-1.djvu/{p}' for p in pages]
        source='《山海经·东山经》（《四部丛刊》景明成化本，郭璞传）'
        common=dict(source=source,source_chapter='《东山经》',source_book=4,region='东山经',source_locator='卷第四 · 影印页 '+'、'.join(map(str,pages)),source_pages=urls,url=urls[0],source_unit_ids=stage['source_unit_ids'],reveal_chapter='04',content_batch='dongshan-'+slug,review_status='facsimile_reviewed',artwork_pending=True,direction='按东山经篇内顺序及古述方位阅读，不换算现代坐标或实测里程。',editorial_note='经文、捕获和郭注分存；白话及英文为项目整理。食用、治病与灾异属古籍记述。')
        encommon=dict(source='Shanhaijing · Eastern Mountains (Sibu Congkan edition, Guo Pu commentary)',source_chapter='Dongshan Jing',region='Dongshan Jing',source_locator='Volume 4 · scan pages '+', '.join(map(str,pages)),direction='Read the Eastern textual sequence and ancient directions, not modern coordinates or measured distances.',editorial_note='Text, captured transcription and commentary remain separate. Explanations and English are editorial; eating, healing and omen claims are ancient accounts.')
        commentary='\n'.join(f'〔影印页{corrections.get(id,int(line["page"].split("/")[-1]))}〕'+'；'.join(line['annotations']) for id,line in zip(stage['source_unit_ids'],refs) if line['annotations'])
        p={**common,'id':pid,'kind':'passage','name':stage['name'],'range':stage['range'],'order':order,'description':row['description'],'quote':raw,'captured_text':captured,'commentary_quote':commentary,'captured_commentary':[{'source_unit_id':id,'annotations':l['annotations']} for id,l in zip(stage['source_unit_ids'],refs)],'content_note':stage['note'],'source_span':[sum(len(x['text']) for x in chapter['lines'][:a-1]),sum(len(x['text']) for x in chapter['lines'][:b])],'subjects':[stage['name']],'related_entry_ids':[place]}
        english[pid]={**encommon,'name':row['en_name'],'description':row['en_description'],'quote':row['en_quote'],'content_note':row['en_note']}
        cards.append({**common,'id':place,'kind':('rite' if stage['kind']=='summary' else 'place'),'name':stage['name'],'description':row['description'],'quote':raw,'commentary_quote':commentary,'content_note':stage['note'],'source_passage_ids':[pid],'related_entry_ids':[pid]})
        english[place]=dict(english[pid])
        comments=''.join(x for l in refs for x in l['annotations'])
        for e in [e for e in ENTITIES if e['slug']==slug]:
            assert e['quote'] in raw,e['id']
            for q in e.get('commentary','').split('；'):
                assert not q or q in comments,(e['id'],q)
            c={**common,**{k:e[k] for k in ['id','kind','name','quote','description']},'commentary_quote':e.get('commentary',''),'context_place_id':place,'source_passage_ids':[pid],'related_entry_ids':[pid]}
            english[c['id']]={**encommon,'name':e['en_name'],'description':e['en_description'],'quote':e['en_quote'],'commentary_quote':e.get('en_commentary','')}
            if e['kind']=='water' or e.get('water'):c['relation_scope']='water'
            if e.get('unknown'):
                c.update(appearance_unknown=True,artwork_caption='形貌未详或依据不足 · 统一问号占位不代表本生物形态。')
                english[c['id']]['artwork_caption']='Appearance unspecified or evidence insufficient; the shared question-mark placeholder is not a depiction.'
            elif (art:=jobs.get(e['id'])) and art['status']=='reviewed':
                c.update(artwork='dongshan/'+art['name']+'-v1.webp',artwork_pending=False,artwork_caption='经文或郭注形貌与木刻演绎 · 器官依据见说明，配色、比例和姿态为艺术解释。')
                english[c['id']]['artwork_caption']='Textual or commentary-based form in woodcut interpretation; the description identifies the evidence, while colors, proportions and pose are artistic.'
            if stage['kind']=='summary':
                c.pop('context_place_id',None)
                c['related_entry_ids'].append(place)
                next(x for x in cards if x['id']==place)['related_entry_ids'].append(c['id'])
            cards.append(c);p['subjects'].append(c['name']);p['related_entry_ids'].append(c['id'])
        passages.append(p)
    index={x['id']:x for x in cards+passages}
    def share(id,slug,q,eq):
        c=index[id];p=index['passage-dongshan-'+slug];place='place-dongshan-'+slug
        c['source_passage_ids']=[*c['source_passage_ids'],p['id']]
        c['context_place_ids']=list(dict.fromkeys([c['context_place_id'],*c.get('context_place_ids',[]),place]))
        c['source_unit_ids']=list(dict.fromkeys([*c['source_unit_ids'],*p['source_unit_ids']]))
        c['source_pages']=list(dict.fromkeys([*c['source_pages'],*p['source_pages']]))
        c['source_locator']='卷第四 · 影印页 '+'、'.join(str(x) for x in sorted({int(u.split('/')[-1]) for u in c['source_pages']}))
        c['quote']+='；'+q;c['related_entry_ids'].append(p['id']);p['related_entry_ids'].append(id)
        c['content_note']='分号分隔不同段落摘句；共享文本名目不代表现代地理同一性已定。'
        english[id]['quote']+=' Separately, '+eq
        english[id]['source_locator']='Volume 4 · scan pages '+', '.join(str(x) for x in sorted({int(u.split('/')[-1]) for u in c['source_pages']}))
        english[id]['content_note']='Semicolons separate excerpts from different passages; the shared textual index does not settle modern geographic identity.'
    share('water-dongshan-shi','leishan','東流注于食水','the Hu flows east into the Shi.')
    share('water-dongshan-hu','xunzhuang','北流注于湖水','the Zhi flows north into the Hu.')
    share('water-dongshan-sea','fantiao','北流注于海','the Jian flows north into the sea.')
    share('water-dongshan-sea','guer','北流注于海','the Guer flows north into the sea.')
    share('beast-dongshan-gan-fantiao','guer','其中多鱤魚','Gan fish are abundant in the Guer water account.')
    share('water-dongshan-shi','kongsang-east','北臨食水','Kongsang faces Shi water to the north.')
    share('water-dongshan-jiang','zhushan','錞于江','Zhu adjoins the Jiang.')
    links=[('water-dongshan-shi','water-dongshan-sea'),('water-dongshan-shi','beast-dongshan-yongyong-suzhu'),('water-dongshan-hu','water-dongshan-shi'),('water-dongshan-hu','beast-dongshan-huoshi-leishan'),('water-dongshan-zhi-xunzhuang','water-dongshan-hu'),('water-dongshan-zhi-xunzhuang','beast-dongshan-zhen-xunzhuang'),('water-dongshan-jian-fantiao','water-dongshan-sea'),('water-dongshan-jian-fantiao','beast-dongshan-gan-fantiao')]
    links += [('water-dongshan-guer','water-dongshan-sea'),('water-dongshan-guer','beast-dongshan-gan-fantiao'),('water-dongshan-zhusheng','water-dongshan-ze-gaoshi'),('water-dongshan-luo','water-dongshan-ze-yue'),('water-dongshan-unnamed-chai','beast-dongshan-kanyu-chai'),('water-dongshan-motu','water-dongshan-mian'),('water-dongshan-motu','beast-dongshan-tiaoyong-dushan'),('water-dongshan-huan','water-dongshan-jiang'),('water-dongshan-ji-zhu','water-dongshan-qutan'),('water-dongshan-ji-zhu','beast-dongshan-zilei-zhu')]
    links += [('water-dongshan-yigao', 'water-dongshan-jinv'), ('water-dongshan-yigao', 'beast-dongshan-shen-yigao'), ('water-dongshan-yigao', 'beast-dongshan-yao-yigao'), ('water-dongshan-li-geshan-head', 'water-dongshan-yu-marsh'), ('water-dongshan-li-geshan-head', 'beast-dongshan-zhubie-geshan-head'), ('water-dongshan-zayu', 'water-dongshan-huang-yue'), ('beast-dongshan-qiuyu-yue', 'animal-dongshan-zhong-yue'), ('beast-dongshan-qiuyu-yue', 'animal-dongshan-huang-insects-yue')]
    for a,b in links:
        index[a]['related_entry_ids'].append(b);index[b]['related_entry_ids'].append(a)
    for a,b in zip(passages,passages[1:]):
        a['related_entry_ids'].append(b['id']);b['related_entry_ids'].append(a['id'])
    batches={'dongshan-'+r['slug'] for r in ROWS}
    for group,values in [('passages',passages),('text_entities',[c for c in cards if c['kind'] in {'place','rite','deity','animal'}]),('beasts',[c for c in cards if c['kind']=='beast']),('natural_features',[c for c in cards if c['kind'] in {'water','material','plant'}])]:
        world[group]=[c for c in world[group] if c.get('content_batch') not in batches]+values
    world['revision']='myth-world-2026-10-25-dongshan-twenty-v1'
    review.update(status='partially_implemented',scope='前20阅读段已核109—115页；全篇段界已规划，其他段待双语、实体及页面接入。',implemented_stages=20,remaining_stages=31,entry_ids=[c['id'] for c in cards],passages=[dict(id=p['id'],source_unit_ids=p['source_unit_ids'],source_span=p['source_span'],status='facsimile_reviewed') for p in passages],batch_size=5,next=dict(name='耿山',source_units=[56,58],facsimile_pages=[115],status='pending_bilingual_entity_review'),artwork_summary=dict(selected=sum(a['status']=='reviewed' for a in jobs.values()),appearance_unknown=sum(c.get('appearance_unknown',False) for c in cards)))
    for stage in review['stage_plan'][:20]:
        stage.update(content_status='facsimile_reviewed',browser_status='see local handoff acceptance',passage_id='passage-dongshan-'+stage['slug'],new_cards=sum(c['content_batch']=='dongshan-'+stage['slug'] for c in cards))
    for issue in review['glyph_issues']:
        if issue['kind']=='missing_image_glyph':
            matches=[p for p in passages if issue['source_unit_id'] in p['source_unit_ids']]
            if matches:issue.update(status='restored_in_reading_layer',passage_id=matches[0]['id'])
    assert len(cards)==len(ENTITIES)+len(ROWS),len(cards)
    write('frontend/public/data/myth-world.json',world);write('frontend/src/locale-content-en.json',english);write('data/dongshan-edition-review.json',review)
    print(f'Built Eastern: {len(passages)} passages, {len(cards)} cards; 31 stages remain')
if __name__=='__main__':
    build()
