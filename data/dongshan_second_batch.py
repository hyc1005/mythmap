"""Eastern stages 6–15: edition-specific readings and entities."""

def R(slug, en_name, description, en_description, en_quote, en_note):
    return dict(slug=slug,en_name=en_name,description=description,en_description=en_description,en_quote=en_quote,en_note=en_note)

ROWS=[
R('guer','Mount Guer','番條向南四百里为姑兒，上多漆、下多桑柘。姑兒水北注海，其中鱤魚与番條共用文本索引，仍无可据以绘制的独立形貌。','Guer lies 400 li south of Fantiao, with qi above and sang and zhe below. Guer water flows north into the sea. Gan fish share a textual index with Fantiao and retain an unspecified-form placeholder.','Four hundred li south is Mount Guer, with abundant qi above and sang and zhe below. Guer water rises here and flows north into the sea; Gan fish are abundant.','Units 16–17 are on scan 110. The shared Gan fish and sea indexes preserve separate contexts, without a modern species or coastline inference.'),
R('gaoshi-east','Mount Gaoshi (Eastern)','姑兒向南四百里为髙氏，上多玉、下多箴石。諸繩水东注泽，水中金玉另列。可以／為砥針治癰腫者跨行归箴石；古代治疗记述不作今用建议。不并北山髙是。','Gaoshi lies 400 li south of Guer, with jade above and zhen stone below. The Zhusheng flows east into an unnamed marsh, with gold and jade in its water account. The cross-line stone gloss describes an ancient treatment, not present advice; this mountain stays separate from the Northern Gaoshi.','Four hundred li south is Mount Gaoshi, with jade above and zhen stone below. The Zhusheng rises here and flows east into a marsh, with abundant gold and jade.','Unit 18 actually ends scan 110; 19 is on 111. The divided commentary belongs to zhen stone, not the water’s gold and jade. The unnamed marsh is not equated with Yue’s marsh.'),
R('yueshan','Mount Yue','髙氏向南三百里为嶽山，上桑下樗。濼水东注泽，水中金玉分录；音樂为水名郭注，不将两处未名泽强并。','Yue lies 300 li south of Gaoshi, with sang above and chu below. The Luo flows east into an unnamed marsh, with gold and jade recorded separately. The pronunciation gloss belongs to Luo water; the unnamed marsh is not equated with Gaoshi’s.','Three hundred li south is Mount Yue, with sang above and chu below. The Luo rises here and flows east into a marsh, with abundant gold and jade.','Units 20–21 are on scan 111. The pronunciation gloss belongs to the water name; the two unnamed marsh contexts remain separate.'),
R('chaishan','Mount Chai','嶽山向南三百里为犲山，上无草木、下多水。堪㐨之鱼郭注明言未详。另有未名兽状如夸父而彘毛、音如呼，洪水兆为古述；夸父比拟依据不足，不借逐日人物造型补图，两者均留占位。','Chai lies 300 li south of Yue, with no vegetation above and much water below. Commentary explicitly leaves Kanxu fish unexplained. An unnamed beast resembles Kuafu, has pig-like hair and a calling sound; its flood omen is ancient. Both retain placeholders, without borrowing the sun-chasing figure’s anatomy.','Three hundred li south is Mount Chai, without vegetation above and with much water below, containing Kanxu fish. A beast resembles Kuafu with pig-like hair and sounds like a call; its appearance is said to bring a great flood.','Units 22–24 are on scan 111. The fish gloss says unexplained and supplies xu pronunciation; Kanxu follows that gloss. The unnamed beast’s comparison does not securely establish independent anatomy.'),
R('dushan','Mount Du','犲山向南三百里为獨山，上多金玉、下多羙石。末塗水东南注沔。䖺䗤如黄蛇、鱼翼、出入有光，旱兆为古述；插画保蛇身及鱼鳍状膜翼，翼数、位置、鳞纹和亮纹为艺术解释。','Du lies 300 li south of Chai, with gold and jade above and fine stone below. The Motu flows southeast into the Mian. Tiaoyong resembles a yellow snake with fish wings and light on emerging and entering; its drought omen is ancient. Fin count, placement, scales and luminous incisions are artistic.','Three hundred li south is Mount Du, with gold and jade above and fine stone below. The Motu rises here and flows southeast into the Mian. Tiaoyong resembles a yellow snake with fish wings and shines on entering and emerging; its appearance is said to bring drought.','Units 25–27 are all on scan 111, including 27 captured as 112. Fish wings do not establish feathers or bat wings; light does not establish flames or a halo.'),
R('taishan-range1','Mount Tai (Eastern first range)','獨山向南三百里为泰山，上玉下金。狪狪豚状有珠、名自䚯；独立珠子的数量与位置属艺术解释。環水东注江，其中水玉另列；一作海归江的异文。山顶四十八里三百步是跨行山名郭注，不是狪狪形貌。','Tai lies 300 li south of Du, with jade above and gold below. Tongtong resembles a piglet, has pearls and calls its name; the depicted loose pearl’s count and position are artistic. The Huan flows east into the Jiang, with water jade; the sea variant belongs to Jiang. The summit-distance gloss describes the mountain, not the beast.','Three hundred li south is Mount Tai, with jade above and gold below. Tongtong resembles a piglet and has pearls, calling its own name. The Huan rises here and flows east into the Jiang; water jade is abundant.','Units 28–31 are on scan 112. The mountain gloss continues across 28–29. The sea variant follows Jiang, not water jade. This Tai remains separate from the later fourth-range mountain.'),
R('zhushan','Mount Zhu','泰山向南三百里为竹山，錞于江，无草木、多瑶碧。江后一作涯按原位置保留。激水东南注娶檀水，其中茈羸仅有名目，形貌不足留占位，不据别篇补形。','Zhu lies 300 li south of Tai and is described as adjoining the Jiang, without vegetation and with much yaobi. The variant ya follows Jiang in the captured layout. The Ji flows southeast into the Qutan, with Zilei named but not independently described; its placeholder borrows no form from another passage.','Three hundred li south is Mount Zhu, adjoining the Jiang, without grasses or trees and with much yaobi. The Ji rises here and flows southeast into the Qutan; Zilei are abundant.','Units 32–33 are on scan 112. The variant after Jiang is preserved in place without relocating it to Ji or Zilei. The shared Jiang index is textual and supplies no modern course.'),
R('range1-summary','First-range summary and rites','首列从樕𧑤至竹山，正文总括十二山、三千六百里。神皆人身龍首；祠毛用一犬、祈䎶用鱼为古礼。郭注血涂祭及引公羊传独存，配图只示人身龙首神，不画祭杀。','The first range runs from Suzhu to Zhu and reports twelve mountains and 3,600 li. Its gods have human bodies and dragon heads. A dog and fish belong to ancient rites; the blood-anointing gloss and Gongyang citation remain commentary. The image depicts only the deity’s stated form.','The first Eastern range, from Suzhu to Zhu, comprises twelve mountains and 3,600 li. Its gods all have human bodies and dragon heads. The fur offering uses one dog; the prayer and er rite use fish.','Units 34–36 are all on scan 112; 36 was captured as 113. The complete ritual gloss ends before the next range. The stated total is preserved without silently recalculating it.'),
R('kongsang-east','Mount Kongsang (Eastern second range)','东次二经首为空桑，北临食水，东望沮呉、南望沙𨹧、西望湣泽，四向不混。軨軨如牛而虎文、音如欽、鸣自叫，洪水兆为古述；或作吟归声音异文，音靈归名。琴瑟材为山名郭注，不添树种。','Kongsang opens the second Eastern range, facing Shi water northward, Ju Wu eastward, Shaling southward and Min marsh westward. Lingling is ox-shaped with tiger patterns and a qin-like sound, calling its name; its flood omen is ancient. The yin variant belongs to the sound and ling to the name. Instrument wood is commentary, without an identified tree species.','The second Eastern range begins at Mount Kongsang, facing Shi water to the north, Ju Wu to the east, Shaling to the south and Min marsh to the west. Lingling resembles an ox with tiger patterns, sounds like qin and calls its own name; its appearance is said to bring a great flood.','Units 37–40 are on scan 113. Four directions remain distinct; this mountain is not merged with Northern Kongsang. Shared Shi water records another textual context, not a surveyed river.'),
R('caoxi','Mount Caoxi','空桑向南六百里为曹夕，山下多榖而无水、多鸟兽。榖按植物名保留，不改作谷物；鸟兽为泛称，不补具体种类或形貌。','Caoxi lies 600 li south of Kongsang, with much gu below, no water and many birds and beasts. Gu remains a plant name rather than grain; the generic animals supply no individual species or anatomy.','Six hundred li south is Mount Caoxi, with much gu below, no water and many birds and beasts.','Unit 41 is on scan 113. The plant character and absence of water remain explicit; generic birds and beasts do not justify invented species.')
]

