# 开发交接：山海寻踪

更新：2026-11-10。线上基线为 `2943be2`；本地整理提交 `c4aad1f` 已推送，CI 运行 [42729532502](https://github.com/hyc1005/mythmap/actions/runs/42729532502) 正在收尾，部署成功后以新 SHA 为准。

## 当前已上线

- 远端 `main` 为 `c4aad1f` 之后的文档提交（以 `git ls-remote origin main` 为准）；线上仍可能是 `2943be2`，以 Pages 实际部署为准。
- `2943be2` 已包含：专题路线第二版、阅读优先抽屉、搜索顶部锚定 / 滚轮转发、开屏红墨。
- 搜索修复运行 [42629992694](https://github.com/hyc1005/mythmap/actions/runs/42629992694) 27 个 Job 全绿；线上 CSS 已确认 `margin:8svh auto 0`。
- 站点是纯静态构建：没有运行时世界数据 API，没有后端服务，没有数据库。
- 专题路线 4 条：同一灾异不同范围（8 站）、服佩辟邪（4 站）、同名异物（5 对）、山神形貌公式（2 对）；共 19 个站点、26 个条目引用。
- 详情抽屉顺序：插画 → 篇名 → 原文 → 白话 → 校读与依据 → 来源与说明；证据与形态默认折叠。
- 全站搜索：顶部 8svh 锚定；输入框/标题/工具栏滚轮转发到结果列表。
- 开屏：移除 ghost 残影；红墨保留红色并提亮到 `#c73a20`，不染黑。

## 本次推送状态（2026-11-10）

- `c4aad1f` 已推送到 `main`，运行 [42729532502](https://github.com/hyc1005/mythmap/actions/runs/42729532502) 已触发；后续文档提交只改 `docs/`，不触发部署。
- 截至交接时 26 个 Job 中 25 个完成且无失败；`verify / Browser webkit / southern-cards` 仍在长跑（已知 WebKit 偶发长尾），deploy 尚未确认。不要把这轮写成已部署，等运行结束后以 Pages SHA 为准。
- 若该 Job 最终失败，按既有规则只重跑该 Job，不取消其他已通过结果；若超时，记录时间与 Job URL。

## 本次整理（2026-11-10）

- **移除可选 Java 后端**：删除 `backend-java/`、Vite `/api` 代理、`VITE_API_BASE_URL` 运行时请求、部署路径过滤和相关 README/文档引用。`frontend/src/App.jsx` 只读打包的 `myth-world.json`；`world-validation.js` 保留给 `verify-data` 使用。
- **本地清理**：删除根目录与 `output/` 的旧交接文档、下载的线上 bundle、CI 日志和早期开屏迭代截图；保留当前 QA 截图、开屏实验目录（验证脚本会写入）和部署包。
- **仓库结构**：根目录只保留站点、数据、文档、部署脚本与仓库元文件；可选后端不再占位。
- **生图提示词**：新增 [生图提示词模板](artwork-prompt-template.md)。仓库没有单一模板文件，公共风格前缀存放在 `frontend/artwork-source/<篇目>/generation.json`、`entities-generation.json` 与 `frontend/public/data/atlas/artwork-manifest.json` 的 `initial_prompt`；模板文档是抽取整理，并说明落盘流程。
- **部署包**：新增 `deploy/` 源码与 `output/deploy/mythmap-static-20261110.zip`（188.7 MB，1237 个文件，SHA-256 `6ca4fc350d913ab4e1f0df1db7c04c726f2c2b7b0a91d51178bf4e0bc666829b`，`SHA256SUMS` 全量校验）。包内 `Deploy.ps1` / `deploy.sh` 支持 serve 与 copy，检查环境、完整性、端口/目标目录并要求确认。
- **文档**：`CHANGELOG.md` 补本会话详细记录；`docs/API_CONTRACT.md` 改为静态数据契约；`docs/README.md` 增加生图模板入口；课程报告中的 Java 说明标为历史。

## 仓库结构

| 路径 | 职责 |
| --- | --- |
| `frontend/` | React/Vite 站点；`src` 界面与本地化，`public/data` 运行数据与发布图 |
| `frontend/artwork-source/` | 原图、生成记录、提示词与复现材料（体积最大，勿随意移动） |
| `data/` | 分卷构建器、原文快照、来源与审核记录 |
| `docs/` | 交接、路线图、复审、数据契约、生图模板、清单与历史课程材料 |
| `deploy/` | 静态部署包生成器与一键脚本（不包含构建产物） |
| `.github/workflows/` | 构建、验证、Pages 部署 |
| `output/` | 本地忽略：QA 截图、部署包、实验目录；不提交 |

## 未解决与待解决

1. **复审第 6 项免责文案**：抽屉与路线区块“自动抽取/编排”的边界说明仍未定稿；不要把它写成已经完成。
2. **差评反馈机制**：已评估，暂不实现。若以后恢复，需先明确“点击时一次 POST”是否算违反“无运行时请求”，并解决图片版本绑定；不要把计数当自动重画阈值。
3. **生图**：模板已抽出，但历史每条提示词仍是各自记录；具体模型名、参考图权利和逐条审校并非全部可考。新图必须写 `review_note`，区分原文/郭注/艺术解释。
4. **部署包**：当前是 `base=/` 的静态包，适合根路径或复制到静态服务器；正式 GitHub Pages 仍走 Actions。远端一键发布需要凭证/主机信息，未纳入包内，避免脚本携带密钥。
5. **CI 稳定性**：WebKit 偶发超时/崩溃仍有历史记录；工作流已有单次新浏览器重试，不把重试当修复。最近一次 27 Job 全绿。
6. **数据缺口**：45 条形貌分类仍 `unresolved`，119 个条目使用共享占位图；这是内容工作，不是页面 bug。
7. **性能**：`app-entry` 约 8.9 MB raw / 1 MB gzip，主要来自静态 world 数据；未做拆包。25 KiB gzip 预算只是文档约定，没有强制脚本或按功能记账。
8. **完整验证**：`verify-locale` 完整逐条模式、低端 Android/Safari 真机、GPU/滤镜开销没有在本轮全部复跑；不要把局部通过写成全量真机通过。
9. **本地秘密**：`frontend/.env.local` 含本地地图 key，已被 Git 忽略；不要提交，也不要写进部署包。

## 下次接续顺序

1. 先看 `git status --short`、本文件与 `CHANGELOG.md`，确认没有把 `output/`、`dist/`、`.env.local` 或部署包提交。
2. 若要发布站点：在 `frontend/` 构建并跑相关验证，推送 `main`；GitHub Actions 从源码构建，不使用本地 zip。
3. 若要交生图：把 `docs/artwork-prompt-template.md` 与对应 `generation.json` 一起给模型；新图用 `-vN` 文件名，更新 manifest 与素材清单。
4. 若要改路线：只改 `guide-routes.json` 的文字与 `entryId/withId`，不要把原文复制进路线；`verify-bestiary` 的对照/引文/反筛选断言必须保留。
5. 若要动部署包：在 `deploy/` 改脚本后运行 `powershell -File deploy/make-package.ps1`，再用包内 `Deploy.ps1 -Mode serve` 和 `-Mode copy` 各测一次。

## 验证命令

```powershell
cd frontend
npm run build -- --base /mythmap/ --logLevel error
node scripts/verify-data.mjs
npm run verify:assets
node scripts/with-preview.mjs --base /mythmap/ -- node scripts/verify-bestiary.mjs
node scripts/with-preview.mjs --base /mythmap/ -- node scripts/verify-search.mjs
```

部署包：

```powershell
powershell -ExecutionPolicy Bypass -File deploy/make-package.ps1
powershell -ExecutionPolicy Bypass -File output/deploy/mythmap-static/Deploy.ps1 -Mode serve -Port 8091 -Force
```

## 边界

- 不新增运行时依赖、后端、数据库或页面加载时的第三方脚本。
- 不提交 `frontend/dist/`、`output/`、`node_modules/`、`.env.local` 或部署 zip。
- 不把比较记述/郭注混入正文；不改写原文；不把艺术解释写成原文形貌。
- 不把未执行的检查写成“已验证”；失败的重试不写成根因已修复。
