# 资产来源与许可 / Asset provenance and licensing

盘点日期：2026-11-07（当前文件复核；早期来源平台核对日期仍按原记录）。本清单逐文件记录磁盘现状；许可结论与生成事实分开。

2026-11-07补登记：`frontend/src/assets/shanhai-nav.woff2`（7,512字节）由既有 `frontend/public/fonts/shanhai-title.woff2` 使用 fontTools 裁出导航字形；源字库为 Noto Serif SC，沿用已保存的 OFL。源文件、子集字节摘要和来源限制登记在素材清单；没有替换原字库。开屏 `stage.html` 的题字轮廓来自既有 Ma Shan Zheng 样稿，保留原作者与完整 OFL metadata；流体源码保留 MIT 头。

2026-11-01补登记西王母角色与插画关联表，并更新玉山绑定后的数据文件摘要；原图、派生图字节和许可政策均未改变。

2026-11-01追加：以原会见图为身份基准的新西王母单人原画及三种派生尺寸已登记，旧版与两张原场景图保留；许可政策不变。

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
| 原始插画 | 484 |
| 字体 | 14 |
| 扫描图 | 178 |
| 数据/来源/许可文件 | 91 |
| README展示媒体 | 5 |
| 运行/发布图像（不含SVG） | 1262 |
| SVG | 2 |
| 展示媒体来源记录 | 1 |

当前清单共 2033 个文件。文本记录与字段组沿用独立清单。字体依赖来自本地安装包。

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
4. 两份DjVu底本已核到Commons的Public domain标记；仍需区分影印、电子录文与现代译注，核对适用条件。东山119页细节图已于2026-11-05定位专用URL及匹配的本地登记哈希；当前远端渲染不同，历史获取方法仍未记录，详见下节。
5. 字体子集的版权/许可/重命名对应；Source Sans 3实际WOFF2内嵌版权为Adobe，与包内Google Inc.署名不符，本批已拟补充Adobe声明并保留原包文字；未改字体字节。其他版本及修改条件仍逐项核对。
6. 旧地图矢量的原始下载/派生链及ODbL适用范围；历史天地图服务条款、署名与截图使用条件。本批Natural Earth的固定版本来源另见下节，不替代旧素材待核事项。地图许可不自动变成整站代码许可。
7. 代码按维护者声明采用MIT，仍需保留第三方依赖许可；不据“由模型创建”断言没有第三方权利。

2026-11-03审计快照（2034项；不是当前文件数量）：2017项已定位记录但仍有明确限制，16项直接来源未知，1项复合组成可核而原始创建来源未知。未知项共17项，包含旧14项、东山119页细节图及2个历史创建链未记录的既有内容/关系元数据；另7个新增元数据按已定位构建/派生链核对（含4个内容或关系构建器）。哈希校验与来源证明分开；有记录不等于全部来源或权利已确认。

本次通过Git精确字节匹配补定位72个图像文件的历史素材记录；工具与模型仍按各记录实际字段登记。

<details>
<summary>2026-10-29旧清单快照（14项；当前结果以上文及新表为准）</summary>

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


## 2026-11-03逐文件复核与只读校验

本轮以e1e8b2170cca6d04bf2b80966866bed599dbf2d1为基线，复核2034项当前文件、已登记工作区来源/处理指针，以及31个Git素材清单修订；本轮补登记9个既有JSON，文件内容未改。对旧缺口进行精确Git blob比对，没有找到足以补写逐文件生成事实的新记录。同名、视觉相似、提交日期均没有当作生成来源、模型或生成日期。

`docs/assets-inventory.tsv`新增`audit_status`、`audit_evidence`、`audit_unknowns`、`audit_scope`，每项明确已查证内容和限制。来源事实、模型未知和许可声明分别保留；2017项“已定位记录”也不代表完整参考链或独立授权核定。既有上游引用按记录定位，本轮未将历史平台声明改称新的在线核验结果。

五项README媒体是二进制，原误填的LF文本摘要改为`-`；文件本身未改。角色登记中已修复的伏羲旧状态文字同步纠正。原画、历史记录和既有许可政策全部保留。

从仓库根目录运行`python frontend/scripts/verify-assets.py`，或在frontend运行`npm run verify:assets`。命令只读，检查文件/原始或LF文本摘要、完整性、JSON来源指针、发布派生映射/大小、循环关系和角色覆盖/哈希；不下载素材、不重编码、不补写登记。完整表不在浏览器入口导入。

下表保留2026-11-03待补项及其最新结果；2026-11-06已补定位其余16项记录，逐项证据与限制见TSV及下方补录。缺失的具体模型、未保留的参考附件和未核定的历史条件继续保留为未知；已恢复的工具事件时间见补录。东山细节图不能以相邻原页替代直接裁切证据；SVG代码/嵌入图像分别登记。

