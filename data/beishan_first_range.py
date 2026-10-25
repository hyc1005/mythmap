"""Reviewed first-range extension for the Northern Mountains builder."""
import json
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGE_CORRECTIONS = {'source-03-0018': 77, 'source-03-0027': 78,
                    'source-03-0036': 79, 'source-03-0045': 80,
                    'source-03-0054': 81, 'source-03-0063': 82,
                    'source-03-0072': 83, 'source-03-0081': 84,
                    'source-03-0090': 85, 'source-03-0099': 86,
                    'source-03-0108': 87, 'source-03-0117': 88, 'source-03-0126': 89,
                    'source-03-0135': 90, 'source-03-0144': 91,
                    'source-03-0153': 92, 'source-03-0162': 93,
                    'source-03-0171': 94, 'source-03-0180': 95,
                    'source-03-0189': 96, 'source-03-0198': 97,
                    'source-03-0207': 98, 'source-03-0216': 99, 'source-03-0225': 100, 'source-03-0234': 101, 'source-03-0243': 102, 'source-03-0252': 103}
TEXT_CORRECTIONS = [
    dict(source_unit_id='source-03-0221',captured='⟦缺字图:滏⟧',replacement='滏',page=100,basis='100页神囷滏水按影印恢复，捕获不改。'),
    dict(source_unit_id='source-03-0233',captured='⟦缺字图:滏⟧',replacement='滏',page=101,basis='101页錫山牛首注滏按影印恢复，捕获不改。'),
    dict(source_unit_id='source-03-0081',captured='⟦缺字图:⿱彐⿰垁凡--彘⟧',replacement='彘',page=84,basis='84页末人目彘耳，恢复缺字图，捕获另存。'),
    dict(source_unit_id='source-03-0082',captured='⟦缺字图:囂⟧',replacement='囂',page=85,basis='85页诸懐水西注囂水。'),
    dict(source_unit_id='source-03-0085',captured='⟦缺字图:囂⟧',replacement='囂',page=85,basis='85页渾夕囂水出焉。'),
    dict(source_unit_id='source-03-0128',captured='⟦缺字图:囂⟧',replacement='囂',page=90,basis='90页北囂山名按影印恢复，原始捕获标记另存。'),
    dict(source_unit_id='source-03-0136',captured='⟦缺字图:囂⟧',replacement='囂',page=91,basis='91页梁渠鸟名囂按影印恢复。'),
    dict(source_unit_id='source-03-0149',captured='⟦缺字图:⿱彐⿰垁凡--彘⟧',replacement='彘',page=92,basis='92页次二祭礼彘瘗按影印恢复。'),
    dict(source_unit_id='source-03-0169',captured='⟦缺字图:兎⟧',replacement='兎',page=94,basis='94页飛䑕兎状按影印恢复。'),
]


def restored(id, text):
    for c in TEXT_CORRECTIONS:
        if c['source_unit_id'] == id:
            text = text.replace(c['captured'], c['replacement'])
    return text
ROWS = [
    dict(slug='daishan', name='帶山', en_name='Mount Dai', units=(11,16),
         description='求如向北三百里为帶山，上多玉、下多青碧。䑏䟽形如马、一角有错；鵸䳜形如乌、五彩赤文，自为牝牡。彭水向西注芘湖之水，水中儵魚如鸡、赤毛、三尾六足四首。郭注对角错、同名鸟和儵字读音另释，不借西山同名鸟形貌。',
         en_description='Dai lies 300 li north of Qiuru, with jade above and qingbi below. Huanshu is horse-shaped with one plated horn; Qiyu is crow-shaped, five-colored with red markings, and described as being male and female in itself. The Peng flows west into the Pihu, whose water account records red-feathered, chicken-shaped Youyu with three tails, six feet and four heads. The commentary treats horn plates, the namesake bird and pronunciation separately.',
         en_quote='Three hundred li north is Mount Dai, with jade above and qingbi below. Huanshu is horse-shaped, with one horn bearing plates, and is said to ward off fire. Qiyu is crow-shaped, five-colored with red markings, being male and female in itself; eating it is said to prevent sores. The Peng rises here and flows west into the Pihu. Youyu is chicken-shaped with red feathers, three tails, six feet and four heads; it sounds like a magpie and eating it is said to relieve worry.',
         note='0011—0016全核77页，0017譙明另段。䑏䟽一角有錯与郭注甲錯分列；鵸䳜注上已、有此鳥疑同名跨13—14连读，不合并西山三首六尾。儵魚郭注音由，英文采用Youyu，中文与稳定ID保留；不改为普通鱼形。',
         en_note='Units 11–16 are on scan 77; 17 begins Qiaoming. The horn-plate gloss remains commentary. Qiyu’s namesake note continues across units 13–14, without merging it with the Western three-headed six-tailed bird. Youyu follows the pronunciation gloss; its chicken form is retained.'),
    dict(slug='qiaoming', name='譙明之山', en_name='Mount Qiaoming', units=(17,21),
         description='帶山向北四百里为譙明。譙水向西注河，其中何羅之魚一首十身、声音如吠犬。孟槐形如貆而赤豪，郭注以豪猪释貆；本山无草木，多青雄黄，异文多青碧另列，不强拆颜色与矿物。',
         en_description='Qiaoming lies 400 li north of Dai. The Qiao flows west into the He and contains Heluo, with one head and ten bodies, sounding like a barking dog. Menghuai resembles huan with red bristles; Guo Pu glosses huan as a porcupine. The mountain has no vegetation and records qing xionghuang, with a qingbi variant kept separately.',
         en_quote='Four hundred li north is Mount Qiaoming. The Qiao rises here and flows west into the He. Heluo fish have one head and ten bodies, sound like barking dogs, and are said to relieve swellings when eaten. Menghuai resembles huan with red bristles, sounds like liuliu, and is said to ward off misfortune. The mountain has no grasses or trees and much qing xionghuang.',
         note='0017—0018均见77页末，0018虽捕获78页仍校回77；0019—0021在78页。孟槐貆的豪猪释义来自郭注，不画成正文另称豪猪。多青与雄黄跨行连读，按青雄黄整项留歧义，一作多青碧另列，不擅改底本。',
         en_note='Units 17–18 are at the end of scan 77, despite 18 being captured as 78; 19–21 are on 78. The porcupine reading comes from commentary. Qing xionghuang spans a captured line break and remains one uncertain expression; its qingbi variant is not substituted into the main text.'),
    dict(slug='zhuoguang', name='涿光之山', en_name='Mount Zhuoguang', units=(22,25),
         description='譙明向北三百五十里为涿光。囂水向西注河，水中鰼鰼之魚形如鹊、十翼，鳞皆在羽端。山上多松栢，下多㯶橿，兽多麢羊、鸟多蕃。郭注称蕃未详，或云即鴞；异说保留，不借其他山的鸮形补图。',
         en_description='Zhuoguang lies 350 li north of Qiaoming. The Xiao flows west into the He. Xixi is magpie-shaped with ten wings and scales at feather tips. Pines and bai trees grow above, zong and jiang below; lingyang and Fan are named. Guo Pu calls Fan uncertain and offers an owl comparison, retained without borrowing another mountain’s owl illustration.',
         en_quote='Three hundred and fifty li north is Mount Zhuoguang. The Xiao rises here and flows west into the He, containing Xixi fish shaped like magpies with ten wings and scales at feather tips. They sound like magpies and are said to ward off fire and prevent illness when eaten. Pines and bai trees grow above, zong and jiang below; lingyang and Fan are abundant.',
         note='0022—0025全核78页。鰼鰼十翼、鳞在羽端及鹊状同时保留，不据鱼名补鱼尾。㯶、栢、橿依底本；麢羊仅列名，蕃注未詳或云即鴞仍为不确定注说，二者用统一占位。',
         en_note='Units 22–25 are on scan 78. The magpie form, ten wings and scales at feather tips remain together; the fish name adds no fish tail. Edition tree characters remain. Lingyang is name-only and Fan’s owl gloss uncertain, so both keep the shared placeholder.'),
    dict(slug='guoshan', name='虢山', en_name='Mount Guo', units=(26,29),
         description='涿光向北三百八十里为虢山，上多漆，下多桐椐，阳多玉、阴多铁。伊水向西注河，兽多橐駝；寓鸟形如鼠而有鸟翼，声音如羊。桐椐与橐駝的解释来自郭注，正文、注说及图像艺术处理分别记录。',
         en_description='Guo lies 380 li north of Zhuoguang, with qi above, tong and ju below, jade on the sunny side and iron on the shaded side. The Yi flows west into the He. Tuotuo is named; Yu has a mouse-like form with bird wings and a sheep-like sound. Tree and camel explanations remain commentary, distinct from the main text and artistic treatment.',
         en_quote='Three hundred and eighty li north is Mount Guo, with qi above and tong and ju below, jade on its sunny side and iron on its shaded side. The Yi rises here and flows west into the He. Tuotuo beasts are abundant. Yu birds are mouse-shaped with bird wings, sound like sheep, and are said to ward off warfare.',
         note='0026—0027在78页，0027捕获79校回78；79页从注于河及橐駝续。桐梧与桐也跨26—27连读，后句椐樻木腫節中椐桾音祛独归椐，疑难用字不强解。橐駝注有肉鞍等不足决定驼峰数量，暂留占位；寓鼠状鸟翼有明确依据才生图。',
         en_note='Units 26–27 are on scan 78; 27 was captured as 79 and is corrected to 78. Scan 79 continues the confluence and Tuotuo. The tong gloss spans units; the following knotted-wood phrase belongs to ju and is not over-interpreted. The camel gloss does not fix hump count, so it keeps a placeholder; Yu’s mouse-and-bird-wing form supports its illustration.'),
    dict(slug='guowei', name='虢山之尾', en_name='Guo mountain tail', units=(30,31),
         description='虢山向北四百里至虢山之尾，多玉而无石，鱼水出焉，向西注河，水中多文貝。山名与物产看似相异的叙述同时保留，不改无石为有石，不给文貝补造纹色或现代贝种。',
         en_description='Four hundred li north of Guo is its mountain tail, with much jade but no stone. The Yu rises here and flows west into the He, with patterned shells in the water. Both statements about jade and stone remain, without changing the text or assigning colors or a modern shell species.',
         en_quote='Four hundred li north comes the tail of Mount Guo, with much jade but no stone. The Yu River rises here and flows west into the He; patterned shells are abundant in the water.',
         note='0030—0031全核79页，0032丹熏另段。魚水为水名，不将鱼字算作本段新增鱼类；文貝仅列名、玉与无石并存保留。河复用北山本批共享索引，四段摘句各存出处，不与西山河索引或现代河道合并。',
         en_note='Units 30–31 are on scan 79; 32 begins Danxun. Yu is the river name, not an added fish record. Patterned shells remain name-only, and jade and no stone coexist in the quotation. The Northern He index retains four separate contexts without a Western or modern-river merger.'),
]


def E(slug, kind, key, name, en_name, quote, description, en_description, en_quote, **extra):
    return dict(slug=slug,kind=kind,id=f'{kind}-beishan-{key}',name=name,en_name=en_name,quote=quote,
                description=description,en_description=en_description,en_quote=en_quote,**extra)


