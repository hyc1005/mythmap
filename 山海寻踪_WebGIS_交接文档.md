# 山海寻踪 WebGIS 交接文档

更新日期：2026-10-03
用途：下一会话先读当前状态、验收结果和待办。部署与 GitHub 上传的完整操作计划统一放在 README.md，不再维护重复计划文档。

## 当前版本与用户已确认方向

- 前端是 React 19、JavaScript/JSX、Vite 与一个 OpenLayers 示意地图。普通页面以地图为主体，桌面左侧章节故事、右侧地图与时间轴；手机故事列表默认折叠。
- 首页导语、英文眉题和导航宣传副标题已删除。保留“山海寻踪”；导航为“地图”“异兽谱”“读图与依据”，使用纸色、墨色、细线和克制朱红。
- 读图说明集中在异兽谱之后并常展开。地图内部只保留方位、符号与短状态；原文、出处和插画仍在详情抽屉展示。
- 时间轴是 00 盘古序章 + 01–07 七章。启用的七段动画为盘古、女娲、燧人、夸父、精卫、大羿、大禹；第六、七章动态已停用，不能再按旧记录要求每章都加动画。
- 女娲、燧人、精卫、大羿、大禹由 StoryAnimation.jsx 绘制在地图矢量层；夸父由 KuafuJourney.jsx 独立绘制；盘古由 PanguOpening.jsx 驱动 Remotion Player。旧 NuwaCreation.jsx 已无引用并删除。
- 1×/2× 作用于现有时钟；暂停切倍率不继续播放，重播保留倍率，换故事/章节恢复 1×。第三章默认夸父，可切换精卫。只有夸父、精卫保留跟随镜头入口。

## 本轮全屏跳动修复

问题来源：全屏底栏原先自动增高，预览卡与动画控件共用 flex 容器。预览出现/消失或动画阶段文字换行会改变底栏高度，挤压地图；ResizeObserver 随后调整地图尺寸和镜头，可能让鼠标失去命中目标，再触发卡片关闭，形成反馈跳动。

当前修复：

1. 全屏继续采用“顶部工具带—中间画布—底部控制带”三行布局。
2. 底栏使用稳定的明确高度，桌面/窄横屏 126px、手机竖屏 154px；内部划分播放区与一直预留的地点预览区。
3. 动画组件的 controlContainer portal 只挂载到播放区；预览卡挂载到独立 fullscreen-preview-slot。加载、暂停、播放完成及阶段文案变化不会增高底栏。
4. 阶段文案单行省略；有限高度的播放区可内部滚动。预览显示名称与操作按钮，长说明仍从原文详情查看。
5. 地图镜头依据中间画布的实际尺寸。主动展开地图工具仍按用户要求推动布局，这是主动操作的预期变化。

涉及 App.jsx、myth-world.css、verify-narrative.mjs。验证新增动画推进时画布 x/y/width/height 稳定断言及反复悬浮的稳定断言（允许 1px 舍入误差）。

## 动画与素材的当前实现

- 燧人使用六帧整合图集 animations/suiren-after-fire-v3.png。人物、柴堆、火均来自图集，不再叠独立柴堆或火焰；旧素材及修复前备份保存在 frontend/artwork-source/archived/，其中 suiren-after-fire-v2-original.webp 用于对照恢复。
- suiren-after-fire-v2.webp 与 original 版本经 SHA-256 比对完全相同，已删除重复文件；旧导出与当前来源/路径同步到 artwork-manifest.json。
- 大羿时序为 6.5 秒放箭、7.6 秒命中、9.2 秒进入后续展示。同一个太阳对象在命中后锁定坐标，受击序列结束持续保持裂纹终帧；不恢复普通太阳、不漂移、不创建重复太阳、不定义最终剩余太阳数量。重播清除旧受击状态。
- 大禹局部洪水→疏导→水流→退水，依据《淮南子·本经训》“疏三江五湖，注之东海，以利黔首”。不画真实巡行路线、不表示洪水完全退尽。
- 盘古 30fps、390 帧、13 秒，非循环；全屏等比完整显示，结束停在末帧，静态图供减少动态效果和加载失败时回退。
- 夸父河/渭处于同一饮水阶段，止于“大泽未至”，杖化邓林；不添加饮水先后或河道干涸。
- 精卫飞行/投放/返程为叙事示意，不表示东海已经填平。动画图解码成功才推进时钟，详情或后台暂停、重试及减少动态效果行为沿用既有实现。