| 文件 | 本轮结论 |
| --- | --- |
| `data/reference-scans/dongshan/page-119-detail-1920.jpg` | 2026-11-05已定位本图专用URL与匹配的登记哈希；当前URL返回1920×2909，本地为1920×2910，字节不同，历史获取及渲染方式仍未记录 |
| `frontend/artwork-source/archived/pangu.png` | 2026-11-06已补定位创建/派生记录；见[证据补录](docs/asset-source-recovery.json)。具体模型、未保留的输入附件和历史条件仍有限制 |
| `frontend/artwork-source/archived/suiren-after-fire-v2-original.webp` | 2026-11-06已补定位创建/派生记录；见[证据补录](docs/asset-source-recovery.json)。具体模型、未保留的输入附件和历史条件仍有限制 |
| `frontend/artwork-source/brand/favicon-original.png` | 2026-11-06已补定位创建/派生记录；见[证据补录](docs/asset-source-recovery.json)。具体模型、未保留的输入附件和历史条件仍有限制 |
| `frontend/artwork-source/brand/shanhai-mark-reference.png` | 2026-11-06已补定位创建/派生记录；见[证据补录](docs/asset-source-recovery.json)。具体模型、未保留的输入附件和历史条件仍有限制 |
| `frontend/artwork-source/optimized-originals/myth-icons/kunlun.png` | 2026-11-06已补定位创建/派生记录；见[证据补录](docs/asset-source-recovery.json)。具体模型、未保留的输入附件和历史条件仍有限制 |
| `frontend/artwork-source/optimized-originals/myth-icons/nuwa.png` | 2026-11-06已补定位创建/派生记录；见[证据补录](docs/asset-source-recovery.json)。具体模型、未保留的输入附件和历史条件仍有限制 |
| `frontend/artwork-source/optimized-originals/myth-icons/xi-wang-mu.png` | 2026-11-06已补定位创建/派生记录；见[证据补录](docs/asset-source-recovery.json)。具体模型、未保留的输入附件和历史条件仍有限制 |
| `frontend/artwork-source/optimized-originals/myth-paper.png` | 2026-11-06已补定位创建/派生记录；见[证据补录](docs/asset-source-recovery.json)。具体模型、未保留的输入附件和历史条件仍有限制 |
| `frontend/public/data/atlas/myth-icons/characters/fuxi-corrected.svg` | 2026-11-06已补定位创建/派生记录；见[证据补录](docs/asset-source-recovery.json)。具体模型、未保留的输入附件和历史条件仍有限制 |
| `frontend/public/data/atlas/myth-icons/kunlun.webp` | 2026-11-06已补定位创建/派生记录；见[证据补录](docs/asset-source-recovery.json)。具体模型、未保留的输入附件和历史条件仍有限制 |
| `frontend/public/data/atlas/myth-icons/nuwa.webp` | 2026-11-06已补定位创建/派生记录；见[证据补录](docs/asset-source-recovery.json)。具体模型、未保留的输入附件和历史条件仍有限制 |
| `frontend/public/data/atlas/myth-icons/xi-wang-mu.webp` | 2026-11-06已补定位创建/派生记录；见[证据补录](docs/asset-source-recovery.json)。具体模型、未保留的输入附件和历史条件仍有限制 |
| `frontend/public/data/atlas/myth-paper.webp` | 2026-11-06已补定位创建/派生记录；见[证据补录](docs/asset-source-recovery.json)。具体模型、未保留的输入附件和历史条件仍有限制 |
| `frontend/public/data/shanhai-ornament.svg` | 2026-11-06已补定位创建/派生记录；见[证据补录](docs/asset-source-recovery.json)。具体模型、未保留的输入附件和历史条件仍有限制 |
| `frontend/src/bestiary-metadata.json` | 2026-11-06已补定位创建/派生记录；见[证据补录](docs/asset-source-recovery.json)。具体模型、未保留的输入附件和历史条件仍有限制 |
| `frontend/src/geography-associations.json` | 2026-11-06已补定位创建/派生记录；见[证据补录](docs/asset-source-recovery.json)。具体模型、未保留的输入附件和历史条件仍有限制 |

## 2026-11-05补充核查

逐项重查此前17项的当前文件、已有清单与跟随重命名的Git历史。东山119页细节图已有专用URL及与本地文件一致的SHA-256，现改为“已定位记录但有限制”。本次未用相邻页替代证据，也未修改影印字节；本次下载只在内存比较，远端当前字节与历史本地字节不一致，具体值写入 `data/reference-scans/dongshan/sources.json#/10/detail_source_recheck`。

