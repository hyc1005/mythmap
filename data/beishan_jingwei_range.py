"""Northern passages Pengpi through Xi, reviewed against scans 98–101."""
from beishan_later_ranges import R

ROWS = [
 R('pengpi','彭毗之山','Mount Pengpi',(202,204),
   '虫尾向东三百里为彭毗，上无草木、多金玉，下多水。蚤林水东南注河，肥水南注牀水，肥遺蛇见于后者水文；仅列蛇名，不借渾夕形貌。',
   'Pengpi lies 300 li east of Chongwei, without vegetation above, with gold and jade, and much water below. The Zaolin flows southeast into the He; the Fei flows south into Chuang water. Feiyi snakes are only named.',
   'Three hundred li east is Mount Pengpi, without vegetation above and with gold and jade, and much water below. The Zaolin rises here and flows southeast into the He. The Fei rises here and flows south into Chuang water, with many Feiyi snakes.',
   '0202—0204核98页。音早归蚤林；肥遺仅列名，不混渾夕一首两身六足四翼，牀水不借他篇同名。','Units 202–204 are on scan 98. Zao pronunciation belongs to Zaolin. Feiyi adds no anatomy borrowed from Hunxi.'),
 R('xiaohou','小侯之山','Mount Xiaohou',(205,207),
   '彭毗向东百八十里为小侯，明漳水南注黄泽。鴣𪄶如乌而白文；不灂及郭注不瞧白、或作㬭等疑义保留，不作现实食疗。',
   'Xiaohou lies 180 li east of Pengpi. The Mingzhang flows south into Huangze. Guxi is crow-shaped with white markings; the difficult eating claim and commentary variants remain unresolved.',
   'One hundred and eighty li east is Mount Xiaohou. The Mingzhang rises here and flows south into Huangze. Guxi resembles a crow with white markings; eating it is said to prevent zhuo.',
   '0205—0207均在98页，0207捕获99校回98。姑習二音归鴣𪄶，不灂疑义不强改；白文位置与行走姿态为解释。','Units 205–207 are on scan 98; 207 was captured as 99. The gu-xi gloss belongs to the bird. White-pattern placement and walking pose are artistic.'),
 R('taitou','泰頭之山','Mount Taitou',(208,209),
   '小侯向东三百七十里为泰頭，共水南注虖池；山上多金玉，下多竹箭。共音恭、虖池呼佗二音分归水名，不混敦頭或現代同名河道。',
   'Taitou lies 370 li east of Xiaohou. The Gong flows south into Huchi. Gold and jade occur above, arrow bamboo below; the two river pronunciation glosses remain distinct.',
   'Three hundred and seventy li east is Mount Taitou. The Gong rises here and flows south into Huchi. Gold and jade occur above; arrow bamboo is abundant below.',
   '0208—0209核99页。竹箭保留原词，不拆成已制箭器；两水独立索引，不据音定现代河。','Units 208–209 are on scan 99. Arrow bamboo is not an invented manufactured arrow; pronunciation does not fix a modern river.'),
 R('xuanyuan','軒轅之山','Mount Xuanyuan',(210,212),
   '泰頭向东北二百里为軒轅，上多铜、下多竹。黄鸟如梟而白首，鸣自詨；不因山名补黄帝，也不因鸟名强定全身黄色。',
   'Xuanyuan lies 200 li northeast of Taitou, with copper above and bamboo below. Huangniao is owl-shaped with a white head, calling its name. Neither a deity nor an entirely yellow body is inferred from the names.',
   'Two hundred li northeast is Mount Xuanyuan, with copper above and bamboo below. Huangniao resembles an owl with a white head and calls its name; eating it is said to prevent jealousy.',
   '0210—0212核99页。如梟白首明确；褐身、收翼回首与面盘形为插画解释，食之不妬为古述。','Units 210–212 are on scan 99. Owl form and white head are textual; brown body, folded pose and facial disk are artistic.'),
 R('yeli','謁戾之山','Mount Yeli',(213,216),
   '軒轅向北二百里为謁戾，有松栢金玉；沁水南注河。东有丹林，丹林水南注河，嬰侯水北注汜水。郭注古郡县及异说另存，不推现代源头。',
   'Yeli lies 200 li north of Xuanyuan, with pine, bai trees, gold and jade. The Qin and Danlin separately flow south into the He; the Yinghou flows north into Fan water. Historical commentary is not a modern source identification.',
   'Two hundred li north is Mount Yeli, with pine, bai trees, gold and jade. The Qin rises here and flows south into the He. To the east is a forest called Danlin, whose water flows south into the He. The Yinghou rises here and flows north into Fan water.',
   '0213—0216实际99页，0216捕获100校回99。丹林为段内东向林地，水另建卡；沁水郭注疑难地名字照捕获，不强改今地。','Units 213–216 are on scan 99; 216 was captured as 100. Danlin is a nested forest with a separate river; difficult historical place spellings remain captured.'),
 R('juru','沮洳之山','Mount Juru',(217,218),
   '謁戾向东三百里为沮洳，无草木、有金玉；濝水南注河。经文濝字与郭注淇水叙述分存，不擅改水名字或合现代水系。',
   'Juru lies 300 li east of Yeli, without vegetation and with gold and jade. The Qi flows south into the He. The textual spelling and commentary comparison remain distinct.',
   'Three hundred li east is Mount Juru, without vegetation and with gold and jade. The Qi rises here and flows south into the He.',
   '0217—0218核100页。音其归濝水；郭注淇水出大號山、白溝为古注，不强定同一现代河。','Units 217–218 are on scan 100. The qi gloss belongs to the river; Guo Pu’s historical course is not imposed as a modern identification.'),
 R('shenqun','神囷之山','Mount Shenqun',(219,222),
   '沮洳向北三百里为神囷，上有文石，下有白蛇、飞虫。黄水东注洹水，滏水东注歐水；飞虫与黄水分词，不画黄色虫。神囷山名不另造山神。',
   'Shenqun lies 300 li north of Juru, with patterned stone above and white snakes and flying insects below. The Huang flows east into Huan water; the Fu flows east into Ou water. Insects and the Huang river are separate.',
   'Three hundred li north is Mount Shenqun, with patterned stones above, white snakes and flying insects below. The Huang rises here and flows east into Huan water. The Fu rises here and flows east into Ou water.',
   '0219—0222核100页；0221滏缺字依影印恢复，0222空正文续滏水郭注。洹水非洹山；洹音丸及入清水属洹注，临水县釡口等属滏注。','Units 219–222 are on scan 100. Fu is restored in 221; empty unit 222 continues its commentary. Huan river is not Mount Huan, and the river glosses remain aligned.'),
 R('fajiu','發鳩之山','Mount Fajiu',(223,228),
   '神囷向北二百里为發鳩，多柘木。精衛如乌、文首白喙赤足，为炎帝少女女娃溺东海而化，常衔西山木石堙海；漳水东注河。复用既有發鳩与精衛ID和已核旧图。',
   'Fajiu lies 200 li north of Shenqun, with zhe trees. Jingwei is crow-shaped with a patterned head, white beak and red feet. The youngest daughter of Yandi, Nuwa, drowned in the Eastern Sea and became Jingwei, carrying western wood and stones to fill it. The Zhang flows east into the He.',
   'Two hundred li north is Mount Fajiu, with many zhe trees. Jingwei resembles a crow with a patterned head, white beak and red feet, calling its name. Yandi’s youngest daughter Nuwa drowned while traveling in the Eastern Sea and did not return; she became Jingwei, constantly carrying wood and stones from the western mountains to fill the sea. The Zhang rises here and flows east into the He.',
   '0223—0225在100页，0225捕获101校回100；0226—0228在101页，0228空正文续漳注。女娃不混女媧；西山为叙事来源地，不直接连《西山经》山系。保留原地图坐标作示意，不升级现代定位。','Units 223–225 are on scan 100; 225 was captured as 101. Units 226–228 are on 101; 228 is commentary only. Nuwa is the daughter’s name, not the creator goddess. Western mountains are a narrative source, not the Western chapter.',place_id='place-fajiu'),
 R('shaoshan','少山','Mount Shao',(229,231),
   '發鳩向东北百二十里为少山，上有金玉、下有铜。清漳水东流于濁漳，复用發鳩漳水索引但经名漳与郭注濁漳分别注明；不把郭注古流向当现代汇流点。',
   'Shao lies 120 li northeast of Fajiu, with gold and jade above and copper below. The Qingzhang flows east into the Zhuozhang, linked to Fajiu’s Zhang through the explicit commentary gloss, without a modern confluence claim.',
   'One hundred and twenty li northeast is Mount Shao, with gold and jade above and copper below. The Qingzhang rises here and flows east into the Zhuozhang.',
   '0229—0231核101页；0231空正文续清漳注。郭注清漳一词从230接231，不误接山名；或曰东北入大河是注文异说，不改正文东流于濁漳。','Units 229–231 are on scan 101; 231 continues the Qingzhang gloss. Its alternative northeast course is commentary, not a replacement for the eastward text.'),
 R('xishan-north','錫山','Mount Xi (Northern)',(232,233),
   '少山向东北二百里为錫山，上多玉、下有砥；牛首水东注滏水，滏水与神囷共享索引。錫山不等同《西山经》，也不凭山名增加锡矿。',
   'Xi lies 200 li northeast of Shao, with jade above and whetstone below. The Niushou flows east into the Fu, sharing the Shenqun river index. The mountain’s name adds no tin deposit.',
   'Two hundred li northeast is Mount Xi, with jade above and whetstone below. The Niushou rises here and flows east into the Fu.',
   '0232—0233核101页；0233滏缺字恢复，捕获保留。0234景山实际101页末而捕获102，下轮校核，勿并本段。','Units 232–233 are on scan 101. Fu is restored in 233, with its captured marker preserved. Jing begins at 234, actually ending scan 101 despite capture as 102, and remains pending.'),
]

