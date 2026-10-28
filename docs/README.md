# 文档导航

当前网站的启动、构建与发布入口在根目录[中文README](../README.zh-CN.md)及[English README](../README.md)。

| 文档 | 用途与维护方式 |
| --- | --- |
| [内容盘点](content-coverage.md) | 十八篇覆盖、出处与待核状态；由`data/audit_shanhaijing.py`生成 |
| [API与数据约定](API_CONTRACT.md) | 当前world数据、本地Java服务及独立FastAPI/PostGIS原型的边界 |
| [数据维护](../data/README.md) | 各山经构建入口、批次内容模块和来源清单 |
| [前端脚本](../frontend/scripts/README.md) | 验收、预览、素材及字体工具分类 |
| [后端说明](../backend/README.md)、[数据库说明](../database/README.md) | 可选原型、测试与导入；静态网页不依赖它们 |
| [课程报告](coursework/课程报告.md)、[答辩流程](coursework/答辩演示流程.md) | 历史课程材料，保留当时记录；不作为当前操作说明 |

## 2026-10-28结构整理

- 素材工具集中到`frontend/scripts/assets/`，字体工具集中到`frontend/scripts/fonts/`，浏览器验收和预览入口保持稳定。
- 已停用的中山初始计划和Natural Earth底图配置归档到`data/archive/`；课程材料归入`docs/coursework/`。
- 分批数据模块仍被主构建器导入；Java服务仍被开发代理使用；原图、影印页和来源哈希承担复现职责，均保留。
- 本地临时探针移入被忽略的`output/diagnostics/`，未删除任何过程文件。发布资源清单继续排除重复原图。

本地交接文档、`output/`、依赖、构建产物及环境配置不上传GitHub。
