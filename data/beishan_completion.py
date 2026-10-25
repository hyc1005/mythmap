"""Final fifteen Northern reading stages, source units 259–297, scans 104–108."""
from beishan_later_ranges import R

REMAINING = []

def C(slug,name,en_name,units,description,en_quote,note,en_note,**kw):
    return R(slug,name,en_name,units,description,en_quote,en_quote,note,en_note,**kw)

ROWS = [
 C('shishan','石山','Mount Shi',(259,261),
   '泰戱向北三百里为石山，多蔵金玉。濩濩水东注虖沱，鮮于水南注虖沱；濩音尺蠖之蠖为跨行郭注，不当虫名或物产。',
   'Three hundred li north is Mount Shi, storing much gold and jade. The Huohuo rises here and flows east into Hutuo; the Xianyu rises here and flows south into Hutuo.',
   '0259—0261实际104页，0261捕获105校回104。音尺蠖之蠖跨259—260连读，仅释濩字；两水流向分别保存。','Units 259–261 are on scan 104; 261 was captured as 105. The cross-unit pronunciation gloss belongs to Huohuo, not a creature; the two directions stay separate.'),
 C('tongrong','童戎之山','Mount Tongrong',(262,263),
   '石山向北二百里为童戎，皐涂水东注漊液水。漊液按本段连写受水名留存，不直接合并泰戱漊水或液女。',
   'Two hundred li north is Mount Tongrong. The Gaotu rises here and flows east into Louye water.',
   '0262—0263核105页；漊液水与上文漊水、液女词界不同，不据近名强拆或定为二水合流。','Units 262–263 are on scan 105. Louye remains this written recipient, without a forced split or a merger with Lou and Yenu.'),
 C('gaoshi','髙是之山','Mount Gaoshi',(264,266),
   '童戎向北三百里为髙是，滋水南注虖沱，多㯶木、條草；𣸦水东注河。音慈归滋、音冦归𣸦；郭注古地名与东北入易水异说另存。',
   'Three hundred li north is Mount Gaoshi. The Zi rises here and flows south into Hutuo. Its trees include zong and its grasses include tiao. The Kou rises here and flows east into the He.',
   '0264—0266核105页。條草与𣸦水分词，不合成水名；过博陵及东北入易水归𣸦水郭注，不替正文东注河。古郡县疑读照捕获存，不作现代定位。','Units 264–266 are on scan 105. Tiao grass and Kou water are distinct. Historical places and the alternative northeast course remain commentary, not replacements for the eastward main text.'),
 C('lushan','陸山','Mount Lu',(267,268),
   '髙是向北三百里为陸山，多羙玉；𨜰水东注河。郯水为郭注或作，不替正文罕字，英名借异写整理。',
   'Three hundred li north is Mount Lu, with much fine jade. The Tan water rises here and flows east into the He.',
   '0267—0268核105页。正文𨜰、郭注或作郯水分存，不静默改字或据异写定位现代河。','Units 267–268 are on scan 105. The rare textual spelling and commentary variant Tan remain distinct; the English name follows the variant for readability.'),
 C('yishan','沂山','Mount Yi',(269,269),
   '陸山向北二百里为沂山，般水东注河。音祈释沂、音盤释般，山水注分开。',
   'Two hundred li north is Mount Yi. The Ban rises here and flows east into the He.',
   '0269核105页；两音不混，般字不改盘，未定现代沂山或水系。','Unit 269 is on scan 105. The mountain and river pronunciation glosses remain separate, without modern location claims.'),
 C('yanshan','燕山','Mount Yan',(270,271),
   '沂山向北百二十里为燕山，多嬰石；燕水东注河。郭注石似玉、有符彩嬰帶为古物产描述，不定现代矿种。',
   'One hundred and twenty li north is Mount Yan, with much ying stone. The Yan rises here and flows east into the He.',
   '0270实际105页末而捕获106，校回105；0271在106页。燕与后续山行水行至饒分段，不沿用合并候选。','Unit 270 ends scan 105 despite capture as 106; 271 is on 106. Yan and the following land-and-water journey to Rao remain separate stages.'),
 C('raoshan','饒山','Mount Rao',(272,274),
   '燕山向北山行五百里、水行五百里至饒，二路分记；无草木、多瑶碧，有槖駝、鶹歷。歷虢水东注河，其中師魚食之杀人为古述。三生物形貌不足，保留异说与占位。',
   'Northward, travel five hundred li over mountains and five hundred li by water to Mount Rao, without vegetation and with much yaobi. Its beasts include tuotuo and birds liuli. The Liguo rises here and flows east into the He; shi fish occur in it and are said to kill when eaten.',
   '0272—0274核106页。槖駝仅名，不借早段橐駝注定峰数；鶹歷未详或鶹鵂鶹、師魚未详或鯢均存，不凭异说补图；山行水行不改纯陆程。','Units 272–274 are on scan 106. Camel hump count and uncertain bird/fish variants are not forced; the two journey modes stay separate, and the eating claim is ancient.'),
 C('ganshan','乾山','Mount Gan',(275,277),
   '饒山向北四百里为乾山，无草木，阳金玉、阴鐡且无水。獂牛状三足，鸣自詨；三足位置、体色及无角造型为插画解释，不补第四足。',
   'Four hundred li north is Mount Gan, without vegetation, with gold and jade on its sunny side, iron on its shaded side, and no water. Yuan resembles an ox with three feet and calls its name.',
   '0275—0277核106页。音元归獂；不将无水句删去，也不因三足安排补第四足或形体之外灾景。','Units 275–277 are on scan 106. Yuan pronunciation is retained; leg arrangement and appearance details are artistic, with exactly three feet.'),
 C('lunshan','倫山','Mount Lun',(278,279),
   '乾山向北五百里为倫山，倫水东注河。羆如麋，其川在尾上；郭注川窍也。名羆不当熊形，尾上窍按原文部位记，不强定现代器官解释。',
   'Five hundred li north is Mount Lun. The Lun rises here and flows east into the He. Pi resembles mi deer, with its opening above the tail.',
   '0278—0279实际106页，0279捕获107校回106；川窍也独归羆。图为被毛鹿形及尾根上方小窍，不画伤口、暴露组织或熊体。','Units 278–279 are on scan 106; 279 was captured as 107. The opening gloss belongs to Pi. Its discreet anatomical mark, hornless form, coat and pose are artistic, without bear anatomy.'),
 C('jieshi','碣石之山','Mount Jieshi',(280,282),
   '倫山向北五百里为碣石，繩水东注河，水中蒲夷鱼未详；山上玉、下青碧。郭注辽西或右北平两古说跨行保留，不强定今地。',
   'Five hundred li north is Mount Jieshi. The Sheng rises here and flows east into the He, with many Puyi fish. Jade occurs above and qingbi below.',
   '0280—0282核107页；山名郭注跨280—281连读，未详归蒲夷，不移动为玉石注；鱼无形貌不补图。','Units 280–282 are on scan 107. The historical place gloss spans 280–281; uncertain refers to Puyi fish, without invented anatomy or a modern Jieshi location.'),
 C('yanmenshan','鴈門之山（北水行）','Mount Yanmen (northern water journey)',(283,284),
   '碣石向北水行五百里至鴈門之山，无草木。郭注北𨹧西隃与鴈出处、髙柳北另存，不混梁渠水名或少咸水名。',
   'Northward, travel five hundred li by water to Mount Yanmen, without grasses or trees.',
   '0283—0284核107页，0284空正文续鴈門郭注，不并下一泰澤。水行与山名保持，不凭雁字造雁图。','Units 283–284 are on scan 107; 284 continues commentary only. The water journey and mountain remain distinct from earlier Yanmen waters.'),
 C('taize-didu','泰澤水行與帝都之山','Taize water journey and Mount Didu',(285,286),
   '鴈門向北水行四百里至泰澤，其中帝都之山广员百里，无草木、有玉金。泰澤与帝都分层建档，不把广员换算现代面积；此水行索引与较早㤗澤关系未强定。',
   'Northward, travel four hundred li by water to Taize. Within it is Mount Didu, with an extent of one hundred li, without vegetation and with jade and gold.',
   '0285—0286核107页。帝都为段内山，玉金归其上下文；泰澤水行与早段㤗澤分别保留，不因同名替换地理语境。','Units 285–286 are on scan 107. Didu is nested within the water account; jade and gold use that context, without a modern area conversion or forced merger with earlier Taize.'),
 C('mufeng','錞于母逢之山','Mount Chunyumufeng',(287,289),
   '泰澤向北五百里为錞于母逢，北望鷄號，载风如䬅；西望幽都、浴水出焉，郭注浴即黒水。段尾大蛇赤首白身、音如牛，见邑大旱为古述；蛇声不添牛角。',
   'Five hundred li north is Mount Chunyumufeng. To the north is a view of Mount Jihao, with wind described as li; to the west is a view of Mount Youdu, where the Yu water rises. There is a great snake with a red head and white body, sounding like an ox; its appearance is said to bring severe drought to the settlement.',
   '0287—0288实际107页，0288捕获108校回107；0289在108页。山名母逢与总括無逢分别保留；浴即黒水也跨288—289连注，不移也字给蛇形。风指代不强定现代山风，蛇不据音加牛器官。','Units 287–288 are on scan 107; 288 was captured as 108. Unit 289 is on 108. Mufeng and the summary’s Wufeng retain their spellings. The Black Water gloss continues across units; ox-like sound adds no ox anatomy.'),
 C('range3-summary','北次三经总括与祭礼','Third Northern range summary and rites',(290,296),
   '总括太行至無逢，原报46山、12350里，当前47列名阅读山段的差异照留。20神马身人面、14神彘身载玉、10神彘身八足蛇尾，共44神。藻茝瘗、玉不瘗、璧瘗及稌糈米不火食分录，不混祭物和神形。',
   'The third Northern range runs from Taihang to Wufeng: forty-six mountains and twelve thousand three hundred and fifty li. Twenty deities have horse bodies and human faces; their rites use the recorded yi zao zhi with burial. Fourteen have pig bodies carrying jade; their rites use jade without burial. Ten have pig bodies, eight feet and snake tails; their rites use one bi with burial. In all, forty-four deities are worshipped with tu grain and rice offerings, described as not fire-eating.',
   '0290—0296核108页。原报46与列名阅读山段47不合，不补删山。茝音昌代反跨292—293；不埋所用玉也跨293—294属不瘗祭玉，不当载玉形貌注。三组20+14+10=44与大凡44相合，神数不当山数。','Units 290–296 are on scan 108. Reported 46 and 47 named reading passages differ. The zhi pronunciation and no-burial jade glosses span units; ritual jade is not an anatomical gloss. The deity groups total 44, not a mountain count.',entry_kind='rite'),
 C('book-total','北山经篇末总计与数字核对','Northern closing total and numerical review',(297,297),
   '篇末原报北经87山、23230里。三列原报山数合88、里程合23530，分别较篇末多1山、300里；列名山段亦合88。各层数字与当前分段口径分别记录，不静默改成一致。',
   'The Northern mountain account totals eighty-seven mountains and twenty-three thousand two hundred and thirty li.',
   '0297核108页，与次三祭礼分开。列数25+17+46=88、里程5490+5690+12350=23530，对照篇末87/23230；差异分别保留，不把阅读段数92冒充山数。','Unit 297 is on scan 108, separate from the third-range rites. The reported range sums are 88 mountains and 23,530 li, against 87 and 23,230 at the close; neither is silently corrected, and 92 reading passages are not mountains.',entry_kind='rite',range=4),
]

