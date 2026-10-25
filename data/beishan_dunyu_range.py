"""Five Northern passages Jing after Xi through Dunyu, scans 101–103."""
from beishan_later_ranges import R

ROWS = [
 R('jingshan-after-xi','景山（錫山北）','Mount Jing (north of Xi)',(234,235),
   '錫山向北二百里为此景山，有羙玉；景水东南注海澤。与教山南的景山、平山东的京山分别建档，不因同名或音近合并。',
   'This Jing lies 200 li north of Xi, with fine jade. The Jing river flows southeast into Haize. It is distinct from the earlier Jing south of Jiao and the other Jing east of Ping.',
   'Two hundred li north is Mount Jing, with fine jade. The Jing water rises here and flows southeast into Haize.',
   '0234在101页末而捕获102，校回101；0235海澤在102页。新建独立景山ID；海澤不拆成海与泽、不并泛称海或東海。','Unit 234 ends scan 101 despite capture as 102; 235 is on 102. Jing receives a distinct ID. Haize is kept as one water name, without a merger with generic or Eastern seas.'),
 R('tishou','題首之山','Mount Tishou',(236,236),
   '景山向北百里为題首，有玉、多石、无水。短段独立保留，不由首字补首列总括，不因无水造空河索引。',
   'Tishou lies 100 li north of Jing, with jade and many stones but no water. The short passage remains independent, without an invented river.',
   'One hundred li north is Mount Tishou, with jade, many stones and no water.',
   '0236全在102页。无水为正文，不按别山水文补名或坐标。','Unit 236 is on scan 102. The absence of water is textual, without a borrowed river or coordinates.'),
 R('xiushan','繡山','Mount Xiu',(237,239),
   '題首向北百里为繡山，有玉、青碧，木多栒、草多芍藥芎窮；洧水东注河。水中鱯黽连写，郭注分别述似鲇大白及似小青蟾，又存一物名异说；物名分合不强定。',
   'Xiu lies 100 li north of Tishou, with jade, qingbi, xun trees, shaoyao and qiongqiong grasses. The Wei flows east into the He. Huomin is written together; commentary gives separate fish and small green toad comparisons, but also a single-name alternative.',
   'One hundred li north is Mount Xiu, with jade and qingbi above. Its trees include xun; its grasses include shaoyao and qiongqiong. The Wei rises here and flows east into the He. Huomin occurs in the water.',
   '0237—0239核102页。栒木中枚与音荀归栒；芍藥一名辛夷为古注，不现代物种合并。鱯黽保留双注及蠖黽一物名异说，先设一文本索引、留占位，不擅拼鱼蟾或拆成已定两种。','Units 237–239 are on scan 102. Xun and shaoyao glosses remain aligned. The combined animal name retains both comparisons and the single-name alternative as one unresolved textual index, without a fish-toad composite or fixed two-species split.'),
 R('songshan','松山','Mount Song',(240,240),
   '繡山向北百二十里为松山，陽水东北注河。山名松不当正文多松，陽水东北方向照录，不混陽山留水。',
   'Song lies 120 li north of Xiu. The Yang flows northeast into the He. The mountain name does not establish pine products, and the river remains distinct from Yang’s Liu river.',
   'One hundred and twenty li north is Mount Song. The Yang rises here and flows northeast into the He.',
   '0240全在102页。不凭山名新增松木卡，东北流不改东流或南流。','Unit 240 is on scan 102. No pine card is inferred from the mountain name, and northeast remains unchanged.'),
 R('dunyu','敦與之山','Mount Dunyu',(241,244),
   '松山向北百二十里为敦與，上无草木、有金玉。溹水出阳东注泰陸，泜水出阴东注彭水，槐水东注泜澤。郭注大陸水与泜水古流向跨行分归，不将无草木改为全山无物产。',
   'Dunyu lies 120 li north of Song, without vegetation above and with gold and jade. The Suo rises on the sunny side and flows east into Tailu; the Zhi rises on the shaded side and flows east into Peng water; the Huai flows east into Zhize. Cross-line commentary remains separately aligned.',
   'One hundred and twenty li north is Mount Dunyu, without vegetation above and with gold and jade. The Suo rises on its sunny side and flows east into Tailu water. The Zhi rises on its shaded side and flows east into Peng water. The Huai rises here and flows east into Zhize.',
   '0241—0243实际102页，0243捕获103校回102；0244在103页。大陸水今鉅鹿北廣平澤即其水跨242—243属泰陸，泜水出中丘等跨243—244属泜水，不移给槐水。彭水此处不据同名并帶山彭水。','Units 241–243 are on scan 102; 243 was captured as 103. Unit 244 is on 103. Tailu and Zhi commentary continue across unit boundaries, without assignment to the Huai. Peng remains separate from the Dai namesake.'),
]