## 文件整理结果与边界

- 删除无引用的 NuwaCreation.jsx，以及 atlas.css、attribution.css、mythic.css、story-scene.css、style.css。当前页面的主样式只有 myth-world.css。
- 删除可重新生成的旧静态地图 maps/、layers/ 和旧 public render-manifest.json，以及未使用的 ink-stamp.svg 和重复的燧人 v2 WebP。
- 静态地图原始章节插画迁至 frontend/artwork-source/atlas-illustrations/；退役角色/特效参考素材迁至 artwork-source/archived/。保留的源图有生成、风格参考或恢复用途，不进入网站部署。
- data/render_myth_atlas.py 改为从源图目录读取，输出到 output/atlas/；manifest、catalog 的可选导出路径及相关旧后端测试同步。导出测试需先生成 output/atlas，未生成时明确跳过。
- 调试/验收截图、缓存和生成日志在本轮验收结束后清理，output、dist、node_modules、本机环境配置均不提交到 Git。
- backend-java 保留可选 /api/world；backend、database、data 来源快照与维护脚本有独立功能或来源追溯用途，保留原目录。静态 Demo 不部署它们。
- 网页 public 素材由约 230.5 MiB 降至约 165.1 MiB（约减少 28%）；仍以高分辨率 PNG 为主，源图被移出 public，不等于图像已经压缩优化。
- 生产版默认使用内置数据并不请求 API。需要独立 API 时设置公开的 VITE_API_BASE_URL；开发版仍支持本机 Java 代理。

## 验收结果与已知问题

- 开发版布局专项：通过。覆盖 1920×1080、1366×768、1280×720、390×844、844×390，七段动画、神域/异兽、地图工具、地点预览、详情、原生/模拟全屏、动画播放及反复悬浮时画布尺寸稳定。
- 生产构建：通过，frontend/dist 由 Vite build 生成。
- 生产预览专项：通过。在 http://127.0.0.1:4173 静态生产预览复查五种视口和七段动画，图层、预览、详情及原生/模拟全屏检查通过；播放与反复悬浮不改变画布边界。
- 最终素材路径检查：132 条运行时引用与 103 条 artwork manifest 目标路径均存在；修改后的三个 Python 维护/测试文件语法解析通过。
- 此前完整 verify-narrative.mjs 运行到夸父专项后通过部分回归，后续长时间没有输出，被中止；不能把该次运行登记为“完整通过”。脚本后半段用虚拟时钟逐帧运行多故事、多视口并大量截图，定位耗时阶段需要增加逐场景进度和拆分执行入口。
- 原生全屏的浏览器物理 Esc、触屏浏览器工具栏动态变化以及目标上线网络速度仍建议真实设备人工复查，自动布局检查不替代这些环境。

## 部署准备阶段补查与修复（2026-10-03）

- /mythmap/ 子路径下的场景、图集、地图底图、图标和详情图片统一通过 assetUrl 处理，避免仅设置 Vite base 后运行时图片仍请求网站根目录。
- 全屏切章及 resize 不再触发普通页面 scrollIntoView，防止后台页面滚动及退出全屏时位置变化。
- 详情抽屉加入 Tab/Shift+Tab 焦点循环；全屏焦点初始化避开已打开抽屉，防止键盘焦点被地图抢走。
- 可选 API 验证必要数组及章节 ID/顺序，不完整数据保持使用内置数据。
- 子路径生产构建通过；http://127.0.0.1:4174/mythmap/ 的布局专项通过，覆盖五种视口、七段故事、原生/模拟全屏、图层、工具、预览、详情焦点及背景滚动稳定；检查同源资源 HTTP 错误。
- 长叙事回归增加逐故事与视口进度日志。完整长测试仍未全部通过，当前不能把专项结果等同完整叙事通过。
- 图片压缩以外的建议：优先拆分长测试并接入 CI；实际触屏设备核对底栏滚动、物理 Esc、后台恢复和减少动态效果；可选 API 后续增加失败/异常结构专项覆盖。没有发现新的专项布局阻塞项。

