# 资产来源与许可 / Asset provenance and licensing

盘点日期：2026-10-29。本清单逐文件记录磁盘现状；许可结论与生成事实分开。

## 许可边界 / Licensing boundaries

- 根目录 LICENSE 的 MIT 许可适用于 hyc1005 有权授权的项目程序代码及软件操作文档。古籍录文、内容数据、项目白话、模型翻译、插画、扫描、字体、地图、品牌图及其变体不因位于本仓库而获得 MIT 授权。
- 项目内容和AI插画暂不额外授予复用许可，仅在维护者依法享有的权利范围内保留权利；这不是对AI输出可版权性、独占性或无侵权的保证，也不撤回第三方既有许可或限制公有领域内容。
- 维护者已说明：代码由其驱动模型创建，翻译由模型生成，插画使用 OpenAI 图像生成工具。项目维护者署名为 hyc1005，不将模型列为人类作者；具体历史模型没有记录时写“未记录”。
- 部分记录明确引用项目内部插画作风格参考，不声称所有图像都没有参考。未定位逐图记录与未发现第三方参考证据不是“已排除第三方权利”。
- The MIT license covers project software and operational documentation only to the extent hyc1005 can license them. Content data, paraphrases, translations, artwork, scans, fonts, maps and branding are excluded. No additional reuse permission is granted for project content or AI artwork; existing third-party licenses and public-domain freedoms remain unaffected.
- This is a provenance inventory, not legal clearance. Unknown models and rights remain explicitly unresolved. The maintainer reports model-assisted code and translations and OpenAI-generated artwork; some assets use internal style references.

## 盘点口径与摘要

文件SHA-256与字节数记录本次本地盘点的原始文件；文本另附`sha256_lf`与`bytes_lf`，按UTF-8内容将CRLF/CR统一为LF后计算，供跨平台核验；二进制资产这两列记为`-`。Git自动换行可能改变文本的原始字节摘要，不能因此判定内容被改写。文本字段摘要按所列字段的UTF-8、键排序、无多余空白JSON计算。每行档案指针采用JSON Pointer；长路径或表内文字不构成许可授予。生成记录中的私人绝对路径不复制到本表，使用仓库内证据指针追溯。

以git:开头的证据先按当前文件与旧发布文件的Git blob逐字节匹配，再关联该修订中的素材记录；不以同名文件或外观相似推定来源。旧记录只写“既有项目插画”的，生成工具仍需确认。历史记录的存在不证明授权已核定。

| 类别 | 文件数 |
| --- | --- |
| 原始插画 | 482 |
| 字体 | 13 |
| 扫描图 | 178 |
| 数据/来源/许可文件 | 73 |
| README展示媒体 | 5 |
| 运行/发布图像 | 1254 |

总计 2005 个文件；另登记 7433 个文本记录/字段组。引用的字体依赖文件为本地安装包，不新增跟踪 node_modules。

## 许可与来源配置档 / Profiles

| 配置档 | 来源/作者与工具 | 许可及状态 |
| --- | --- | --- |
| AI-P | hyc1005组织生成（用户说明）；OpenAI内置image_gen；记录提及时包含既有项目插画及内部风格参考；模型见逐图列 | 不额外授权；历史服务条款、参考链与可授权范围需确认 |
| SVG-CODE | 原生SVG路径/文字代码；hyc1005组织模型编写代码（用户说明），具体工具/模型未记录 | 图形资产不因代码形式自动纳入MIT；暂不额外开放复用，不能登记为image_gen直接输出 |
| SVG-COMPOSITE | 原生SVG代码叠加嵌入图像；底图来源按derived_from追溯，矢量代码具体生成工具/模型未记录 | 复合资产按组成分别核对；底图image_gen记录不能替代整个SVG的生成记录或许可 |
| AI-TEXT | hyc1005组织的模型翻译（用户说明）；生成工具/具体模型未记录；未声称已专业人工审校 | 不额外授权；第三方底文/译注权利需确认 |
| MIXED-TEXT | 古籍/郭璞注/项目整理/模型文字混合；原作者、来源与记录内字段对应；现代整理贡献及工具未逐条记录 | 古籍原作与电子录文、现代说明分开核对；不得整体声明MIT或整体私有 |
| SCAN-U | 古籍原作；晋郭璞传；维基文库/Wikimedia影印来源；扫描制作者及图像处理工具未记录 | 文件级许可需确认；不以古籍年代代替扫描/录文来源许可 |
| SCAN-PD-CLAIM | 古籍原作/晋郭璞注；Commons Artist字段为Guo Pu，不等于扫描制作者证明；扫描工具/模型未记录 | 来源文件在Commons标记Public domain，2026-10-29核对；仅记录平台声明，不替用户作法律结论 |
| FONT-OFL | 见各字体行、上游包及许可文件；子集与转换由项目字体脚本生成；AI模型不适用 | SIL Open Font License 1.1；需保留版权、许可及适用重命名要求 |
| FONT-APL | Arphic Technology / Andrew West；BabelStone Han系列；项目fontTools子集/重命名；AI模型不适用 | Arphic Public License（见随附原文）；修改再分发条件需逐项核对 |
| FONT-HANA | GlyphWiki Project / HanaMinB；项目fontTools子集/重命名；AI模型不适用 | 随附Hanazono Font License与OFL双许可；按适用原许可保留说明 |
| MIXED-DATA | 容器内可能包含古籍录文、项目内容、地理数据及资产元数据；工具/模型不统一推定 | 按记录来源分别核对，不对整个JSON/GeoJSON统一授予MIT |
| UI-MEDIA | hyc1005项目界面的Playwright实录；Pillow编码；无生成模型，内嵌素材继承各自来源 | 复合截图/录屏；代码MIT不覆盖内嵌插画、字体和地图，暂不额外开放内容复用 |
| EVIDENCE | 来源、提示词、审核记录或许可文本；不表示记录内所指资产已获许可 | 保留原许可与来源说明；未载许可不推定开放 |

