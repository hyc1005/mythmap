"""Reviewed Northern continuation: Liangqu through Chongwei, source units 133–201."""


def R(slug, name, en_name, units, description, en_description, en_quote, note, en_note, range=3, **extra):
    return dict(slug=slug, name=name, en_name=en_name, units=units, description=description,
                en_description=en_description, en_quote=en_quote, note=note, en_note=en_note,
                range=range, **extra)


ROWS = [
    R('liangqu','梁渠之山','Mount Liangqu',(133,137),
      '北囂向北三百五十里为梁渠，无草木，多金玉。脩水东注鴈門，郭注明言水名。居暨如彚而赤毛，音如豚；囂鸟如夸父、四翼一目犬尾，其主体比拟未定，不借别山舉父补形。',
      'Liangqu lies 350 li north of Beixiao, without vegetation and with gold and jade. The Xiu flows east into Yanmen, explicitly a water name in commentary. Juji resembles hui with red hair. Xiao has four wings, one eye and a dog tail, but its Kuafu comparison remains unresolved.',
      'Three hundred and fifty li north is Mount Liangqu, without vegetation and with gold and jade. The Xiu rises here and flows east into Yanmen. Juji resembles hui with red hair and a pig-like sound. Xiao resembles Kuafu, with four wings, one eye and a dog tail, sounds like a magpie, and is said to relieve abdominal pain and dong when eaten.',
      '0133—0135在90页，0135捕获91校回90；0136—0137在91页。囂缺字图恢复。或作舉父释夸父比拟，不据此借西山器官；鴈門独作本段水名，不并少咸。',
      'Units 133–135 are on scan 90; 135 was captured as 91. Units 136–137 are on scan 91. Xiao is restored. The Jufu variant concerns the Kuafu comparison, without borrowed Western anatomy. Yanmen remains this passage’s water name.',range=2),
    R('guguan','姑灌之山','Mount Guguan',(138,138),
      '梁渠向北四百里为姑灌，无草木，冬夏有雪。保留独立短段，不与湖灌混名，也不补物产、生物或现代雪线。',
      'Guguan lies 400 li north of Liangqu, without vegetation and with snow in winter and summer. It remains separate from Huguan, without invented products or a modern snow line.',
      'Four hundred li north is Mount Guguan, without grasses or trees, with snow in winter and summer.',
      '0138全核91页；姑灌与0139湖灌不同山，不因近名合并。',
      'Unit 138 is on scan 91. Guguan and the following Huguan remain distinct.',range=2),
    R('huguan','湖灌之山','Mount Huguan',(139,141),
      '姑灌向北三百八十里为湖灌，阳多玉、阴多碧，多马。湖灌水东注海，水文列䱇，郭注仅释亦鱓鱼字；另有叶如柳而赤理的无名木。马与䱇不借别处形貌，树的分枝根形为插画解释。',
      'Huguan lies 380 li north of Guguan, with jade on its sunny side, bi on the shaded side and many horses. Its river flows east into the sea; shan is only glossed as another eel character. An unnamed tree has willow-like leaves and red grain.',
      'Three hundred and eighty li north is Mount Huguan, with jade on its sunny side, bi on its shaded side and many horses. Huguan water rises here and flows east into the sea, with abundant shan. An unnamed tree has leaves like willow and red grain.',
      '0139—0141全在91页。䱇的字义注不当详细形貌；赤理按纹理记，不强定红叶或现代树种。',
      'Units 139–141 are on scan 91. Shan’s spelling gloss is not detailed anatomy. Red grain adds no red leaves or modern species.',range=2),
    R('huan','洹山','Mount Huan',(142,144),
      '向北水行五百里、流沙三百里至洹山，上多金玉。三桑生此，树皆无枝、高百仞；百果树生此，下多怪蛇。路程两段不合并为单纯陆程，怪蛇与百果树仅列名。',
      'Huan is reached northward by 500 li on water and 300 li through flowing sand, kept as distinct route segments. It has gold and jade, branchless Sansang trees a hundred ren tall, fruit trees and strange snakes.',
      'Northward, travel five hundred li by water and three hundred li through flowing sand to Mount Huan. Gold and jade occur above. Sansang trees grow here, all branchless and a hundred ren tall. Fruit trees grow here; strange snakes are abundant below.',
      '0142—0144在91页，0144捕获92校回91。三桑作为名目不强定三株；无枝树干代表图不补叶果或换算百仞。流沙不并西山同名。',
      'Units 142–144 are on scan 91; 144 was captured as 92. Sansang is not forced into an exact count of three; the representative trunk adds no foliage or height conversion. Flowing sand is a local route account.',range=2),
    R('dunti','敦題之山','Mount Dunti',(145,146),
      '洹山向北三百里为敦題，无草木、多金玉，是錞于北海。錞字及临北海的古述照录，不与敦頭、敦薨混名，不补现代海岸线。',
      'Dunti lies 300 li north of Huan, without vegetation and with gold and jade, described as chun against the Northern Sea. The difficult term and coastal account remain ancient, distinct from Duntou and Dunhong.',
      'Three hundred li north is Mount Dunti, without grasses or trees and with gold and jade; it stands chun against the Northern Sea.',
      '0145—0146核92页，北海跨行续，不将海字删去；錞不擅改为现代地貌术语。',
      'Units 145–146 are on scan 92. Northern Sea continues across the line break; chun is not silently replaced by a modern landform term.',range=2),
    R('range2-summary','北次二经总括与祭礼','Second Northern range summary and rites',(147,150),
      '总括自管涔至敦題，原报十七山、五千六百九十里；逐段列名为16山，差异保留，不补山凑数。神皆蛇身人面。祭礼牲瘗埋，璧珪投而不糈；郭注明确投玉不埋，与牲祭分开。',
      'The summary reports 17 mountains and 5,690 li from Guancen to Dunti, against 16 named mountain passages; the discrepancy remains. Deities have serpent bodies and human faces. Animal burial and the casting of bi and gui jade without ritual grain are distinct rites.',
      'The second Northern range runs from Guancen to Dunti: seventeen mountains, five thousand six hundred and ninety li. Its deities all have serpent bodies and human faces. The animal offering records a cock and pig with burial; one bi and one gui are cast, without ritual grain.',
      '0147—0150核92页，0149彘缺字图恢复，0150空正文的之也承投玉不埋注。原报17与列名16另记，牲埋和玉投不混，不补彘数量。',
      'Units 147–150 are on scan 92. Zhi is restored; empty main-text unit 150 continues the no-burial jade gloss. Reported 17 and named 16 remain separate. Pig count is not invented.',range=2,entry_kind='rite'),
    R('taihang','太行之山','Mount Taihang',(151,155),
      '北次三经首曰太行，其首曰歸山；归山上有金玉，下有碧。䮝如麢羊，四角、马尾、有距、善还；䴅鹊状白身赤尾六足，善惊。太行与归山分层建档，不把郭注古地名换成坐标。',
      'The third Northern range opens with Taihang, whose head is called Gui. Gui has gold and jade above and bi below. Hui is antelope-like with four horns, a horse tail and spurs; Fen is magpie-shaped, white-bodied, red-tailed and six-legged.',
      'The third Northern range begins with Mount Taihang; its head is called Mount Gui. Gold and jade occur above, bi below. Hui resembles lingyang with four horns, a horse tail and spurs, turns well and calls its name. Fen resembles a magpie with a white body, red tail and six legs, is easily startled and calls its name.',
      '0151—0153在92页，0153捕获93校回92；0154—0155核93页。归山作为太行之首单卡，物产与生物归其上下文。距位置数量、四蹄与配色为解释；新开次三目录。',
      'Units 151–153 are on scan 92; 153 was captured as 93. Units 154–155 are on scan 93. Gui is a nested place; its objects use that context. Spur placement, number and colors are artistic. Range three has its own catalog group.'),
    R('longhou','龍侯之山','Mount Longhou',(156,159),
      '太行向东北二百里为龍侯，无草木、多金玉。决决水向东注河，人鱼如䱱鱼四足、音如婴儿；郭注以鲵似鲇四足说明，不画人首人身或现代美人鱼。',
      'Longhou lies 200 li northeast of Taihang, without vegetation and with gold and jade. The Juejue flows east into the He. Renyu resembles ti fish with four feet and an infant-like cry; Guo Pu’s catfish comparison adds no human anatomy.',
      'Two hundred li northeast is Mount Longhou, without vegetation and with gold and jade. The Juejue rises here and flows east into the He. Renyu resembles ti fish with four feet and an infant-like cry; eating it is said to prevent chi illness.',
      '0156—0159核93页。音訣归决决，䱱注跨158—159连读；不将人鱼名当人身，食用与癡疾为古述。',
      'Units 156–159 are on scan 93. The jue gloss belongs to the river; the ti gloss spans 158–159. Renyu’s name adds no human body; the illness claim remains ancient.'),
    R('macheng','馬成之山','Mount Macheng',(160,164),
      '龍侯向东北二百里为馬成，上多文石、阴多金玉。天马如白犬黑头，见人飞，肉翅来自郭注；鶌鶋如乌，首白身青足黄。寓的释义未详与猶誤异说并存，不强定现代病名。',
      'Macheng lies 200 li northeast of Longhou, with patterned stones above and gold and jade on its shaded side. Tianma is a white dog with a black head, flying on seeing people; fleshy wings are commentary. Quju is crow-shaped, white-headed, qing-bodied and yellow-footed.',
      'Two hundred li northeast is Mount Macheng, with patterned stones above and gold and jade on its shaded side. Tianma resembles a white dog with a black head, flies on seeing people and calls its name. Quju resembles a crow with a white head, qing body and yellow feet, calls its name, and is said to prevent hunger and relieve yu when eaten.',
      '0160—0162在93页，0162捕获94校回93；0163—0164在94页。天马不是马形，双肉翼数为解释。屈居两音归鶌鶋，或作鳴疑义保留；寓未详不现代诊断。',
      'Units 160–162 are on scan 93; 162 was captured as 94. Units 163–164 are on 94. Tianma is dog-shaped; two fleshy wings are artistic. The Quju pronunciation and variant remain separate from uncertain yu.'),
    R('xianshan','咸山','Mount Xian',(165,167),
      '馬成向东北七十里为咸山，上多玉、下多铜，多松栢，草多茈草。條菅水向西南注長澤，其中噐酸三岁一成。郭注所未详，物类不强定，食之已癘为古述；不混大小咸或少咸。',
      'Xian lies 70 li northeast of Macheng, with jade above, copper below, pines, bai trees and zi grass. The Tiaojian flows southwest into Changze. Qisuan matures once in three years but is called uncertain in commentary, without an invented organism type.',
      'Seventy li northeast is Mount Xian, with jade above, copper below, pines and bai trees, and zi grass. The Tiaojian rises here and flows southwest into Changze. Qisuan is abundant, matures once in three years and is said to relieve li illness when eaten.',
      '0165—0167核94页。條菅音間，西南方向照录；噐酸按未详物产卡处理，不补鱼或植物形貌。',
      'Units 165–167 are on scan 94. The jian gloss and southwest direction remain. Qisuan is an unspecified product, without invented fish or plant anatomy.'),
    R('tianchi','天池之山','Mount Tianchi',(168,170),
      '咸山向东北二百里为天池，无草木、多文石。飛䑕兔状鼠首、以背飞；郭注背毛飞则仰，图不添翼膜或鸟翼。澠水出而潜其下，黄堊为土类郭注。',
      'Tianchi lies 200 li northeast of Xian, without vegetation and with patterned stones. Feishu has a rabbit form and rat head, flying with its back; commentary describes back hair and belly-up flight, without added wings. The Sheng emerges and goes beneath; yellow e is glossed as earth.',
      'Two hundred li northeast is Mount Tianchi, without vegetation and with patterned stones. Feishu resembles a rabbit with a rat head and flies with its back. The Sheng rises here and goes beneath the mountain; yellow e is abundant in the water account.',
      '0168—0170核94页，0169兎缺字图恢复，捕获保留。鼠首不加兔长耳，以背飞不擅画翼；停山底与堊土注分归澠水、黄堊。',
      'Units 168–170 are on scan 94. Tu is restored, with the captured marker preserved. Rat head adds no long rabbit ears or wings. The base-water and earth glosses belong to the river and yellow e.'),
    R('yangshan','陽山','Mount Yang',(171,176),
      '天池向东三百里为陽山，上多玉、下多金铜。領胡牛状赤尾颈腎，郭注颈上肉腎；𧰼蛇雌雉状五彩，自为牝牡，不因蛇名添蛇体。留水南注河，𩹴父鱼如鲫而鱼首彘身。',
      'Yang lies 300 li east of Tianchi, with jade above and gold and copper below. Linghu is cattle-shaped with a red tail and neck flesh explained in commentary. Xiangshe is five-colored and female-pheasant-shaped. The Liu flows south into the He; Xianfu has a fish head and pig body.',
      'Three hundred li east is Mount Yang, with jade above and gold and copper below. Linghu resembles cattle with a red tail and neck shen, compared to gouqu; it calls its name and is said to relieve madness when eaten. Xiangshe resembles a five-colored female pheasant, is male and female in itself and calls its name. The Liu rises here and flows south into the He. Xianfu fish resemble crucian fish, with fish heads and pig bodies, and are said to relieve vomiting when eaten.',
      '0171在94页末，捕获95校回94；0172—0176在95页。音劬归勾瞿、音䧟归𩹴；颈肉包块位置与数量为解释，不画内脏。𧰼蛇与𩹴父不据名颠倒形貌。',
      'Unit 171 ends scan 94 despite capture as 95; 172–176 are on 95. The qu and xian glosses are aligned separately. Neck-bulge placement is artistic, not an exposed organ. Names do not reverse the bird or fish-pig anatomy.'),
    R('benwen','賁聞之山','Mount Benwen',(177,178),
      '陽山向东三百五十里为賁聞，上多蒼玉、下多黄堊和𣵀石。三类物产分录，𣵀字依底本，不因物名猜现代成分或补图。',
      'Benwen lies 350 li east of Yang, with dark jade above and yellow e and nie stone below. These products remain separate, without modern chemical identifications.',
      'Three hundred and fifty li east is Mount Benwen, with much dark jade above, and yellow e and nie stone below.',
      '0177—0178核95页，𣵀石字形照捕获，不强改或借别山矿物图。',
      'Units 177–178 are on scan 95. The captured nie character remains, without replacement or borrowed mineral imagery.'),
    R('wangwu','王屋之山','Mount Wangwu',(179,181),
      '賁聞向北百里为王屋，多石。㶌水西北注㤗澤；郭注以音近疑与沇、濟水相关，仍保留为古注，不认定现代河流同一性或位置。',
      'Wangwu lies 100 li north of Benwen and has many stones. The Lian flows northwest into Taize. Guo Pu’s sound-based comparison with Yan and Ji remains a historical conjecture, without a modern river merger.',
      'One hundred li north is Mount Wangwu, with many stones. The Lian rises here and flows northwest into Taize.',
      '0179—0180在95页，0180捕获96校回95；0181在96页仅续近殆一水耳等郭注，归本段。音輦与地理志注分开，㤗澤复用北山索引。',
      'Units 179–180 are on scan 95; 180 was captured as 96. Empty main-text unit 181 continues commentary on scan 96. Pronunciation and the historical conjecture remain separate; Taize reuses the Northern index.'),
    R('jiaoshan','教山','Mount Jiao',(182,185),
      '王屋向东北三百里为教山，上多玉而无石。教水西注河，冬乾夏流、实惟乾河。水中记两山，广员三百步，名發丸，其上有金玉。两山记述保留，不虚构第二山名或现代尺度。',
      'Jiao lies 300 li northeast of Wangwu, with jade above but no stones. The Jiao flows west into the He, dry in winter and flowing in summer, called Dry River. Two hills within it are described as Fawan, 300 bu around, with gold and jade; no second name or modern scale is invented.',
      'Three hundred li northeast is Mount Jiao, with much jade above but no stones. The Jiao rises here and flows west into the He, dry in winter and flowing in summer, called Dry River. There are two hills within it, three hundred bu around, named Mount Fawan, with gold and jade above.',
      '0182—0185核96页。教水与乾河同段别称建一索引；郭注闻喜古沟不作现今水文。發丸为其中两山记述的单一列名，另建上下文卡，不拆成虚构额外行程。',
      'Units 182–185 are on scan 96. Jiao and Dry River share an alias index; the Wenxi old-channel gloss is historical. Fawan is a nested place for the two-hill account, without an invented second name or travel stage.'),
]