ENTITIES = [
    E('daishan','material','jade-daishan','玉（帶山）','Jade (Dai)','其上多玉','帶山上多玉，未详颜色或现代种类。','Jade is abundant above Dai; color and modern type are unstated.','Jade is abundant above.'),
    E('daishan','material','qingbi-daishan','青碧（帶山）','Qingbi (Dai)','其下多青碧','帶山下多青碧，保留古籍物产名，不定现代矿物成分。','Qingbi is recorded below Dai, without a modern mineral composition.','Qingbi is abundant below.'),
    E('daishan','beast','huanshu-daishan','䑏䟽（帶山）','Huanshu (Dai)','其状如馬一角有錯其名曰䑏䟽可以辟火','䑏䟽如马、一角有错，郭注释角有甲错。辟火为古籍说法，不画火灾或另加角翼。','Huanshu is horse-shaped with one plated horn, the plates clarified in commentary. The fire-warding claim adds no flames, horns or wings.','Huanshu is horse-shaped with one horn bearing plates and is said to ward off fire.',commentary='言角有甲錯也或作暦；音歡',en_commentary='Guo Pu explains plates on the horn, records a variant and glosses the first name character huan.'),
    E('daishan','beast','qitu-daishan','鵸䳜（帶山）','Qiyu (Dai)','有鳥焉其状如烏五彩而赤文名曰鵸䳜是自為牝牡食之不疽','北山鵸䳜如乌、五彩赤文，自为牝牡；郭注疑与前见同名。与西山三首六尾者分卡，不混其形貌。','The Northern Qiyu is crow-shaped, five-colored with red markings and described as male and female in itself. Guo Pu suspects a namesake; the Western three-headed six-tailed form remains separate.','Qiyu is crow-shaped, five-colored with red markings and male and female in itself; eating it is said to prevent sores.',commentary='上已有此鳥疑同名；無廱疽病也',en_commentary='Guo Pu notes a previously mentioned bird and suspects the same name, then glosses the sores.'),
    E('daishan','water','peng-daishan','彭水（帶山）','Peng River (Dai)','彭水出焉而西流注于芘湖之水','彭水出于帶山，西流注芘湖之水，儵魚见其后水文。','The Peng rises at Dai and flows west into the Pihu; Youyu follows in the water account.','The Peng rises here and flows west into the Pihu.'),
    E('daishan','water','pihu-daishan','芘湖之水（帶山）','Pihu water (Dai)','西流注于芘湖之水','芘湖之水为彭水所注，保留芘字，不据湖名强定现代湖岸或水域。','Pihu receives the Peng; the edition spelling supplies no modern shoreline or waterbody.','It flows west into the Pihu water.'),
    E('daishan','beast','youyu-daishan','儵魚（帶山）','Youyu (Dai)','其中多儵魚其状如鷄而赤毛三尾六足四首其音如鵲食之可以己憂','儵魚鸡状赤毛，三尾、六足、四首，音如鹊；郭注儵音由。解忧食用说为古籍记述，不据鱼名增鱼鳍。','Youyu is chicken-shaped with red feathers, three tails, six feet and four heads, sounding like a magpie. Its pronunciation follows commentary; the eating claim adds no fish fins.','Youyu is chicken-shaped with red feathers, three tails, six feet and four heads; it sounds like a magpie and is said to relieve worry when eaten.',commentary='音由',en_commentary='Guo Pu glosses the name character you.',water=True),
    E('qiaoming','water','qiao-qiaoming','譙水（譙明）','Qiao River (Qiaoming)','譙水出焉西流注于河','譙水出于譙明，西流注河，其中何羅一首十身；不推出现代汇流点。','The Qiao rises at Qiaoming and flows west into the He, with one-headed ten-bodied Heluo; no modern confluence is inferred.','The Qiao rises here and flows west into the He.'),
    E('qiaoming','beast','heluo-qiaoming','何羅之魚','Heluo fish','其中多何羅之魚一首而十身其音如吠犬食之已癰','何羅一首十身，声音如吠犬。十身配图各为独立鱼身，不画十头或章鱼触腕；治癰食用说为古籍记述。','Heluo has one head and ten bodies, sounding like a barking dog. Each illustrated branch is a fish body, not an extra head or octopus arm; the healing claim remains an ancient account.','Heluo fish have one head and ten bodies, sound like barking dogs, and are said to relieve swellings when eaten.',water=True),
    E('qiaoming','beast','menghuai-qiaoming','孟槐','Menghuai','有獸焉其状如貆而赤豪其音如榴榴名曰孟槐可以禦凶','孟槐如貆、赤豪，声音如榴榴。豪猪释义来自郭注；配图赤刺不作火焰，禦凶说不新增战斗情节。','Menghuai resembles huan with red bristles and a liuliu sound. The porcupine reading comes from commentary; red quills are not flames and the warding claim adds no battle scene.','Menghuai resembles huan with red bristles, sounds like liuliu, and is said to ward off misfortune.',commentary='貆豪猪也音丸；辟凶邪氣也亦在畏狩畫中也',en_commentary='Guo Pu identifies huan as a porcupine, glosses its pronunciation and explains the warding account.'),
    E('qiaoming','material','qingxionghuang-qiaoming','青雄黄（譙明）','Qing xionghuang (Qiaoming)','多青雄黄','多青与雄黄跨行连读，保留青雄黄整项；郭注一作多青碧为异文，不强定现代成分。','Qing xionghuang spans the line break and remains one expression. The qingbi alternative is a variant, not a modern identification.','Much qing xionghuang occurs here.',commentary='一作多青碧',en_commentary='A variant reads much qingbi.'),
    E('zhuoguang','water','xiao-zhuoguang','囂水（涿光）','Xiao River (Zhuoguang)','囂水出焉而西流注于河','囂水出于涿光，西流注河，鰼鰼见于本段水文；与西山同名水分开。','The Xiao rises at Zhuoguang and flows west into the He; Xixi belongs to this water account, separate from Western namesakes.','The Xiao rises here and flows west into the He.'),
    E('zhuoguang','beast','xixi-zhuoguang','鰼鰼之魚','Xixi fish','其中多鰼鰼之魚其状如鵲而十翼鱗皆在羽端其音如鵲可以禦火食之不癉','鰼鰼如鹊而十翼，鳞皆在羽端，音如鹊。禦火与食用不癉为古籍记述，不把鱼名画成鱼尾或把十翼混作尾羽。','Xixi is magpie-shaped with ten wings, scales at feather tips and a magpie-like sound. The ancient fire and eating claims add no fish tail, and ten wings are counted separately from tail feathers.','Xixi is magpie-shaped with ten wings and scales at feather tips, sounds like a magpie, and is said to ward off fire and prevent illness when eaten.',commentary='音袴褶之褶',en_commentary='Guo Pu supplies a pronunciation comparison for the name.',water=True),
    E('zhuoguang','plant','pine-zhuoguang','松（涿光）','Pines (Zhuoguang)','其上多松栢','涿光上多松栢，此卡只录松，不借别山树形。','Pines and bai are recorded above Zhuoguang; this card isolates pines without borrowing another mountain’s form.','Pines and bai trees are abundant above.'),
    E('zhuoguang','plant','bai-zhuoguang','栢（涿光）','Bai trees (Zhuoguang)','其上多松栢','栢依底本字形，未详本段树貌。','The edition’s bai spelling is retained; its form is unstated here.','Pines and bai trees are abundant above.'),
    E('zhuoguang','plant','zong-zhuoguang','㯶（涿光）','Zong trees (Zhuoguang)','其下多㯶橿','山下多㯶，保留底本异体，不追加叶形或功效。','Zong grows below; the edition character is retained without added leaf form or uses.','Zong and jiang trees are abundant below.'),
    E('zhuoguang','plant','jiang-zhuoguang','橿（涿光）','Jiang trees (Zhuoguang)','其下多㯶橿','橿与㯶并列，不强定现代树种或借用西山同名图。','Jiang appears beside zong, without a modern species claim or borrowed Western illustration.','Zong and jiang trees are abundant below.'),
    E('zhuoguang','beast','lingyang-zhuoguang','麢羊（涿光）','Lingyang (Zhuoguang)','其獸多麢羊','本段麢羊仅列名，未述角数、毛色等形貌，继续统一占位。','Lingyang is only named here, with no horn count or coat color; it keeps the shared placeholder.','Lingyang beasts are abundant.',unknown=True),
    E('zhuoguang','beast','fan-zhuoguang','蕃（涿光）','Fan (Zhuoguang)','其鳥多蕃','蕃只列名，郭注未詳或云即鴞；不把不确定的鸮说当已核定形貌，保留占位。','Fan is only named; Guo Pu calls it uncertain and offers an owl comparison. This uncertain gloss does not fix its form, so the placeholder remains.','Fan birds are abundant.',commentary='未詳或云即鴞音煩',en_commentary='Guo Pu calls it uncertain, offers an owl comparison and glosses its pronunciation fan.',unknown=True),
    E('guoshan','plant','qi-guoshan','漆（虢山）','Qi trees (Guo)','其上多漆','虢山上多漆，作为本段草木名录，不附加现代树种形态。','Qi is recorded above Guo as a plant entry without an added modern botanical form.','Qi is abundant above.'),
    E('guoshan','plant','tong-guoshan','桐（虢山）','Tong trees (Guo)','其下多桐椐','桐与椐并列；桐梧与下一单元桐也连读为郭注，和椐的腫節说明分开。','Tong stands beside ju. Its commentary spans the captured line break and remains separate from the knotted-wood gloss for ju.','Tong and ju are abundant below.',commentary='桐梧桐也',en_commentary='Guo Pu identifies tong with wutong.'),
    E('guoshan','plant','ju-guoshan','椐（虢山）','Ju trees (Guo)','其下多桐椐','椐的郭注有腫節等描述，中椐桾等疑难录文保留，不强定现代树种、器物或功效。','The ju commentary mentions knots in the wood. Difficult captured wording is retained without asserting a modern species, object or use.','Tong and ju are abundant below.',commentary='椐樻木腫節中椐桾音祛',en_commentary='The captured gloss describes knotted wood and retains a difficult use-related phrase and a pronunciation comparison.'),
    E('guoshan','material','jade-guoshan','玉（虢山）','Jade (Guo)','其陽多玉','虢山阳面多玉，阴面铁另卡保存，不推出现代矿带。','Jade is abundant on Guo’s sunny side; the shaded-side iron has its own card, without a modern mineral belt.','Jade is abundant on its sunny side.'),
    E('guoshan','material','iron-guoshan','铁（虢山）','Iron (Guo)','其隂多鐡','虢山阴面多铁，保留鐡字引文，不增加开采年代。','Iron is abundant on Guo’s shaded side; the edition character remains, without an invented mining date.','Iron is abundant on its shaded side.'),
    E('guoshan','water','yi-guoshan','伊水（虢山）','Yi River (Guo)','伊水出焉西流注于河','伊水出虢山，西流注河。名称不直接确定现代伊河，也不据此改变流向。','The Yi rises at Guo and flows west into the He; its name does not establish a modern river identity or change its textual direction.','The Yi rises here and flows west into the He.'),
    E('guoshan','beast','tuotuo-guoshan','橐駝（虢山）','Tuotuo (Guo)','其獸多橐駝','郭注说橐駝有肉鞍、善行流沙等，未明确峰数等造型信息；古籍载重里程另作注说，暂不借现代骆驼图补定形貌。','Guo Pu describes a fleshy saddle and travel through sand but does not fix hump count or other design details. Load and distance claims remain commentary; a modern camel image is not used to settle its form.','Tuotuo beasts are abundant.',commentary='有肉鞍善行流沙中日行三百里其負千斤知水泉所在也',en_commentary='Guo Pu records a fleshy saddle, sand travel, daily distance, carrying load and awareness of water sources.',unknown=True),
    E('guoshan','beast','yu-guoshan','寓（虢山）','Yu (Guo)','其鳥多寓状如䑕而鳥翼其音如羊可以禦兵','寓鼠状而有鸟翼，音如羊，禦兵为古籍说法。配图用鼠首鼠身及羽翼，不画蝙蝠膜翼或兵器战场。','Yu is mouse-shaped with bird wings and a sheep-like sound; its warfare-warding claim remains an ancient account. The image uses a mouse body and feathered wings rather than bat membranes or weapons.','Yu birds are mouse-shaped with bird wings, sound like sheep and are said to ward off warfare.'),
    E('guowei','material','jade-guowei','玉（虢山之尾）','Jade (Guo tail)','其上多玉而無石','多玉而无石并存保留，不按现代矿物知识擅改经文。','Much jade and no stone remain together, without emending the text using modern mineral concepts.','Much jade occurs here, but no stone.'),
    E('guowei','water','yu-guowei','魚水（虢山之尾）','Yu River (Guo tail)','魚水出焉而西流注于河','魚水为水名，西流注河，不另建无依据的鱼类卡。','Yu is a river name and flows west into the He; it does not create an unsupported fish entry.','The Yu rises here and flows west into the He.'),
    E('guowei','material','wenbei-guowei','文貝（虢山之尾）','Patterned shells (Guo tail)','其中多文貝','鱼水水文中多文貝，仅有名称，不补纹色或现代贝种，图片留空。','Patterned shells occur in the Yu water account; no specific pattern, color or modern species is supplied, so no illustration is added.','Patterned shells are abundant in the water.',water=True),
]


ROWS += [
    dict(slug='danxun', name='丹熏之山', en_name='Mount Danxun', units=(32,36),
         description='虢山之尾向北二百里为丹熏，上多樗柏，草多韭薤，多丹雘。熏水向西注棠水。耳䑕鼠状、莬首、麋身，音如獋犬，以尾飞；郭注或作髯飞另存。食用不䐆与禦百毒为古籍记述。',
         en_description='Danxun lies 200 li north of the Guo tail, with chu and bai trees, jiu and xie herbs, and danhuo. The Xun flows west into the Tang. Ershu is mouse-like, with a tu head and deer body, a barking sound, and flight by its tail. The alternative beard-flight gloss and ancient eating claims remain separate.',
         en_quote='Two hundred li north is Mount Danxun, with chu and bai trees, jiu and xie herbs, and much danhuo. The Xun rises here and flows west into the Tang. Ershu is mouse-like, with a tu head and a deer body, sounding like a barking dog and flying by its tail. Eating it is said to prevent abdominal swelling and ward off poisons.',
         note='0032—0036全在79页，0036百毒捕获80校回79。皆山果爾雅有其名为捕获注文，所指不强解。正文莬首、以其尾飛保留；配图兔形首为艺术解释，或作髯飛属郭注异文，不并入正文。䐆大腹也与獋音豪分列。',
         en_note='Units 32–36 are on scan 79; 36 was captured as 80. The fruit-name gloss has an uncertain referent. Tu is retained in transcription; the rabbit-like illustrated head is an interpretation. The alternative beard-flight reading remains commentary, separate from tail flight and the abdominal-swelling gloss.'),
    dict(slug='shizhe', name='石者之山', en_name='Mount Shizhe', units=(37,39),
         description='丹熏向北二百八十里为石者，无草木，多瑶碧。泚水向西注河。孟極如豹、文题白身，善伏、鸣自呼；郭注释题为额，配图额文与白身分明。',
         en_description='Shizhe lies 280 li north of Danxun, without vegetation and with abundant yaobi. The Ci flows west into the He. Mengji resembles a leopard, with a patterned forehead and white body; it hides low and calls its own name. The forehead reading follows commentary.',
         en_quote='Two hundred and eighty li north is Mount Shizhe, without grasses or trees and with much yaobi. The Ci rises here and flows west into the He. Mengji is leopard-shaped, with a patterned forehead and a white body; it is skilled at lying concealed and calls its own name.',
         note='0037—0039全核80页，0040邊春另段。文題白身不可读成全身豹斑；題額也为郭注。河复用本篇共享索引，新增泚水出处，不与西山或现代河道合并。',
         en_note='Units 37–39 are on scan 80; 40 begins Bianchun. The forehead gloss does not authorize spots across the white body. The shared Northern He gains the Ci context without a Western or modern-river merger.'),
    dict(slug='bianchun', name='邊春之山', en_name='Mount Bianchun', units=(40,43),
         description='石者向北百一十里为邊春，多葱葵韭、桃李。杠水西流注泑澤。幽鴳禺状文身，善𥬇、见人则卧、鸣自呼；郭注以佯眠释卧，嬻嬒异名另存。',
         en_description='Bianchun lies 110 li north of Shizhe, with cong, kui, jiu, peach and plum. The Gang flows west into Youze. Youan is monkey-like with a patterned body, laughs, lies down on seeing people and calls its name. Feigned sleep and the alternative name remain commentary.',
         en_quote='One hundred and ten li north is Mount Bianchun, with cong, kui, jiu, peach and plum. The Gang rises here and flows west into Youze. Youan resembles a monkey, has a patterned body, laughs readily, lies down on seeing people and calls its own name.',
         note='0040—0043全核80页。春山异名、葱茖大叶、桃小不解核、幽鴳佯眠与嬻嬒异文分开；不据鴳字补鸟形。杠水与后文櫟水相接，泑澤单设北山索引，不混單狐泑水和西山泑澤。',
         en_note='Units 40–43 are on scan 80. Mountain-name, plant and animal glosses remain separate. The name character does not turn Youan into a bird. The Gang receives the later Li; Northern Youze stays separate from Danhu’s You River and Western namesakes.'),
    dict(slug='manlian', name='蔓聮之山', en_name='Mount Manlian', units=(44,47),
         description='邊春向北二百里为蔓聮，无草木。足訾禺状有鬣，牛尾、文臂、马蹄，见人则呼、鸣自呼。鵁群居朋飞，毛如雌雉、其名自呼；食之已风为古籍说法。',
         en_description='Manlian lies 200 li north of Bianchun and has no vegetation. Zuzi is monkey-like, with a mane, ox tail, patterned arms and horse hooves, calling on seeing people. Jiao lives and flies in groups, has female-pheasant-like plumage and calls its own name; its eating claim is ancient.',
         en_quote='Two hundred li north is Mount Manlian, without grasses or trees. Zuzi resembles a monkey, with a mane, ox tail, patterned arms and horse hooves; it calls on seeing people and cries its own name. Jiao lives and flies in groups, with plumage like a female pheasant; it calls its name and eating it is said to relieve wind illness.',
         note='0044—0045在80页，0045捕获81校回80；0046—0047在81页。足与訾跨页合名；足訾文臂、牛尾、马蹄分别核对。朋猶軰是郭注，群飞写入内容，鵁单体配图不冒充群景；音义注文的渇等疑字依捕获另存，不强解异文；雌雉羽色不借白鵺白翼黄足。',
         en_note='Units 44–45 are on scan 80 and 46–47 on 81; 45 was captured as 81. Zuzi’s name crosses the page break. The mane, patterned arms, ox tail and horse hooves remain distinct. A single Jiao illustration does not depict the textual flock or borrow Baiye’s white wings and yellow feet. Difficult characters in the captured pronunciation/variant gloss remain unresolved.'),
    dict(slug='danzhang', name='單張之山', en_name='Mount Danzhang', units=(48,53),
         description='蔓聮向北百八十里为單張，无草木。諸犍豹状长尾、人首牛耳一目，善吒，行则㗸尾、居则蟠尾。白鵺雉状文首、白翼黄足，食用已嗌痛、已痸为古籍说法。櫟水南流注杠水。',
         en_description='Danzhang lies 180 li north of Manlian, without vegetation. Zhujian is leopard-shaped with a long tail, human head, ox ears and one eye; it roars, holds its tail while walking and coils it at rest. Baiye is pheasant-shaped, with a patterned head, white wings and yellow feet. The Li flows south into the Gang.',
         en_quote='One hundred and eighty li north is Mount Danzhang, without grasses or trees. Zhujian is leopard-shaped with a long tail, human head, ox ears and one eye. It roars, holds its tail while walking and coils it at rest. Baiye is pheasant-shaped, with a patterned head, white wings and yellow feet; eating it is said to relieve throat pain and chi illness. The Li rises here and flows south into the Gang.',
         note='0048—0053全核81页，0054灌題另段。諸犍复用既有稳定ID和图，保留旧篇目锚点，补本山出处；㗸字依捕获，不改写快照。嗌咽也谷梁傳曰嗌与下单元不容粒等连读；痸癡病也为古注，不按现代病种认定。櫟水南流不误作西流。',
         en_note='Units 48–53 are on scan 81; 54 begins Guanti. Zhujian retains its stable ID, artwork and old range anchor while gaining a specific textual context. The throat gloss spans captured units. Chi remains an ancient gloss rather than a modern diagnosis. The Li flows south, not west.'),
]