## 必须人工确认的事实缺口

1. 历史生成服务及当时适用条款；具体模型未记录的保留未知，不按当前默认型号补写。
2. 品牌图、既有插画、SVG及未定位逐图记录的生成/参考链；内部参考链应最终指向有来源记录的资产。
3. 模型译文及现代说明是否输入或实质使用第三方现代译注；引用出处不是整段复制的授权证明。
4. 两份DjVu底本已核到Commons的Public domain标记；仍需区分影印、电子录文与现代译注，核对适用条件。东山119页细节图缺少直接来源条目，须确认是否为同目录原页裁切及其生成方法。
5. 字体子集的版权/许可/重命名对应；Source Sans 3实际WOFF2内嵌版权为Adobe，与包内Google Inc.署名不符，本批已拟补充Adobe声明并保留原包文字；未改字体字节。其他版本及修改条件仍逐项核对。
6. 地图矢量的原始下载/派生链及ODbL适用范围；天地图实际服务条款、署名与README截图使用条件。地图许可不自动变成整站代码许可。
7. 代码按维护者声明采用MIT，仍需保留第三方依赖许可；不据“由模型创建”断言没有第三方权利。

尚未定位逐图来源记录的图像：14 个；来源清单声明哈希与当前文件不符：0 项。工具、模型和法律许可另外核对，记录存在不等于授权已获确认。

本次通过Git精确字节匹配补定位72个图像文件的历史素材记录；工具与模型仍按各记录实际字段登记。

<details>
<summary>缺少逐图来源记录的14项</summary>

- `frontend/artwork-source/archived/pangu.png`
- `frontend/artwork-source/archived/suiren-after-fire-v2-original.webp`
- `frontend/artwork-source/brand/favicon-original.png`
- `frontend/artwork-source/brand/shanhai-mark-reference.png`
- `frontend/artwork-source/optimized-originals/myth-icons/kunlun.png`
- `frontend/artwork-source/optimized-originals/myth-icons/nuwa.png`
- `frontend/artwork-source/optimized-originals/myth-icons/xi-wang-mu.png`
- `frontend/artwork-source/optimized-originals/myth-paper.png`
- `frontend/public/data/atlas/myth-icons/characters/fuxi-corrected.svg`
- `frontend/public/data/atlas/myth-icons/kunlun.webp`
- `frontend/public/data/atlas/myth-icons/nuwa.webp`
- `frontend/public/data/atlas/myth-icons/xi-wang-mu.webp`
- `frontend/public/data/atlas/myth-paper.webp`
- `frontend/public/data/shanhai-ornament.svg`

</details>

## 官方规则入口