2026-11-05维护批次共2031项，其中2015项为 `record_located_with_limits`、15项为 `source_unknown`、1项为 `composition_recorded_origin_unknown`。当时16项未定位创建记录；2026-11-06的补录结果见下节。所有17项均补记已查Git提交，但提交日期不能当作生成日期。地理关系元数据本轮仅修正Zhangzi拼写，不将新修改记作原始创建证据。

本轮逐项结论见[内容与来源复核](docs/editorial-review.md)。定位记录及派生链不等于完整权利核定。

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

四张WebP截图与一段12秒GIF由实际本地界面采集，无模拟底图。逐文件哈希、尺寸、工具与原构建commit见[媒体清单](docs/media/manifest.json)，同样逐项登记于[资产文件清单](docs/assets-inventory.tsv)。截图与录屏是复合内容，不因展示代码采用MIT而改变内嵌资产的原许可；当前地理截图保留Natural Earth署名；历史天地图截图的使用条件仍未核定，复合界面内嵌素材不因此获得额外授权。


## 本地自然地理底图（Natural Earth v5.1.2）

地理页面使用Natural Earth固定版本的1:50m陆地、湖泊及主要河流，原始文件保存在`data/reference-maps/natural-earth-v5.1.2/`，派生文件及来源记录为`frontend/public/data/geography/natural-earth-50m-v5.1.2.geojson`和同名`.sources.json`。原始下载URL、SHA、裁切/拓扑保持简化、坐标精度与工具版本均记录其中，重建脚本为`data/build_geography_basemap.py`。Natural Earth在其[使用条款](https://www.naturalearthdata.com/about/terms-of-use/)中声明这些数据属于公有领域。此记录只适用于该组地图数据，不改变项目插画、字体、古籍转写及历史天地图截图的使用条件。显示为现代地理参照的古风绘制，不是古代地理复原。


## 可选原图与影印分发包

[2026-11-05 v1分发版本](https://github.com/hyc1005/mythmap/releases/tag/assets-2026-11-05-v1)按目录提供18个ZIP，共678个源文件，来源提交`c6ca994`。原文件仍保留在主仓库。`data/asset-bundles.json`记录每包及每文件的SHA-256、原路径、字节数和下载地址；JSON统一LF，图像保持原字节。恢复步骤见[数据维护入口](data/README.md#轻量检出与原图分发)。

发布前已在独立轻量检出中恢复，并完成全量素材审计；上传后逐文件核对GitHub返回的摘要和大小。分发包随附本声明及LICENSE，沿用各源文件的原许可与未知状态，不新增复用授权。该分发版本保留2026-11-05的来源审计快照；2026-11-06补录在主仓库中另行提供，不覆盖固定分发包。


## 2026-11-06历史记录补录

从本机Codex会话数据库的历史投影中恢复了与16项缺口直接相关的15个工具条目，包含8个图像生成条目。原JSONL已缺失，数据库仍保留工具条目、提示词、时间和图像结果。仅导出本项目相关的脱敏证据，见[`asset-source-recovery.json`](docs/asset-source-recovery.json)；不上传完整会话、数据库、用户绝对路径或图像base64。

- 七个PNG原图文件（其中两份品牌图为同一输出）与生成结果的原始字节SHA-256一致，恢复对应提示词、透明参数及工具记录时间。时间来自工具条目，不用Git提交日期代替。
- 昆仑、女娲、西王母和纸纹WebP与对应PNG的完整RGBA像素一致，并定位成功执行的无损转换命令。当前编码器未重现旧WebP字节，不将像素等价写成字节重现。
- 燧人旧WebP关联到保留的原始PNG和生成条目，透明度、可见合成RGBA一致；透明区域下隐藏RGB不同，单独记录，未修改文件。
- 装饰SVG与原始新增补丁的LF文本完全一致。伏羲组合SVG定位到原生代码新增补丁，所用人物PNG与生成输出字节一致，后续修订仍由Git记录。
- 两个元数据文件定位到成功执行的创建命令、输入路径和方法。异兽元数据创建使用硬编码条目序号及正则等方法；这解释创建来源，不构成分类正确性的独立证明。45条形貌限制继续保留。

当前2032项均为`record_located_with_limits`，未定位创建记录的16项已补定位。**这不表示所有来源不确定性都已消除**：确切模型、原始附件全集、历史服务与权利条件仍未完全建立，古籍释读、形貌分类和地理关联也未因记录恢复而获得新的专业核定。原图、译文、网页和许可政策均未更改。11月5日固定Release不覆盖，新证据另见当前主仓库。

另核得8个相关生成PNG的caBX/C2PA中均有softwareAgent声明`ChatGPT / gpt-image`，已登记原字节位置和CBOR字节片段。此为文件内嵌声明，未独立验证签名，不能据此推定gpt-image-1、1.5或其他精确API模型/后端版本。