def entities(E):
    out = []
    def add(slug, kind, key, name, en, quote, desc, en_desc, en_quote, **extra):
        out.append(E(slug,kind,key,name,en,quote,desc,en_desc,en_quote,**extra))
    for slug, key, name, en, quote, water, context in [
        ('liangqu','gold-liangqu','金（梁渠）','Gold (Liangqu)','多金玉',False,None),
        ('liangqu','jade-liangqu','玉（梁渠）','Jade (Liangqu)','多金玉',False,None),
        ('huguan','jade-huguan','玉（湖灌）','Jade (Huguan)','其陽多玉',False,None),
        ('huguan','bi-huguan','碧（湖灌）','Bi (Huguan)','其隂多碧',False,None),
        ('huan','gold-huan','金（洹山）','Gold (Huan)','其上多金玉',False,None),
        ('huan','jade-huan','玉（洹山）','Jade (Huan)','其上多金玉',False,None),
        ('dunti','gold-dunti','金（敦題）','Gold (Dunti)','多金玉',False,None),
        ('dunti','jade-dunti','玉（敦題）','Jade (Dunti)','多金玉',False,None),
        ('taihang','gold-guishan','金（歸山）','Gold (Gui)','其上有金玉',False,'place-beishan-guishan'),
        ('taihang','jade-guishan','玉（歸山）','Jade (Gui)','其上有金玉',False,'place-beishan-guishan'),
        ('taihang','bi-guishan','碧（歸山）','Bi (Gui)','其下有碧',False,'place-beishan-guishan'),
        ('longhou','gold-longhou','金（龍侯）','Gold (Longhou)','多金玉',False,None),
        ('longhou','jade-longhou','玉（龍侯）','Jade (Longhou)','多金玉',False,None),
        ('macheng','wenstone-macheng','文石（馬成）','Patterned stones (Macheng)','其上多文石',False,None),
        ('macheng','gold-macheng','金（馬成）','Gold (Macheng)','其隂多金玉',False,None),
        ('macheng','jade-macheng','玉（馬成）','Jade (Macheng)','其隂多金玉',False,None),
        ('xianshan','jade-xianshan','玉（咸山）','Jade (Xian)','其上多玉',False,None),
        ('xianshan','copper-xianshan','铜（咸山）','Copper (Xian)','其下多銅',False,None),
        ('tianchi','wenstone-tianchi','文石（天池）','Patterned stones (Tianchi)','多文石',False,None),
        ('tianchi','yellow-e-tianchi','黄堊（天池）','Yellow e (Tianchi)','其中多黄堊',True,None),
        ('yangshan','jade-yangshan','玉（陽山）','Jade (Yang)','其上多玉',False,None),
        ('yangshan','gold-yangshan','金（陽山）','Gold (Yang)','其下多金銅',False,None),
        ('yangshan','copper-yangshan','铜（陽山）','Copper (Yang)','其下多金銅',False,None),
        ('benwen','dark-jade-benwen','蒼玉（賁聞）','Dark jade (Benwen)','其上多蒼玉',False,None),
        ('benwen','yellow-e-benwen','黄堊（賁聞）','Yellow e (Benwen)','其下多黄堊',False,None),
        ('benwen','nie-stone-benwen','𣵀石（賁聞）','Nie stone (Benwen)','多𣵀石',False,None),
        ('wangwu','stones-wangwu','石（王屋）','Stones (Wangwu)','是多石',False,None),
        ('jiaoshan','jade-jiaoshan','玉（教山）','Jade (Jiao)','其上多玉而無石',False,None),
        ('jiaoshan','gold-fawan','金（發丸）','Gold (Fawan)','其上有金玉',False,'place-beishan-fawan'),
        ('jiaoshan','jade-fawan','玉（發丸）','Jade (Fawan)','其上有金玉',False,'place-beishan-fawan'),
    ]:
        add(slug,'material',key,name,en,quote,'依本段录物产，不强定现代成分、坐标或器形。','This local product is recorded without a modern composition, coordinate or artifact shape.',en+' is recorded here.',water=water,context=context)
    for slug,key,name,en,quote,desc,en_desc,en_quote in [
        ('liangqu','xiu-liangqu','脩水（梁渠）','Xiu River (Liangqu)','脩水出焉而東流注于鴈門','脩水东注鴈門，鴈門郭注水名。','The Xiu flows east into Yanmen, glossed as a water name.','The Xiu rises here and flows east into Yanmen.'),
        ('liangqu','yanmen-liangqu','鴈門（梁渠水名）','Yanmen water (Liangqu)','東流注于鴈門','鴈門是水名，不自动并少咸鴈門之水或郭注山名。','Yanmen is a water name, without an automatic merger with Shaoxian’s namesake.','It flows east into Yanmen.'),
        ('huguan','huguan','湖灌之水','Huguan River','湖灌之水出焉而東流注于海','湖灌水东入海，不补现代河道。','The Huguan flows east into the sea without a modern course.','The Huguan rises here and flows east into the sea.'),
        ('huguan','sea-huguan','海（湖灌）','Sea (Huguan)','東流注于海','海为本段湖灌水所注，未据泛名合并其他海域。','The sea receives Huguan water in this context.','It flows east into the sea.'),
        ('dunti','north-sea-dunti','北海（敦題）','Northern Sea (Dunti)','是錞于北海','北海随敦題临海古述保存，不换成现代海岸线。','The Northern Sea remains part of Dunti’s ancient account, without a modern coastline.','It stands chun against the Northern Sea.'),
        ('longhou','juejue-longhou','决决之水','Juejue River','决决之水出焉而東流注于河','决决水东注河，音訣只归水名。','The Juejue flows east into the He; the pronunciation belongs to the river.','The Juejue rises here and flows east into the He.'),
        ('xianshan','tiaojian-xianshan','條菅之水','Tiaojian River','條菅之水出焉而西南流注于長澤','條菅水西南注長澤，菅音間为郭注。','The Tiaojian flows southwest into Changze; jian is a commentary gloss.','The Tiaojian rises here and flows southwest into Changze.'),
        ('xianshan','changze-xianshan','長澤（咸山）','Changze (Xian)','西南流注于長澤','長澤承條菅西南来水，不定现代湖泊。','Changze receives the southwest-flowing Tiaojian, without a modern lake identity.','It flows southwest into Changze.'),
        ('tianchi','sheng-tianchi','澠水（天池）','Sheng River (Tianchi)','澠水出焉潜于其下','澠水出而下潜，郭注停山底也，不强绘地下河道。','The Sheng emerges and goes beneath; commentary says it gathers at the base, without an invented underground course.','The Sheng rises here and goes beneath it.'),
        ('yangshan','liu-yangshan','留水','Liu River','留水出焉而南流注于河','留水南注河，不混其他篇留水。','The Liu flows south into the He in this local context.','The Liu rises here and flows south into the He.'),
        ('wangwu','lian-wangwu','㶌水（王屋）','Lian River (Wangwu)','㶌水出焉而西北流注于㤗澤','㶌水西北注㤗澤，音近沇濟是郭注疑说，不认定现代同水。','The Lian flows northwest into Taize. The sound-based Yan/Ji comparison is commentary, not a modern merger.','The Lian rises here and flows northwest into Taize.'),
        ('jiaoshan','jiao-jiaoshan','教水（乾河）','Jiao River (Dry River)','教水出焉西流注于河是水冬乾而夏流實惟乾河','教水西注河、冬乾夏流，乾河为同段古称；古沟注不作现今水文。','The Jiao flows west into the He, dry in winter and flowing in summer, called Dry River; the old-channel gloss is historical.','The Jiao rises here and flows west into the He, dry in winter and flowing in summer, called Dry River.'),
    ]:
        add(slug,'water',key,name,en,quote,desc,en_desc,en_quote,aliases=['乾河'] if slug=='jiaoshan' else [])
    add('liangqu','beast','juji-liangqu','居暨','Juji','其獸多居暨其状如彚而赤毛其音如豚','居暨如彚赤毛、音如豚；郭注彚似鼠、赤毛如刺，鼠状刺毛依注，配色姿态为解释，不因声音添猪鼻。','Juji resembles hui with red prickly hair and a pig-like sound. Mouse comparison and prickly hair follow commentary; pose is artistic and sound adds no pig nose.','Juji resembles hui with red hair and a pig-like sound.',commentary='彚似鼠赤毛如剌也猬彚音渭',en_commentary='Guo Pu compares hui to a mouse with red prickly hair and supplies pronunciation.')
    add('liangqu','beast','xiao-liangqu','囂（梁渠鸟）','Xiao (Liangqu bird)','有鳥焉其状如夸父四翼一目犬尾名曰囂其音如鵲食之已腹痛可以止衕','囂如夸父、四翼一目犬尾，但夸父主体比拟及舉父异文未定，留占位，不借西山猿体或别处鸟形；食用为古述。','Xiao has four wings, one eye and a dog tail, but the Kuafu/Jufu comparison is unresolved, so no borrowed ape or bird torso is illustrated. Eating claims remain ancient.','Xiao resembles Kuafu with four wings, one eye and a dog tail, sounds like a magpie and is said to relieve abdominal pain and dong.',commentary='或作舉父；治洞下也音洞',en_commentary='Guo Pu gives a Jufu variant for the comparison and glosses dong as bowel discharge.',unknown=True)
    add('huguan','beast','ma-huguan','马（湖灌）','Horses (Huguan)','多馬','马仅列名，不借别山图补形。','Horses are only named, without borrowed anatomy.','There are many horses.',unknown=True)
    add('huguan','beast','shan-huguan','䱇（湖灌）','Shan (Huguan)','其中多䱇','䱇郭注亦鱓魚字仅字义，未展开形貌，留占位。','The alternate eel-character gloss supplies no detailed anatomy, so shan keeps the placeholder.','Shan is abundant in the water account.',commentary='亦鱓魚字',en_commentary='Guo Pu calls it another character for shan fish.',unknown=True,water=True)
    add('huguan','plant','redgrain-huguan','赤理无名木（湖灌）','Unnamed red-grained tree (Huguan)','有木焉其葉如柳而赤理','无名木叶如柳而赤理。叶色、分枝根形及红纹表现为插画解释，不认定现代种。','The unnamed tree has willow-like leaves and red grain. Leaf color, branching, roots and grain rendering are artistic, not a modern species.','An unnamed tree has leaves like willow and red grain.')
    add('huan','place','liusha-huan','流沙（洹山行程）','Flowing sand (Huan route)','又北水行五百里流沙三百里至于洹山','水行五百、流沙三百分段保留，不并西山流沙或现代沙漠。','The water and flowing-sand route segments remain distinct, without a Western namesake or modern desert merger.','Travel north five hundred li by water and three hundred li through flowing sand to Huan.')
    add('huan','plant','sansang-huan','三桑（洹山）','Sansang (Huan)','三桑生之其樹皆無枝其髙百仞','三桑皆无枝、高百仞；一株无枝树干代表图，根皮与轮廓为解释，不强定三株、不补叶果或换算高度。','Sansang trees are branchless and a hundred ren tall. One representative trunk shows the shared form; roots and bark are artistic, without an exact count of three or height conversion.','Sansang trees grow here, all branchless and a hundred ren tall.')
    add('huan','plant','fruit-trees-huan','百果树（洹山）','Fruit-tree account (Huan)','百果樹生之','百果树只按原词记录，不补百种果形或树图。','The fruit-tree expression remains as written, without a hundred invented fruit forms.','Fruit trees grow here.')
    add('huan','beast','strange-snakes-huan','怪蛇（洹山）','Strange snakes (Huan)','其下多怪蛇','怪蛇仅泛名，不添首足翼数。','Strange snakes are only named, without invented heads, feet or wings.','Strange snakes are abundant below.',unknown=True)
    add('range2-summary','deity','human-serpent-range2-summary','次二山神（蛇身人面）','Second-range deities (serpent body, human face)','其神皆蛇身人靣','山神共形蛇身人面，代表图的灰须侧脸、盘曲与配色为解释，不认作首列同一神。','The deities share serpent bodies and human faces. Gray beard, profile, coil and color are artistic, without identifying them as the first-range individuals.','All its deities have serpent bodies and human faces.')
    add('range2-summary','rite','animal-burial-range2','次二牲祭瘗埋','Second-range animal burial','其祠毛用一雄雞彘瘞','雄鸡与彘的牲祭瘗埋，不把郭注投玉不埋移作牲祭；不擅定彘数量。','The cock-and-pig animal offering is buried; the no-burial jade gloss is separate. Pig count is unspecified.','The animal offering records a cock and pig with burial.',commentary='埋之',en_commentary='Guo Pu glosses burial.')
    add('range2-summary','rite','jade-casting-range2','次二投玉不糈','Second-range jade casting without grain','用一璧一珪投而不糈','一璧一珪投而不糈，郭注掷玉山中礼神不埋，不改为瘗玉。','One bi and one gui are cast without grain; commentary explicitly says jade is not buried.','One bi and one gui are cast without ritual grain.',commentary='擿玉於山中以禮神不埋之也',en_commentary='Guo Pu says jade is cast into the mountain to honor the deity, not buried.')
    for key,name,en,quote in [('bi-range2','璧（次二祭玉）','Bi jade (range two)','用一璧一珪投而不糈'),('gui-range2','珪（次二祭玉）','Gui jade (range two)','用一璧一珪投而不糈')]:
        add('range2-summary','rite',key,name,en,quote,'祭玉依文各一，形制尺寸不补定。','The ritual jade is recorded as one each, without fixed dimensions.','One bi and one gui are cast without ritual grain.')
    add('taihang','place','guishan','歸山（太行之首）','Mount Gui (head of Taihang)','其首曰歸山','歸山为太行之首的同段地名，物产与两生物归此，不另补跨山距离。','Gui is named as the head of Taihang; its products and two creatures use this nested context, without an invented journey.','Its head is called Mount Gui.')
    add('taihang','beast','hui-guishan','䮝（歸山）','Hui (Gui)','有獸焉其状如麢羊而四角馬尾而有距其名曰䮝善還其鳴自䚯','䮝麢羊状四角、马尾有距，善还旋舞为郭注；双后踝距位置数量、四蹄、姿态与配色为解释。','Hui is antelope-like with four horns, a horse tail and spurs. Commentary explains turning; two rear-ankle spurs, hooves, pose and colors are artistic.','Hui resembles lingyang with four horns, a horse tail and spurs, turns well and calls its name.',commentary='還旋旋儛也䮝音暉',en_commentary='Guo Pu glosses turning as whirling dance and gives hui pronunciation.',context='place-beishan-guishan')
    add('taihang','beast','fen-guishan','䴅（歸山）','Fen (Gui)','有鳥焉其状如鵲白身赤尾六足其名曰䴅是善驚其鳴自詨','䴅鹊状白身赤尾六足，善惊；六足须逐数，双翼单尾、足色与惊姿为解释。','Fen is magpie-shaped, white-bodied, red-tailed and six-legged, easily startled. Two wings, one tail, leg color and pose are artistic.','Fen resembles a magpie with a white body, red tail and six legs, is easily startled and calls its name.',commentary='音犇；今呉人謂呼為詨音呼交反',en_commentary='Guo Pu gives ben pronunciation and a regional calling gloss.',context='place-beishan-guishan')
    add('longhou','beast','renyu-longhou','人魚（龍侯）','Renyu (Longhou)','其中多人魚其状如䱱魚四足其音如嬰兒食之無癡疾','人鱼䱱状四足，鲵似鲇四足为郭注；不画人身或擅加外鳃，配色与短须等鱼形细节为解释，癡疾古述不定现代诊断。','Renyu is ti-shaped with four feet; Guo Pu compares catfish. No human torso or external gills are added. Color, short barbels and pose are artistic; chi is not a modern diagnosis.','Renyu resembles ti fish with four feet and an infant-like cry; eating it is said to prevent chi illness.',commentary='䱱見山中經或曰人魚即鯢也似鮎而四足聲如小兒啼今亦呼鮎為䱱音蹄',en_commentary='Guo Pu compares ni to catfish with four feet and an infant-like cry; the note continues across two units.',water=True)
    add('macheng','beast','tianma-macheng','天馬（馬成）','Tianma (Macheng)','有獸焉其状如白犬而黑頭見人則飛其名曰天馬其鳴自䚯','天马白犬黑头，见人飞；郭注肉翅，双肉翼数量和支架为解释，不画马身或羽翼。','Tianma is a white dog with a black head. Fleshy wings follow commentary; two-wing count and framework are artistic, without horse anatomy or feather wings.','Tianma resembles a white dog with a black head, flies on seeing people and calls its name.',commentary='言肉翅飛行自在',en_commentary='Guo Pu explains free flight with fleshy wings.')
    add('macheng','beast','quju-macheng','鶌鶋','Quju','有鳥焉其状如烏首白而身青足黄是名曰鶌鶋其鳴自詨食之不飢可以已寓','鶌鶋乌状首白身青足黄，青作深蓝绿为配色解释，不画鹰钩喙；寓未详，食用为古述。','Quju is crow-shaped with a white head, qing body and yellow feet. Deep blue-green interprets qing; no raptor hook is added. Yu remains uncertain and the eating claim ancient.','Quju resembles a crow with a white head, qing body and yellow feet, calls its name and is said to prevent hunger and relieve yu.',commentary='屈居二音或作鳴；不詳或曰寓猶誤也',en_commentary='Guo Pu gives qu-ju pronunciation and a variant, calling yu uncertain and offering a wu comparison.')
    for key,name,en in [('pine-xianshan','松（咸山）','Pines (Xian)'),('bai-xianshan','栢（咸山）','Bai trees (Xian)'),('zi-xianshan','茈草（咸山）','Zi grass (Xian)')]:
        quote='草多茈草' if key.startswith('zi-') else '是多松栢'
        add('xianshan','plant',key,name,en,quote,'本山草木仅列名，不借别山叶果或配图。','This local plant is only named, without borrowed leaf, fruit or artwork details.',en+' is recorded here.')
    add('xianshan','material','qisuan-xianshan','噐酸（未详物产）','Qisuan (unspecified product)','其中多噐酸三歲一成食之已癘','噐酸三岁一成，郭注所未详；不强定鱼、植物或矿物类，食用为古述，不作现代病名。','Qisuan matures once in three years but is uncertain in commentary. No fish, plant or mineral identity is imposed, and the eating claim is ancient.','Qisuan is abundant, matures once in three years and is said to relieve li illness.',commentary='所未詳也',en_commentary='Guo Pu calls it uncertain.',water=True)
    add('tianchi','beast','feishu-tianchi','飛䑕（天池）','Feishu (Tianchi)','有獸焉其状如兎而䑕首以其背飛其名曰飛䑕','飛䑕兔状鼠首、以背飞；郭注背毛飞则仰。四足仰腹与背毛形态为解释，不添翼、翼膜或兔长耳。','Feishu has a rabbit form and rat head, flying with its back. Commentary specifies back hair and belly-up flight. Four paws and hair arrangement are artistic; no wings, membranes or long rabbit ears are added.','Feishu resembles a rabbit with a rat head and flies with its back.',commentary='用其背上毛飛飛則仰也',en_commentary='Guo Pu says back hair enables flight and it flies belly-up.')
    add('yangshan','beast','linghu-yangshan','領胡','Linghu','有獸焉其状如牛而赤尾其頸腎其状如勾瞿其名曰領胡其鳴自詨食之已狂','領胡牛状赤尾颈腎，郭注颈上肉腎；一处颈侧皮下包块、双角和姿态为解释，不画外露内脏。','Linghu is cattle-shaped with a red tail and neck flesh. One intact neck bulge, two horns and pose are artistic; no exposed organ is depicted.','Linghu resembles cattle with a red tail and neck shen, compared to gouqu, calls its name and is said to relieve madness.',commentary='言頸上有肉腎勾瞿牛也；音劬',en_commentary='Guo Pu explains neck flesh and a cattle comparison, with qu pronunciation.')
    add('yangshan','beast','xiangshe-yangshan','𧰼蛇（陽山鸟）','Xiangshe (Yang bird)','有鳥焉其状如雌雉而五彩以文是自為牝牡名曰𧰼蛇其鳴自詨','𧰼蛇雌雉状五彩，自为牝牡为古述，不添双头或生殖器，不因蛇名补蛇身。','Xiangshe is female-pheasant-shaped and five-colored. The ancient sex statement adds no duplicate heads or genitals, and the name adds no snake body.','Xiangshe resembles a five-colored female pheasant, is described as male and female in itself, and calls its name.')
    add('yangshan','beast','xianfu-yangshan','𩹴父之魚','Xianfu fish','其中有𩹴父之魚其状如鮒魚魚首而彘身食之已嘔','𩹴父如鲫、鱼首彘身，四猪蹄、猪尾与配色为彘身演绎，不画反向猪首鱼身。','Xianfu is compared to crucian fish with a fish head and pig body. Four pig hooves, pig tail and colors interpret that body; the anatomy is not reversed.','Xianfu resembles crucian fish with a fish head and pig body; eating it is said to relieve vomiting.',commentary='音䧟',en_commentary='Guo Pu supplies xian pronunciation.',water=True)
    add('jiaoshan','place','fawan','發丸之山（两山记述）','Mount Fawan (two-hill account)','其中有兩山是山也廣員三百步其名曰發丸之山其上有金玉','水中两山记广员三百步、名發丸，上有金玉。单一列名不虚造第二山名或新增行程。','The two hills are described as Fawan, three hundred bu around, with gold and jade. A second name or journey is not invented.','Two hills within it are three hundred bu around, named Mount Fawan, with gold and jade above.')
    for e in out:
        if e['id']=='water-beishan-yanmen-liangqu':e.update(commentary='水名',en_commentary='Guo Pu explicitly calls Yanmen a water name.')
        elif e['id']=='water-beishan-tiaojian-xianshan':e.update(commentary='菅音間',en_commentary='Guo Pu supplies jian pronunciation.')
        elif e['id']=='water-beishan-sheng-tianchi':e.update(commentary='停山底也',en_commentary='Guo Pu says it gathers at the mountain base.')
        elif e['id']=='material-beishan-yellow-e-tianchi':e.update(commentary='堊土也',en_commentary='Guo Pu glosses e as earth.')
        elif e['id']=='water-beishan-lian-wangwu':e.update(commentary='㶌音輦；地理志王屋山沇水所出聲相近殆一水耳沇則濟㶌水也',en_commentary='Guo Pu gives lian pronunciation and tentatively compares a similarly sounding Yan/Ji water name; the cross-unit gloss is preserved as a historical conjecture.')
        elif e['id']=='water-beishan-jiao-jiaoshan':e.update(commentary='今河東聞喜縣東北有乾河口因名乾河里但有故溝䖏無復水即是也',en_commentary='Guo Pu describes an old Dry River channel near historical Wenxi; this is not a claim about present hydrology.')
    return out + next_entities(E)