def entities(E):
    out=[]
    def add(slug,kind,key,name,en_name,q,cn,en,eq,**extra):
        out.append(E(slug,kind,key,name,en_name,q,cn,en,eq,**extra))
    def product(slug,kind,key,name,en_name,q,scope):
        add(slug,kind,key,name,en_name,q,scope+'；仅录本段名目，不补未述形貌、现代定位或成分。',scope_en[scope]+' The textual name supplies no unstated anatomy, modern location or composition.',scope_en[scope])
    scope_en={
      '姑兒山上多漆':'Qi is abundant above Guer.','姑兒山下多桑柘，此卡分录桑':'Sang and zhe occur below Guer; this card records sang.',
      '姑兒山下多桑柘，此卡分录柘':'Sang and zhe occur below Guer; this card records zhe.',
      '髙氏山上多玉':'Jade is abundant above Gaoshi.','諸繩水文多金玉，此卡分录金':'Gold and jade occur in the Zhusheng water account; this card records gold.',
      '諸繩水文多金玉，此卡分录玉':'Gold and jade occur in the Zhusheng water account; this card records jade.',
      '嶽山上多桑':'Sang is abundant above Yue.','嶽山下多樗':'Chu is abundant below Yue.',
      '濼水文多金玉，此卡分录金':'Gold and jade occur in the Luo water account; this card records gold.',
      '濼水文多金玉，此卡分录玉':'Gold and jade occur in the Luo water account; this card records jade.',
      '獨山上多金玉，此卡分录金':'Gold and jade occur above Du; this card records gold.',
      '獨山上多金玉，此卡分录玉':'Gold and jade occur above Du; this card records jade.',
      '獨山下多羙石':'Fine stone is abundant below Du.','泰山上多玉':'Jade is abundant above Tai.','泰山下多金':'Gold is abundant below Tai.',
      '環水文多水玉':'Water jade occurs in the Huan water account.','竹山多瑶碧':'Yaobi is abundant at Zhu.',
      '曹夕山下多榖':'Gu is abundant below Caoxi.'}
    for args in [
      ('guer','plant','qi-guer','漆（姑兒）','Qi (Guer)','其上多漆','姑兒山上多漆'),
      ('guer','plant','sang-guer','桑（姑兒）','Sang (Guer)','其下多桑柘','姑兒山下多桑柘，此卡分录桑'),
      ('guer','plant','zhe-guer','柘（姑兒）','Zhe (Guer)','其下多桑柘','姑兒山下多桑柘，此卡分录柘'),
      ('gaoshi-east','material','jade-gaoshi-east','玉（髙氏山上）','Jade (above Gaoshi)','其上多玉','髙氏山上多玉'),
      ('gaoshi-east','material','gold-zhusheng','金（諸繩水文）','Gold (Zhusheng account)','其中多金玉','諸繩水文多金玉，此卡分录金'),
      ('gaoshi-east','material','jade-zhusheng','玉（諸繩水文）','Jade (Zhusheng account)','其中多金玉','諸繩水文多金玉，此卡分录玉'),
      ('yueshan','plant','sang-yue','桑（嶽山）','Sang (Yue)','其上多桑','嶽山上多桑'),
      ('yueshan','plant','chu-yue','樗（嶽山）','Chu (Yue)','其下多樗','嶽山下多樗'),
      ('yueshan','material','gold-luo','金（濼水文）','Gold (Luo account)','其中多金玉','濼水文多金玉，此卡分录金'),
      ('yueshan','material','jade-luo','玉（濼水文）','Jade (Luo account)','其中多金玉','濼水文多金玉，此卡分录玉'),
      ('dushan','material','gold-du','金（獨山）','Gold (Du)','其上多金玉','獨山上多金玉，此卡分录金'),
      ('dushan','material','jade-du','玉（獨山）','Jade (Du)','其上多金玉','獨山上多金玉，此卡分录玉'),
      ('dushan','material','fine-stone-du','羙石（獨山）','Fine stone (Du)','其下多羙石','獨山下多羙石'),
      ('taishan-range1','material','jade-tai','玉（泰山）','Jade (Tai)','其上多玉','泰山上多玉'),
      ('taishan-range1','material','gold-tai','金（泰山）','Gold (Tai)','其下多金','泰山下多金'),
      ('taishan-range1','material','water-jade-huan','水玉（環水文）','Water jade (Huan account)','其中多水玉','環水文多水玉'),
      ('zhushan','material','yaobi-zhu','瑶碧（竹山）','Yaobi (Zhu)','多瑶碧','竹山多瑶碧'),
      ('caoxi','plant','gu-caoxi','榖（曹夕）','Gu (Caoxi)','其下多榖','曹夕山下多榖')]:product(*args)
    for s,k,n,en,q,cn,eq in [
      ('guer','guer','姑兒之水','Guer water','姑兒之水出焉北流注于海','姑兒水北注海，源、流向和受水体分录。','Guer water rises here and flows north into the sea.'),
      ('gaoshi-east','zhusheng','諸繩之水','Zhusheng water','諸繩之水出焉東流注于澤','諸繩水东注未名泽，不定现代河道。','The Zhusheng rises here and flows east into a marsh.'),
      ('gaoshi-east','ze-gaoshi','澤（髙氏受水体）','Unnamed marsh (Gaoshi recipient)','東流注于澤','髙氏段受水体仅称泽，不强并嶽山未名泽。','It flows east into a marsh.'),
      ('yueshan','luo','濼水','Luo water','濼水出焉東流注于澤','濼水出嶽山而东注未名泽；音樂为水名注。','The Luo rises here and flows east into a marsh.'),
      ('yueshan','ze-yue','澤（嶽山受水体）','Unnamed marsh (Yue recipient)','東流注于澤','嶽山受水体仅称泽，与髙氏段各存出处。','It flows east into a marsh.'),
      ('chaishan','unnamed-chai','水（犲山下）','Unnamed water (below Chai)','其下多水','犲山下多水，不补水名或流向。','There is much water below.'),
      ('dushan','motu','末塗之水','Motu water','末塗之水出焉而東南流注于沔','末塗水东南注沔，保留古述方向。','The Motu rises here and flows southeast into the Mian.'),
      ('dushan','mian','沔（末塗受水体）','Mian (Motu recipient)','東南流注于沔','沔为末塗受水体，不补现代河道。','It flows southeast into the Mian.'),
      ('taishan-range1','huan','環水','Huan water','環水出焉東流注于江','環水自泰山东注江；江另有一作海异文，不归水玉。','The Huan rises here and flows east into the Jiang.'),
      ('taishan-range1','jiang','江（泰山、竹山文本索引）','Jiang (Tai and Zhu textual index)','東流注于江','泰山環水注江、竹山錞于江逐段分录，不定现代同一河段。','It flows east into the Jiang.'),
      ('zhushan','ji-zhu','激水（竹山）','Ji water (Zhu)','激水出焉而東南流注于娶檀之水','激水东南注娶檀，不将江旁一作涯移给激水。','The Ji rises here and flows southeast into the Qutan.'),
      ('zhushan','qutan','娶檀之水','Qutan water','東南流注于娶檀之水','娶檀为激水受水体。','It flows southeast into the Qutan.'),
      ('kongsang-east','min-marsh','湣澤','Min marsh','西望湣澤','空桑西望湣泽；音旻归此泽名。','Kongsang faces Min marsh to the west.')]:
        extra={}
        if k=='luo':extra=dict(commentary='音樂',en_commentary='A pronunciation gloss for the Luo water name.')
        if k=='min-marsh':extra=dict(commentary='音旻',en_commentary='Guo Pu gives min pronunciation for the marsh name.')
        if k=='jiang':extra=dict(commentary='一作海',en_commentary='Jiang has sea as a textual variant in the Huan account.')
        add(s,'water',k,n,en,q,cn,eq,eq,**extra)
    add('gaoshi-east','material','zhenstone-gaoshi','箴石（髙氏）','Zhen stone (Gaoshi)','其下多箴石','箴石郭注可以／為砥針治癰腫者跨行连读，只作古代器用、治疗记载。','The divided commentary describes stone needles and an ancient treatment; it is retained as historical text.','Zhen stone is abundant below.',commentary='可以；為砥針治癰腫者',en_commentary='The cross-unit gloss describes making stone needles for treating swellings in antiquity.')
    for kind,key,n,en,q,cn,eq,extra in [
      ('beast','kanyu-chai','堪㐨之魚','Kanxu fish','其中多堪㐨之魚','堪㐨之鱼仅列名，郭注明言未详；统一占位不代表鱼形。','Kanxu fish are abundant in the water account.',dict(commentary='未詳音序',en_commentary='Guo Pu says unexplained and supplies the pronunciation xu.',water=True)),
      ('beast','kuafu-like-chai','夸父状彘毛兽（犲山未名）','Unnamed Kuafu-like beast (Chai)','有獸焉其状如夸父而彘毛其音如呼見則天下大水','未名兽如夸父而彘毛、音如呼，洪水兆为古述；不借逐日人物推定完整形貌。','An unnamed beast resembles Kuafu with pig-like hair and a calling sound; its appearance is said to bring a great flood.',{}),
      ('beast','zilei-zhu','茈羸（竹山）','Zilei (Zhu)','其中多茈羸','本段仅名茈羸，没有独立形貌；不借别篇造型。','Zilei are abundant in the water account.',dict(water=True))]:
        slug='zhushan' if key=='zilei-zhu' else 'chaishan'
        add(slug,kind,key,n,en,q,cn,'The passage supplies insufficient independent anatomy; a placeholder preserves the limits of its wording.',eq,unknown=True,**extra)
    add('dushan','beast','tiaoyong-dushan','䖺䗤','Tiaoyong','其中多䖺䗤其状如黄蛇魚翼出入有光見則其邑大旱','䖺䗤黄蛇状、鱼翼、出入有光。插画两片鱼鳍状膜翼的数量与位置、鳞纹与亮纹为艺术解释；不添羽翼、蝠翼、足或火焰。旱兆为古述。','Tiaoyong resembles a yellow snake with fish wings and light on entering and emerging. The two fin membranes, placement, scales and light incisions are artistic, without feathers, bat wings, legs or flames. The drought omen is ancient.','Tiaoyong resembles a yellow snake with fish wings and shines on entering and emerging; its appearance is said to bring drought.',commentary='條容二音',en_commentary='Guo Pu glosses the two syllables tiao and yong.',water=True)
    add('taishan-range1','beast','tongtong-taishan','狪狪','Tongtong','有獸焉其状如豚而有珠名曰狪狪其名自䚯','狪狪豚状有珠、名自䚯；配图一颗独立珠子的数量与位置、四裂蹄、毛色与坐姿为艺术解释，不作额珠器官或獠牙兽。','Tongtong resembles a piglet, has pearls and calls its name. One loose pearl, its placement, four cloven hooves, coat and seated pose are artistic, without a forehead jewel or tusks.','Tongtong resembles a piglet, has pearls and calls its own name.',commentary='音如吟桐之桐',en_commentary='Guo Pu supplies tong pronunciation.')
    add('range1-summary','deity','human-dragon-range1','人身龍首神（东山首列）','Human-bodied dragon-headed gods (Eastern first range)','其神状皆人身龍首','神形据正文人身龍首；图中一位代表，双人手双人足、龙首角须、服装配色与站姿为艺术解释。不画龙躯蛇尾或祭杀。','The main text gives human bodies and dragon heads. One representative, human hands and feet, dragon horns and whiskers, clothing, color and stance are artistic; no dragon torso, serpent tail or sacrifice is depicted.','Its gods all have human bodies and dragon heads.')
    add('range1-summary','rite','fur-offering-range1','祠毛用一犬（首列祭礼）','One-dog fur offering (first-range rite)','祠毛用一犬','古礼用一犬，独立于神形记载；不把祭物作新生物形貌或操作建议。','The ancient rite specifies one dog, separately from the deity’s anatomy; no animal illustration or present instruction is inferred.','The fur offering uses one dog.')
    add('range1-summary','rite','fish-er-range1','祈䎶用魚（首列祭礼）','Fish prayer and er rite (first range)','祈䎶用魚','用鱼为古礼，郭注血涂祭及公羊传引文完整独存，不画血腥祭杀。','Fish belong to an ancient rite. The full blood-anointing gloss and Gongyang citation remain separate commentary, without a graphic sacrifice.','The prayer and er rite use fish.',commentary='以血塗祭為䎶也公羊傳云蓋叩其鼻以䎶社音鈎餌之餌',en_commentary='Guo Pu explains er as an ancient blood-anointing rite, quotes the Gongyang tradition and supplies its pronunciation.')
    for key,n,en,q,eq in [('juwu','沮呉（空桑东望）','Ju Wu (eastward reference)','東望沮呉','Kongsang faces Ju Wu to the east.'),('shaling','沙𨹧（空桑南望）','Shaling (southward reference)','南望沙𨹧','Kongsang faces Shaling to the south.')]:
        add('kongsang-east','place',key,n,en,q,'空桑所望名目，保留原字与方位，不定现代坐标或擅加地类。',eq+' Its textual name supplies no modern coordinate or unstated landform.',eq)
    add('kongsang-east','beast','lingling-kongsang-east','軨軨（东次二）','Lingling (Eastern second range)','有獸焉其状如牛而虎文其音如欽其名曰軨軨其鳴自叫見則天下大水','軨軨牛状虎文，音如欽、鸣自叫。图中厚重前躯、炭黑底金纹、两短牛角、四裂蹄与近正面站姿为艺术解释；与首山鱅鱅分卡。洪水兆为古述。','Lingling is ox-shaped with tiger patterns and a qin-like sound, calling its name. Heavy shoulders, charcoal and gold colors, two short cattle horns, four cloven hooves and near-frontal pose are artistic. It stays separate from Yongyong; the flood omen is ancient.','Lingling resembles an ox with tiger patterns, sounds like qin and calls its name; its appearance is said to bring a great flood.',commentary='或作吟；音靈',en_commentary='Yin is a variant of the sound comparison; ling is the name pronunciation.')
    return out