def entities(E):
 out=[]
 def add(slug,kind,key,name,en,q,d,ed,eq,**kw):out.append(E(slug,kind,key,name,en,q,d,ed,eq,**kw))
 for slug,key,name,en,q in [
 ('shishan','gold-shishan','金（石山）','Gold (Shi)','多蔵金玉'),('shishan','jade-shishan','玉（石山）','Jade (Shi)','多蔵金玉'),
 ('lushan','fine-jade-lushan','羙玉（陸山）','Fine jade (Lu)','多羙玉'),
 ('raoshan','yaobi-raoshan','瑶碧（饒山）','Yaobi (Rao)','多瑶碧'),
 ('ganshan','gold-ganshan','金（乾山）','Gold (Gan)','其陽有金玉'),('ganshan','jade-ganshan','玉（乾山）','Jade (Gan)','其陽有金玉'),('ganshan','iron-ganshan','鐡（乾山）','Iron (Gan)','其隂有鐡'),
 ('jieshi','jade-jieshi','玉（碣石）','Jade (Jieshi)','其上有玉'),('jieshi','qingbi-jieshi','青碧（碣石）','Qingbi (Jieshi)','其下多青碧'),
 ('taize-didu','jade-didu','玉（帝都）','Jade (Didu)','有玉金'),('taize-didu','gold-didu','金（帝都）','Gold (Didu)','有玉金')]:
  kw={'context':'place-beishan-didu'} if slug=='taize-didu' else {}
  add(slug,'material',key,name,en,q,'本段物产按原词及上下文分录，不定现代成分或借其他山图。','The local product retains its textual name and context, without modern composition or borrowed imagery.',en+' is recorded here.',**kw)
 add('yanshan','material','yingstone-yanshan','嬰石（燕山）','Ying stone (Yan)','多嬰石','嬰石郭注似玉有符彩嬰帶，燕石古比拟不定现代矿种或外观图。','Commentary compares ying stone to jade with patterned banding; this is not a modern mineral identification.','Ying stone is abundant.',commentary='言石似玉有符彩嬰帶所謂燕石者',en_commentary='Guo Pu compares it to jade with patterned banding and calls it Yan stone.')
 for key,name,en,q in [('zong-gaoshi','㯶（髙是木）','Zong trees (Gaoshi)','其木多㯶'),('tiao-gaoshi','條草（髙是）','Tiao grass (Gaoshi)','其草多條')]:
  add('gaoshi','plant',key,name,en,q,'草木仅列名，形貌未详，不以现代同名补叶果或物种图。','This plant is only named, without modern leaf, fruit or species imagery.',en+' is recorded here.')
 for slug,key,name,en,q,d,ed,eq in [
 ('shishan','huohuo-shishan','濩濩之水','Huohuo water','濩濩之水出焉而東流注于虖沱','濩濩水出石山东注虖沱，音尺蠖之蠖跨行属水名。','The Huohuo flows east into Hutuo; its cross-line pronunciation gloss belongs to the water.','The Huohuo rises here and flows east into Hutuo.'),
 ('shishan','xianyu-shishan','鮮于之水（石山）','Xianyu water (Shi)','鮮于之水出焉而南流注于虖沱','鮮于水南注虖沱，不把同段濩濩东向移给本水。','The Xianyu flows south into Hutuo, distinct from the east-flowing Huohuo.','The Xianyu rises here and flows south into Hutuo.'),
 ('tongrong','gaotu-tongrong','皐涂之水','Gaotu water','皐涂之水出焉而東流注于漊液水','皐涂水东注漊液，涂字与皐泽不同，不合水名。','The Gaotu flows east into Louye; it is not Gaoze.','The Gaotu rises here and flows east into Louye.'),
 ('tongrong','louye-tongrong','漊液水（童戎受水名）','Louye water (Tongrong recipient)','東流注于漊液水','漊液按受水名连写保留，不把上段漊水与液女断定为此水或二水合流。','Louye remains this recipient wording, without a forced equation to Lou or Yenu.','The Gaotu flows east into Louye.'),
 ('gaoshi','zi-gaoshi','滋水（髙是）','Zi water (Gaoshi)','滋水出焉而南流注于虖沱','滋水南注虖沱，音慈归滋；不移𣸦水东注河的语句。','The Zi flows south into Hutuo; its pronunciation and direction remain separate from Kou.','The Zi rises here and flows south into Hutuo.'),
 ('gaoshi','kou-gaoshi','𣸦水（髙是）','Kou water (Gaoshi)','𣸦水出焉東流注于河','𣸦水正文东注河，郭注过博陵又东北入易水为古另述，不改主文方向。','The Kou flows east into the He; the historical northeast course into Yi remains commentary.','The Kou rises here and flows east into the He.'),
 ('lushan','tan-lushan','𨜰水（陸山）','Tan water (Lu, variant name)','𨜰水出焉而東流注于河','𨜰字按主文，或作郯水是郭注；英名按异写整理，不换现代河道。','The textual spelling remains; Tan is a commentary variant used for the English name, without a modern river claim.','The Tan rises here and flows east into the He.'),
 ('yishan','ban-yishan','般水（沂山）','Ban water (Yi)','般水出焉而東流注于河','般水东注河，音盤归般；沂山音祈另归山名。','The Ban flows east into the He; its pan gloss is separate from the mountain pronunciation.','The Ban rises here and flows east into the He.'),
 ('yanshan','yan-yanshan','燕水（燕山）','Yan water (Yan)','燕水出焉東流注于河','燕水东注河，不混燕山嬰石注。','The Yan flows east into the He, separate from the stone gloss.','The Yan rises here and flows east into the He.'),
 ('raoshan','liguo-raoshan','歷虢之水','Liguo water','歷虢之水出焉而東流注于河','歷虢水东注河，其中師魚古食用凶述另存，不当现代鉴毒依据。','The Liguo flows east into the He; its ancient fish eating claim is not modern toxicity guidance.','The Liguo rises here and flows east into the He.'),
 ('lunshan','lun-lunshan','倫水','Lun water','倫水出焉而東流注于河','倫水东注河，羆随后为兽述，不擅定水生兽。','The Lun flows east into the He; the following Pi account does not establish an aquatic animal.','The Lun rises here and flows east into the He.'),
 ('jieshi','sheng-jieshi','繩水（碣石）','Sheng water (Jieshi)','繩水出焉而東流注于河','繩水东注河，蒲夷鱼见其水文，名中繩不合澠水。','The Sheng flows east into the He, with Puyi fish; it remains separate from the differently written Sheng at Tianchi.','The Sheng rises here and flows east into the He.'),
 ('taize-didu','taize-didu','泰澤（帝都水行）','Taize (Didu water journey)','又北水行四百里至于泰澤','水行所至泰澤为本段水域，帝都山在其中；与早段㤗澤的地理同一性未定，保持独立索引。','This Taize contains Didu in the water journey; its identity with the earlier Taize is unresolved, so the index remains separate.','Travel north four hundred li by water to Taize.'),
 ('mufeng','yu-youdu-mufeng','浴水（幽都相邻记述）','Yu water (Youdu account)','浴水出焉','浴水按紧接幽都的语序组织阅读；郭注浴即黒水也跨行，未改正文浴或强并西山黑水。','Yu follows Youdu in the textual sequence; the cross-line Black Water gloss does not replace the text or merge Western namesakes.','The Yu water rises there.')]:
  kw={'context':'place-beishan-youdu-mufeng'} if slug=='mufeng' else {}
  add(slug,'water',key,name,en,q,d,ed,eq,**kw)
 for key,name,en,q in [('tuotuo-raoshan','槖駝（饒山）','Tuotuo (Rao)','其獸多槖駝'),('liuli-raoshan','鶹歷（饒山）','Liuli (Rao)','其鳥多鶹歷'),('shiyu-raoshan','師魚（饒山）','Shi fish (Rao)','其中有師魚食之殺人')]:
  add('raoshan','beast',key,name,en,q,'名目或未详异说留存，形貌不足，不借同名或异说定器官；古食用说不作现实指引。','The name and uncertain variants remain without borrowed anatomy; ancient eating claims are not present guidance.',en+' is recorded here.',unknown=True,water=key.startswith('shiyu'))
 add('ganshan','beast','yuan-ganshan','獂（乾山）','Yuan (Gan)','有獸焉其状如牛而三足其名曰獂其鳴自詨','牛状三足，音元归獂。单前足与两后足的安排、无角造型、体色与站姿为解释，必须三条足胫与三蹄可数，不添第四足。','Yuan is ox-shaped with three feet. One foreleg and two hind legs, hornless form, color and pose are artistic; exactly three legs and hooves must be countable.','Yuan resembles an ox with three feet and calls its name.',commentary='音元',en_commentary='Guo Pu gives yuan pronunciation.')
 add('lunshan','beast','pi-lunshan','羆（倫山麋状兽）','Pi (Lun deer-shaped creature)','有獸焉其状如麋其川在尾上其名曰羆','麋状而川在尾上，郭注川窍也；名羆不画熊。被毛躯体尾根上方一小窍的具体呈现、无角造型、四蹄与姿态为解释，不画伤口或强定现代器官。','Pi is mi-deer-shaped with an opening above the tail. The name adds no bear anatomy. The discreet mark, hornless form, four hooves and pose are artistic, without a wound or fixed modern organ interpretation.','Pi resembles mi deer, with its opening above the tail.',commentary='川竅也',en_commentary='Guo Pu glosses chuan as an opening.')
 add('jieshi','beast','puyi-jieshi','蒲夷之魚（碣石）','Puyi fish (Jieshi)','其中多蒲夷之魚','蒲夷鱼郭注未详，器官颜色未载，留占位。','Puyi fish are called uncertain in commentary, without stated organs or colors.','Puyi fish are abundant in the water.',commentary='未詳',en_commentary='Guo Pu calls it uncertain.',unknown=True,water=True)
 add('taize-didu','place','didu','帝都之山（泰澤中）','Mount Didu (within Taize)','其中有山焉曰帝都之山廣員百里無草木有玉金','帝都在泰澤中，广员百里、无草木、有玉金，古尺度不换算面积或附会现代都城。','Didu is within Taize, a hundred li in extent, without vegetation and with jade and gold; no modern area or capital is inferred.','Within it is Mount Didu, a hundred li in extent, without vegetation and with jade and gold.')
 for key,name,en,q in [('jihao-mufeng','鷄號之山（北望）','Mount Jihao (northward view)','北望鷄號之山'),('youdu-mufeng','幽都之山（西望）','Mount Youdu (westward view)','西望幽都之山')]:
  add('mufeng','place',key,name,en,q,'方向性望见地点按本段建档，不借他篇幽都或补现代坐标。','This viewed place retains its passage direction, without a chapter merger or modern coordinates.', 'The passage records a northward view of Jihao.' if key.startswith('jihao') else 'The passage records a westward view of Youdu.')
 add('mufeng','wind','li-mufeng','如䬅之风（末段）','Li-like wind (closing mountain account)','其風如䬅','其风如䬅为古风述，郭注急风貌或飘风及音戻；其字指代不强定，未换现代风级。','The li-like wind is glossed as swift or whirling wind. The pronoun and ancient term do not fix a modern wind grade.','Its wind is described as li.',commentary='䬅急風貌也音戻或云飄風也',en_commentary='Guo Pu describes swift or whirling wind and gives a pronunciation gloss.')
 add('mufeng','beast','redhead-snake-mufeng','赤首白身大蛇（末段）','Red-headed white-bodied great snake','是有大蛇赤首白身其音如牛見則其邑大旱','大蛇赤首白身、音如牛；牛音不添牛角或牛耳。盘曲、鳞纹及头目细节为解释，旱兆为古述，不把是字强解成现代栖息地定位。','The great snake has a red head and white body and an ox-like sound, without ox organs. Coil, scales and head details are artistic; the omen and pronoun do not fix a modern habitat.','There is a great snake with a red head and white body, sounding like an ox; its appearance is said to bring severe drought to the settlement.')
 for key,name,en,q,d,ed,eq in [
 ('horse-human-range3','次三二十神（馬身人面）','Twenty third-range deities (horse body, human face)','其神状皆馬身而人靣者廿神','马身人面二十神，代表图单体不当二十个体的实景。四马蹄、成人女性面孔、发式、色彩与头颈连接为解释，无人躯干或人臂。','Twenty deities have horse bodies and human faces. One representative uses four horse hooves and an adult feminine face; hair, color and the head-neck transition are artistic, without a human torso or arms.','Twenty deities have horse bodies and human faces.'),
 ('pig-jade-range3','次三十四神（彘身載玉）','Fourteen third-range deities (pig body, carrying jade)','其十四神状皆彘身而載玉','彘身载玉十四神，代表图一猪体载一小玉片；猪首、四蹄、玉片数量形制位置及配色为解释，不从不瘗郭注增加身体器官。','Fourteen deities have pig bodies carrying jade. The representative pig head, four hooves, one jade slab, its shape and placement, and colors are artistic; the no-burial gloss concerns ritual.','Fourteen deities have pig bodies carrying jade.'),
 ('pig-eight-snake-range3','次三十神（彘身八足蛇尾）','Ten third-range deities (pig body, eight feet, snake tail)','其十神状皆彘身而八足蛇尾','彘身八足蛇尾十神，单体代表图须八足胫八蹄可逐数、蛇尾渐尖无蛇首；猪首、足位、体色为解释，不加玉饰或人面。','Ten deities have pig bodies, eight feet and snake tails. The representative must show eight independent legs and hoof sets; the tapering snake tail has no head. Pig head, leg placement and color are artistic, without jade or a human face.','Ten deities have pig bodies, eight feet and snake tails.')]:
  add('range3-summary','deity',key,name,en,q,d,ed,eq)
 for key,name,en,q,d,ed,eq,comment,ec in [
 ('zaozhi-burial-range3','次三馬身神藻茝瘗礼','Third-range horse-deity zao-zhi burial','其祠之皆用一藻茝瘞之','一藻茝与瘗照录，不补束数、重量或动物祭牲。','The recorded yi zao zhi and burial wording supplies no invented bundle, weight or animal offering.','Their rites use the recorded yi zao zhi with burial.','',''),
 ('jade-not-buried-range3','次三載玉神祭玉不瘗','Third-range jade offering without burial','其祠之皆玉不瘞','皆玉不瘗为祭礼，郭注不埋所用玉也跨行，非载玉身体形貌注。','The jade rite is not buried; its cross-line gloss concerns the jade used in ritual, not body shape.','Their rites use jade without burial.','不埋所用玉也','Guo Pu says not to bury the jade used, continuing across units 293–294.'),
 ('bi-burial-range3','次三八足神一璧瘗礼','Third-range eight-footed deity bi burial','其祠之皆用一璧瘞之','八足蛇尾神的祭礼一璧瘗之，不与前组玉不瘗互改。','One bi is buried in this group’s rite, distinct from the preceding no-burial jade rite.','Their rites use one bi with burial.','',''),
 ('grain-no-fire-range3','次三四十四神稌糈与不火食','Third-range forty-four-deity grain and no-fire account','大凡四十四神皆用稌糈米祠之此皆不火食','四十四神用稌糈米、皆不火食照录；不加肉祭、燃烧程序或现代饮食指引。','The forty-four-deity grain and no-fire wording adds no meat offering, burning procedure or modern dietary instruction.','All forty-four deities receive tu grain and rice offerings, described as not fire-eating.','','')]:
  add('range3-summary','rite',key,name,en,q,d,ed,eq,commentary=comment,en_commentary=ec)
 for key,name,en,q,comment,ec in [
 ('zao-range3','藻（次三祭物）','Zao (third-range ritual plant)','一藻茝瘞之','藻聚藻','Guo Pu glosses zao as juzao.'),
 ('zhi-range3','茝（次三祭物）','Zhi (third-range ritual plant)','一藻茝瘞之','茝香草蘭之𩔗音昌代反','Guo Pu calls zhi an aromatic grass in the orchid-like category and gives a cross-unit pronunciation gloss.'),
 ('tu-range3','稌（次三祭米）','Tu grain (third-range rites)','皆用稌糈米祠之','','')]:
  add('range3-summary','plant',key,name,en,q,'祭物名目按原词及郭注留存，不补现代种属或植物图。','The ritual plant name and commentary remain without a modern species or image.',en+' is recorded in the rite.',commentary=comment,en_commentary=ec)
 for kind,key,name,en,q,eq in [
 ('material','jade-carried-range3','玉（次三神所載）','Jade carried by third-range deities','彘身而載玉','The pig-bodied deities carry jade.'),
 ('rite','bi-range3','璧（次三瘗礼）','Bi jade (third-range burial)','用一璧瘞之','The rite uses one bi with burial.'),
 ('material','rice-range3','糈米（次三祭物）','Rice offering (third-range rites)','稌糈米祠之','The rites use tu grain and rice offerings.')]:
  add('range3-summary',kind,key,name,en,q,'神形所载与祭礼所用分开，尺寸形制与现代物种不补。','Carried jade and ritual offerings remain distinct, without fixed dimensions or modern species.',eq)
 for key,name,en,q,eq in [
 ('mountains-book-total','八十七山（北经原报总数）','Eighty-seven mountains (reported Northern total)','凡八十七山','The reported Northern total is eighty-seven mountains.'),
 ('distance-book-total','二萬三千二百三十里（原报总程）','Twenty-three thousand two hundred and thirty li (reported total)','二萬三千二百三十里','The reported Northern distance is twenty-three thousand two hundred and thirty li.')]:
  add('book-total','rite',key,name,en,q,'篇末原报数照录，不用分段数或列数合计静默替换；差异见篇末说明与三列总括。','The closing reported number is retained; range sums and reading-passage counts do not silently replace it.',eq)
 notes={
 'water-beishan-huohuo-shishan':('濩音尺蠖之蠖','Guo Pu’s pronunciation gloss continues across units 259–260.'),
 'water-beishan-zi-gaoshi':('音慈','Guo Pu gives zi pronunciation.'),
 'water-beishan-kou-gaoshi':('音冦；過博陵縣南又東北入于易水','Guo Pu gives kou pronunciation and a historical northeast course, distinct from the main text.'),
 'water-beishan-tan-lushan':('或作郯水','Guo Pu records Tan water as a variant.'),
 'water-beishan-ban-yishan':('音盤','Guo Pu gives pan pronunciation.'),
 'water-beishan-yu-youdu-mufeng':('浴即黒水也','Guo Pu glosses Yu as Black Water; the note continues into unit 289.'),
 'beast-beishan-liuli-raoshan':('未詳或曰鶹鵂鶹也','Guo Pu calls it uncertain and records a liu/xiuliu alternative.'),
 'beast-beishan-shiyu-raoshan':('未詳或作鯢','Guo Pu calls it uncertain and records ni as a variant.')}
 for e in out:
  if e['id'] in notes:e.update(commentary=notes[e['id']][0],en_commentary=notes[e['id']][1])
  if e['id']=='water-beishan-tan-lushan':e['aliases']=['𨜰水','郯水']
  if e['id']=='beast-beishan-shiyu-raoshan':e.update(en_quote='Shi fish occur in the water; eating them is said to kill people.',en_description='Shi fish are named in the Liguo water account. Guo Pu calls them uncertain and records ni as a variant; their form stays unknown. The fatal-eating claim is an ancient account, not present guidance.',description='師魚见歷虢水，郭注未详或作鯢，形貌不足留占位；食之杀人为古籍记述，不作现实鉴毒或食用指引。')
 return out
