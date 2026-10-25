"""Five Northern passages Zhe through Taixi, reviewed against scans 103–104."""
from beishan_later_ranges import R
from beishan_dunyu_range import REMAINING as PREVIOUS_REMAINING

REMAINING = PREVIOUS_REMAINING[5:]
ROWS = [
 R('zheshan','柘山','Mount Zhe',(245,246),
   '敦與向北百七十里为柘山，阳有金玉、阴有铁；歷聚水北注洧水。洧保留繡山源出东注河与本段受水两处文本上下文，不据同名认定现代河道。',
   'Zhe lies 170 li north of Dunyu, with gold and jade on its sunny side and iron on its shaded side. The Liju flows north into Wei water. The Wei name retains separate source and recipient contexts, without a modern river identification.',
   'One hundred and seventy li north is Mount Zhe, with gold and jade on its sunny side and iron on its shaded side. The Liju rises here and flows north into Wei water.',
   '0245—0246核103页；歷聚北流不改东流。与繡山洧水共用文本水名索引，但分存两段摘句与上下文，不据此推现代同一水系。','Units 245–246 are on scan 103. Liju flows north. The Wei textual name index retains both passages separately, without a modern shared-course claim.'),
 R('weilong','維龍之山','Mount Weilong',(247,250),
   '柘山向北三百里为維龍，上有碧玉、阳有金、阴有铁。肥水东注皐澤，水中礨石郭注未详及异说保留；敞鐡水北注大澤。肥水不混彭毗同名水，大澤不并其他泰澤。',
   'Weilong lies 300 li north of Zhe, with green jade above, gold on the sunny side and iron on the shaded side. The Fei flows east into Gaoze, with uncertain lei stone; the Changtie flows north into Daze. Namesakes remain separate.',
   'Three hundred li north is Mount Weilong, with green jade above, gold on its sunny side and iron on its shaded side. The Fei rises here and flows east into Gaoze, with much lei stone. The Changtie rises here and flows north into Daze.',
   '0247—0250全在103页。礨石未詳也音雷等注跨248—249连读，不移给敞鐡水；異作壘、磈壘及石名说均存，不擅定矿种。維龍山名不造龙。','Units 247–250 are on scan 103. The uncertain lei-stone gloss spans 248–249 and is not assigned to Changtie. Variants remain, without a mineral identity or a dragon inferred from the mountain name.'),
 R('baima','白馬之山','Mount Baima',(251,252),
   '維龍向北百八十里为白馬，阳多石玉、阴多鐡，并多赤铜。木馬水东北注虖沱；石玉保留连写，不擅定玉种；白馬与木馬均不据名造马形生物。',
   'Baima lies 180 li north of Weilong, with the written expression shiyu on its sunny side, iron on its shaded side and red copper. The Muma flows northeast into Hutuo. Names do not add horses or a modern jade variety.',
   'One hundred and eighty li north is Mount Baima, with much shiyu on its sunny side, iron on its shaded side and red copper. The Muma rises here and flows northeast into Hutuo.',
   '0251—0252实际103页，0252捕获104校回103。呼佗二音归虖沱；石玉连写按物产表达保存，不加白马或木马图。','Units 251–252 are on scan 103; 252 was captured as 104. Hu-tuo belongs to the water name; shiyu remains as written, without horse imagery.'),
 R('kongsang-north','空桑之山（北山经）','Mount Kongsang (Northern)',(253,254),
   '白馬向北二百里为空桑，无草木，冬夏有雪；空桑水东注虖沱。郭注疑与前见同名山，仍分篇建档，不因桑字补桑树或现代雪线。',
   'Kongsang lies 200 li north of Baima, without vegetation and with snow in winter and summer. Its river flows east into Hutuo. Commentary suspects a namesake; chapter-specific identities remain separate.',
   'Two hundred li north is Mount Kongsang, without grasses or trees, with snow in winter and summer. Kongsang water rises here and flows east into Hutuo.',
   '0253—0254核104页，冬夏有雪跨行。上已有此山疑同名为郭注，不强并他篇空桑或造桑木卡。','Units 253–254 are on scan 104. The snow statement continues across lines. The namesake conjecture remains commentary, without a chapter merger or mulberry card.'),
 R('taixi','泰戱之山','Mount Taixi',(255,258),
   '空桑向北三百里为泰戱，无草木、多金玉。䍶䍶羊状一角一目，目在耳后，鸣自䚯；虖沱水出此东注漊，液女水出阳南注沁水。角目数量与位置不借其他羊兽形。',
   'Taixi lies 300 li north of Kongsang, without vegetation and with gold and jade. Dongdong is sheep-shaped with one horn and one eye behind the ear. Hutuo rises here and flows east into Lou; the Yenu rises on the sunny side and flows south into Qin water.',
   'Three hundred li north is Mount Taixi, without vegetation and with gold and jade. Dongdong resembles a sheep with one horn and one eye behind the ear, calling its name. Hutuo rises here and flows east into Lou. The Yenu rises on its sunny side and flows south into Qin water.',
   '0255—0258核104页；音屋棟之棟归䍶，音樓归漊，液音恱懌之懌归液女。图需单角、单眼在耳后，面前不添正常眼；四蹄、角形、毛色与站姿另标解释。郭注古水源不认作现代坐标。','Units 255–258 are on scan 104. The dong, lou and ye pronunciation glosses remain separate. Art must show one horn and the sole eye behind the ear, without a normal face eye; hooves, horn shape, fleece color and stance are artistic. Ancient source geography adds no modern coordinates.'),
]