ENTITIES += [
    E('danxun','plant','chu-danxun','樗（丹熏）','Chu trees (Danxun)','其上多樗柏','丹熏上多樗，未详树貌。','Chu is recorded above Danxun; its form is unstated.','Chu and bai trees are abundant above.'),
    E('danxun','plant','bai-danxun','柏（丹熏）','Bai trees (Danxun)','其上多樗柏','柏依底本，与涿光栢字分别存录。','Bai retains this edition spelling, separately from Zhuoguang.','Chu and bai trees are abundant above.'),
    E('danxun','plant','jiu-danxun','韭（丹熏）','Jiu (Danxun)','其草多韭薤','本山草类韭，仅列名不补叶形。','Jiu is a named herb here without an added leaf form.','Jiu and xie herbs are abundant.'),
    E('danxun','plant','xie-danxun','薤（丹熏）','Xie (Danxun)','其草多韭薤','本山草类薤，不强定现代种。','Xie is retained without a modern species identification.','Jiu and xie herbs are abundant.'),
    E('danxun','material','danhuo-danxun','丹雘（丹熏）','Danhuo (Danxun)','多丹雘','丹雘依底本物产名，不借丹木或指定化学成分。','Danhuo is an edition material name, not dan wood or an asserted chemical composition.','Much danhuo occurs here.'),
    E('danxun','water','xun-danxun','熏水（丹熏）','Xun River (Danxun)','熏水出焉而西流注于棠水','熏水出本山，向西注棠水。','The Xun rises here and flows west into the Tang.','The Xun rises here and flows west into the Tang.'),
    E('danxun','water','tang-danxun','棠水（丹熏）','Tang River (Danxun)','西流注于棠水','棠水承接熏水，未述其源流。','The Tang receives the Xun; its own origin and course are unstated.','It flows west into the Tang.'),
    E('danxun','beast','ershu-danxun','耳䑕','Ershu','有獸焉其状如䑕而莬首麋身其音如獋犬以其尾飛名曰耳䑕食之不䐆又可以禦百毒','耳䑕鼠状、莬首麋身，以尾飞、音如獋犬。兔形首为配图解释，髯飞异文不改正文；食用功效属古籍说法。','Ershu is mouse-like with a tu head, deer body, barking sound and tail-powered flight. A rabbit-like illustrated head is interpretive; beard flight remains a variant and eating claims remain ancient.','Ershu is mouse-like with a tu head and deer body, barking like a dog and flying by its tail; eating it is said to prevent abdominal swelling and ward off poisons.',commentary='或作髯飛；獋音豪；䐆大腹也見禆倉音采也',en_commentary='An alternative reads beard flight; pronunciation and abdominal-swelling glosses are separate.'),
    E('shizhe','material','yaobi-shizhe','瑶碧（石者）','Yaobi (Shizhe)','多瑶碧','瑶碧为本山物产名，未定现代矿物成分。','Yaobi is a material name here without a modern composition.','Much yaobi occurs here.'),
    E('shizhe','water','ci-shizhe','泚水（石者）','Ci River (Shizhe)','泚水出焉而西流注于河','泚水从石者出，西流注河，出处加入北山共享河索引。','The Ci rises at Shizhe and flows west into the shared Northern He index.','The Ci rises here and flows west into the He.'),
    E('shizhe','beast','mengji-shizhe','孟極','Mengji','有獸焉其状如豹而文題白身名曰孟極是善伏其鳴自呼','孟極豹状文题白身、善伏、鸣自呼；题释额来自郭注，不作全身豹斑。','Mengji is leopard-shaped with a patterned forehead and white body, hides low and calls its own name; forehead follows commentary, not full-body spots.','Mengji is leopard-shaped with a patterned forehead and white body, skilled at hiding and calling its own name.',commentary='題額也',en_commentary='Guo Pu glosses ti as forehead.'),
    E('bianchun','plant','cong-bianchun','葱（邊春）','Cong (Bianchun)','多葱葵韭','葱为本山草类；山葱名茖大叶为郭注，未补整株图。','Cong is a local herb; the broad-leaf gloss is commentary and does not supply a full plant illustration.','Cong, kui and jiu are abundant.',commentary='山葱名茖大葉',en_commentary='The mountain cong is called ge and has broad leaves.'),
    E('bianchun','plant','kui-bianchun','葵（邊春）','Kui (Bianchun)','多葱葵韭','葵只列名，不补花色。','Kui is only named; no flower color is added.','Cong, kui and jiu are abundant.'),
    E('bianchun','plant','jiu-bianchun','韭（邊春）','Jiu (Bianchun)','多葱葵韭','本山韭单存出处，不合并丹熏草类卡。','Jiu retains this context separately from Danxun.','Cong, kui and jiu are abundant.'),
    E('bianchun','plant','tao-bianchun','桃（邊春）','Peach (Bianchun)','桃李','桃与李并列；山桃榹桃、子小不解核来自郭注。','Peach stands beside plum; the small clingstone-fruit description comes from commentary.','Peach and plum occur here.',commentary='山桃榹桃子小不解核也',en_commentary='Guo Pu describes mountain peach, called sitao, with small fruit whose flesh clings to the stone.'),
    E('bianchun','plant','li-bianchun','李（邊春）','Plum (Bianchun)','桃李','李仅列名，不把桃的郭注移给李。','Plum is only named; the peach commentary is not assigned to it.','Peach and plum occur here.'),
    E('bianchun','water','gang','杠水（北山经）','Gang River (Northern Mountains)','杠水出焉而西流注于泑澤','杠水出邊春西注泑澤；單張櫟水南流来注，保留两段关系。','The Gang rises at Bianchun and flows west into Youze; the south-flowing Li from Danzhang joins it in a separate passage.','The Gang rises here and flows west into Youze.'),
    E('bianchun','water','youze','泑澤（北山经）','Youze (Northern Mountains)','西流注于泑澤','泑澤承接杠水，不与單狐泑水或西山泑澤自动合并。','Youze receives the Gang and stays separate from Danhu’s You River and Western namesakes.','It flows west into Youze.'),
    E('bianchun','beast','youan-bianchun','幽鴳','Youan','有獸焉其状如禺而文身善𥬇見人則卧名曰幽鴳其鳴自呼','幽鴳禺状文身，善𥬇、见人则卧、鸣自呼；郭注佯眠与异名另存，不加鸟翼。','Youan is monkey-like with a patterned body, laughs, lies down on seeing people and calls its name. Feigned sleep and an alternative name remain commentary; no wings are added.','Youan is monkey-like with a patterned body, laughs, lies down on seeing people and calls its own name.',commentary='言佯眠也；或作嬻嬒鴳音遏',en_commentary='Guo Pu explains feigned sleep, records an alternative name and glosses the final character with e.'),
    E('manlian','beast','zuzi-manlian','足訾','Zuzi','有獸焉其状如禺而有鬛牛尾文臂馬蹄見人則呼名曰足訾其鳴自呼','足訾禺状有鬣、牛尾、文臂、马蹄，见人则呼、鸣自呼。四肢蹄端与配色为插画解释，不增加角翼。','Zuzi is monkey-like with a mane, ox tail, patterned arms and horse hooves, calling on seeing people and crying its name. Hoof placement and color are artistic interpretations.','Zuzi resembles a monkey with a mane, ox tail, patterned arms and horse hooves; it calls on seeing people and cries its own name.'),
    E('manlian','beast','jiao-manlian','鵁','Jiao','有鳥焉群居而朋飛其毛如雌雉名曰鵁其名自呼食之已風','鵁群居朋飞，毛如雌雉、其名自呼。单体图据雌雉般羽毛，不补雄雉艳羽；已风为古籍食用说。','Jiao lives and flies in groups, has female-pheasant-like plumage and calls its own name. Its single-bird illustration adds no bright male plumage; the eating claim is ancient.','Jiao lives and flies in groups, has plumage like a female pheasant and calls its own name; eating it is said to relieve wind illness.',commentary='朋猶軰；交音或作渇也',en_commentary='Guo Pu explains companions and supplies the captured pronunciation and variant gloss.'),
    E('danzhang','beast','zhujian-danzhang','諸犍','Zhujian','有獸焉其状如豹而長尾人首而牛耳一目名曰諸犍善吒行則㗸其尾居則蟠其尾','諸犍豹状长尾、人首牛耳一目，善吒，行则㗸尾、居则蟠尾。复用既有稳定条目与盘尾图，旧篇目锚点保留。','Zhujian has a leopard form, long tail, human head, ox ears and one eye; it roars, holds its tail while walking and coils it at rest. Its stable entry and coiled-tail artwork remain.','Zhujian is leopard-shaped with a long tail, human head, ox ears and one eye; it roars, holds its tail while walking and coils it at rest.',commentary='音如犍牛之犍',en_commentary='Guo Pu supplies a pronunciation comparison.'),
    E('danzhang','beast','baiye-danzhang','白鵺','Baiye','有鳥焉其状如雉而文首白翼黄足名曰白鵺食之已嗌痛可以已痸','白鵺雉状文首、白翼黄足。已嗌痛及已痸为古籍说法，嗌咽也与痸癡病也郭注另列，不当现代治疗依据。','Baiye is pheasant-shaped with a patterned head, white wings and yellow feet. Ancient throat and chi-illness claims are separate from commentary and do not imply modern treatment.','Baiye is pheasant-shaped with a patterned head, white wings and yellow feet; eating it is said to relieve throat pain and chi illness.',commentary='音夜；嗌咽也谷梁傳曰嗌不容粒今呉人呼咽為嗌音隘；痸癡病也',en_commentary='Guo Pu glosses ye, the throat term across captured units, and chi illness.'),
    E('danzhang','water','li-danzhang','櫟水（單張）','Li River (Danzhang)','櫟水出焉而南流注于杠水','櫟水出單張，向南注杠水，不误作其他段的西流。','The Li rises at Danzhang and flows south into the Gang, not west.','The Li rises here and flows south into the Gang.'),
]
next(e for e in ENTITIES if e['id']=='beast-beishan-zhujian-danzhang')['id']='beast-zhu-jian'