def entities(E):
 out=[]
 def add(slug,kind,key,name,en,q,desc,ed,eq,**kw):out.append(E(slug,kind,key,name,en,q,desc,ed,eq,**kw))
 for slug,key,name,en,q in [
 ('pengpi','gold-pengpi','金（彭毗）','Gold (Pengpi)','多金玉'),('pengpi','jade-pengpi','玉（彭毗）','Jade (Pengpi)','多金玉'),
 ('taitou','gold-taitou','金（泰頭）','Gold (Taitou)','其上多金玉'),('taitou','jade-taitou','玉（泰頭）','Jade (Taitou)','其上多金玉'),
 ('xuanyuan','copper-xuanyuan','铜（軒轅）','Copper (Xuanyuan)','其上多銅'),
 ('yeli','gold-yeli','金（謁戾）','Gold (Yeli)','有金玉'),('yeli','jade-yeli','玉（謁戾）','Jade (Yeli)','有金玉'),
 ('juru','gold-juru','金（沮洳）','Gold (Juru)','有金玉'),('juru','jade-juru','玉（沮洳）','Jade (Juru)','有金玉'),
 ('shenqun','wenstone-shenqun','文石（神囷）','Patterned stones (Shenqun)','其上有文石'),
 ('shaoshan','gold-shaoshan','金（少山）','Gold (Shao)','其上有金玉'),('shaoshan','jade-shaoshan','玉（少山）','Jade (Shao)','其上有金玉'),
 ('shaoshan','copper-shaoshan','铜（少山）','Copper (Shao)','其下有銅'),
 ('xishan-north','jade-xishan-north','玉（錫山）','Jade (Xi)','其上多玉'),('xishan-north','whetstone-xishan-north','砥（錫山）','Whetstone (Xi)','其下有砥')]:
  add(slug,'material',key,name,en,q,'依本段原文记物产，不补现代成分或借别山图。','This local product is recorded without modern composition or borrowed imagery.',en+' is recorded here.')
 for slug,key,name,en,q in [
 ('taitou','arrow-bamboo-taitou','竹箭（泰頭）','Arrow bamboo (Taitou)','其下多竹箭'),
 ('xuanyuan','bamboo-xuanyuan','竹（軒轅）','Bamboo (Xuanyuan)','其下多竹'),
 ('yeli','pine-yeli','松（謁戾）','Pine (Yeli)','其上多松栢'),('yeli','bai-yeli','栢（謁戾）','Bai trees (Yeli)','其上多松栢'),
 ('fajiu','zhe-fajiu','柘木（發鳩）','Zhe trees (Fajiu)','其上多柘木')]:
  add(slug,'plant',key,name,en,q,'本段草木仅列名，形貌未详，不补树种、叶果或图。','This plant is only named, without invented species, leaf, fruit or image details.',en+' is recorded here.')
 for slug,key,name,en,q,desc,ed,eq in [
 ('pengpi','zaolin-pengpi','蚤林之水','Zaolin water','蚤林之水出焉東南流注于河','蚤林水出彭毗，东南注河，音早归蚤字。','The Zaolin rises at Pengpi and flows southeast into the He.','The Zaolin rises here and flows southeast into the He.'),
 ('pengpi','fei-pengpi','肥水（彭毗）','Fei water (Pengpi)','肥水出焉而南流注于牀水','肥水南注牀水，肥遺蛇见后接水文，不与同音兽名混义。','The Fei flows south into Chuang water; Feiyi snakes follow in the water account.','The Fei rises here and flows south into Chuang water.'),
 ('pengpi','chuang-pengpi','牀水（肥水所注）','Chuang water','南流注于牀水','牀水承肥水南流，仅记本段关系，不借现代水系。','Chuang receives the south-flowing Fei, without a modern course.','The Fei flows south into Chuang water.'),
 ('xiaohou','mingzhang-xiaohou','明漳之水','Mingzhang water','明漳之水出焉南流注于黄澤','明漳水出小侯南注黄泽，不混清漳、濁漳。','The Mingzhang flows south into Huangze, distinct from Qingzhang and Zhuozhang.','The Mingzhang rises here and flows south into Huangze.'),
 ('taitou','gong-taitou','共水（泰頭）','Gong water (Taitou)','共水出焉南注于虖池','共水出泰頭南注虖池，共音恭。','The Gong flows south into Huchi; the name is glossed gong.','The Gong rises here and flows south into Huchi.'),
 ('taitou','huchi-taitou','虖池（共水所注）','Huchi water','南注于虖池','虖池承共水，郭注呼佗二音，不直接替换现代河名。','Huchi receives the Gong; the hu-tuo pronunciation does not fix a modern river.','The Gong flows south into Huchi.'),
 ('yeli','qin-yeli','沁水（謁戾）','Qin water (Yeli)','沁水出焉南流注于河','沁水南注河，郭注古郡县与或出羊头山异说另存。','The Qin flows south into the He; historical places and an alternative source remain commentary.','The Qin rises here and flows south into the He.'),
 ('yeli','danlin-yeli','丹林之水','Danlin water','丹林之水出焉南流注于河','丹林水与同名林地分卡，南注河。','The Danlin river is distinct from its forest namesake and flows south into the He.','The Danlin rises here and flows south into the He.'),
 ('yeli','yinghou-yeli','嬰侯之水','Yinghou water','嬰侯之水出焉北流注于汜水','嬰侯水北注汜水，方向不随邻段河流改南。','The Yinghou flows north into Fan water, without borrowing neighboring southward directions.','The Yinghou rises here and flows north into Fan water.'),
 ('yeli','fan-yeli','汜水（嬰侯所注）','Fan water','北流注于汜水','汜水承嬰侯北流，不借别篇同名定位。','Fan receives the north-flowing Yinghou, without a namesake merger.','The Yinghou flows north into Fan water.'),
 ('juru','qi-juru','濝水（沮洳）','Qi water (Juru)','濝水出焉南流注于河','濝字依正文，郭注另写淇水并记古流向，不擅改经文。','The textual Qi spelling is preserved; the commentary uses another spelling and an ancient course.','The Qi rises here and flows south into the He.'),
 ('shenqun','huang-shenqun','黄水（神囷）','Huang water (Shenqun)','黄水出焉而東流注于洹','黄水东注洹水，与前句飞虫分词。','The Huang flows east into Huan water and is separate from the preceding insects.','The Huang rises here and flows east into Huan water.'),
 ('shenqun','huan-shenqun','洹水（黄水所注）','Huan water (Huang recipient)','東流注于洹','洹为水域，不等同已核洹山；郭注音丸及入清水古述另存。','Huan is water, distinct from Mount Huan; pronunciation and the historical course remain commentary.','The Huang flows east into Huan water.'),
 ('shenqun','fu-shenqun','滏水（神囷、錫山）','Fu water (Shenqun and Xi)','滏水出焉而東流注于歐水','滏水出神囷东注歐水；後文錫山牛首东注此，单索引分存出处。','The Fu rises at Shenqun and flows east into Ou water; later the Niushou joins it from Xi.','The Fu rises here and flows east into Ou water.'),
 ('shenqun','ou-shenqun','歐水（滏水所注）','Ou water','東流注于歐水','歐水承滏水东流，不因郭注清水、漳等字改正文所注。','Ou receives the east-flowing Fu; commentary names do not replace the textual recipient.','The Fu flows east into Ou water.'),
 ('fajiu','donghai-fajiu','東海（精衛叙事）','Eastern Sea (Jingwei account)','遊于東海溺而不返','东海为女娃溺而化鸟及精衛堙海的叙事水域，不并湖灌泛称海。','The Eastern Sea belongs to the transformation and filling account, without merging Huguan’s generic sea.','Nuwa traveled in the Eastern Sea, drowned and did not return.'),
 ('fajiu','zhang-fajiu','漳水、濁漳（發鳩、少山）','Zhang / Zhuozhang (Fajiu and Shao)','漳水出焉東流注于河','發鳩正文漳水，郭注濁漳；少山清漳东流于濁漳，按明确郭注共用索引，不推现代河口。','Fajiu names Zhang, glossed Zhuozhang; Shao sends Qingzhang east into Zhuozhang. The explicit gloss supports one textual index, without a modern confluence.','The Zhang rises here and flows east into the He.'),
 ('shaoshan','qingzhang-shaoshan','清漳之水','Qingzhang water','清漳之水出焉東流于濁漳之水','清漳东流于濁漳；郭注或曰东北入大河为另说，不代替正文。','The Qingzhang flows east into Zhuozhang; the alternative northeast course remains commentary.','The Qingzhang rises here and flows east into the Zhuozhang.'),
 ('xishan-north','niushou-xishan-north','牛首之水（錫山）','Niushou water (Xi)','牛首之水出焉而東流注于滏水','牛首水出錫山东注滏水，不因牛首名造牛首生物。','The Niushou flows east into the Fu; its name adds no ox-headed creature.','The Niushou rises here and flows east into the Fu.')]:
  add(slug,'water',key,name,en,q,desc,ed,eq)
 add('pengpi','beast','feiyi-pengpi','肥遺之蛇（彭毗）','Feiyi snakes (Pengpi)','其中多肥遺之蛇','仅载肥遺蛇名，形貌不足；不借渾夕或西山同名的首足翼数。','Feiyi snakes are only named; no heads, feet or wings are borrowed from namesakes.','Feiyi snakes are abundant in the water account.',unknown=True,water=True)
 add('xiaohou','beast','guxi-xiaohou','鴣𪄶（小侯）','Guxi (Xiaohou)','有鳥其状如烏而白文名曰鴣𪄶食之不灂','乌状白文，白纹位置、黑身与行走姿态为如乌的插画解释；不灂疑义及郭注异文保留。','Guxi is crow-shaped with white markings. Mark placement, black body and walking pose are artistic; the difficult eating claim remains unresolved.','Guxi resembles a crow with white markings; eating it is said to prevent zhuo.',commentary='姑習二音；不瞧白也或作㬭音醮',en_commentary='Guo Pu gives gu-xi pronunciation and records difficult wording and a variant for the eating claim.')
 add('xuanyuan','beast','huangniao-xuanyuan','黄鳥（軒轅）','Huangniao (Xuanyuan)','有鳥焉其状如梟而白首其名曰黄鳥其鳴自詨食之不妬','梟状白首，褐色躯体、回首收翼、无角羽的面盘为解释；不借西山黄鸟形态，不因名强定全身黄色。','Huangniao is owl-shaped and white-headed. Brown body, turned head, folded wings and smooth facial disk are artistic; the Western namesake is not copied.','Huangniao resembles an owl with a white head, calls its name, and is said to prevent jealousy when eaten.')
 add('yeli','place','danlin-forest-yeli','丹林（謁戾东林）','Danlin forest (east of Yeli)','其東有林焉名曰丹林','謁戾东有丹林，林地与丹林水分别建卡；丹字不强定红树种或整体叶色。','Danlin is a forest east of Yeli, separate from its river; the name does not fix red foliage or a tree species.','To its east is a forest called Danlin.')
 for key,name,en,q in [('white-snakes-shenqun','白蛇（神囷）','White snakes (Shenqun)','其下有白蛇'),('flying-insects-shenqun','飛蟲（神囷）','Flying insects (Shenqun)','有飛蟲')]:
  add('shenqun','beast',key,name,en,q,'仅列名与有限特征，不定具体物种或首翼足数；留占位。','Only a name and limited traits are given, without a fixed species or invented anatomy.',en+' are recorded here.',unknown=True)
 add('fajiu','beast','jingwei-fajiu','精衛','Jingwei','有鳥焉其状如烏文首白喙赤足名曰精衛其鳴自詨是炎帝之少女名曰女娃女娃遊于東海溺而不返故為精衛常銜西山之木石以堙于東海','精衛乌状文首、白喙赤足。女娃为炎帝少女，溺东海而化鸟，衔西山木石堙海；不混女媧。旧图文首白喙赤足及衔石已核，旋纹、黑羽和飞姿为解释。','Jingwei is crow-shaped with a patterned head, white beak and red feet. Yandi’s youngest daughter Nuwa drowned in the Eastern Sea and became the bird, carrying western wood and stones to fill it. The retained image matches the stated form; carved curls, black plumage and flight pose are artistic.','Jingwei resembles a crow with a patterned head, white beak and red feet, calling its name. Yandi’s youngest daughter Nuwa drowned in the Eastern Sea and became Jingwei, carrying western wood and stones to fill it.',commentary='炎帝神農也娃惡佳反語誤或作階；堙塞也音因',en_commentary='Guo Pu identifies Yandi as Shennong, records daughter-name pronunciation and variants, and glosses filling.',aliases=['精卫','精衛','女娃'])
 out[-1]['id']='beast-jingwei'
 add('fajiu','place','western-mountains-fajiu','西山（精衛取材叙事）','Western mountains (Jingwei account)','常銜西山之木石以堙于東海','西山是精衛衔木石的叙事来源，不直接指向《西山经》全部已核山，不补坐标或路线。','The western mountains supply the carried materials in this account, without a link to every Western-chapter mountain or an invented route.','It constantly carries wood and stones from the western mountains to fill the Eastern Sea.')
 for key,name,en in [('wood-fajiu','木（精衛所衔）','Wood (carried by Jingwei)'),('stones-fajiu','石（精衛所衔）','Stones (carried by Jingwei)')]:
  add('fajiu','material',key,name,en,'常銜西山之木石以堙于東海','木石为堙海叙事材料，不指定树种矿种；旧图单衔石代表，不冒充木石同时出现。','Wood and stones are narrative materials without a fixed species or mineral; the retained single stone is representative.',en+' comes from the western mountains.')
 notes={
 'water-beishan-zaolin-pengpi':('音早','Guo Pu gives zao pronunciation.'),
 'water-beishan-gong-taitou':('音恭','Guo Pu gives gong pronunciation.'),
 'water-beishan-huchi-taitou':('呼佗二音下同','Guo Pu gives hu-tuo pronunciation.'),
 'water-beishan-qin-yeli':('至滎陽縣東北入河或出榖述縣羊頭山也','Guo Pu records a historical course and an alternative Yangtou source; difficult place spelling is retained.'),
 'water-beishan-qi-juru':('音其；今淇水出汲郡隆慮縣大號山東過河内縣南為白溝','Guo Pu gives qi pronunciation and a historical river comparison.'),
 'water-beishan-huan-shenqun':('洹水出汲郡林慮縣東北至魏郡長樂入清水洹音丸','Guo Pu describes Huan’s historical course and gives wan pronunciation.'),
 'water-beishan-fu-shenqun':('水今出臨水縣西釡口山經鄴西北至列人縣入于漳其水𤍠','Guo Pu’s Fu gloss continues into the empty main-text unit, including an ancient course and warm-water account.'),
 'water-beishan-zhang-fajiu':('濁漳音章或曰出長子縣鹿谷山而東至鄴入清漳','Guo Pu explicitly glosses Zhang as Zhuozhang, gives pronunciation and records an alternative historical course.'),
 'water-beishan-qingzhang-shaoshan':('清漳出少山大繩谷至武安縣南暴宫邑入濁漳或曰東北至邑城入于大河也','Guo Pu’s Qingzhang gloss spans units 230–231 and records an alternative course.')}
 for e in out:
  if e['id']=='water-beishan-danlin-yeli':e['context']='place-beishan-danlin-forest-yeli'
  if e['id'] in {'material-beishan-wood-fajiu','material-beishan-stones-fajiu'}:e['context']='place-beishan-western-mountains-fajiu'
  if e['id'] in notes:e.update(commentary=notes[e['id']][0],en_commentary=notes[e['id']][1])
 return out

