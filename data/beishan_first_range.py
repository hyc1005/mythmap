"""Reviewed first-range extension for the Northern Mountains builder."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGE_CORRECTIONS = {'source-03-0018': 77, 'source-03-0027': 78,
                    'source-03-0036': 79, 'source-03-0045': 80}
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


def extend(world, english, chapter, review):
    folder = ROOT / 'frontend/artwork-source/beishan'
    jobs = {a['entry_id']:a for a in json.loads((folder/'entities-generation.json').read_text(encoding='utf-8'))['assets']}
    lines = chapter['lines']
    source, en_source = world['passages'][-1]['source'], english['passage-beishan-qiuru']['source']
    batches = {'beishan-'+r['slug'] for r in ROWS}
    core = next(c.copy() for c in world['beasts'] if c['id']=='beast-zhu-jian')
    core['legacy_quote'] = core.get('legacy_quote', core['quote'])
    core['aliases'] = list(dict.fromkeys([*core.get('aliases', []), '诸犍']))
    for group in ['passages','text_entities','natural_features','beasts']:
        world[group] = [r for r in world[group] if r.get('content_batch') not in batches and r['id']!='beast-zhu-jian']
    passages, cards = [], []
    for order,row in enumerate(ROWS,3):
        slug=row['slug']; first,last=row['units']; pid='passage-beishan-'+slug; place='place-beishan-'+slug
        refs=[(f'source-03-{i+1:04}',lines[i]) for i in range(first-1,last)]
        pages=sorted({PAGE_CORRECTIONS.get(id,int(l['page'].rsplit('/',1)[1])) for id,l in refs})
        urls=[f'https://zh.wikisource.org/wiki/Page:Sibu_Congkan0465-郭璞-山海經-2-1.djvu/{n}' for n in pages]
        raw=''.join(l['text'] for _,l in refs)
        common=dict(source=source,source_chapter='《北山经》',source_book=3,region='北山经',source_locator='卷第三 · 影印页 '+'、'.join(map(str,pages)),source_pages=urls,url=urls[0],source_unit_ids=[id for id,_ in refs],reveal_chapter='03',content_batch='beishan-'+slug,review_status='facsimile_reviewed',artwork_pending=True,direction='按北山经篇内次序与方位阅读，不换算现代坐标或实测里程。',editorial_note='经文、捕获快照和郭注分存；白话及英文为项目整理。食用、治病与灾异为古籍记述。')
        translation=dict(source=en_source,source_chapter='Beishan Jing',region='Beishan Jing',source_locator='Volume 3 · scan pages '+', '.join(map(str,pages)),direction='Read the Northern textual sequence and directions; these are not modern coordinates or measured distances.',editorial_note='Text, captured transcription and commentary are separate; explanations and English are editorial. Eating, healing and omen claims are ancient accounts.')
        commentary='\n'.join(f'〔影印页{PAGE_CORRECTIONS.get(id,int(l["page"].rsplit("/",1)[1]))}〕'+'；'.join(l['annotations']) for id,l in refs if l['annotations'])
        p={**common,'id':pid,'kind':'passage','name':row['name'],'range':1,'order':order,'description':row['description'],'quote':raw,'captured_text':raw,'commentary_quote':commentary,'content_note':row['note'],'captured_commentary':[{'source_unit_id':id,'annotations':l['annotations']} for id,l in refs],'source_span':[sum(len(l['text']) for l in lines[:first-1]),sum(len(l['text']) for l in lines[:last])],'related_entry_ids':[place],'subjects':[row['name']]}
        english[pid]={**translation,'name':row['en_name'],'description':row['en_description'],'quote':row['en_quote'],'content_note':row['en_note']}
        c={**common,'id':place,'kind':'place','name':row['name'],'description':row['description'],'quote':raw,'commentary_quote':commentary,'content_note':row['note'],'source_passage_ids':[pid],'related_entry_ids':[pid]}
        english[place]=dict(english[pid]); cards.append(c)
        for e in [e for e in ENTITIES if e['slug']==slug]:
            assert e['quote'] in raw,e['id']
            c={**(core if e['id']=='beast-zhu-jian' else {}),**common,**{k:e[k] for k in ['id','kind','name','description','quote']},'commentary_quote':e.get('commentary',''),'context_place_id':place,'source_passage_ids':[pid],'related_entry_ids':[pid]}
            english[e['id']]={**translation,'name':e['en_name'],'description':e['en_description'],'quote':e['en_quote'],'commentary_quote':e.get('en_commentary','')}
            if e['kind']=='water' or e.get('water'):c['relation_scope']='water'
            a=jobs.get(e['id'])
            if a and a['status']=='reviewed':
                c.update(artwork='beishan/'+a['name']+'-v1.webp',artwork_pending=False,artwork_caption='原文形貌与木刻演绎 · 刻纹、配色和姿态为艺术解释；郭注形貌另有说明。')
                english[e['id']]['artwork_caption']='Textual form in woodcut interpretation; carving, colors and pose are artistic, with commentary-based form identified separately.'
            elif e['id']=='beast-zhu-jian':
                c.update(artwork_pending=False,artwork_caption='旧图复核：独目、人首牛耳、豹身长尾；盘尾为居态演绎。')
                english[e['id']]['artwork_caption']='Existing artwork reviewed: one eye, human head, ox ears, leopard body and long tail; the coiled tail interprets resting posture.'
            elif e['kind']=='beast':
                c.update(appearance_unknown=True,artwork_caption='形貌未详或依据不足 · 统一问号占位不代表本生物形态。')
                english[e['id']]['artwork_caption']='Appearance unspecified or evidence insufficient; the shared question-mark placeholder is not a depiction.'
            cards.append(c);p['related_entry_ids'].append(c['id']);p['subjects'].append(c['name'])
        passages.append(p)
    byid={c['id']:c for c in cards}
    contexts=[p for p in passages if p['id'] in {'passage-beishan-'+s for s in ['qiaoming','zhuoguang','guoshan','guowei','shizhe']}]
    he={**{k:v for k,v in contexts[0].items() if k not in ['id','kind','name','range','order','description','quote','captured_text','captured_commentary','commentary_quote','content_note','source_span','subjects']},'id':'water-beishan-he','kind':'water','name':'河（北山经）','description':'河分别承接譙水、囂水、伊水、魚水和泚水的西流。五段独立保存出处，不据同名与西山河合并或认定现代汇流点。','quote':'；'.join(['譙水出焉西流注于河','囂水出焉而西流注于河','伊水出焉西流注于河','魚水出焉而西流注于河','泚水出焉而西流注于河']),'commentary_quote':'','source_passage_ids':[p['id'] for p in contexts],'context_place_id':'place-beishan-qiaoming','context_place_ids':['place-beishan-zhuoguang','place-beishan-guoshan','place-beishan-guowei','place-beishan-shizhe'],'source_unit_ids':list(dict.fromkeys(id for p in contexts for id in p['source_unit_ids'])),'source_pages':list(dict.fromkeys(u for p in contexts for u in p['source_pages'])),'source_locator':'卷第三 · 影印页 77、78、79、80','relation_scope':'water','related_entry_ids':[p['id'] for p in contexts],'content_note':'分号分开五段摘句，不是连续经文或一条完整河道。'}
    english[he['id']]={**english['water-beishan-qiao-qiaoming'],'name':'He (Northern Mountains)','description':'The He separately receives the west-flowing Qiao, Xiao, Yi, Yu and Ci in five passages. Their sources remain separate, without a merger with the Western He or modern confluences.','quote':'The Qiao flows west into the He; separately, the Xiao flows west into the He; the Yi flows west into the He; the Yu flows west into the He; and the Ci flows west into the He.','source_locator':'Volume 3 · scan pages 77, 78, 79, 80','content_note':'Semicolons separate five excerpts, not a continuous quotation or complete river course.'}
    cards.append(he);byid[he['id']]=he
    for p in contexts:p['related_entry_ids'].append(he['id'])
    links=[('water-beishan-peng-daishan','water-beishan-pihu-daishan'),('water-beishan-peng-daishan','beast-beishan-youyu-daishan'),('water-beishan-qiao-qiaoming','beast-beishan-heluo-qiaoming'),('water-beishan-xiao-zhuoguang','beast-beishan-xixi-zhuoguang'),('water-beishan-yu-guowei','material-beishan-wenbei-guowei')]
    links += [(id,'water-beishan-he') for id in ['water-beishan-qiao-qiaoming','water-beishan-xiao-zhuoguang','water-beishan-yi-guoshan','water-beishan-yu-guowei','water-beishan-ci-shizhe']]
    links += [('water-beishan-xun-danxun','water-beishan-tang-danxun'),('water-beishan-gang','water-beishan-youze'),('water-beishan-li-danzhang','water-beishan-gang')]
    gang=byid['water-beishan-gang']; last=next(p for p in passages if p['id']=='passage-beishan-danzhang')
    gang['source_passage_ids'].append(last['id']); gang['context_place_ids']=['place-beishan-danzhang']
    gang['source_unit_ids'] += last['source_unit_ids']; gang['source_pages'] += last['source_pages']
    gang['source_locator']='卷第三 · 影印页 80、81'
    gang['quote'] += '；櫟水出焉而南流注于杠水'
    gang['content_note']='分号分开邊春与單張摘句，不是连续经文。'
    last['related_entry_ids'].append(gang['id'])
    english[gang['id']].update(quote='The Gang rises here and flows west into Youze; separately, the Li rises at Danzhang and flows south into the Gang.',source_locator='Volume 3 · scan pages 80, 81',content_note='Semicolons separate Bianchun and Danzhang excerpts, not a continuous quotation.')
    for a,b in links:byid[a]['related_entry_ids'].append(b);byid[b]['related_entry_ids'].append(a)
    for group,values in [('passages',passages),('text_entities',[c for c in cards if c['kind']=='place']),('natural_features',[c for c in cards if c['kind'] in {'plant','water','material'}]),('beasts',[c for c in cards if c['kind']=='beast'])]:world[group]+=values
    northern=sorted([p for p in world['passages'] if p.get('source_book')==3],key=lambda p:p['order'])
    for left,right in zip(northern,northern[1:]):
        for a,b in [(left,right),(right,left)]:
            if b['id'] not in a['related_entry_ids']:a['related_entry_ids'].append(b['id'])
    world['revision']='myth-world-2026-10-24-beishan-twelve-v1'
    review.update(scope='北山经首列前12段：單狐至單張，12阅读/80独立卡（含复用諸犍），后文待核。',scan_pages=[76,77,78,79,80,81],limits='已核76—81页正文段界与形貌，经文/逐行郭注/捕获/编辑说明分存；保留青雄黄异文、疑难注文和形貌不足占位，不宣称全篇或逐字多版本校勘。')
    review['source_unit_page_corrections'].update(PAGE_CORRECTIONS)
    review['entry_ids'] += [c['id'] for c in cards]
    review['passages'] += [{'id':p['id'],'source_unit_ids':p['source_unit_ids'],'source_span':p['source_span'],'status':'facsimile_reviewed'} for p in passages]
    review['commentary_alignment'] += [{'source_unit_ids':p['source_unit_ids'],'basis':p['content_note']} for p in passages]
    review['next']={'name':'灌題之山','source_units':[54,58],'captured_pages':[81,82],'status':'pending_facsimile_review','notes':'0054实际见81页末，需核82页正文续；那父、竦斯及匠韓水分别核对，复用北山泑澤，不借同名旧图。'}
    review['five_stage_plan']=[{'name':r['name'],'passage_id':p['id'],'source_units':list(r['units']),'new_cards':sum(c.get('content_batch')=='beishan-'+r['slug'] and c['id']!='beast-zhu-jian' for c in cards),'reused_entry_ids':['beast-zhu-jian'] if r['slug']=='danzhang' else [],'text_status':'facsimile_reviewed','browser_status':'see local handoff stage results'} for r,p in zip(ROWS[-5:],passages[-5:])]
    review['reused_entry_ids']=['beast-zhu-jian']
    assert len(cards)==65,len(cards)