ROWS += [
    dict(slug='guanti',name='灌題之山',en_name='Mount Guanti',units=(54,58),
         description='單張向北三百二十里为灌題，上多樗柘，下多流沙和砥。那父如牛而白尾，音如訆；竦斯如雌雉而人面，见人则跃、鸣自呼。匠韓水西注泑澤，其中多磁石；取铁与山下有铜的说法来自郭注。',
         en_description='Guanti lies 320 li north of Danzhang, with chu and zhe above, shifting sand and whetstone below. Nafu is cattle-shaped with a white tail and a calling sound. Songsi has a female-pheasant form and human face, hopping on seeing people and calling its name. The Jianghan flows west into Youze, with magnetic stones in the water account; iron-attraction and copper claims are commentary.',
         en_quote='Three hundred and twenty li north is Mount Guanti, with chu and zhe above and shifting sand and whetstone below. Nafu resembles cattle with a white tail and sounds like a human call. Songsi resembles a female pheasant with a human face; it hops on seeing people and calls its name. The Jianghan rises here and flows west into Youze; magnetic stones are abundant in the water account.',
         note='0054在81页末，捕获82校回81；0055—0058在82页。訆的如人呼喚与音呌跨单元分别回释，不归竦斯。躍跳为郭注。磁石取铁与管子说山下有铜均为古注，不换算现代矿点；泑澤复用北山索引。',
         en_note='Unit 54 is at the end of scan 81, corrected from captured 82; 55–58 are on 82. The human-call and pronunciation glosses belong to Nafu, while the hopping gloss belongs to Songsi. Magnetic-stone and copper claims remain commentary without modern mineral locations.'),
    dict(slug='panhou',name='潘侯之山',en_name='Mount Panhou',units=(59,62),
         description='灌題向北二百里为潘侯，上多松栢，下多榛楛，阳多玉、阴多铁。旄牛牛状四节生毛，背、膝、胡、尾长毛来自郭注。邊水向南注櫟澤；櫟澤不与單張櫟水混并。',
         en_description='Panhou lies 200 li north of Guanti, with pine and bai above, zhen and hu below, jade on the sunny side and iron on the shaded side. Maoniu is cattle-shaped with hair at four joint regions; long hair on the back, knees, dewlap and tail comes from commentary. The Bian flows south into Lize, separate from Danzhang’s Li River.',
         en_quote='Two hundred li north is Mount Panhou, with pine and bai above, zhen and hu below, jade on the sunny side and iron on the shaded side. Maoniu resembles cattle with hair growing at four joint regions. The Bian rises here and flows south into Lize.',
         note='0059—0062全在82页，0062澤为邊水所注櫟澤的续字；0063小咸另段。四節生毛属正文，背膝及胡尾长毛属郭注，不互相替代。北山旄牛不借西山翠山图，櫟澤不按櫟字合并櫟水。',
         en_note='Units 59–62 are on scan 82; the final ze completes Lize. Unit 63 begins Xiaoxian. Hair at four joint regions is main text; the back, knees, dewlap and tail are commentary. The illustration is not borrowed from the Western Maoniu, and Lize is not merged with the Li River.'),
    dict(slug='xiaoxian',name='小咸之山',en_name='Mount Xiaoxian',units=(63,63),
         description='潘侯向北二百三十里为小咸，无草木，冬夏有雪。此段只有山名、方位与雪况；不补生物、现代雪线或山景图，和下一大咸及后文少咸各自分段。',
         en_description='Xiaoxian lies 230 li north of Panhou, without vegetation and with snow in winter and summer. The short passage supplies no creatures or modern snowline. It remains separate from Daxian and the later Shaoxian.',
         en_quote='Two hundred and thirty li north is Mount Xiaoxian, without grasses or trees, with snow in winter and summer.',
         note='0063整句在82页末，捕获83校回82。0064北二百八十里另起大咸，虽无又字仍须独立；小咸与0072少咸不混名。冬夏有雪只作本山记述，不推定现代气候数据。',
         en_note='Unit 63 is at the end of scan 82, corrected from captured 83. Unit 64 begins Daxian without the usual initial again. Xiaoxian is separate from Shaoxian at unit 72. The snow account is not modern climate data.'),
    dict(slug='daxian',name='大咸之山',en_name='Mount Daxian',units=(64,67),
         description='小咸向北二百八十里为大咸，无草木，下多玉，四方不可以上。長蛇毛如彘豪，音如皷柝；郭注百寻及蝮蛇、常山长蛇的比拟另存，不把正文长蛇画成多首有足的龙。',
         en_description='Daxian lies 280 li north of Xiaoxian, without vegetation, with jade below and no ascent from any side. Changshe has pig-bristle-like hair and sounds like drums and watch-clappers. Commentary about length and other snakes remains separate; the main text supplies no extra heads or dragon limbs.',
         en_quote='Two hundred and eighty li north is Mount Daxian, without grasses or trees and with jade below. It cannot be climbed from any side. Changshe is a snake with hair like pig bristles; its sound resembles drums and watch-clappers.',
         note='0064—0067全核83页。皷与柝跨行连读为一种声响描述，0068敦薨另段。郭注長与百尋跨65—66相接；蝮蛇艾綬文及常山长蛇形不同属于比拟，不替正文补定长度、花纹或另一蛇形。',
         en_note='Units 64–67 are on scan 83; drum and clapper span captured lines. Dunhong begins at 68. The commentary length gloss spans 65–66; comparisons to other snakes do not fix the main text’s length, markings or another snake form.'),
    dict(slug='dunhong',name='敦薨之山',en_name='Mount Dunhong',units=(68,71),
         description='大咸向北三百二十里为敦薨，上多㯶柟，下多茈草。敦薨水西注泑澤，随后记出于崑崙东北隅、实惟河源。水中赤鮭与山中兕、旄牛、鳲鳩各存出处；不据郭注名称比拟或别山图补定形貌，不把河源古述当现代定位。',
         en_description='Dunhong lies 320 li north of Daxian, with zong and nan above and zicao below. The Dunhong flows west into Youze, followed by an account of the northeastern corner of Kunlun and a source of the He. Red Gui fish, Si, Maoniu and Shijiu retain local records without borrowing forms from other mountains or treating the ancient source claim as modern geography.',
         en_quote='Three hundred and twenty li north is Mount Dunhong, with zong and nan above and zicao below. The Dunhong rises here and flows west into Youze. The account speaks of the northeastern corner of Kunlun as a source of the He. Red Gui fish are abundant in the water; Si and Maoniu beasts and Shijiu birds are abundant on the mountain.',
         note='0068—0071全在83页，0072少咸始于本页末但留下一阶段。赤鮭注文音与下一单元圭连读，英文Gui据此，不译成现代鲑鱼。出于崑崙东北隅实惟河源原句保留，河源古述与郭注即河水出崑崙之虚分开；撲牛异文所指保留疑义，不强配某兽。四个形貌不足生物用占位，不借潘侯旄牛或西山兕图。',
         en_note='Units 68–71 are on scan 83; Shaoxian begins at the page end but remains for the next stage. Gui follows the pronunciation gloss continuing into unit 71, not a modern salmon identification. The ancient source wording and commentary stay separate. The alternative pu-niu gloss remains uncertain in scope. Four insufficiently described creatures keep placeholders.'),
]

ENTITIES += [
    E('guanti','plant','chu-guanti','樗（灌題）','Chu trees (Guanti)','其上多樗柘','樗与柘并列，仅录本山出处。','Chu stands beside zhe, with this mountain context retained.','Chu and zhe are abundant above.'),
    E('guanti','plant','zhe-guanti','柘（灌題）','Zhe trees (Guanti)','其上多樗柘','柘仅列名，不补树貌。','Zhe is only named, without an added tree form.','Chu and zhe are abundant above.'),
    E('guanti','material','sand-guanti','流沙（灌題）','Shifting sand (Guanti)','其下多流沙','山下多流沙，不推定现代沙漠范围。','Shifting sand occurs below, without a modern desert boundary.','Shifting sand is abundant below.'),
    E('guanti','material','whetstone-guanti','砥（灌題）','Whetstone (Guanti)','多砥','砥为本段石物名，不补现代矿物成分。','Di is a stone material here without an asserted modern composition.','Much whetstone occurs here.'),
    E('guanti','beast','nafu-guanti','那父','Nafu','有獸焉其状如牛而白尾其音如訆名曰那父','那父牛状白尾，音如訆；如人呼唤及訆音呌来自郭注。白尾逐项核对，体色和姿态为艺术解释。','Nafu is cattle-shaped with a white tail and calling sound. Human calling and pronunciation are commentary; body color and pose are artistic interpretations.','Nafu resembles cattle with a white tail and a calling sound.',commentary='如人呼喚；訆音呌',en_commentary='Guo Pu compares the sound to a human call and supplies pronunciation.'),
    E('guanti','beast','songsi-guanti','竦斯','Songsi','有鳥焉其状如雌雉而人靣見人則躍名曰竦斯其鳴自呼也','竦斯如雌雉而人面，见人则跃、鸣自呼。保留人唇鼻面和鸟体，不用同款猛禽脸、展翼或艳雄雉羽替代。','Songsi has a female-pheasant form and human face, hops on seeing people and calls its name. Its human lips and nose and restrained hen plumage distinguish it from a fierce spread-wing bird.','Songsi resembles a female pheasant with a human face; it hops on seeing people and calls its name.',commentary='躍跳',en_commentary='Guo Pu glosses the movement as hopping.'),
    E('guanti','water','jianghan-guanti','匠韓之水','Jianghan River','匠韓之水出焉而西流注于泑澤','匠韓水出灌題，西流注北山泑澤。','The Jianghan rises at Guanti and flows west into Northern Youze.','The Jianghan rises here and flows west into Youze.'),
    E('guanti','material','magnetic-guanti','磁石（灌題水文）','Magnetic stones (Guanti water account)','其中多磁石','磁石在本段水文中；取铁及管子说山上磁石下有铜来自郭注，不作现代矿产定位。','Magnetic stones occur in the water account. Iron attraction and a Guanzi copper claim are commentary, not modern mineral mapping.','Magnetic stones are abundant in this water account.',commentary='可以取鐡管子曰山上有磁石者下必有銅音慈',en_commentary='Guo Pu records iron attraction, cites Guanzi on copper below magnetic stones and glosses the pronunciation ci.',water=True),
    E('panhou','plant','pine-panhou','松（潘侯）','Pine (Panhou)','其上多松栢','松为本山树名，不借别山插画。','Pine is retained in this context without borrowed artwork.','Pine and bai are abundant above.'),
    E('panhou','plant','bai-panhou','栢（潘侯）','Bai (Panhou)','其上多松栢','栢依底本，不改柏字快照。','Bai retains the edition character without rewriting the snapshot.','Pine and bai are abundant above.'),
    E('panhou','plant','zhen-panhou','榛（潘侯）','Zhen (Panhou)','其下多榛楛','榛在山下物产中，仅列名。','Zhen is named among plants below.','Zhen and hu are abundant below.'),
    E('panhou','plant','hu-panhou','楛（潘侯）','Hu (Panhou)','其下多榛楛','楛只列名，不补颜色功效。','Hu is only named, without added colors or uses.','Zhen and hu are abundant below.'),
    E('panhou','material','jade-panhou','玉（潘侯）','Jade (Panhou)','其陽多玉','潘侯阳面多玉，未详成分颜色。','Jade is abundant on the sunny side, with no stated color or composition.','Jade is abundant on its sunny side.'),
    E('panhou','material','iron-panhou','铁（潘侯）','Iron (Panhou)','其隂多鐡','潘侯阴面多铁，保留鐡字引文。','Iron is abundant on the shaded side; the edition character remains.','Iron is abundant on its shaded side.'),
    E('panhou','beast','maoniu-panhou','旄牛（潘侯）','Maoniu (Panhou)','有獸焉其状如牛而四節生毛名曰旄牛','旄牛牛状四节生毛；背膝胡尾长毛来自郭注，逐项另标。深色、长毛垂落方向与姿态为艺术解释，不借西山或本篇仅列名的旄牛形貌。','Maoniu is cattle-shaped with hair at four joint regions. Long hair on the back, knees, dewlap and tail comes from commentary. Dark color, hanging strands and pose are artistic; no Western or name-only form is borrowed.','Maoniu resembles cattle with hair growing at four joint regions.',commentary='今旄牛背膝及胡尾皆有長毛',en_commentary='Guo Pu describes long hair on the back, knees, dewlap and tail.'),
    E('panhou','water','bian-panhou','邊水（潘侯）','Bian River (Panhou)','邊水出焉而南流注于櫟澤','邊水从潘侯出，南流注櫟澤，不把邊水认作邊春杠水。','The Bian rises at Panhou and flows south into Lize, not Bianchun’s Gang.','The Bian rises here and flows south into Lize.'),
    E('panhou','water','lize-panhou','櫟澤（潘侯）','Lize (Panhou)','南流注于櫟澤','櫟澤承接邊水，澤字跨行；与單張櫟水保持独立。','Lize receives the Bian; its name crosses a captured line and stays separate from Danzhang’s Li River.','It flows south into Lize.'),
    E('daxian','material','jade-daxian','玉（大咸）','Jade (Daxian)','其下多玉','大咸山下多玉，不增添矿带。','Jade is abundant below Daxian, without an invented mineral belt.','Jade is abundant below.'),
    E('daxian','beast','changshe-daxian','長蛇（大咸）','Changshe (Daxian)','有蛇名曰長蛇其毛如彘豪其音如皷柝','長蛇有彘豪般毛，音如皷柝。用短硬刺毛与连续蛇身表现，不加肢角；郭注百寻及其他蛇类比拟另存，不强定正文长度。','Changshe has pig-bristle-like hair and a drum-and-clapper sound. Stiff short bristles and a continuous serpent body add no limbs or horns. Commentary about length and other snakes remains separate.','Changshe is a snake with hair like pig bristles and a sound like drums and watch-clappers.',commentary='說者云長百尋今蝮蛇色似艾綬文文間有毛如猪鬐此其𩔗也常山亦有長蛇與此形不同；如人行夜敲木柝聲音託',en_commentary='Guo Pu reports a hundred-xun length, compares a patterned hairy snake, distinguishes the Changshan snake and explains a night-watch clapper. These are commentary comparisons.'),
    E('dunhong','plant','zong-dunhong','㯶（敦薨）','Zong (Dunhong)','其上多㯶柟','㯶依底本异体，只列本山出处。','Zong retains the edition character and this mountain context.','Zong and nan are abundant above.'),
    E('dunhong','plant','nan-dunhong','柟（敦薨）','Nan (Dunhong)','其上多㯶柟','柟只列名，不认定现代树种。','Nan is only named without a modern species claim.','Zong and nan are abundant above.'),
    E('dunhong','plant','zicao-dunhong','茈草（敦薨）','Zicao (Dunhong)','其下多茈草','茈草在山下，仅有名称，不借别山紫茎红花等形貌。','Zicao grows below; no form such as another mountain’s colored stems or flowers is borrowed.','Zicao is abundant below.'),
    E('dunhong','water','dunhong','敦薨之水','Dunhong River','敦薨之水出焉而西流注于泑澤出于崑崙之東北隅實惟河源','敦薨水西注泑澤，后续崑崙东北隅、河源记述依底本存录；不把古述改为现代河源或反推河道。','The Dunhong flows west into Youze, followed by Kunlun’s northeastern corner and a He-source claim. This is retained as an ancient account, not modern hydrography.','The Dunhong rises here and flows west into Youze; the account then speaks of Kunlun’s northeastern corner as a source of the He.',commentary='即河水出崑崙之虚',en_commentary='Guo Pu explains the account as the He emerging from Kunlun’s height.'),
    E('dunhong','place','kunlun-dunhong','崑崙（敦薨水文）','Kunlun (Dunhong water account)','出于崑崙之東北隅實惟河源','崑崙在敦薨段河源记述中出现，东北隅与郭注之虚分开；不合并西山崑崙图示坐标。','Kunlun appears in the Dunhong source account. The northeastern corner and commentary remain distinct, without merging Western diagram coordinates.','The account describes the northeastern corner of Kunlun as a source of the He.',water=True),
    E('dunhong','beast','chigui-dunhong','赤鮭（敦薨）','Red Gui (Dunhong)','其中多赤鮭','赤鮭在敦薨水文中；郭注以鯸鮐为名并音圭，未提供足够独立形貌，留统一占位，不译成现代鲑鱼。','Red Gui occurs in the water account. A commentary name comparison and pronunciation gui do not fix its form; it keeps a placeholder and is not translated as modern salmon.','Red Gui fish are abundant in the water.',commentary='今名鯸鮐為鮭魚音圭',en_commentary='Guo Pu supplies a contemporary fish-name comparison and the pronunciation gui.',unknown=True,water=True),
    E('dunhong','beast','si-dunhong','兕（敦薨）','Si (Dunhong)','其獸多兕旄牛','兕在本山仅列名，不借西山独角兽图补形貌；撲牛异文留在段注。','Si is only named here; no Western horned form is borrowed, and the pu-niu variant stays in the passage commentary.','Si and Maoniu beasts are abundant.',unknown=True),
    E('dunhong','beast','maoniu-dunhong','旄牛（敦薨）','Maoniu (Dunhong)','其獸多兕旄牛','本山旄牛仅列名，保留占位，不将潘侯四节生毛和郭注自动移入本段。','Maoniu is only named here and keeps a placeholder; Panhou’s form and commentary are not transferred automatically.','Si and Maoniu beasts are abundant.',unknown=True),
    E('dunhong','beast','shijiu-dunhong','鳲鳩（敦薨）','Shijiu (Dunhong)','其鳥多鳲鳩','鳲鳩仅列名，未述羽色翼足，不补现代鸟种图。','Shijiu is only named, without feather color or anatomical detail; no modern bird image is added.','Shijiu birds are abundant.',unknown=True),
]


