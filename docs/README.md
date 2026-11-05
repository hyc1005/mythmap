# 文档导航

当前网站的启动、构建与发布入口在根目录[中文README](../README.zh-CN.md)及[English README](../README.md)。

| 文档 | 用途与维护方式 |
| --- | --- |
| [更新记录](../CHANGELOG.md) | 按发布批次记录站点和仓库的主要变化 |
| [内容盘点](content-coverage.md) | 十八篇覆盖、出处与待核状态；由`data/audit_shanhaijing.py`生成 |
| [内容与来源复核](editorial-review.md) | 人鱼共图、45条形貌复核、17项来源追溯及英文审校的实际范围 |
| [API与数据约定](API_CONTRACT.md) | 当前world数据、本地Java服务及独立FastAPI/PostGIS原型的边界 |
| [数据维护](../data/README.md) | 各山经构建入口、批次内容模块和来源清单 |
| [前端脚本](../frontend/scripts/README.md) | 验收、预览、素材及字体工具分类 |
| [Java开发服务](../backend-java/run.ps1) | 开发模式的可选只读 `/api/world` 服务 |

## 2026-10-28结构整理

- 素材工具集中到`frontend/scripts/assets/`，字体工具集中到`frontend/scripts/fonts/`，浏览器验收和预览入口保持稳定。
- 历史课程材料保存在`docs/coursework/`；已停用的中山初始计划和Natural Earth生成链经引用复核后删除。
- 分批数据模块仍被主构建器导入；Java服务仍被开发代理使用；原图、影印页和来源哈希承担复现职责，均保留。独立 FastAPI/PostGIS 原型已在 2026-11-05 从主分支移除，历史课程资料引用清理前版本。
- 本地临时探针移入被忽略的`output/diagnostics/`，未删除任何过程文件。发布资源清单继续排除重复原图。

本地交接文档、`output/`、依赖、构建产物及环境配置不上传GitHub。

2026-10-28 的删除清单为中山初始计划脚本、旧 Natural Earth 生成脚本与配置，以及当时停用的 `relief.webp`。当前各山经的批次模块与新 Natural Earth v5.1.2 构建链继续保留。

<details>
<summary>历史课程材料</summary>

[课程报告](coursework/课程报告.md) · [答辩流程](coursework/答辩演示流程.md)

保留历史记录，不作为当前操作说明。

</details>