- [MIT标准文本](https://opensource.org/license/mit)
- [OpenAI个人服务条款](https://openai.com/policies/terms-of-use/)；实际API/商业服务需对应其适用条款，不能以当前页面替代生成时记录。
- [Wikimedia使用条款](https://foundation.wikimedia.org/wiki/Policy:Terms_of_Use/en#7._Licensing_of_Content)
- [OpenStreetMap版权与ODbL说明](https://www.openstreetmap.org/copyright)
- [BabelStone Han许可说明](https://www.babelstone.co.uk/Fonts/Han.html)

## 影印来源的平台声明

2026-10-29通过Commons官方imageinfo/extmetadata接口核对。下面只转记来源平台字段，不把Public domain标签写成本项目的独立法律认定，也不将影印文件标签推广到电子录文、现代译文或未确认裁切。扫描制作人员和设备仍未记录。

| 来源文件 | Commons许可字段 | Artist字段的边界 | 核对日期 |
| --- | --- | --- | --- |
| [File:Sibu Congkan0465-郭璞-山海經-2-1.djvu](https://commons.wikimedia.org/wiki/File:Sibu_Congkan0465-%E9%83%AD%E7%92%9E-%E5%B1%B1%E6%B5%B7%E7%B6%93-2-1.djvu) | Public domain | Guo Pu（底本注者，不等同扫描制作人员） | 2026-10-29 |
| [File:Sibu Congkan0466-郭璞-山海經-2-2.djvu](https://commons.wikimedia.org/wiki/File:Sibu_Congkan0466-%E9%83%AD%E7%92%9E-%E5%B1%B1%E6%B5%B7%E7%B6%93-2-2.djvu) | Public domain | Guo Pu（底本注者，不等同扫描制作人员） | 2026-10-29 |

[本次官方API查询](https://commons.wikimedia.org/w/api.php?action=query&format=json&titles=File%3ASibu_Congkan0465-%E9%83%AD%E7%92%9E-%E5%B1%B1%E6%B5%B7%E7%B6%93-2-1.djvu%7CFile%3ASibu_Congkan0466-%E9%83%AD%E7%92%9E-%E5%B1%B1%E6%B5%B7%E7%B6%93-2-2.djvu&prop=imageinfo&iiprop=extmetadata)。项目仍保留原始来源、修订和页码，用于溯源。

## 插画与图像逐文件表

配置档提供每行的维护者、生成工具和许可边界；原生SVG和含底图的SVG单独登记，不推定为图像工具直接输出。文件级生成证据优先于用户总体说明。模型列未记录即未知。记录存在不等于授权已核定。

完整逐图表见[资产文件清单](docs/assets-inventory.tsv)，筛选类型“插画/图像”或“SVG”。每个原图与发布变体独立一行，含字节SHA-256、来源证据、模型、派生与参考关系；不按目录合并。

## 扫描逐文件表

完整逐页表见[资产文件清单](docs/assets-inventory.tsv)，筛选类型“扫描图”；178张图均独立登记。来源页面与图像URL分列，细节图的可能派生关系不当作已确认事实。

## 字体逐文件表

| 文件 | SHA-256 | 来源/作者 | 工具/许可档 | 具体模型 | 许可证据 | 状态 |
| --- | --- | --- | --- | --- | --- | --- |
| `frontend/node_modules/@fontsource-variable/lora/files/lora-latin-wght-normal.woff2` | ddb8c66035104e233fc024669183aad3738b6daa16deee2ebb1241bd0f98ace1 | lora；Lora Project Authors | FONT-OFL | 不适用 | frontend/public/fonts/lora-LICENSE.txt | 许可文本已定位；版本/修改条件逐项核对 |
| `frontend/node_modules/@fontsource-variable/source-sans-3/files/source-sans-3-latin-wght-normal.woff2` | 19143dca075972bc84e3fd9eab7416dd40cc565dccb2435a044bdfabe060c7d5 | source-sans-3；Adobe（实际WOFF2内嵌版权2023）；原包许可误署Google Inc.，本批补充Adobe并保留原声明 | FONT-OFL | 不适用 | frontend/public/fonts/source-sans-3-LICENSE.txt | 字体内嵌Adobe署名已核对；随附说明补充署名并保留原包文字 |
| `frontend/public/fonts/atlas-central-exth.woff2` | 30d6c28713d3da08499f725842b1388ddc708f61b779af09036e8629f0d41b47 | BabelStone Han / Han Extra；Arphic Technology / Andrew West | FONT-APL | 不适用 | frontend/public/fonts/atlas-central-exth-LICENSE.txt | 许可文本已定位；版本/修改条件逐项核对 |
| `frontend/public/fonts/atlas-central-rare.woff2` | fd55b5a7cb15d796823df8f75369b3fbd961e60ae5c8469a6dac5acd45affc55 | HanaMinB；GlyphWiki Project（见原许可） | FONT-HANA | 不适用 | frontend/public/fonts/atlas-central-rare-LICENSE.txt | 许可文本已定位；版本/修改条件逐项核对 |
| `frontend/public/fonts/atlas-eastern-rare.woff2` | f0317b09a3510d931d82717a311423726ee92c33805ba697720d4a0a7ca7a81b | HanaMinB；GlyphWiki Project（见原许可） | FONT-HANA | 不适用 | frontend/public/fonts/atlas-eastern-rare-LICENSE.txt | 许可文本已定位；版本/修改条件逐项核对 |
| `frontend/public/fonts/atlas-northern-extb.woff2` | 888bcf2f75f4012eb095fe78e1fbe6379f5208509ce51623d647b572b6c3dcab | BabelStone Han / Han Extra；Arphic Technology / Andrew West | FONT-APL | 不适用 | frontend/public/fonts/atlas-northern-extb-LICENSE.txt | 许可文本已定位；版本/修改条件逐项核对 |
| `frontend/public/fonts/atlas-northern-tan.woff2` | dcfd0badb8ff642ae5c3950e45d354aba30c0bee8d0d6251241a6dc3eff21311 | HanaMinB；GlyphWiki Project（见原许可） | FONT-HANA | 不适用 | frontend/public/fonts/atlas-northern-tan-LICENSE.txt | 许可文本已定位；版本/修改条件逐项核对 |
| `frontend/public/fonts/shanhai-bestiary.woff2` | 9c49c4f126a197078145b801e127865c7fa220c3b4e098ea05738f6876fb6a50 | Noto Serif SC；Google/Noto贡献者（见原许可） | FONT-OFL | 不适用 | frontend/public/fonts/noto-serif-sc-LICENSE.txt | 许可文本已定位；版本/修改条件逐项核对 |
| `frontend/public/fonts/shanhai-rare.woff2` | dcf1c5f6fb0d87658f8bd72b25966fea36744e47618c1fe0e74121e8d742a817 | BabelStone Han 16.0.3；Arphic Technology / Andrew West | FONT-APL | 不适用 | frontend/public/fonts/ShanhaiRare-LICENSE.txt | 许可文本已定位；版本/修改条件逐项核对 |
| `frontend/public/fonts/shanhai-title-beishan.woff2` | a11eaffdb07c0468882bb3e46a1d641c147b9b9e8ac94b28883d2aed0de2de7d | Noto Serif SC；Google/Noto贡献者（见原许可） | FONT-OFL | 不适用 | frontend/public/fonts/noto-serif-sc-LICENSE.txt | 许可文本已定位；版本/修改条件逐项核对 |
| `frontend/public/fonts/shanhai-title-dongshan.woff2` | b6130f18c03ac46eb528ddfc5f7b1f291f3f018768964406404011b5c85fca33 | Noto Serif SC；Google/Noto贡献者（见原许可） | FONT-OFL | 不适用 | frontend/public/fonts/noto-serif-sc-LICENSE.txt | 许可文本已定位；版本/修改条件逐项核对 |
| `frontend/public/fonts/shanhai-title-zhongshan.woff2` | 9358c33be7fbe90cadf8efea25e5f4ad674b264a33efe828e998875e0d9ba96c | Noto Serif SC；Google/Noto贡献者（见原许可） | FONT-OFL | 不适用 | frontend/public/fonts/noto-serif-sc-LICENSE.txt | 许可文本已定位；版本/修改条件逐项核对 |
| `frontend/public/fonts/shanhai-title.woff2` | 37db4f82aaa15ab3a2f765cbcfd4d537f8dfb4b2b78a94fce788802150581826 | Noto Serif SC；Google/Noto贡献者（见原许可） | FONT-OFL | 不适用 | frontend/public/fonts/noto-serif-sc-LICENSE.txt | 许可文本已定位；版本/修改条件逐项核对 |

## 数据、生成记录及许可文本逐文件表

完整清单见[资产文件清单](docs/assets-inventory.tsv)，含全部数据、生成记录、来源记录与随附许可文本；配置档为EVIDENCE或MIXED-DATA。

## 内容与模型译文逐记录表

本表不复制正文。MIXED-TEXT记录所列字段包含古籍与现代整理，须逐字段依原记录分辨；AI-TEXT由用户说明为模型翻译。标题与姓名不据此主张独占。文件本身哈希见前表，下面是字段组摘要。

完整逐记录表见[内容与译文许可清单](docs/content-rights-inventory.tsv)。记录ID、JSON指针、字段列表、字段组SHA-256及许可档均独立保留，不复制正文。

## 复核边界

本批新增来源与许可说明并补充一份字体署名；不改原图、扫描、字体二进制、译文、数据结构或发布行为。后续新增README媒体须同步登记来源和摘要。文件增加或字节变化后需重新盘点；本清单不将已有文件自动判断为可压缩或可删除。

## README截图与演示

四张WebP截图与一段12秒GIF由实际本地界面采集，无模拟底图。逐文件哈希、尺寸、工具与原构建commit见[媒体清单](docs/media/manifest.json)，同样逐项登记于[资产文件清单](docs/assets-inventory.tsv)。截图与录屏是复合内容，不因展示代码采用MIT而改变内嵌资产的原许可；地理截图保留天地图署名，其再利用条件仍需确认。