## 下一步建议与优先级

1. **持续发布质量：**GitHub Actions 构建与 Pages 发布已配置；建议后续在发布前增加独立的浏览器快速回归，覆盖首页、素材加载、全屏及详情焦点。完整长测试先拆分再接入 CI，避免构建长期等待。
2. **优先优化图片加载：**为实际详情/异兽图生成适当分辨率的 WebP 发布版本，保留源 PNG；逐张更新引用和 manifest，验证透明边、版画细节与移动端效果。当前 165 MiB 是全站资源总量，不是首屏同时下载量，但移动网络仍可能感到慢。
3. **梳理完整验证耗时：**将数据校验、布局、加载失败、故事时序分段执行；增加明确章节/故事加载同步与阶段日志，给真正等待设限。布局专用入口已经提供，避免用长时间无输出推断页面失败或脚本完成。
4. **真实设备复查：**Chrome/Edge 全屏、物理 Esc、详情关闭焦点回归，手机竖/横屏、减少动态效果、后台恢复。优先根据实际使用反馈调整底栏滚动与短地图空间。
5. **继续复核来源与空间语义：**有图不等于有可靠点位，异兽同名异篇保持不同 ID；重要位置以原文和稳定地点关联判断，争议解释继续保留待核验状态。

## Git 与部署状态

公开仓库为 https://github.com/hyc1005/mythmap，origin 已配置，main 已上传。提交者使用 hyc1005 / 用户提供的邮箱。Pages Source 已设置为 GitHub Actions，workflow 自动构建 frontend/dist 后发布，不需要 Vercel。Demo 已发布：https://hyc1005.github.io/mythmap/ 。首次 Actions 运行 37096855074 成功，总耗时 41 秒。线上未登录 Chromium 核对首页、女娲动画和原生全屏通过，未捕获页面异常或 HTTP 400+ 素材响应；五视口完整布局专项使用本地同一子路径产物验证。首次发布提交为 331e0bd。

Vite base 与运行时 /data 地址已通过 asset-url.js 统一适配项目子路径；README 包含实际仓库、部署、更新和回退操作。文档变更不触发重复部署，可手动 Run workflow。

## 用户确认的内容与代码约束

- 文献边界：图面不是测绘地图，时间轴不是精确年代；原事件 geometry 为空时保持为空，布局坐标仅为叙事示意。
- 不将 08 大荒/海外重新加成第八时间阶段；作为空间/神域专题资料。第二章兄妹婚 archive 记录不重新放入正常地图故事。
- 32 条异兽按稳定 ID 与篇目关联；无可靠地点就留在谱录，不伪造地图坐标。“逐章显现”不表示异兽诞生年代。
- 插画只解释形象与动作，不能新增文献事实。地名/路线/中文 UI 用结构化数据和代码确定性绘制。
- 继续使用 JavaScript、React hooks、同一个 OpenLayers 实例。不要另建时钟、地图实例或通用状态框架。
- 保留本项目纸色/墨色/赭石/克制朱红；无需在线字体。窗口布局变化应观察实际画布，悬浮内容不能推动画布尺寸。
- build_myth_atlas.py 是早期维护工具，不要无审查覆盖人工修改后的 catalog/myth-world；使用前检查会覆盖哪些字段，并用 Git 核对差异。
- 只改必要文件，不新增泛化说明文档。生产产物通过 build 生成；素材来源和变更记录写进既有 artwork-manifest.json。

## 生图与美术统一规范（后续请严格遵守）

### 互动地图素材的标准风格

以已通过目视检查的透明素材作为主参考：

- `frontend/public/data/atlas/myth-icons/terrain/peak.png`：山体刻线与纸色/朱砂比例。
- `frontend/public/data/atlas/myth-icons/stories/nuwa-create.png`：人物线条、衣纹、面部和木版颗粒。
- 同类故事图可再参考 `nuwa-repair.png`、`ch03-banquan.png`、`ch04-dayi-shoots-suns.png`。
- 盘古全幅场景参考 `myth-icons/scenes/pangu-opening.png`；异兽参考相同目录中已有关联插画的兽图。