ROWS += [
 R('jingshan','景山','Mount Jing',(186,190),
   '教山向南三百里为景山，南望𬐱販泽、北望少泽；郭注前者为盐池。藷藇根似羊蹄为注，秦椒子似椒而细、叶草为注；阴多赭、阳多玉。酸與蛇状四翼六目三足，不借鸟名补鹰首。',
   'Jing lies 300 li south of Jiao, overlooking Yanfan marsh to the south and Shaoze to the north. Commentary calls the former a salt pool and separately glosses the plants. Suanyu is snake-shaped with four wings, six eyes and three feet.',
   'Three hundred li south is Mount Jing, overlooking Yanfan marsh to the south and Shaoze to the north. Its grasses include zhuyu and Qin pepper. Its shaded side has ochre and its sunny side jade. Suanyu is a snake-shaped bird with four wings, six eyes and three feet, calling its name; its appearance is said to bring fear to the settlement.',
   '0186—0189在96页，0189捕获97校回96；0190续名酸與在97页。𬐱贩字形照底本，或无販字仅作异文；根、子叶的郭注分归两植物，不补现代物种。六眼排列、四羽翼和三爪足为插画解释。',
   'Units 186–189 are on scan 96; 189 was captured as 97. Unit 190 continues on 97. The marsh spelling and variant remain separate. Plant glosses are aligned without modern species identification. Eye arrangement, feathered wings and claws are artistic.'),
 R('mengmen','孟門之山','Mount Mengmen',(191,193),
   '景山向东南三百二十里为孟門，上多蒼玉、金，下多黄堊、𣵀石。尸子、穆天子传的洪水与古地名引文为郭注，不当本段实测河源或现代地貌。',
   'Mengmen lies 320 li southeast of Jing, with dark jade and gold above and yellow e and nie stone below. Commentary quotations about ancient flooding and place names do not establish a modern river source.',
   'Three hundred and twenty li southeast is Mount Mengmen, with dark jade and gold above, and yellow e and nie stone below.',
   '0191—0193在97页；其上多与蒼玉跨行，洪水叙事及九河之澄另存郭注，不补正文灾异事件。','Units 191–193 are on scan 97. The product phrase continues across lines; the flood narrative remains commentary.'),
 R('pingshan','平山','Mount Ping',(194,195),
   '孟門向东南三百二十里为平山；平水出于其上而潜于其下，多羙玉。潜流为古述，不补地下河线或现代洞穴。',
   'Ping lies 320 li southeast of Mengmen. The Ping rises above and goes beneath the mountain, with fine jade. This ancient account adds no mapped underground course.',
   'Three hundred and twenty li southeast is Mount Ping. The Ping water rises above and goes beneath it; fine jade is abundant.',
   '0194—0195核97页，潜于其下与是多羙玉的行接续保留；山、水分别建卡。','Units 194–195 are on scan 97. Mountain and river remain separate cards; the line continuation is preserved.'),
 R('jingshan-east','京山','Mount Jing (capital character)',(196,198),
   '平山向东三百里为京山，多羙玉、漆木、竹；阳有赤铜，阴有𤣥䃤，郭注黑砥名。髙水南注河。京山与景山分名，髙水不凭同音并别篇。',
   'Jing (capital character) lies 300 li east of Ping, with fine jade, lacquer trees and bamboo, red copper on its sunny side and xuansu on its shaded side, glossed as a black whetstone. The Gao flows south into the He. This mountain is distinct from Jing (landscape character).',
   'Three hundred li east is Mount Jing (capital character), with fine jade, lacquer trees and bamboo. Red copper occurs on its sunny side and xuansu on its shaded side. The Gao rises here and flows south into the He.',
   '0196—0198实际97页，0198捕获98校回97；𤣥䃤不按罕字猜矿物，郭注黑砥及音篠分存。','Units 196–198 are on scan 97; 198 was captured as 98. Xuansu retains the edition spelling and separate black-whetstone and pronunciation glosses.'),
 R('chongwei','虫尾之山','Mount Chongwei',(199,201),
   '京山向东二百里为虫尾，上多金玉，下多竹和青碧。丹水南注河，薄水东南注黄泽；淮南子薄水出鲜于山为郭注另说，不改本段源头。',
   'Chongwei lies 200 li east of Jing, with gold and jade above, bamboo and qingbi below. The Dan flows south into the He; the Bo flows southeast into Huangze. A Huainanzi source variant remains commentary.',
   'Two hundred li east is Mount Chongwei, with gold and jade above, bamboo and qingbi below. The Dan rises here and flows south into the He; the Bo rises here and flows southeast into Huangze.',
   '0199—0201核98页；虫尾照底本，不改蟲；丹水与西山同名水分开，黄泽为本段水域。0202彭毗另段待核。','Units 199–201 are on scan 98. Chongwei retains its spelling; the Northern Dan remains separate from Western namesakes. Pengpi begins at unit 202 and remains pending.'),
]

