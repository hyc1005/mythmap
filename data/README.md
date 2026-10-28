# 数据维护入口

当前网页数据位于`frontend/public/data/`，此目录保存构建器、影印依据与审核清单，不是网页发布目录。原始经文、稳定ID、来源关联和图片审核记录需要一并保留。

## 当前山经构建器

所有命令从仓库根目录运行；只在需要更新相应内容时运行构建器。

| 篇目 | 主入口 | 核查记录 |
| --- | --- | --- |
| 南山经43段 | `build_nanshan.py`、`build_nanshan_reader.py`、`build_nanshan_entities.py` | `nanshan-edition-review.json`、`nanshan-entity-coverage.json` |
| 西山经82段 | `build_xishan.py` | `xishan-edition-review.json` |
| 北山经92段 | `build_beishan.py` | `beishan-edition-review.json` |
| 东山经51段 | `build_dongshan.py` | `dongshan-edition-review.json` |
| 中山经212段 | `build_zhongshan.py` | `zhongshan-edition-review.json` |

南山reader或首批构建器运行后，需要用`build_nanshan_entities.py`恢复最终实体与关系。其他篇的`*_completion.py`、`*_range*.py`、`*_batch.py`、`zhongshan_stages*.py`及`zhongshan_next30.py`仍被主构建器导入，是内容模块，不是可以删除的旧脚本。

## 来源与生成清单

- `shanhaijing-reference.json`：保留的十八篇录文快照。
- `reference-scans/`：影印页、页码和来源哈希。
- `build_source_inventory.py`：构建`shanhaijing-inventory.json`，保留未接入和待核状态。
- `audit_shanhaijing.py`：生成[内容盘点](../docs/content-coverage.md)及前端来源分类。内容盘点是生成文件，不手工编辑。
- 短名、同名组和形貌位于`frontend/src/bestiary-metadata.json`；生成经文不会覆盖它们。

仅检查、不重建：

```bash
python data/build_source_inventory.py --check
python data/audit_shanhaijing.py --check
```

素材和字体生成已分到[frontend/scripts/assets/与fonts/](../frontend/scripts/README.md)。

## 可选原型

- `seed.json`、`validate_seed.py`供FastAPI/PostGIS原型使用；数据规模与来源见[数据库说明](../database/README.md#prototype-seed-and-source-notes)。
- `build_myth_atlas.py`只输出`output/legacy-atlas/`，拒绝覆盖已审网页数据；`render_myth_atlas.py`和`generate_myth_stage_boundaries.py`保留用于旧版静态图复现，不是当前网站构建步骤。

五山经共480段阅读已接入；海经十三篇仍有缺口，当前实现不等于十八篇逐字校勘完成。每次内容更新后运行上述清单检查和对应浏览器验收。

已停用的中山初始计划工具和Natural Earth底图生成链已移除；当前中山维护入口是`build_zhongshan.py`，底图配置是`frontend/src/geography-map-config.js`。旧版本可从Git历史恢复。