ROWS += [
    dict(slug='shaoxian',name='少咸之山',en_name='Mount Shaoxian',units=(72,75),
         description='敦薨向北二百里为少咸，无草木，多青碧。窫窳牛状赤身、人面马足，音如婴儿，食人；尔雅虎爪异说另存。敦水东注鴈門之水，其中䰽䰽鱼的食用杀人说为古籍记述；不混小咸或敦薨水。',
         en_description='Two hundred li north is Mount Shaoxian, without vegetation and with much qingbi. Yayu is cattle-shaped with a red body, human face and horse feet, cries like an infant and eats people. The Dun flows east into Yanmen water, with Peipei fish whose consumption is said to be fatal.',
         note='0072在83页末，捕获84校回83；0073—0075在84页。少咸不混小咸，敦水不混敦薨水。窫窳马足与郭注尔雅虎爪异说分列；䰽郭注未详或作鯆不足补定形貌，留占位。鴈門山间为郭注地点，不加现代坐标。',
         en_note='Unit 72 is on scan 83, corrected from captured 84; 73–75 are on 84. Shaoxian and the Dun differ from Xiaoxian and Dunhong. Tiger claws and Yanmen mountain are commentary. Peipei remains insufficiently described.'),
    dict(slug='yufa',name='獄法之山',en_name='Mount Yufa',units=(76,79),
         description='少咸向北二百里为獄法。瀤澤水东北注㤗澤，䲃鱼鲤状鸡足。山𤟤犬状人面，善投、见人则笑，行如风；天下大风及食䲃已疣均为古籍说法，不增人手兵器。',
         en_description='Two hundred li north is Mount Yufa. The Huaize flows northeast into Taize, with carp-shaped Zao fish having chicken feet, said to relieve warts when eaten. Shanhui is dog-shaped with a human face, skilled at throwing, smiles on seeing people and moves like wind; its appearance is said to bring great winds.',
         note='0076—0079全核84页，0080北嶽另段。瀤音懐、䲃音藻、𤟤音暉、行风言疾各归其词。善投不据此补人手兵器；鸡足未定数，配图两足为解释。㤗保留捕获异体。',
         en_note='Units 76–79 are on scan 84. Pronunciations and the speed gloss stay separate. Throwing supplies no human hands or weapons. Two illustrated chicken feet are interpretive; the Taize character is retained.'),
    dict(slug='beiyue',name='北嶽之山',en_name='Mount Beiyue',units=(80,84),
         description='獄法向北一百里为北嶽，多枳𣗥刚木。諸懐牛状四角、人目彘耳，音如鸣雁、食人。諸懐水西注囂水，鮨鱼鱼身犬首、音如婴儿；不借郭注其他海鱼的虎鹿猪首。',
         en_description='One hundred li north is Mount Beiyue, with zhi, ji and gang wood. Zhuhuai is cattle-shaped with four horns, human eyes and pig ears, sounds like a goose and eats people. The Zhuhuai flows west into the Xiao, with dog-headed fish-bodied Yi fish that cry like infants and are said to relieve madness when eaten.',
         note='0080—0081在84页，0081捕获85校回84；0082—0084在85页。彘耳及囂水缺字图按影印恢复，捕获标记另存。人目不是人面，四角与彘耳逐项核。檀柘之属为刚木郭注；鮨鱼犬首不改注中虎鹿猪首，音𭥍疑字依捕获保留。',
         en_note='Units 80–81 are on scan 84; 81 is corrected from captured 85. Units 82–84 are on 85. Pig and Xiao are restored from missing-image markers, with captured text retained. Human eyes are not a human face; other wood and fish comparisons remain commentary.'),
    dict(slug='hunxi',name='渾夕之山',en_name='Mount Hunxi',units=(85,88),
         description='北嶽向北百八十里为渾夕，无草木，多铜玉。囂水从此出，西北入海；与北嶽水文关联，不并涿光同名水。肥遺一首两身，国大旱为古述；郭注蟡、八尺与取鱼龟另列，不添西山六足四翼。',
         en_description='One hundred and eighty li north is Mount Hunxi, without vegetation and with copper and jade. The local Xiao rises here and flows northwest into the sea. Feiyi is a snake with one head and two bodies; its appearance is said to bring great drought.',
         note='0085—0088全核85页；0088正文为空但郭注亦此𩔗承87，随本段保留。囂字缺图恢复，一首两身不加西山足翼。郭注𬋩子、蟡、八尺、取鱼龟不作正文形貌或现代灾害预测。',
         en_note='Units 85–88 are on scan 85. Unit 88 has no main text but continues commentary. Xiao is restored; no Western legs or wings are added. Commentary names, length and fish-catching claims remain separate.'),
    dict(slug='beidan',name='北單之山',en_name='Mount Beidan',units=(89,89),
         description='渾夕向北五十里为北單，无草木而多葱韭。两种说法依原句同时保留，不改底本或以现代植被分类强解，不补未述生物或山景。',
         en_description='Fifty li north is Mount Beidan, without grasses or trees, with abundant cong and jiu.',
         note='0089全在85页，0090羆差另段仍待核。无草木与多葱韭并存，不擅改或漏录；北單不与單狐、單張混名。',
         en_note='Unit 89 is on scan 85; 90 begins the next pending passage. Both vegetation statements remain, without a modern reconciliation. Beidan differs from Danhu and Danzhang.'),
]
for r in ROWS[-5:]:
    r['en_quote'] = r['en_description']

ENTITIES += [
    E('shaoxian','material','qingbi-shaoxian','青碧（少咸）','Qingbi (Shaoxian)','多青碧','青碧仅列名，不定现代成分。','Qingbi is named without modern composition.','Much qingbi occurs here.'),
    E('shaoxian','beast','yayu-shaoxian','窫窳（少咸）','Yayu (Shaoxian)','有獸焉其状如牛而赤身人靣馬足名曰窫窳其音如嬰兒是食人','窫窳牛状赤身、人面马足，音如婴儿；食人为古述，不画伤害。郭注尔雅虎爪异说不改正文。','Yayu has a red cattle body, human face and horse feet, with an infant-like cry. The ancient eating account adds no harm scene or commentary tiger claws.','Yayu is cattle-shaped with a red body, human face and horse feet, cries like an infant and eats people.',commentary='爾雅云窫窳似𤠾虎爪與此錯；軋愈二音',en_commentary='Guo Pu records a differing Erya form with tiger claws and supplies pronunciation.'),
    E('shaoxian','water','dun-shaoxian','敦水（少咸）','Dun River (Shaoxian)','敦水出焉東流注于鴈門之水','敦水东注鴈門水，不混敦薨水。','The Dun flows east into Yanmen water, separately from the Dunhong.','The Dun rises here and flows east into Yanmen water.'),
    E('shaoxian','water','yanmen-shaoxian','鴈門之水','Yanmen water','東流注于鴈門之水','鴈門承接敦水，郭注山间水源不推现代位置。','Yanmen receives the Dun; commentary supplies no modern coordinate.','It flows east into Yanmen water.',commentary='水出鴈門山間',en_commentary='Guo Pu says the water emerges between the Yanmen mountains.'),
    E('shaoxian','place','yanmen-shaoxian','鴈門山（郭注）','Yanmen mountain (commentary)','鴈門之水','山名依郭注水出鴈門山间，不冒充正文新增山段。','The mountain comes from commentary, not an added main-text mountain.','Yanmen water is named here.',commentary='水出鴈門山間',en_commentary='Guo Pu locates the water between the Yanmen mountains.',water=True),
    E('shaoxian','beast','peipei-shaoxian','䰽䰽之魚','Peipei fish','其中多䰽䰽之魚食之殺人','䰽䰽仅列名，郭注未详或作鯆，留占位；食之杀人为古述。','Peipei is only named with an uncertain gloss and keeps a placeholder; the fatal-eating claim is ancient.','Peipei fish are abundant; eating them is said to kill people.',commentary='音沛未詳或作鯆',en_commentary='Guo Pu glosses pei, calls it uncertain and gives a variant.',unknown=True,water=True),
    E('yufa','water','huaize-yufa','瀤澤之水','Huaize River','瀤澤之水出焉而東北流注于㤗澤','瀤澤水东北注㤗澤，瀤音懐为郭注。','The Huaize flows northeast into Taize; pronunciation follows commentary.','The Huaize rises here and flows northeast into Taize.',commentary='音懐',en_commentary='Guo Pu glosses huai.'),
    E('yufa','water','taize','㤗澤（北山经）','Taize (Northern Mountains)','東北流注于㤗澤','㤗澤接瀤澤水，保留㤗字，不定现代湖泊。','Taize receives the Huaize; the edition character supplies no modern lake identity.','It flows northeast into Taize.'),
    E('yufa','beast','zao-yufa','䲃魚','Zao fish','其中多䲃魚其状如鯉而雞足食之已疣','䲃鱼鲤状鸡足，音藻来自郭注；配图两足为艺术解释，食用说为古述。','Zao is carp-shaped with chicken feet; two pictured feet are interpretive and the eating claim is ancient.','Zao fish are carp-shaped with chicken feet; eating them is said to relieve warts.',commentary='音藻',en_commentary='Guo Pu glosses zao.',water=True),
    E('yufa','beast','shanhui-yufa','山𤟤','Shanhui','有獸焉其状如犬而人靣善投見人則𥬇其名山𤟤其行如風見則天下大風','山𤟤犬状人面、善投、见人则𥬇，行如风；配图四犬足不增人手兵器，大风为古述；年长面相、灰发与笑纹是艺术解释，非经文所定年龄。','Shanhui is dog-shaped with a human face, skilled at throwing, smiles and moves like wind. The image adds no human hands or weapons; the omen is ancient. The elderly face, gray hair and laugh lines are artistic, not a textual age.','Shanhui is dog-shaped with a human face, skilled at throwing, smiles on seeing people and moves like wind; its appearance is said to bring great winds.',commentary='音暉；言疾',en_commentary='Guo Pu glosses hui and explains rapid motion.'),
    E('beiyue','plant','zhi-beiyue','枳（北嶽）','Zhi (Beiyue)','多枳𣗥剛木','枳仅列名，不补叶果。','Zhi is named without added leaf or fruit form.','Zhi, ji and gang wood are abundant.'),
    E('beiyue','plant','ji-beiyue','𣗥（北嶽）','Ji (Beiyue)','多枳𣗥剛木','𣗥依捕获字形，不借别山树图。','Ji retains the captured character without borrowed artwork.','Zhi, ji and gang wood are abundant.'),
    E('beiyue','plant','gang-beiyue','刚木（北嶽）','Gang wood (Beiyue)','多枳𣗥剛木','刚木檀柘之属为郭注，不增本山檀柘卡。','The tan-and-zhe comparison is commentary, not extra local plants.','Zhi, ji and gang wood are abundant.',commentary='檀柘之属',en_commentary='Guo Pu compares it to tan and zhe wood.'),
    E('beiyue','beast','zhuhuai-beiyue','諸懐','Zhuhuai','有獸焉其状如牛而四角人目彘耳其名曰諸懐其音如鳴鴈是食人','諸懐牛状四角、人目彘耳，音如鸣雁；人目不作人面，四角逐数，不画伤害。','Zhuhuai is cattle-shaped with four horns, human eyes and pig ears, sounding like a goose. Human eyes are not a human face; no harm scene is added.','Zhuhuai resembles cattle with four horns, human eyes and pig ears, sounds like a goose and eats people.'),
    E('beiyue','water','zhuhuai-beiyue','諸懐之水','Zhuhuai River','諸懐之水出焉而西流注于囂水','諸懐水西注囂水，囂缺图依85页恢复。','The Zhuhuai flows west into the local Xiao; the missing character is restored.','The Zhuhuai rises here and flows west into the Xiao.'),
    E('beiyue','water','xiao-beiyue-hunxi','囂水（北嶽—渾夕）','Xiao (Beiyue–Hunxi)','西流注于囂水','本地囂水接諸懐水，渾夕段记源头和西北入海；不并涿光同名水。','The local Xiao receives the Zhuhuai and has a Hunxi source and northwest-to-sea account, separate from Zhuoguang’s namesake.','It flows west into the local Xiao.'),
    E('beiyue','beast','yi-beiyue','鮨魚','Yi fish','其中多鮨魚魚身而犬首其音如嬰兒食之已狂','鮨鱼鱼身犬首、音如婴儿；郭注其他海鱼虎鹿猪头不作本鱼形貌，音𭥍疑字保留，食用说为古述。','Yi fish have fish bodies and dog heads with infant-like cries. Other sea-fish comparisons add no tiger, deer or pig head; the difficult gloss and eating claim remain separate.','Yi fish have fish bodies and dog heads with infant-like cries; eating them is said to relieve madness.',commentary='音𭥍；今海中有虎鹿魚及海狶体皆如魚而頭似虎鹿猪此其𩔗也',en_commentary='The captured pronunciation is retained; Guo Pu compares other sea fish with animal-like heads.',water=True),
    E('hunxi','material','copper-hunxi','铜（渾夕）','Copper (Hunxi)','多銅玉','铜与玉分录出处。','Copper is recorded separately from jade.','Copper and jade are abundant.'),
    E('hunxi','material','jade-hunxi','玉（渾夕）','Jade (Hunxi)','多銅玉','玉只列名，不补成分颜色。','Jade is named without composition or color.','Copper and jade are abundant.'),
    E('hunxi','water','sea-hunxi','海（渾夕水文）','Sea (Hunxi water account)','西北流注于海','海为本地囂水所注，不定现代边界。','The sea receives the local Xiao without a modern boundary.','It flows northwest into the sea.'),
    E('hunxi','beast','feiyi-hunxi','肥遺（渾夕蛇）','Feiyi (Hunxi snake)','有蛇一首兩身名曰肥遺見則其國大旱','肥遺一首两身，旱灾为古述；不与西山六足四翼蛇或英山鸟混形，郭注蟡等另存。','Feiyi has one head and two bodies with an ancient drought account. It gains no Western legs or wings, and stays separate from the Ying bird.','Feiyi is a snake with one head and two bodies; its appearance is said to bring great drought.',commentary='𬋩子曰涸水之精名曰蟡一頭而两身其状如蛇長八尺以其名呼之可使取魚龜亦此𩔗',en_commentary='The captured commentary gives a spirit name, one head and two bodies, a length and a fish-catching claim.'),
    E('beidan','plant','cong-beidan','葱（北單）','Cong (Beidan)','無草木多葱韭','无草木与多葱韭同存，此卡录葱。','Both vegetation statements remain; this card records cong.','No grasses or trees are recorded, together with abundant cong and jiu.'),
    E('beidan','plant','jiu-beidan','韭（北單）','Jiu (Beidan)','無草木多葱韭','韭单存，不因无草木漏录。','Jiu retains its record despite the no-vegetation statement.','No grasses or trees are recorded, together with abundant cong and jiu.'),
]