目标是“古代《山海经》图谱/粗粝木刻印图”，而不是现代奇幻概念图：黑褐/炭墨的有力刻线，线条略粗且带手刻不匀感；旧纸赭黄、米白留空；克制朱砂用于局部标记或少量衣饰；局部可用淡赭石。整体像粗糙古地图的木版印图，有纸纤维、墨色斑驳与边缘颗粒，不追求数码光滑。

### 不可混用的视觉类别

- 互动地图里的山体、人物、异兽和 hover 浮影要保持透明背景的木刻 cutout 风格，边缘干净；透明素材导出需检查 alpha，不要用一块带底色的矩形图盖住地图。
- `frontend/artwork-source/atlas-illustrations/01.png` 到 `07.png` 是章节总览/故事卷轴类别，部分采用更丰富的手绘矿物色与水墨场景。不要直接把这些大幅卷轴图当作新互动点位的风格模板；点位素材优先引用上面的透明木刻参考图。
- 山形模板只是淡墨装饰，不是“某座神山”的画面证据，不加题字、神名或交互热点。真正地点单独由带来源的点位数据表示。

### 生图工作流

1. 新插画使用内置 ImageGen；编辑既有素材时把已核准的透明木刻素材作为参考图，特别是对应角色的既有人物图，固定脸型、发式、服饰、身体形态与配色。不要每次只写文字重新抽样，导致同一女娲/黄帝/异兽换脸或服装。
2. 在提示词中明确：同一项目风格、透明背景（地图 cutout）、粗粝木刻/古籍插图、炭墨线、旧纸赭色、克制朱砂、无现代物件、无照片/3D/发光特效、无文字/标签/边框/地图线。
3. 以《山海经》原文描述决定异兽特征，证据不足就画克制剪影，不补足没有出处的角、翅膀、颜色或能力。故事插画只表现对应动作，不自行添加地名、因果关系或“看起来合理”的文献细节。
4. 不用 ImageGen 生成整张精确地图、地名或中文 UI。地图底纹/图层、节点、路线、题签和中文由现有代码及结构化数据确定性绘制；图片像素永远不能反推经纬度或拓扑关系。
5. 新素材加入后检查透明边、暗底、裁切、人物完整度、缩小到点位图标尺寸后的可辨性；更新 artwork manifest 的稳定 ID、destination、style/status、原文篇目/引文。
6. 每章至少保留一张通过检查的参考 PNG，下一章沿用，而不是每章更换绘画提示风格。生成后在实际网站里和地图纸纹、山形、文字卡同屏检查。

### 推荐提示词骨架

> Create one transparent-background cutout for the existing Shan Hai Jing atlas. Match the supplied approved reference image exactly: rough antique Chinese woodblock print, irregular charcoal-black carved outlines, worn parchment ochre and warm ivory, restrained cinnabar accents, visible print grain, hand-cut edges. Depict only [原文可支持的主体与动作], with the same established character design as [角色参考素材]. No text, calligraphy, labels, border, map, extra symbols, glow, gradient, photorealism, 3D, or modern objects. Keep the full silhouette inside generous transparent margins; preserve readable shape at small map-marker size.

提示词必须按具体对象改写，并把稳定角色参考图路径列明；不要只复制骨架里的英文泛化句子。

## 文件导航

| 内容 | 路径 |
|---|---|
| 页面/地图/时间轴/详情/全屏 | frontend/src/App.jsx |
| 唯一主样式与响应式 | frontend/src/myth-world.css |
| 盘古场景与时钟 | frontend/src/PanguOpening.jsx |
| 夸父场景与时钟 | frontend/src/KuafuJourney.jsx |
| 其余地图动画与太阳命中 | frontend/src/StoryAnimation.jsx |
| 运行时故事与地图数据 | frontend/public/data/atlas/catalog.json、frontend/public/data/myth-world.json |
| 动画时序、帧和锚点 | frontend/public/data/atlas/story-animations.json、atlas/kuafu-journey.json |
| 插画来源与复核 | frontend/public/data/atlas/artwork-manifest.json、atlas/review.json |
| 源图与修复前备份 | frontend/artwork-source/ |
| 叙事/全屏布局验证 | frontend/scripts/verify-narrative.mjs |
| 本地运行/GitHub 上传/Demo 部署 | README.md |
| 可选静态导出（生成后存在，不进 Git） | output/atlas/render-manifest.json |
