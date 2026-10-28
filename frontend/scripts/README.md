# 前端脚本索引

网站运行代码在`src/`；此目录只放验收、预览与素材维护工具。Node验收命令从`frontend/`运行，Python生成命令从仓库根目录运行。

## 日常验收与预览

| 入口 | 职责 |
| --- | --- |
| `with-preview.mjs` | 启动独立预览，传入`ATLAS_URL`，退出时关闭并检查端口 |
| `verify-data.mjs`、`verify-cache.mjs`、`verify-publish.mjs` | 引用完整性、缓存行为和发布资源范围 |
| `verify-bestiary.mjs` | 短名、同名分组、组合筛选、原文保留、字体和双语布局 |
| `verify-reading.mjs`、`verify-resume.mjs`、`verify-reader.mjs` | 已读收藏、续读与原文阅读 |
| `verify-search.mjs`、`verify-place-search.mjs` | 全站搜索、别名、地点资料及返回状态 |
| `verify-design.mjs`、`verify-narrative.mjs` | 布局、全屏、插画、完整故事时钟与叙事 |
| `verify-geography.mjs`、`verify-map-frame.mjs` | 地理证据、底图恢复与画布结构 |
| `verify-guided-tour.mjs`、`verify-onboarding.mjs`、`verify-exploration.mjs` | 游历、首次引导和探索流程 |
| `verify-nanshan.mjs`、`verify-xishan*.mjs`、`verify-beishan.mjs`、`verify-dongshan.mjs`、`verify-zhongshan.mjs` | 各山经的内容与交互回归 |
| `verify-repairs.mjs`、`verify-discovery.mjs`、`verify-ux.mjs`、`verify-playback-speed.mjs` | 修复项、发现入口、操作与播放倍率 |
| `mock-tianditu.mjs` | 浏览器测试的模拟瓦片助手；不是线上底图 |
| `publish-files.mjs` | Vite发布资源清单助手；不是独立验收命令 |

```bash
npm run build -- --base /mythmap/
node scripts/with-preview.mjs --base /mythmap/ -- node scripts/verify-bestiary.mjs
```

一般浏览器脚本使用`ATLAS_BROWSERS=chromium,webkit`；少数历史脚本仅支持Chromium，具体以脚本和Actions矩阵为准。QA保存在被Git忽略的`output/qa/`。

## 素材工具：assets/

- `prepare-nanshan-artwork.py`：导出各山经已审核插画；使用`--chapter`选择篇目。
- `prepare-refined-artwork.py`：从保留原图生成精修插画与地图小图标。
- `optimize-assets.py`：生成优化图像及对应清单。
- `prepare-geography.py`：保留的Natural Earth离线地形资产工具，配置快照归档在`data/archive/geography-basemap.json`，当前线上底图使用天地图。

例如：`python frontend/scripts/assets/prepare-nanshan-artwork.py --chapter zhongshan`。原图和提示词位于`frontend/artwork-source/`，不作为临时缓存删除。

## 字体工具：fonts/

- `subset-title-font.py`、`subset-rare-font.py`：标题与罕字基础子集。
- `supplement-title-font.py`、`supplement-beishan-extb.py`：北山经补字。
- `supplement-dongshan-fonts.py`、`supplement-zhongshan-fonts.py`：东山经、中山经补字。
- `supplement-bestiary-font.py`：从短名、限定信息与界面字串检查并补足异兽谱字形。

例如：`python frontend/scripts/fonts/supplement-bestiary-font.py`。这些维护工具可能下载授权字体；常规网站构建直接使用仓库中的字体，不执行生成工具。授权文件随字体保存在`frontend/public/fonts/`。

## 本地诊断

临时探针与中间结果放`output/diagnostics/`；不进入Git，也不参与网站构建。2026-10-28的结构整理仅移动保留原文件，没有删除诊断记录。