def next_entities(E):
 out=[]
 def add(slug,kind,key,name,en,quote,desc,en_desc,en_quote,**kw):
  out.append(E(slug,kind,key,name,en,quote,desc,en_desc,en_quote,**kw))
 for slug,key,name,en,q in [
 ('jingshan','ochre-jingshan','赭（景山）','Ochre (Jing)','其隂多赭'),
 ('jingshan','jade-jingshan','玉（景山）','Jade (Jing)','其陽多玉'),
 ('mengmen','dark-jade-mengmen','蒼玉（孟門）','Dark jade (Mengmen)','蒼玉'),
 ('mengmen','gold-mengmen','金（孟門）','Gold (Mengmen)','多金'),
 ('mengmen','yellow-e-mengmen','黄堊（孟門）','Yellow e (Mengmen)','其下多黄堊'),
 ('mengmen','nie-mengmen','𣵀石（孟門）','Nie stone (Mengmen)','多𣵀石'),
 ('pingshan','fine-jade-pingshan','羙玉（平山）','Fine jade (Ping)','是多羙玉'),
 ('jingshan-east','fine-jade-jingshan-east','羙玉（京山）','Fine jade (Jing, capital character)','有羙玉'),
 ('jingshan-east','red-copper-jingshan-east','赤铜（京山）','Red copper (Jing, capital character)','其陽有赤銅'),
 ('jingshan-east','xuansu-jingshan-east','𤣥䃤（京山黑砥）','Xuansu (Jing black whetstone)','其隂有𤣥䃤'),
 ('chongwei','gold-chongwei','金（虫尾）','Gold (Chongwei)','其上多金玉'),
 ('chongwei','jade-chongwei','玉（虫尾）','Jade (Chongwei)','其上多金玉'),
 ('chongwei','qingbi-chongwei','青碧（虫尾）','Qingbi (Chongwei)','多青碧')]:
  add(slug,'material',key,name,en,q,'本段物产按原文分录，不补现代成分或借其他山物产图。','The local product is recorded without a modern composition or borrowed imagery.',en+' is recorded here.')
 for slug,key,name,en,q in [
 ('jingshan-east','lacquer-jingshan-east','漆木（京山）','Lacquer trees (Jing, capital character)','多漆木'),
 ('jingshan-east','bamboo-jingshan-east','竹（京山）','Bamboo (Jing, capital character)','多竹'),
 ('chongwei','bamboo-chongwei','竹（虫尾）','Bamboo (Chongwei)','其下多竹')]:
  add(slug,'plant',key,name,en,q,'草木仅列名，形貌未详，不借别山叶果或配图。','This plant is only named, without borrowed leaf, fruit or artwork details.',en+' is recorded here.')
 add('jingshan','water','yanfan-jingshan','𬐱販之澤（景山南望）','Yanfan marsh (south of Jing)','南望𬐱販之澤','景山南望之泽，郭注盐池、今河东猗氏县及或无販字为古注，不直接定位现代坐标。','The marsh is viewed southward from Jing. The salt-pool and historical Yishi gloss, and the variant lacking fan, do not establish modern coordinates.','Jing overlooks Yanfan marsh to the south.',commentary='即塩池也今在河東猗氏縣或無販字',en_commentary='Guo Pu identifies a salt pool in historical Yishi and records a variant without fan.')
 add('jingshan','water','shaoze-jingshan','少澤（景山北望）','Shaoze (north of Jing)','北望少澤','少泽为北望水域，不混少咸或他篇同名泽。','Shaoze is the northern view from Jing, without merging similarly named places.','Jing overlooks Shaoze to the north.')
 add('jingshan','plant','zhuyu-jingshan','藷藇（景山）','Zhuyu (Jing)','其上多草藷藇','藷藇郭注根似羊蹄可食，曙豫二音及江南单呼为藷另存；不强定现代薯类，不补全株图。','Commentary compares the edible root to a sheep hoof and gives pronunciation and regional naming. This does not fix a modern species or full-plant form.','Zhuyu grass is abundant above.',commentary='根似羊蹄可食曙豫二音今江南單呼為藷音儲語有輕重耳',en_commentary='Guo Pu describes a sheep-hoof-like edible root and gives pronunciation and regional naming.')
 add('jingshan','plant','qinjiao-jingshan','秦椒（景山）','Qin pepper (Jing)','其草多秦椒','秦椒郭注子似椒而细、叶草；不按今名画木本花椒，不补现代种属或完整形貌。','Commentary compares its small seeds to pepper and calls the leaves grassy; this does not fix a modern woody pepper species or complete form.','Qin pepper is abundant among the grasses.',commentary='子似椒而細葉草也',en_commentary='Guo Pu compares the small seeds to pepper and calls the leaves grassy.')
 add('jingshan','beast','suanyu-jingshan','酸與（景山）','Suanyu (Jing)','有鳥焉其状如蛇而四翼六目三足名曰酸與其鳴自詨見則其邑有恐','酸與为蛇状鸟，四翼六目三足，鸣自詨；图的六眼排列、羽翼、爪足、鳞纹与配色为解释，不画鹰或猫头鹰首。见邑有恐与或曰食之不醉均为古述。','Suanyu is a snake-shaped bird with four wings, six eyes and three feet, calling its name. Eye arrangement, feathers, claws, scales and colors are artistic, without an owl or eagle head. Fear and the variant eating claim remain ancient.','Suanyu is snake-shaped with four wings, six eyes and three feet, calls its name and is said to bring fear when it appears.',commentary='或曰食之不醉',en_commentary='A variant says eating it prevents drunkenness.')
 add('pingshan','water','ping-pingshan','平水','Ping water','平水出于其上潜于其下','平水出山上而潜于山下，保留古述，不拟地下河坐标或连别水。','The Ping rises above and goes below the mountain, without an invented underground route or water merger.','The Ping rises above and goes below the mountain.')
 add('jingshan-east','water','gao-jingshan-east','髙水（京山）','Gao water (Jing, capital character)','髙水出焉南流注于河','髙水出京山而南注河，与别篇同音水名分开。','The Gao rises at Jing and flows south into the Northern He, separate from namesakes.','The Gao rises here and flows south into the He.')
 add('chongwei','water','dan-chongwei','丹水（虫尾）','Dan water (Chongwei)','丹水出焉南流注于河','丹水出虫尾南注河，不合并西山丹水或现代河道。','The Dan rises at Chongwei and flows south into the He, without merging Western namesakes or modern courses.','The Dan rises here and flows south into the He.')
 add('chongwei','water','bo-chongwei','薄水（虫尾）','Bo water (Chongwei)','薄水出焉而東南流注于黄澤','薄水在本段出虫尾、东南注黄泽；郭引淮南子源出鲜于山另存，不强消歧。','Here the Bo rises at Chongwei and flows southeast into Huangze; the Huainanzi source at Xianyu remains a separate variant.','The Bo rises here and flows southeast into Huangze.',commentary='淮南子曰薄水出鮮于山',en_commentary='Guo Pu quotes Huainanzi placing its source at Mount Xianyu.')
 add('chongwei','water','huangze-chongwei','黄澤（虫尾所注）','Huangze (Bo recipient)','東南流注于黄澤','黄泽为薄水东南所注，后文同名关系留待核定，不借现代黄泽岸线。','Huangze receives the southeast-flowing Bo. Later namesake relations remain to be reviewed, without modern shorelines.','The Bo flows southeast into Huangze.')
 for e in out:
  if e['id']=='material-beishan-xuansu-jingshan-east':
   e.update(commentary='黒砥名也尸子曰加𤣥黄砥明色非一也䃤音竹篠之篠',en_commentary='Guo Pu calls it a black whetstone, quotes Shizi on varied colors and gives a pronunciation gloss.')
 return out
