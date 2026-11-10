# 文档导航

当前网站的启动、构建与发布入口在根目录[中文README](../README.zh-CN.md)及[English README](../README.md)。

| 文档 | 用途与维护方式 |
| --- | --- |
| [更新记录](../CHANGELOG.md) | 按发布批次记录站点和仓库的主要变化 |
| [开发交接](development-handoff.md) | 2026-11-10 当前上线状态、仓库整理、未解决项与下次接续顺序 |
| [深度路线图](depth-roadmap.md) | 4.1–4.4 目标、实现状态与第 8 节复审清单 |
| [复审操作指南](review-guide.md) | 逐项说明 effect/omen 标签、泛称组、异说与路线点位怎么复核 |
| [专题路线评估简报](route-feasibility-brief.md) | 供独立评估：现有路线事实、可用数据、候选形态、约束与评估问题 |
| [路线评估数据包](route-evaluation-packet.md) | 按 A–H 汇总的摘录，供外部模型评估路线实现 |
| [开屏落墨评估](interactive-ink-assessment.md) | 四字动画期间允许用户落笔的可行性、阶段门控、风险与成本 |
| [内容盘点](content-coverage.md) | 十八篇覆盖、出处与待核状态；由`data/audit_shanhaijing.py`生成 |
| [内容与来源复核](editorial-review.md) | 人鱼共图、45条形貌复核、17项来源追溯及英文审校的实际范围 |
| [历史资产证据补录](asset-source-recovery.json) | 16项创建/派生记录的脱敏工具证据、摘要和匹配限制 |
| [数据契约](API_CONTRACT.md) | 当前内置 world 数据、静态构建与本地化边界；无运行时 API |
| [生图提示词模板](artwork-prompt-template.md) | 从生成记录抽出的统一风格模板、文件位置与落盘流程 |
| [数据维护](../data/README.md) | 各山经构建入口、批次内容模块和来源清单 |
| [前端脚本](../frontend/scripts/README.md) | 验收、预览、素材及字体工具分类 |
| [部署脚本](../deploy/README.md) | 静态部署包、一键 serve/copy 与打包入口 |

## 2026-10-28结构整理

- 素材工具集中到`frontend/scripts/assets/`，字体工具集中到`frontend/scripts/fonts/`，浏览器验收和预览入口保持稳定。
- 历史课程材料保存在`docs/coursework/`；已停用的中山初始计划和Natural Earth生成链经引用复核后删除。
- 分批数据模块仍被主构建器导入；Java服务仍被开发代理使用；原图、影印页和来源哈希承担复现职责，均保留。独立 FastAPI/PostGIS 原型已在 2026-11-05 从主分支移除，历史课程资料引用清理前版本。
- 本地临时探针移入被忽略的`output/diagnostics/`，未删除任何过程文件。发布资源清单继续排除重复原图。

根目录的本地历史交接、`output/`、依赖、构建产物及环境配置不上传GitHub；`docs/development-handoff.md` 是可提交的精简开发交接。

2026-10-28 的删除清单为中山初始计划脚本、旧 Natural Earth 生成脚本与配置，以及当时停用的 `relief.webp`。当前各山经的批次模块与新 Natural Earth v5.1.2 构建链继续保留。

<details>
<summary>历史课程材料</summary>

[课程报告](coursework/课程报告.md) · [答辩流程](coursework/答辩演示流程.md)

保留历史记录，不作为当前操作说明。

</details>


## 轻量检出、缓存与原图分发（2026-11-05）

