# 山海寻踪

一卷山海，七章神话。以纸本版画风格呈现中国古代神话，通过地图、动画和异兽插画，探索《山海经》中的世界。

**[在线体验 →](https://hyc1005.github.io/mythmap/)** · [GitHub 仓库](https://github.com/hyc1005/mythmap)

## 可以看什么

- **神话地图**：从盘古开天序章出发，浏览七章故事、地点与神域。
- **故事动画**：支持播放、暂停、重播和全屏展示。
- **异兽谱**：浏览 32 项异兽，按名称、形貌或篇目查找。
- **原文出处**：点击地图地点或异兽卡片，查看描述和所引篇章。

打开网页即可体验，支持电脑和手机。图面表达篇目方位与叙事关系，不表示真实距离或精确年代；插画是依据原文的艺术解释。

---

## 开发与维护

以下内容供本地运行、部署和数据维护使用。

### 技术与目录

前端使用 React、Vite、OpenLayers，动画使用 Remotion。在线版由 GitHub Actions 构建、GitHub Pages 托管，使用内置数据，无需后端或数据库。

| 目录 | 用途 |
| --- | --- |
| `frontend/src/` | 页面组合、动画与样式 |
| `frontend/src/components/` | 地图、详情、时间轴和异兽谱 |
| `frontend/public/data/` | 网站数据与发布素材 |
| `frontend/artwork-source/` | 插画原图与备用素材 |
| `frontend/scripts/` | 布局与叙事验证 |
| `data/` | 图谱维护工具与原始输入 |
| `docs/` | 演示流程与历史课程资料 |

### 本地运行

需要 Node.js 22 或更新的兼容版本。在 `frontend/` 目录执行：

```bash
npm ci
npm run dev -- --host 127.0.0.1
```

打开 [本地开发页面](http://127.0.0.1:5173/#world)。开发和生产模式默认均使用内置数据，无需启动后端。

如需接入外部服务，在 `frontend/.env.local` 设置 `VITE_API_BASE_URL`；只有显式配置时才请求该服务的 `/api/world`，失败时回退到内置数据。服务需允许网站来源的跨域请求；地址会公开到构建产物中，不能包含密钥。配置示例见 `frontend/.env.example`。

### 构建与验证

在 `frontend/` 目录执行，按线上 `/mythmap/` 路径预览：

```bash
npm run build -- --base /mythmap/
npm run preview -- --host 127.0.0.1 --port 4173 --base /mythmap/
```

打开 [本地生产预览](http://127.0.0.1:4173/mythmap/)。保持预览服务运行，在另一个 PowerShell 终端的 `frontend/` 目录执行：

```powershell
$env:ATLAS_URL = 'http://127.0.0.1:4173/mythmap/'
npm run verify:layout
```

`verify:layout` 检查五种视口、动画布局、原生与模拟全屏，以及详情遮挡和焦点恢复。`npm run verify:narrative` 还检查叙事、素材与时间轴，耗时较长；完整长测试尚未全部验收。截图保存在 `output/qa/`。

发布前复查电脑与手机上的动画、地图全屏、异兽搜索、详情关闭和出处链接，并确认刷新正常、图片无 404。

### GitHub Pages 部署

工作流位于 `.github/workflows/deploy-pages.yml`。在仓库 **Settings → Pages** 中选择 **GitHub Actions**；推送到 `main` 的前端或工作流修改会自动构建并发布。文档修改不会触发网页部署。

工作流自动处理 Pages 子路径并发布 `frontend/dist/`，无需手动提交构建产物。部署结果可在仓库 Actions 页面查看；回退使用 `git revert` 后推送。

### 数据与插画维护

- 主要数据位于 `frontend/public/data/`：`myth-world.json` 及 `atlas/` 下的 `catalog.json`、`story-animations.json`、`kuafu-journey.json`。
- 出处与素材核对使用 `atlas/review.json`、`atlas/artwork-manifest.json`；原图保存在 `frontend/artwork-source/`。
- `data/build_myth_atlas.py` 可能覆盖人工审核数据，运行前核对来源和 Git 差异。
- 可选静态地图由 `data/render_myth_atlas.py` 生成，需要 Pillow、pyproj 和指定的 Windows 字体，输出到 `output/atlas/`。
- 图谱工具的使用与局限见 `data/README.md`。旧版后端、数据库和课程原型可从仓库 `main` 的历史版本查阅；精简分支不包含这些运行目录。

`node_modules/`、`frontend/dist/`、`output/` 和本地环境配置均由 Git 忽略。