def entities(E):
 out=[]
 def add(slug,kind,key,name,en,q,d,ed,eq,**kw):out.append(E(slug,kind,key,name,en,q,d,ed,eq,**kw))
 for slug,key,name,en,q in [
 ('zheshan','gold-zheshan','金（柘山）','Gold (Zhe)','其陽有金玉'),('zheshan','jade-zheshan','玉（柘山）','Jade (Zhe)','其陽有金玉'),('zheshan','iron-zheshan','铁（柘山）','Iron (Zhe)','其隂有鐵'),
 ('weilong','green-jade-weilong','碧玉（維龍）','Green jade (Weilong)','其上有碧玉'),('weilong','gold-weilong','金（維龍）','Gold (Weilong)','其陽有金'),('weilong','iron-weilong','铁（維龍）','Iron (Weilong)','其隂有鐵'),
 ('baima','shiyu-baima','石玉（白馬）','Shiyu (Baima)','其陽多石玉'),('baima','iron-baima','鐡（白馬）','Iron (Baima)','其隂多鐡'),('baima','red-copper-baima','赤铜（白馬）','Red copper (Baima)','多赤銅'),
 ('taixi','gold-taixi','金（泰戱）','Gold (Taixi)','多金玉'),('taixi','jade-taixi','玉（泰戱）','Jade (Taixi)','多金玉')]:
  add(slug,'material',key,name,en,q,'本段物产按原文字序分录，不补现代成分；石玉、碧玉等连写表达照留，不借他山图。','The local product retains its written expression without a modern composition or borrowed image.',en+' is recorded here.')
 for slug,key,name,en,q,d,ed,eq in [
 ('zheshan','liju-zheshan','歷聚之水','Liju water','歷聚之水出焉而北流注于洧水','歷聚水出柘山北注洧水，方向与繡山洧水东注河分开。','The Liju flows north into Wei water, separate from Wei’s eastward source account.','The Liju rises here and flows north into Wei water.'),
 ('weilong','fei-weilong','肥水（維龍）','Fei water (Weilong)','肥水出焉而東流注于皐澤','肥水东注皐泽，礨石接其水文；与彭毗南注牀水的肥水分卡。','This Fei flows east into Gaoze, with lei stone in its account; it remains separate from Pengpi’s Fei.','The Fei rises here and flows east into Gaoze.'),
 ('weilong','gaoze-weilong','皐澤（維龍）','Gaoze (Weilong)','東流注于皐澤','皐泽为維龍肥水所注，不因同音合别山高水或现代湖泊。','Gaoze receives this Fei, without a namesake or modern lake merger.','The Fei flows east into Gaoze.'),
 ('weilong','changtie-weilong','敞鐡之水','Changtie water','敞鐡之水出焉而北流注于大澤','敞鐡水北注大泽，按原字保存，不因鐡字新增本水含铁成分。','The Changtie flows north into Daze; the name adds no iron content to its water.','The Changtie rises here and flows north into Daze.'),
 ('weilong','daze-weilong','大澤（敞鐡所注）','Daze (Changtie recipient)','北流注于大澤','大泽承敞鐡水北流，不并北山既有㤗澤或后文泰澤。','Daze receives the north-flowing Changtie, without merging other marsh names.','The Changtie flows north into Daze.'),
 ('baima','muma-baima','木馬之水','Muma water','木馬之水出焉而東北流注于虖沱','木馬水东北注虖沱，木馬为水名，不画木制马或马兽。','The Muma flows northeast into Hutuo; the name adds no wooden horse or creature.','The Muma rises here and flows northeast into Hutuo.'),
 ('kongsang-north','kongsang-north','空桑之水（北山经）','Kongsang water (Northern)','空桑之水出焉東流注于虖沱','空桑水出北山空桑，东注虖沱，不强并他篇同名水。','The Northern Kongsang flows east into Hutuo, without a chapter-name merger.','Kongsang water rises here and flows east into Hutuo.'),
 ('taixi','lou-taixi','漊水（泰戱所注）','Lou water (Taixi)','東流注于漊水','漊水承虖沱东流，音樓归漊；不把液女的液字连为正文漊液水。','Lou receives east-flowing Hutuo; the next Yenu wording is separate, not a combined Louye river.','Hutuo flows east into Lou water.'),
 ('taixi','yenu-taixi','液女之水','Yenu water','液女之水出于其陽南流注于沁水','液女水出泰戱阳面，南注沁水，液音恱懌之懌；不因女字造女神。','The Yenu rises on Taixi’s sunny side and flows south into Qin water; the name adds no goddess.','The Yenu rises on its sunny side and flows south into Qin water.')]:
  add(slug,'water',key,name,en,q,d,ed,eq)
 add('weilong','material','leishi-weilong','礨石（維龍）','Lei stone (Weilong)','其中多礨石','礨石郭注未详、音雷，又作壘、磈壘大石貌或曰石名；不强定矿物、尺寸或形体图。','Lei stone is uncertain in commentary, with pronunciation and alternative lump/stone-name readings, without a fixed mineral or size.','Lei stone is abundant in the water account.',commentary='未詳也音雷或作壘磈壘大石貌或曰石名',en_commentary='Guo Pu’s uncertain stone gloss spans units 248–249, with pronunciation and alternative readings.',water=True)
 add('taixi','beast','dongdong-taixi','䍶䍶（泰戱）','Dongdong (Taixi)','有獸焉其状如羊一角一目目在耳後其名曰䍶䍶其鳴自䚯','䍶䍶羊状、单角单目，唯一眼在耳后；面前不加正常眼。四蹄、短尾、角形、耳可见性、毛色与站姿为插画解释，不借他羊兽人面或多角。','Dongdong is sheep-shaped with one horn and one eye behind the ear, without a normal face eye. Four hooves, short tail, horn shape, ear visibility, fleece color and stance are artistic.','Dongdong resembles a sheep with one horn and one eye behind the ear, calling its name.',commentary='音屋棟之棟',en_commentary='Guo Pu gives the pronunciation of dong as in the roof-ridge character.')
 for e in out:
  if e['id']=='water-beishan-lou-taixi':e.update(commentary='音樓',en_commentary='Guo Pu gives lou pronunciation.')
  if e['id']=='water-beishan-yenu-taixi':e.update(commentary='液音恱懌之懌',en_commentary='Guo Pu gives ye pronunciation by comparison with a character for pleasure.')
 return out