REMAINING = [
 ('柘山',245,246),('維龍之山',247,250),('白馬之山',251,252),('空桑之山',253,254),
 ('泰戱之山',255,258),('石山',259,261),('童戎之山',262,263),('髙是之山',264,266),
 ('陸山',267,268),('沂山',269,269),('燕山',270,271),('饒山',272,274),
 ('乾山',275,277),('倫山',278,279),('碣石之山',280,282),('鴈門之山',283,284),
 ('泰澤與帝都之山',285,286),('錞于母逢之山',287,289),
 ('北次三经总括与祭礼',290,296),('北山经篇末总计',297,297),
]

def entities(E):
 out=[]
 def add(slug,kind,key,name,en,q,d,ed,eq,**kw):out.append(E(slug,kind,key,name,en,q,d,ed,eq,**kw))
 for slug,key,name,en,q in [
 ('jingshan-after-xi','fine-jade-jingshan-after-xi','羙玉（錫山北景山）','Fine jade (Jing north of Xi)','有羙玉'),
 ('tishou','jade-tishou','玉（題首）','Jade (Tishou)','有玉焉'),('tishou','stones-tishou','石（題首）','Stones (Tishou)','多石'),
 ('xiushan','jade-xiushan','玉（繡山）','Jade (Xiu)','其上有玉青碧'),('xiushan','qingbi-xiushan','青碧（繡山）','Qingbi (Xiu)','其上有玉青碧'),
 ('dunyu','gold-dunyu','金（敦與）','Gold (Dunyu)','有金玉'),('dunyu','jade-dunyu','玉（敦與）','Jade (Dunyu)','有金玉')]:
  add(slug,'material',key,name,en,q,'本段物产按原文分录，不补现代成分或借别山图。','This local product is recorded without modern composition or borrowed imagery.',en+' is recorded here.')
 for key,name,en,q,comment,ec in [
 ('xun-xiushan','栒（繡山木）','Xun trees (Xiu)','其木多栒','木中枚也音荀','Guo Pu records a wood-use gloss and xun pronunciation.'),
 ('shaoyao-xiushan','芍藥（繡山）','Shaoyao grass (Xiu)','其草多芍藥芎窮','芍藥一名辛夷亦香草属','Guo Pu gives Xinyi as an alternative name and calls it an aromatic grass, without a modern species merger.'),
 ('qiongqiong-xiushan','芎窮（繡山）','Qiongqiong grass (Xiu)','其草多芍藥芎窮','','')]:
  add('xiushan','plant',key,name,en,q,'本段草木仅列名，郭注另存；不由今名补根叶花果或物种图。','This plant is named here, with commentary separate; no modern root, leaf, flower, fruit or species image is inferred.',en+' is recorded here.',commentary=comment,en_commentary=ec)
 for slug,key,name,en,q,d,ed,eq in [
 ('jingshan-after-xi','jing-after-xi','景水（錫山北景山）','Jing water (north of Xi)','景水出焉東南流注于海澤','景水出此景山东南注海澤，与前景山无水文合并。','The Jing flows southeast into Haize, without a merger with the earlier Jing.','The Jing rises here and flows southeast into Haize.'),
 ('jingshan-after-xi','haize-jingshan-after-xi','海澤（景水所注）','Haize (Jing recipient)','東南流注于海澤','海澤作单一受水名，不拆成泛称海与泽或并東海。','Haize remains one water name, without a split into generic sea and marsh or an Eastern Sea merger.','The Jing flows southeast into Haize.'),
 ('xiushan','wei-xiushan','洧水（繡山）','Wei water (Xiu)','洧水出焉而東流注于河','洧水出繡山向东注河，鱯黽接于水文；不补现代河道。','The Wei flows east into the He; Huomin follows in its water account, without a modern course.','The Wei rises here and flows east into the He.'),
 ('songshan','yang-songshan','陽水（松山）','Yang water (Song)','陽水出焉東北流注于河','陽水东北注河，方向与阳山留水南注分别保存。','The Yang flows northeast into the He, distinct from Yang mountain’s south-flowing Liu.','The Yang rises here and flows northeast into the He.'),
 ('dunyu','suo-dunyu','溹水（敦與）','Suo water (Dunyu)','溹水出于其陽而東流注于泰陸之水','溹水出阳而东注泰陸，音悉各反归溹，不移入泜水。','The Suo rises on the sunny side and flows east into Tailu; its pronunciation gloss remains separate from Zhi.','The Suo rises on its sunny side and flows east into Tailu water.'),
 ('dunyu','tailu-dunyu','泰陸之水','Tailu water','東流注于泰陸之水','泰陸承溹水东流；郭注大陸水今鉅鹿北廣平澤即其水跨行，是古述非现代定位。','Tailu receives the east-flowing Suo; the cross-line Dalu and historical Guangping gloss is not a modern location.','The Suo flows east into Tailu water.'),
 ('dunyu','zhi-dunyu','泜水（敦與）','Zhi water (Dunyu)','泜水出于其隂而東流注于彭水','泜水出阴而东注彭水，古注出中丘及入漳跨行续，不赋给槐水。','The Zhi rises on the shaded side and flows east into Peng water; its historical-course gloss continues across lines and is not assigned to Huai.','The Zhi rises on its shaded side and flows east into Peng water.'),
 ('dunyu','peng-dunyu','彭水（敦與受水名）','Peng water (Dunyu recipient)','東流注于彭水','彭水在本段承泜水东流，不因同名并帶山彭水。','Peng receives the east-flowing Zhi here, without a merger with the Dai namesake.','The Zhi flows east into Peng water.'),
 ('dunyu','huai-dunyu','槐水（敦與）','Huai water (Dunyu)','槐水出焉而東流注于泜澤','槐水东注泜泽，不沿用前句泜水郭注作其源头或改注彭水。','The Huai flows east into Zhize, without borrowing the preceding Zhi source gloss or Peng recipient.','The Huai rises here and flows east into Zhize.'),
 ('dunyu','zhize-dunyu','泜澤（槐水所注）','Zhize (Huai recipient)','東流注于泜澤','泜澤是槐水所注，名字有泜不改为泜水同一索引。','Zhize receives the Huai; its name does not make it identical to Zhi water.','The Huai flows east into Zhize.')]:
  add(slug,'water',key,name,en,q,d,ed,eq)
 add('xiushan','beast','huomin-xiushan','鱯黽（繡山物名异说）','Huomin (Xiu name variants)','其中有鱯黽','底本鱯黽连写。郭注鱯似鲇而大白，䵸黽似小青蟾，又有蠖黽一物名异说；先保留单一文本索引与全部异说，不认定一合成生物或已定两物种，暂留占位。','The text writes Huomin together. Commentary compares huo to a large white catfish and another reading to a small green toad, but also offers Huomin as one name. One unresolved textual index preserves all readings without a composite creature or fixed two-species split.', 'Huomin occurs in the water.',commentary='鱯似鮎而大白色也；䵸黽似蝦蟇小而青或曰蠖黽一物名耳',en_commentary='Guo Pu separately gives the large white catfish and small green toad comparisons, then records an alternative reading as one creature name.',unknown=True,water=True)
 notes={
 'water-beishan-suo-dunyu':('音悉各反','Guo Pu gives a pronunciation gloss for Suo.'),
 'water-beishan-tailu-dunyu':('大陸水今鉅鹿北廣平澤即其水','Guo Pu’s historical Dalu/Guangping gloss spans units 242–243.'),
 'water-beishan-zhi-dunyu':('音抵肆反；今泜水出中丘縣西窮泉谷東注于堂陽縣入于漳水','The Zhi pronunciation and historical course span units 243–244, without assignment to the Huai.')}
 for e in out:
  if e['id'] in notes:e.update(commentary=notes[e['id']][0],en_commentary=notes[e['id']][1])
 return out