from beishan_range_transition import ROWS as TRANSITION_ROWS, entities as transition_entities
ROWS += TRANSITION_ROWS
ENTITIES += transition_entities(E)
from beishan_later_ranges import ROWS as LATER_ROWS, entities as later_entities
ROWS += LATER_ROWS
ENTITIES += later_entities(E)
from beishan_jingwei_range import ROWS as JINGWEI_ROWS, entities as jingwei_entities
ROWS += JINGWEI_ROWS
ENTITIES += jingwei_entities(E)
from beishan_dunyu_range import ROWS as DUNYU_ROWS, entities as dunyu_entities
ROWS += DUNYU_ROWS
ENTITIES += dunyu_entities(E)
from beishan_taixi_range import ROWS as TAIXI_ROWS, entities as taixi_entities, REMAINING
ROWS += TAIXI_ROWS
ENTITIES += taixi_entities(E)


def extend(world, english, chapter, review):
    folder = ROOT / 'frontend/artwork-source/beishan'
    jobs = {a['entry_id']:a for a in json.loads((folder/'entities-generation.json').read_text(encoding='utf-8'))['assets']}
    lines = chapter['lines']
    source, en_source = world['passages'][-1]['source'], english['passage-beishan-qiuru']['source']
    batches = {'beishan-'+r['slug'] for r in ROWS}
    core = next(c.copy() for c in world['beasts'] if c['id']=='beast-zhu-jian')
    core['legacy_quote'] = core.get('legacy_quote', core['quote'])
    core['aliases'] = list(dict.fromkeys([*core.get('aliases', []), '诸犍']))
    jingwei=next(c.copy() for c in world['beasts'] if c['id']=='beast-jingwei')
    fajiu=next(c.copy() for c in world['places'] if c['id']=='place-fajiu')
    for c in (jingwei,fajiu):
        c['legacy_quote']=c.get('legacy_quote',c['quote']);c['legacy_url']=c.get('legacy_url',c['url'])
    fajiu['aliases']=list(dict.fromkeys([*fajiu.get('aliases',[]),'发鸠之山','发鸠山','發鳩之山']))
    for group in ['passages','text_entities','natural_features','beasts','places']:
        world[group] = [r for r in world[group] if r.get('content_batch') not in batches and r['id'] not in {'beast-zhu-jian','beast-jingwei','place-fajiu'}]
    passages, cards = [], []
    for order,row in enumerate(ROWS,3):
        slug=row['slug']; first,last=row['units']; pid='passage-beishan-'+slug; place=row.get('place_id',('rite-' if row.get('entry_kind')=='rite' else 'place-')+'beishan-'+slug)
        refs=[(f'source-03-{i+1:04}',lines[i]) for i in range(first-1,last)]
        pages=sorted({PAGE_CORRECTIONS.get(id,int(l['page'].rsplit('/',1)[1])) for id,l in refs})
        urls=[f'https://zh.wikisource.org/wiki/Page:Sibu_Congkan0465-郭璞-山海經-2-1.djvu/{n}' for n in pages]
        captured=''.join(l['text'] for _,l in refs)
        raw=''.join(restored(id,l['text']) for id,l in refs)
        common=dict(source=source,source_chapter='《北山经》',source_book=3,region='北山经',source_locator='卷第三 · 影印页 '+'、'.join(map(str,pages)),source_pages=urls,url=urls[0],source_unit_ids=[id for id,_ in refs],reveal_chapter='03',content_batch='beishan-'+slug,review_status='facsimile_reviewed',artwork_pending=True,direction='按北山经篇内次序与方位阅读，不换算现代坐标或实测里程。',editorial_note='经文、捕获快照和郭注分存；白话及英文为项目整理。食用、治病与灾异为古籍记述。')
        translation=dict(source=en_source,source_chapter='Beishan Jing',region='Beishan Jing',source_locator='Volume 3 · scan pages '+', '.join(map(str,pages)),direction='Read the Northern textual sequence and directions; these are not modern coordinates or measured distances.',editorial_note='Text, captured transcription and commentary are separate; explanations and English are editorial. Eating, healing and omen claims are ancient accounts.')
        commentary='\n'.join(f'〔影印页{PAGE_CORRECTIONS.get(id,int(l["page"].rsplit("/",1)[1]))}〕'+'；'.join(l['annotations']) for id,l in refs if l['annotations'])
        p={**common,'id':pid,'kind':'passage','name':row['name'],'range':row.get('range',1),'order':order,'description':row['description'],'quote':raw,'captured_text':captured,'commentary_quote':commentary,'content_note':row['note'],'captured_commentary':[{'source_unit_id':id,'annotations':l['annotations']} for id,l in refs],'source_span':[sum(len(l['text']) for l in lines[:first-1]),sum(len(l['text']) for l in lines[:last])],'related_entry_ids':[place],'subjects':[row['name']]}
        english[pid]={**translation,'name':row['en_name'],'description':row['en_description'],'quote':row['en_quote'],'content_note':row['en_note']}
        c={**(fajiu if place=='place-fajiu' else {}),**common,'id':place,'kind':row.get('entry_kind','place'),'name':row['name'],'description':row['description'],'quote':raw,'commentary_quote':commentary,'content_note':row['note'],'source_passage_ids':[pid],'related_entry_ids':[pid]}
        english[place]=dict(english[pid]); cards.append(c)
        context_card=c
        for e in [e for e in ENTITIES if e['slug']==slug]:
            assert e['quote'] in raw,e['id']
            c={**(core if e['id']=='beast-zhu-jian' else jingwei if e['id']=='beast-jingwei' else {}),**common,**{k:e[k] for k in ['id','kind','name','description','quote']},'commentary_quote':e.get('commentary',''),'context_place_id':place,'source_passage_ids':[pid],'related_entry_ids':[pid]}
            english[e['id']]={**translation,'name':e['en_name'],'description':e['en_description'],'quote':e['en_quote'],'commentary_quote':e.get('en_commentary','')}
            if e.get('context'):c['context_place_id']=e['context']
            if e.get('aliases'):c['aliases']=e['aliases']
            if e['kind']=='water' or e.get('water'):c['relation_scope']='water'
            a=jobs.get(e['id'])
            if a and a['status']=='reviewed':
                c.update(artwork='beishan/'+a['name']+'-v1.webp',artwork_pending=False,artwork_caption='原文形貌与木刻演绎 · 刻纹、配色和姿态为艺术解释；郭注形貌另有说明。')
                english[e['id']]['artwork_caption']='Textual form in woodcut interpretation; carving, colors and pose are artistic, with commentary-based form identified separately.'
            elif e['id'] in {'beast-zhu-jian','beast-jingwei'}:
                c.update(artwork_pending=False,artwork_caption='旧图复核：独目、人首牛耳、豹身长尾；盘尾为居态演绎。')
                english[e['id']]['artwork_caption']='Existing artwork reviewed: one eye, human head, ox ears, leopard body and long tail; the coiled tail interprets resting posture.'
                if e['id']=='beast-jingwei':
                    c['artwork_caption']='旧图复核：乌状、文首、白喙赤足，单衔石代表取材叙事；旋纹、配色与飞姿为解释。'
                    english[e['id']]['artwork_caption']='Existing image reviewed: crow form, patterned head, white beak and red feet; one carried stone is representative. Carved curls, colors and flight pose are artistic.'
            elif e['kind'] in {'beast','deity'}:
                c.update(appearance_unknown=True,artwork_caption='形貌未详或依据不足 · 统一问号占位不代表本生物形态。')
                english[e['id']]['artwork_caption']='Appearance unspecified or evidence insufficient; the shared question-mark placeholder is not a depiction.'
            if row.get('entry_kind')=='rite':
                c.pop('context_place_id',None)
                c['related_entry_ids'].append(place)
                context_card['related_entry_ids'].append(c['id'])
            cards.append(c);p['related_entry_ids'].append(c['id']);p['subjects'].append(c['name'])
        passages.append(p)
    byid={c['id']:c for c in cards}
    contexts=[p for p in passages if p['id'] in {'passage-beishan-'+s for s in ['qiaoming','zhuoguang','guoshan','guowei','shizhe','dunhong','guancen']}]
    he={**{k:v for k,v in contexts[0].items() if k not in ['id','kind','name','range','order','description','quote','captured_text','captured_commentary','commentary_quote','content_note','source_span','subjects']},'id':'water-beishan-he','kind':'water','name':'河（北山经）','description':'河分别承接譙水、囂水、伊水、魚水和泚水的西流。五段汇流与敦薨段崑崙东北隅实惟河源的古述分别保存，次二首山另记汾水西注河；不据同名与西山河合并或认定现代汇流点。','quote':'；'.join(['譙水出焉西流注于河','囂水出焉而西流注于河','伊水出焉西流注于河','魚水出焉而西流注于河','泚水出焉而西流注于河','出于崑崙之東北隅實惟河源','汾水出焉而西流注于河']),'commentary_quote':'','source_passage_ids':[p['id'] for p in contexts],'context_place_id':'place-beishan-qiaoming','context_place_ids':['place-beishan-zhuoguang','place-beishan-guoshan','place-beishan-guowei','place-beishan-shizhe','place-beishan-dunhong','place-beishan-guancen'],'source_unit_ids':list(dict.fromkeys(id for p in contexts for id in p['source_unit_ids'])),'source_pages':list(dict.fromkeys(u for p in contexts for u in p['source_pages'])),'source_locator':'卷第三 · 影印页 77、78、79、80、83、87','relation_scope':'water','related_entry_ids':[p['id'] for p in contexts],'content_note':'分号分开五段汇流摘句与敦薨河源古述，另列次二管涔汾水摘句，不是连续经文或现代河道。'}
    english[he['id']]={**english['water-beishan-qiao-qiaoming'],'name':'He (Northern Mountains)','description':'The He separately receives the west-flowing Qiao, Xiao, Yi, Yu and Ci in five passages. Dunhong separately records an ancient source claim at Kunlun’s northeastern corner. These accounts remain separate, without a merger with the Western He or modern confluences. Range two separately adds the west-flowing Fen.','quote':'The Qiao flows west into the He; separately, the Xiao flows west into the He; the Yi flows west into the He; the Yu flows west into the He; and the Ci flows west into the He; separately, the Dunhong passage describes Kunlun’s northeastern corner as a source of the He; separately, the Fen rises at Guancen and flows west into the He.','source_locator':'Volume 3 · scan pages 77, 78, 79, 80, 83, 87','content_note':'Semicolons separate five confluence excerpts and the Dunhong source account, not a continuous quotation or modern river course. The Fen separately rises at Guancen and flows west into the He.'}
    cards.append(he);byid[he['id']]=he
    for p in contexts:p['related_entry_ids'].append(he['id'])
    links=[('water-beishan-peng-daishan','water-beishan-pihu-daishan'),('water-beishan-peng-daishan','beast-beishan-youyu-daishan'),('water-beishan-qiao-qiaoming','beast-beishan-heluo-qiaoming'),('water-beishan-xiao-zhuoguang','beast-beishan-xixi-zhuoguang'),('water-beishan-yu-guowei','material-beishan-wenbei-guowei')]
    links += [(id,'water-beishan-he') for id in ['water-beishan-qiao-qiaoming','water-beishan-xiao-zhuoguang','water-beishan-yi-guoshan','water-beishan-yu-guowei','water-beishan-ci-shizhe']]
    links += [('water-beishan-xun-danxun','water-beishan-tang-danxun'),('water-beishan-gang','water-beishan-youze'),('water-beishan-li-danzhang','water-beishan-gang')]
    gang=byid['water-beishan-gang']; last=next(p for p in passages if p['id']=='passage-beishan-danzhang')
    gang['source_passage_ids'].append(last['id']); gang['context_place_ids']=['place-beishan-danzhang']
    gang['source_unit_ids'] = [*gang['source_unit_ids'], *last['source_unit_ids']]
    gang['source_pages'] = list(dict.fromkeys([*gang['source_pages'], *last['source_pages']]))
    gang['source_locator']='卷第三 · 影印页 80、81'
    gang['quote'] += '；櫟水出焉而南流注于杠水'
    gang['content_note']='分号分开邊春与單張摘句，不是连续经文。'
    last['related_entry_ids'].append(gang['id'])
    english[gang['id']].update(quote='The Gang rises here and flows west into Youze; separately, the Li rises at Danzhang and flows south into the Gang.',source_locator='Volume 3 · scan pages 80, 81',content_note='Semicolons separate Bianchun and Danzhang excerpts, not a continuous quotation.')
    links += [('water-beishan-jianghan-guanti','water-beishan-youze'),('water-beishan-bian-panhou','water-beishan-lize-panhou'),('water-beishan-dunhong','water-beishan-youze'),('water-beishan-dunhong','water-beishan-he'),('water-beishan-dunhong','place-beishan-kunlun-dunhong'),('water-beishan-dunhong','beast-beishan-chigui-dunhong')]
    youze=byid['water-beishan-youze']
    extra=[p for p in passages if p['id'] in {'passage-beishan-guanti','passage-beishan-dunhong'}]
    youze['source_passage_ids'] += [p['id'] for p in extra]
    youze['context_place_ids']=['place-beishan-guanti','place-beishan-dunhong']
    youze['source_unit_ids'] = [*youze['source_unit_ids'], *[id for p in extra for id in p['source_unit_ids']]]
    youze['source_pages']=list(dict.fromkeys(youze['source_pages']+[u for p in extra for u in p['source_pages']]))
    youze.update(source_locator='卷第三 · 影印页 80、81、82、83',quote='西流注于泑澤；匠韓之水出焉而西流注于泑澤；敦薨之水出焉而西流注于泑澤',description='北山泑澤分别承接邊春杠水、灌題匠韓水、敦薨水的西流，三段出处各存；不与單狐泑水或西山泑澤合并。',content_note='分号分开三段摘句，不是连续经文或现代水域定位。')
    youze['related_entry_ids'] += [p['id'] for p in extra]
    for p in extra:p['related_entry_ids'].append(youze['id'])
    english[youze['id']].update(source_locator='Volume 3 · scan pages 80, 81, 82, 83',quote='It flows west into Youze; separately, the Jianghan rises here and flows west into Youze; the Dunhong rises here and flows west into Youze.',description='Northern Youze separately receives the west-flowing Gang, Jianghan and Dunhong. Their three contexts remain distinct from Danhu’s You River and Western Youze.',content_note='Semicolons separate three excerpts, not a continuous quotation or modern waterbody location.')
    links += [('water-beishan-dun-shaoxian','water-beishan-yanmen-shaoxian'),('water-beishan-yanmen-shaoxian','place-beishan-yanmen-shaoxian'),('water-beishan-dun-shaoxian','beast-beishan-peipei-shaoxian'),('water-beishan-huaize-yufa','water-beishan-taize'),('water-beishan-huaize-yufa','beast-beishan-zao-yufa'),('water-beishan-zhuhuai-beiyue','water-beishan-xiao-beiyue-hunxi'),('water-beishan-zhuhuai-beiyue','beast-beishan-yi-beiyue'),('water-beishan-xiao-beiyue-hunxi','water-beishan-sea-hunxi')]
    xiao=byid['water-beishan-xiao-beiyue-hunxi']; hp=next(p for p in passages if p['id']=='passage-beishan-hunxi')
    xiao['source_passage_ids']=[*xiao['source_passage_ids'],hp['id']];xiao['context_place_ids']=['place-beishan-hunxi']
    xiao['source_unit_ids']=[*xiao['source_unit_ids'],*hp['source_unit_ids']]
    xiao['source_pages']=list(dict.fromkeys([*xiao['source_pages'],*hp['source_pages']]))
    xiao.update(source_locator='卷第三 · 影印页 84、85',quote='西流注于囂水；囂水出焉而西北流注于海',content_note='分号分开北嶽与渾夕摘句；两处囂字缺图按85页恢复，不与涿光囂水合并。')
    hp['related_entry_ids'].append(xiao['id']);xiao['related_entry_ids'].append(hp['id'])
    english[xiao['id']].update(source_locator='Volume 3 · scan pages 84, 85',quote='It flows west into the Xiao; separately, the Xiao rises here and flows northwest into the sea.',content_note='Semicolons separate Beiyue and Hunxi excerpts; restored Xiao characters do not merge the Zhuoguang namesake.')
    taize=byid['water-beishan-taize']; dp=next(p for p in passages if p['id']=='passage-beishan-dishan')
    taize['source_passage_ids']=[*taize['source_passage_ids'],dp['id']]
    taize['context_place_ids']=['place-beishan-dishan']
    taize['source_unit_ids']=[*taize['source_unit_ids'],*dp['source_unit_ids']]
    taize['source_pages']=list(dict.fromkeys([*taize['source_pages'],*dp['source_pages']]))
    taize.update(source_locator='卷第三 · 影印页 84、86',quote='東北流注于㤗澤；隄水出焉而東流注于㤗澤',description='北山㤗澤分别承接瀤澤水东北流与隄水东流；出处分开，不定现代湖泊。',content_note='分号分开獄法、隄山摘句，不是连续经文。')
    english[taize['id']].update(source_locator='Volume 3 · scan pages 84, 86',quote='It flows northeast into Taize; separately, the Di rises here and flows east into Taize.',description='Northern Taize receives the northeast-flowing Huaize and east-flowing Di in distinct passages, without a modern lake identification.',content_note='Semicolons separate Yufa and Di excerpts, not a continuous quotation.')
    dp['related_entry_ids'].append(taize['id']);taize['related_entry_ids'].append(dp['id'])
    links += [('water-beishan-xian-beixian','water-beishan-tuwu-beixian'),('water-beishan-di-dishan','water-beishan-taize'),('water-beishan-di-dishan','beast-beishan-longgui-dishan'),('water-beishan-fen-guancen','water-beishan-he')]
    fen=byid['water-beishan-fen-guancen']
    fp=[p for p in passages if p['id'] in {'passage-beishan-'+s for s in ['shaoyang','xianyong','huqi']}]
    fen['source_passage_ids']=[*fen['source_passage_ids'],*[p['id'] for p in fp]]
    fen['context_place_ids']=['place-beishan-'+s for s in ['shaoyang','xianyong','huqi']]
    fen['source_unit_ids']=[*fen['source_unit_ids'],*[u for p in fp for u in p['source_unit_ids']]]
    fen['source_pages']=list(dict.fromkeys([*fen['source_pages'],*[u for p in fp for u in p['source_pages']]]))
    fen['related_entry_ids']=[*fen['related_entry_ids'],*[p['id'] for p in fp]]
    fen.update(source_locator='卷第三 · 影印页 87、88',quote='汾水出焉而西流注于河；酸水出焉而東流注于汾水；晉水出焉而東南流注于汾水；勝水出焉而東北流注于汾水',description='汾水出管涔西注河；少陽酸水东注汾、縣雍晉水东南注汾、狐岐勝水东北注汾，四段分别保存，不换算现代河道。',content_note='分号分开管涔、少陽、縣雍、狐岐摘句，不是连续经文。')
    english[fen['id']].update(source_locator='Volume 3 · scan pages 87, 88',quote='The Fen rises here and flows west into the He; separately, the Suan flows east into the Fen; the Jin flows southeast into the Fen; the Sheng flows northeast into the Fen.',description='The Fen rises at Guancen and flows west into the He. Separate passages record the east-flowing Suan, southeast-flowing Jin and northeast-flowing Sheng entering it, without a modern river course.',content_note='Semicolons separate Guancen, Shaoyang, Xianyong and Huqi excerpts, not a continuous quotation.')
    for p in fp:p['related_entry_ids'].append(fen['id'])
    links += [('water-beishan-suan-shaoyang','water-beishan-fen-guancen'),('water-beishan-suan-shaoyang','material-beishan-ochre-shaoyang'),('water-beishan-jin-xianyong','water-beishan-fen-guancen'),('water-beishan-jin-xianyong','beast-beishan-ci-xianyong'),('water-beishan-sheng-huqi','water-beishan-fen-guancen'),('water-beishan-sheng-huqi','material-beishan-dark-jade-huqi')]
    mao=byid['water-beishan-mao']; mp=next(p for p in passages if p['id']=='passage-beishan-duntou')
    mao['source_passage_ids']=[*mao['source_passage_ids'],mp['id']]
    mao['context_place_ids']=['place-beishan-duntou']
    mao['source_unit_ids']=[*mao['source_unit_ids'],*mp['source_unit_ids']]
    mao['source_pages']=list(dict.fromkeys([*mao['source_pages'],*mp['source_pages']]))
    mao['related_entry_ids']=[*mao['related_entry_ids'],mp['id']]
    mao.update(quote='東流注于旄水；旄水出焉而東流注于印澤',description='旄水先在諸餘段作为东流所注，敦頭另记源头与向东注印澤；两段分别保存，不推现代河道。',content_note='分号分开諸餘与敦頭摘句，不是连续经文。')
    english[mao['id']].update(quote='It flows east into the Mao; separately, the Mao rises here and flows east into Yinze.',description='The Mao receives Zhuyu’s east-flowing river; Duntou separately records its source and eastern outlet into Yinze, without a modern river course.',content_note='Semicolons separate Zhuyu and Duntou excerpts, not a continuous quotation.')
    mp['related_entry_ids'].append(mao['id'])
    links += [('water-beishan-kuang','water-beishan-fu-kuang'),('water-beishan-kuang','material-beishan-fine-jade-kuang'),('water-beishan-zhuyu','water-beishan-mao'),('water-beishan-mao','water-beishan-yinze-duntou'),('water-beishan-mao','beast-beishan-boma-duntou'),('water-beishan-cen-beixiao','water-beishan-qiongze-beixiao')]
    for c in cards:
        ctx=c.get('context_place_id')
        if ctx in {'place-beishan-guishan','place-beishan-fawan','place-beishan-danlin-forest-yeli','place-beishan-western-mountains-fajiu'}:
            if ctx not in c['related_entry_ids']:c['related_entry_ids'].append(ctx)
            if c['id'] not in byid[ctx]['related_entry_ids']:byid[ctx]['related_entry_ids'].append(c['id'])
    links += [('water-beishan-xiu-liangqu','water-beishan-yanmen-liangqu'),('water-beishan-huguan','water-beishan-sea-huguan'),('water-beishan-huguan','beast-beishan-shan-huguan'),('water-beishan-juejue-longhou','water-beishan-he'),('water-beishan-juejue-longhou','beast-beishan-renyu-longhou'),('water-beishan-tiaojian-xianshan','water-beishan-changze-xianshan'),('water-beishan-tiaojian-xianshan','material-beishan-qisuan-xianshan'),('water-beishan-sheng-tianchi','material-beishan-yellow-e-tianchi'),('water-beishan-liu-yangshan','water-beishan-he'),('water-beishan-liu-yangshan','beast-beishan-xianfu-yangshan'),('water-beishan-lian-wangwu','water-beishan-taize'),('water-beishan-jiao-jiaoshan','water-beishan-he')]
    extra_he=[p for p in passages if p['id'] in {'passage-beishan-'+x for x in ['longhou','yangshan','jiaoshan','jingshan-east','chongwei']}]
    he['source_passage_ids']=[*he['source_passage_ids'],*[p['id'] for p in extra_he]]
    he['context_place_ids']=[*he['context_place_ids'],*['place-beishan-'+x for x in ['longhou','yangshan','jiaoshan','jingshan-east','chongwei']]]
    he['source_unit_ids']=[*he['source_unit_ids'],*[u for p in extra_he for u in p['source_unit_ids']]]
    he['source_pages']=list(dict.fromkeys([*he['source_pages'],*[u for p in extra_he for u in p['source_pages']]]))
    he['source_locator']='卷第三 · 影印页 77、78、79、80、83、87、93、94、95、96、97、98'
    he['quote']+='；决决之水出焉而東流注于河；留水出焉而南流注于河；教水出焉西流注于河；髙水出焉南流注于河；丹水出焉南流注于河'
    he['description']+='次三另记决决水东注、留水南注、教水西注，各段方向分存，京山髙水及虫尾丹水另记南注。'
    he['related_entry_ids']=[*he['related_entry_ids'],*[p['id'] for p in extra_he]]
    for p in extra_he:p['related_entry_ids'].append(he['id'])
    english[he['id']].update(source_locator='Volume 3 · scan pages 77, 78, 79, 80, 83, 87, 93, 94, 95, 96, 97, 98',quote=english[he['id']]['quote']+' Separately, the Juejue flows east into the He; the Liu flows south into the He; the Jiao flows west into the He; the Gao and Dan separately flow south into the He.',description=english[he['id']]['description']+' Three third-range passages separately add the east-flowing Juejue, south-flowing Liu and west-flowing Jiao, followed by south-flowing Gao and Dan.')
    he['content_note']='分号分开各段汇流摘句与敦薨河源古述；次三决决东注、留水南注、教水西注、髙水与丹水南注分别保存，不是连续经文或现代河道。'
    english[he['id']]['content_note']='Semicolons separate confluence excerpts and the Dunhong source account. Third-range Juejue flows east, Liu south, Jiao west, and Gao and Dan south; these are distinct ancient accounts, not a continuous quotation or modern river course.'
    wp=next(p for p in passages if p['id']=='passage-beishan-wangwu')
    taize['source_passage_ids']=[*taize['source_passage_ids'],wp['id']];taize['context_place_ids']=[*taize['context_place_ids'],'place-beishan-wangwu']
    taize['source_unit_ids']=[*taize['source_unit_ids'],*wp['source_unit_ids']]
    taize['source_pages']=list(dict.fromkeys([*taize['source_pages'],*wp['source_pages']]))
    taize.update(source_locator='卷第三 · 影印页 84、86、95、96',quote=taize['quote']+'；㶌水出焉而西北流注于㤗澤',description=taize['description']+'王屋另记㶌水西北注此，郭注疑音近不改现代定位。',content_note='分号分开獄法、隄山、王屋摘句，不是连续经文。')
    taize['related_entry_ids']=[*taize['related_entry_ids'],wp['id']];wp['related_entry_ids'].append(taize['id'])
    english[taize['id']].update(source_locator='Volume 3 · scan pages 84, 86, 95, 96',quote=english[taize['id']]['quote']+' Separately, the Lian rises here and flows northwest into Taize.',description=english[taize['id']]['description']+' Wangwu separately adds the northwest-flowing Lian, without a modern location.',content_note='Semicolons separate Yufa, Di and Wangwu excerpts, not a continuous quotation.')
    links += [('water-beishan-gao-jingshan-east','water-beishan-he'),('water-beishan-dan-chongwei','water-beishan-he'),('water-beishan-bo-chongwei','water-beishan-huangze-chongwei')]
    def share(id, slug, quote, en_quote, en_context):
        c=byid[id];p=next(p for p in passages if p['id']=='passage-beishan-'+slug)
        ctx=p['related_entry_ids'][0]
        c['source_passage_ids']=[*c['source_passage_ids'],p['id']]
        c['context_place_ids']=[*c.get('context_place_ids',[]),ctx]
        c['source_unit_ids']=list(dict.fromkeys([*c['source_unit_ids'],*p['source_unit_ids']]))
        c['source_pages']=list(dict.fromkeys([*c['source_pages'],*p['source_pages']]))
        pages=sorted({int(u.rsplit('/',1)[1]) for u in c['source_pages']})
        c['source_locator']='卷第三 · 影印页 '+'、'.join(map(str,pages))
        c['quote']+='；'+quote;c['related_entry_ids']=[*c['related_entry_ids'],p['id']]
        p['related_entry_ids'].append(id)
        english[id]['quote']+=' Separately, '+en_quote
        english[id]['description']+=' '+en_context
        english[id]['source_locator']='Volume 3 · scan pages '+', '.join(map(str,pages))
    for slug,q,eq in [
      ('pengpi','蚤林之水出焉東南流注于河','the Zaolin flows southeast into the He.'),
      ('yeli','沁水出焉南流注于河','the Qin flows south into the He.'),
      ('juru','濝水出焉南流注于河','the Qi flows south into the He.'),
      ('fajiu','漳水出焉東流注于河','the Zhang flows east into the He.')]:
        share(he['id'],slug,q,eq,'This passage adds a separately sourced confluence.')
    he['quote']+='；丹林之水出焉南流注于河'
    he['description']+='彭毗蚤林东南注、謁戾沁水和丹林水南注、沮洳濝水南注、發鳩漳水东注另记。'
    english[he['id']]['quote']+=' Separately, the Danlin flows south into the He.'
    he['content_note']='分号分开各段河源及汇流摘句；同一謁戾段的沁、丹林两水方向分别保存，不是连续经文或现代河道。'
    english[he['id']]['content_note']='Semicolons separate source and confluence excerpts. Qin and Danlin are separately recorded in the same Yeli passage, not a continuous quotation or modern course.'
    hz=byid['water-beishan-huangze-chongwei']
    share(hz['id'],'xiaohou','明漳之水出焉南流注于黄澤','the Mingzhang flows south into Huangze.','Xiaohou separately adds the south-flowing Mingzhang.')
    hz.update(name='黄澤（虫尾、小侯）',description='虫尾薄水东南注黄泽，小侯明漳水南注此；两段方向分存，不据同名定现代岸线。')
    english[hz['id']].update(name='Huangze (Chongwei and Xiaohou)',description='The southeast-flowing Bo and south-flowing Mingzhang separately enter Huangze in two passages, without a modern shoreline.')
    share('water-beishan-fu-shenqun','xishan-north','牛首之水出焉而東流注于滏水','the Niushou rises at Xi and flows east into the Fu.','Xi adds the east-flowing Niushou.')
    share('water-beishan-zhang-fajiu','shaoshan','清漳之水出焉東流于濁漳之水','the Qingzhang rises at Shao and flows east into the Zhuozhang.','Shao separately supplies the explicit Zhuozhang recipient wording.')
    links += [('water-beishan-zaolin-pengpi',he['id']),('water-beishan-fei-pengpi','water-beishan-chuang-pengpi'),('water-beishan-fei-pengpi','beast-beishan-feiyi-pengpi'),
      ('water-beishan-mingzhang-xiaohou',hz['id']),('water-beishan-gong-taitou','water-beishan-huchi-taitou'),
      ('water-beishan-qin-yeli',he['id']),('water-beishan-danlin-yeli',he['id']),('water-beishan-yinghou-yeli','water-beishan-fan-yeli'),
      ('water-beishan-qi-juru',he['id']),('water-beishan-huang-shenqun','water-beishan-huan-shenqun'),('water-beishan-fu-shenqun','water-beishan-ou-shenqun'),
      ('water-beishan-zhang-fajiu',he['id']),('water-beishan-qingzhang-shaoshan','water-beishan-zhang-fajiu'),('water-beishan-niushou-xishan-north','water-beishan-fu-shenqun'),
      ('beast-jingwei','water-beishan-donghai-fajiu'),('beast-jingwei','place-beishan-western-mountains-fajiu'),('beast-jingwei','material-beishan-wood-fajiu'),('beast-jingwei','material-beishan-stones-fajiu')]
    share(he['id'],'xiushan','洧水出焉而東流注于河','the Wei rises at Xiu and flows east into the He.','Xiu separately adds the east-flowing Wei.')
    share(he['id'],'songshan','陽水出焉東北流注于河','the Yang rises at Song and flows northeast into the He.','Song separately adds the northeast-flowing Yang.')
    he['description']+='繡山洧水东注、松山陽水东北注另记，方向不互换。'
    links += [('water-beishan-jing-after-xi','water-beishan-haize-jingshan-after-xi'),('water-beishan-wei-xiushan',he['id']),('water-beishan-wei-xiushan','beast-beishan-huomin-xiushan'),('water-beishan-yang-songshan',he['id']),('water-beishan-suo-dunyu','water-beishan-tailu-dunyu'),('water-beishan-zhi-dunyu','water-beishan-peng-dunyu'),('water-beishan-huai-dunyu','water-beishan-zhize-dunyu')]
    wei=byid['water-beishan-wei-xiushan'];qin=byid['water-beishan-qin-yeli'];hutuo=byid['water-beishan-huchi-taitou']
    for c in (wei,qin,hutuo):
        c['aliases']=list(dict.fromkeys([*c.get('aliases',[]),c['name'],english[c['id']]['name']]))
    share(wei['id'],'zheshan','歷聚之水出焉而北流注于洧水','the Liju rises at Zhe and flows north into Wei water.','Zhe separately names Wei as the recipient of the north-flowing Liju.')
    wei.update(name='洧水（繡山、柘山文本索引）',description='繡山洧水出而东注河，柘山歷聚水北注洧；作为同篇文本水名索引保存两段，不将索引复用当作现代地理同一性定论。',content_note='同篇水名索引，源出与受水的摘句和上下文分开；不据同名补现代河道。')
    english[wei['id']].update(name='Wei water (Xiu and Zhe textual index)',description='Xiu gives the Wei source and eastward flow into the He; Zhe names Wei as the recipient of north-flowing Liju. One textual name index does not establish modern geographic identity.',content_note='Source and recipient excerpts retain independent contexts; the name index adds no modern river course.')
    share(qin['id'],'taixi','液女之水出于其陽南流注于沁水','the Yenu rises on Taixi’s sunny side and flows south into Qin water.','Taixi separately names Qin as the recipient of south-flowing Yenu, without a modern identity claim.')
    qin.update(name='沁水（謁戾、泰戱文本索引）',description=qin['description']+'泰戱液女水南注沁另记；同篇水名索引不代表现代地理同一性已定。')
    english[qin['id']]['name']='Qin water (Yeli and Taixi textual index)'
    for slug,q,eq in [('baima','木馬之水出焉而東北流注于虖沱','the Muma rises at Baima and flows northeast into Hutuo.'),('kongsang-north','空桑之水出焉東流注于虖沱','Kongsang water rises here and flows east into Hutuo.'),('taixi','虖沱之水出焉而東流注于漊水','Hutuo rises at Taixi and flows east into Lou water.')]:
        share(hutuo['id'],slug,q,eq,'This passage retains its Hutuo wording separately.')
    hutuo.update(name='虖池／虖沱（北山经文本索引）',description='泰頭正文作虖池，白馬、空桑、泰戱作虖沱；郭注呼佗二音下同。共水南注、木馬东北注、空桑东注及泰戱源出东注漊分别保存，不推现代水系。',commentary_quote='呼佗二音下同；今虖沱水出鴈門鹵成縣南武夫山',content_note='原文两种写法逐段保留；郭注同音与下同支持同篇文本名目管理，不据此替换原字或认定现代河道。',aliases=[*hutuo['aliases'],'虖池','虖沱'])
    english[hutuo['id']].update(name='Huchi / Hutuo (Northern textual index)',description='Taitou writes Huchi, while Baima, Kongsang and Taixi write Hutuo. Guo Pu gives hu-tuo pronunciation and says it also applies below. Four separately sourced flow accounts share one textual name index, without a modern course.',commentary_quote='Guo Pu gives the shared hu-tuo pronunciation at Taitou and an ancient Hutuo source account at Taixi.',content_note='Both textual spellings and all passage contexts remain separate. The pronunciation gloss supports a textual index, not replacement spelling or a modern river identification.')
    links += [('water-beishan-liju-zheshan',wei['id']),('water-beishan-fei-weilong','water-beishan-gaoze-weilong'),('water-beishan-fei-weilong','material-beishan-leishi-weilong'),('water-beishan-changtie-weilong','water-beishan-daze-weilong'),('water-beishan-muma-baima',hutuo['id']),('water-beishan-kongsang-north',hutuo['id']),(hutuo['id'],'water-beishan-lou-taixi'),('water-beishan-yenu-taixi',qin['id'])]
    for a,b in links:byid[a]['related_entry_ids'].append(b);byid[b]['related_entry_ids'].append(a)
    for group,values in [('passages',passages),('places',[c for c in cards if c['id']=='place-fajiu']),('text_entities',[c for c in cards if c['kind'] in {'place','rite','deity'} and c['id']!='place-fajiu']),('natural_features',[c for c in cards if c['kind'] in {'plant','water','material'}]),('beasts',[c for c in cards if c['kind']=='beast'])]:world[group]+=values
    northern=sorted([p for p in world['passages'] if p.get('source_book')==3],key=lambda p:p['order'])
    for left,right in zip(northern,northern[1:]):
        for a,b in [(left,right),(right,left)]:
            if b['id'] not in a['related_entry_ids']:a['related_entry_ids'].append(b['id'])
    world['revision']='myth-world-2026-10-25-beishan-seventy-seven-v1'
    review.update(scope='北山经首列25山与总括、次二16列名山与总括、次三至泰戱：77阅读/438独立卡（含复用諸犍、精衛、發鳩），后文待核。',scan_pages=list(range(76,105)),limits='已核76—104页正文段界与形貌，经文/逐行郭注/捕获/编辑说明分存；保留青雄黄异文、疑难注文和形貌不足占位，不宣称全篇或逐字多版本校勘。')
    review['source_unit_page_corrections'].update(PAGE_CORRECTIONS)
    review['entry_ids'] += [c['id'] for c in cards]
    review['passages'] += [{'id':p['id'],'source_unit_ids':p['source_unit_ids'],'source_span':p['source_span'],'status':'facsimile_reviewed'} for p in passages]
    review['commentary_alignment'] += [{'source_unit_ids':p['source_unit_ids'],'basis':p['content_note']} for p in passages]
    review['text_corrections']=TEXT_CORRECTIONS
    review['extb_font_supplement']={'family':'Atlas Northern ExtB','characters':'𤟤𤠾𥬇𬋩𭥍𤓰𤞞𩣡𪄀𪃑𣵀𩹴𬐱𪄶𤍠','path':'frontend/public/fonts/atlas-northern-extb.woff2','license':'frontend/public/fonts/atlas-northern-extb-LICENSE.txt','source_url':'https://github.com/babelstone/babelstonehan-ufo/releases/download/v18.0.1/BabelStoneHanExtra.ttf','sha256':hashlib.sha256((ROOT/'frontend/public/fonts/atlas-northern-extb.woff2').read_bytes()).hexdigest(),'upstream_sha256':'cc8868109070c1813479dc2eb72fba508a1a6c33d807a485959e8f5dcd0e5724','weights':[400],'limits':'授权字体内存子集并改名，原版权许可保留；仅400字重，页面禁用伪粗，600请求使用已有400字形；旧30个本机依赖补5后仍有25个，不宣称全书补齐。'}
    review['next']={'name':'石山','source_units':[259,261],'captured_pages':[104,105],'facsimile_pages':[104],'status':'pending_facsimile_review','notes':'复用104页；0261沱实际104页末、捕获105，待校回104。濩濩水东注虖沱、鮮于水南注虖沱；濩音尺蠖之蠖跨259—260连读，不混生物或矿物。0262童戎另段。'}
    review['second_range_summary']={'status':'facsimile_reviewed','named_mountains':16,'reported_mountains':17,'reported_li':5690,'summary_units':[147,150],'note':'原报17与逐段列名16不合，保留差异，不补山凑数；祭牲埋与玉投不埋分开。'}

    review['first_range_summary']={'status':'facsimile_reviewed','named_mountains':25,'reported_mountains':25,'reported_li':5490,'summary_units':[96,99],'note':'山数一致；里程保留原报，未以现代实测校正。'}

    review['stage_plan']=[{'name':r['name'],'passage_id':p['id'],'source_units':list(r['units']),'new_cards':sum(c.get('content_batch')=='beishan-'+r['slug'] and c['id'] not in {'beast-zhu-jian','beast-jingwei','place-fajiu'} for c in cards),'reused_entry_ids':['beast-jingwei','place-fajiu'] if r['slug']=='fajiu' else [],'text_status':'facsimile_reviewed','browser_status':'see local handoff stage results'} for r,p in zip(ROWS[-5:],passages[-5:])]
    review['batch_size']=5
    review['remaining_stage_estimate']={'scope':'北山经已核正文之后，其他篇目另计','count':len(REMAINING),'mountain_passages':13,'summary_and_total':2,'status':'transcription_based_pending_facsimile','basis':'按现有阅读段口径人工拆分录文；不等于结构候选数，后续影印可调整。','before_this_batch':20,'stages':[{'name':n,'source_units':[a,b],'status':'pending_facsimile_review'} for n,a,b in REMAINING]}
    review['reused_entry_ids']=['beast-zhu-jian','beast-jingwei','place-fajiu']
    assert len(cards)==423,len(cards)