入口与命令见[数据维护](../data/README.md#轻量检出与原图分发)。原图留在仓库；不重写历史。CI完整审计保持完整素材和`fetch-depth: 0`，浏览器矩阵按套件补齐所需母图和影印，不删减原有断言。所有套件继续共享同一提交的构建产物。

`c6ca994`真实远端轻量副本实测：受管文件由2211个、1459.99 MiB降至1553个、343.57 MiB（保留默认校验需要的五张母图及全部来源元数据）。实际clone+checkout为257.84秒，未做受控完整克隆对照，不承诺网络提速。1232个发布文件中1226个字节相同，其余6个仅换行不同；数据解析一致。默认数据/发布检查及北山、中山的原图和影印检查通过。

[缓存试验42052512655](https://github.com/hyc1005/mythmap/actions/runs/42052512655)每类3样本，准备耗时含安装或恢复、系统依赖和启动；单位秒：

| 方案 | 冷准备三次 | 缓存命中三次 | 中位数收益 | 决定 |
| --- | --- | --- | --- | --- |
| Chromium only-shell | 21.091 / 25.691 / 19.869 | 19.808 / 22.210 / 17.748 | 1.283 | 不缓存二进制 |
| WebKit | 74.182 / 63.431 / 63.960 | 48.416 / 39.989 / 68.515 | 15.544 | 保留WebKit缓存 |
| Chromium全包 | 26.979 / 24.214 / 23.254 | — | only-shell省3.123 | CI使用only-shell |

冷缓存保存耗时中位数：Chromium3.904秒、WebKit3.988秒。WebKit命中时间波动明显，三样本只支持当前配置选择，不能承诺整轮CI提速；继续观察后续运行。原始15条测量在试验Actions产物中（14天），本表保留长期摘要。系统依赖每次仍安装。

缓存键包含OS、架构、Ubuntu版本、Playwright精确版本和格式版本，无宽泛回退。可信main准备任务保存WebKit及共享ffmpeg目录，矩阵只恢复；版本升级将切换精确键并冷安装。安装命令每次仍执行以校验二进制和安装系统库。此轮没有升级Playwright依赖。npm下载缓存保留，不缓存`node_modules`、测试输出或会话数据。Chromium使用默认无头模式，若未来指定Chrome channel或有头模式，须同步调整安装方式。

[分发验证42052561847](https://github.com/hyc1005/mythmap/actions/runs/42052561847)完成678文件、18包的包级/文件级摘要检查、独立轻量副本恢复及全量资产审计，并核对21个Release文件的远端摘要及大小后发布。还验证了路径越界、错误摘要和本地冲突保护。可选下载不改变素材原许可；当时的16项创建记录缺口已在2026-11-06另行[补定位](asset-source-recovery.json)，具体模型、部分参考附件和历史条件仍有限制。

参考：[Playwright缓存说明](https://playwright.dev/docs/ci#caching-browsers)、[Chromium无头安装](https://playwright.dev/docs/browsers#chromium-headless-shell)。


主分支首次集成运行42053881600已观察到15个浏览器任务的检出＋补图耗时12–30秒、中位16秒；前一成功运行42034369001为42–374秒、中位46秒。不同runner和网络条件，属于运行观测。WebKit矩阵实际命中精确键，未重新下载WebKit；main缓存压缩大小101443727字节（约96.7MiB）。本机公开下载art-brand组并在当前main轻量副本恢复2个缺失源文件，摘要检查通过。


集成验收完成：`7b5d224`的[CI42053881600](https://github.com/hyc1005/mythmap/actions/runs/42053881600)首次17项全部成功，Pages部署7578234189同SHA成功。正式站入口、主JS、完整world JSON和人鱼共图与该次CI验证包逐字节一致；本地构建的入口指纹不同，因此线上对照使用实际CI发布包。


## 界面精修约定（2026-11-06）

保留现有纸色、木刻插画、主布局、字体及生僻字补字链。使用原有React/CSS，不新增UI库、Tailwind、Motion、字体或插画。主题变量共用到body portal弹层，组件状态按现有容器限定，不全局重置地图控件。

实施顺序：控件/焦点/状态 → 章节/搜索键盘 → 筛选摘要/卡片/阅读 → 地图/手机/全站回归。按钮≥44px，装饰线与交互边界区分；新局部反馈150–220ms、位移≤8px，减少动态效果关闭；原有文字渐显不叠加效果。主图谱保持4/3/2列与12/24分页，搜索排序、阅读恢复、数据结构、URL和存储不变。

参考公开设计：[BoardUI](https://www.boardui.com/)（状态/间距）、[HeroUI](https://heroui.com/en/docs/react/getting-started)（键盘/弹层）、[Bencho](https://bencho.dev/)（克制的目录/状态反馈）、[Watermelon](https://ui.watermelon.sh/animated-components)（折叠组织）、[beUI Pro](https://pro.beui.dev/components)（仅公开信息层次参考）、[Libraries.dev](https://libraries.dev/)（真实加载状态过渡思路，本轮不安装效果包）。不复制付费或授权未明确的源码。

新增界面文案同步中英字典及规范化LF摘要；不修改古籍译文。新增JS/CSS gzip预算25KiB；按既有双语六尺寸、两浏览器设计与业务检查验收，发布同一已验证构建。

界面提交 `db7798b` 的 WebKit 检查先后在章节历史点击和引导重放超时，两次部署均跳过，超时根因尚未确认。随后为两套脚本补充页面与字体就绪同步及失败诊断，沿用原断言和超时。Chromium 与 WebKit 本地复验通过。后续提交 `f03519a` 的完整 CI 17 项全部通过，Pages 部署 `7581841679` 使用同一提交，线上抽查五个文件与 CI 构建包逐字节一致。[首轮及重试记录](https://github.com/hyc1005/mythmap/actions/runs/42072802957) · [发布验证](https://github.com/hyc1005/mythmap/actions/runs/42080800033)
