# 生图提示词模板与文件位置

更新：2026-11-10。给后续可生图模型使用。

## 先说明：没有一个单独的“统一提示词文件”

仓库没有 `prompt.md` 之类的单一模板。统一风格是**逐条复制到每个生成记录里的公共前缀**，实际存放位置有三处：

1. `frontend/artwork-source/<篇目>/generation.json`
   - `assets[].prompt`：当次生成提示词。
   - `assets[].revisions[].prompt`：被替换版本的旧提示词。
   - `assets[].reference_images`：参考图路径。
   - 文件：`beishan`、`dongshan`、`nanshan`、`xishan`、`zhongshan`、`woodcut-refinement`。
2. `frontend/public/data/atlas/artwork-manifest.json`
   - `assets[].initial_prompt`：与生成记录对应的初始提示词。
   - 用于发布侧追溯，不参与运行时渲染。
3. `data/character-artwork-registry.json`
   - 条目、角色、发布图、占位状态与 `visual_continuity_review`。
   - 不存提示词，但决定同一角色用哪张图。

**没有统一模板文件**；下面的模板是从上述记录中抽出的公共部分。新增图时，请复制本模板，再替换 `Subject:` 段落。

## 公共模板（孤立主体）

```text
Use case: illustration-story. Project asset for an illustrated Shanhaijing atlas.
Make ONE complete isolated subject on a truly transparent background, generous 8% clear margins,
no text, seal, labels, frame, ground rectangle or watermark.
Ancient Chinese hand-carved woodblock print: bold warm black-brown contours, flat warm ivory and
ochre areas, restrained cinnabar, sparing muted mineral-green, visibly cut curved lines and sparse
stipple. Readable at 320px. Strong decorative archaic silhouette, deliberately non-photoreal,
no 3D, no soft digital lighting, no realistic fur rendering.
The ornament is artistic treatment, not added anatomy.

Subject: <single named subject from the source>. <textual morphology, count, color and pose>.
<explicit prohibitions: no extra heads/wings/legs/tails, no unsupported anatomy, no scene>.
```

## 公共模板（山形/水景）

```text
Use case: illustration-story. Project asset for an illustrated Shanhaijing atlas.
ONE complete compact isolated mountain-and-water vignette on a genuinely transparent background,
generous clear margins.
Ancient Chinese hand-carved woodblock print: bold warm black-brown contours, flat warm ivory and
ochre, restrained muted mineral-green, visibly cut curved lines and sparse stipple.
Archaic decorative silhouette readable at 320px.
No photorealism, 3D, glow, digital gradients, text, labels, seals, compass arrows, frame or watermark.

Subject: <mountain/water name and chapter>. <textual terrain, vegetation, water count and route>.
<explicit prohibitions: no people, animals, buildings, bridges, modern geography>.
```

## 必须遵守的边界

- **只画原文或郭注明确写出的形貌。** 数量（头、翼、足、尾、眼）必须可数；不确定时留占位，不补 anatomy。
- **原文、郭注、后世解释分层。** 郭注异说可以画，但要在 `review_note` 说明依据；不能把注文写成正文。
- **透明背景、完整剪影、8% 留边。** 不画地面矩形、光晕、渐变、文字、印章、边框、水印。
- **风格是木刻版画，不是写实动物摄影/3D。** 暖黑褐轮廓、暖象牙/赭石平涂、克制朱砂、少量矿物绿、刻线与点刻。
- **320px 可读。** 复杂装饰不能吃掉主体轮廓。
- **参考图只用于身份、姿态、服饰连续性。** 不得从参考图复制未在文本中出现的器官或故事。
- **颜色与姿态是艺术选择，除非原文明确。** 在 `review_note` 里区分“原文”与“艺术解释”。

## 生成与落盘流程

1. 在 `frontend/artwork-source/<篇目>/generation.json` 找到条目；没有则新建 `assets[]` 记录。
2. 复制公共模板，替换 `Subject`；写清数量、颜色、姿态、禁止项。
3. 如使用参考图，填 `reference_images`，只引用仓库内相对路径。
4. 输出 PNG（透明背景）到 `frontend/artwork-source/<篇目>/`；文件名带 `-vN`。
5. 目视复核；在 `review_note` 写“原文依据 / 艺术解释 / 未解决点”。
6. 按 `frontend/scripts/assets/README.md` 的流程生成 WebP 变体并更新 `atlas/artwork-manifest.json` 与素材清单。
7. 重画必须使用新文件名或提升 `vN`，避免反馈/缓存把旧图当新图。

## 相关文件

- 生成记录：`frontend/artwork-source/*/generation.json`、`entities-generation.json`、`reader-generation.json`
- 发布清单：`frontend/public/data/atlas/artwork-manifest.json`
- 角色登记：`data/character-artwork-registry.json`
- 素材处理：`frontend/scripts/assets/`
- 素材审计：`frontend/scripts/verify-assets.py`、`docs/assets-inventory.tsv`
- 形貌复核：`frontend/src/bestiary-morphology-review.json`

## 已知限制

- 早期生成记录中的 `review_note` 在 Windows 控制台可能因编码显示乱码；文件本身是 UTF-8，按 UTF-8 读取。
- 具体历史模型名并非每条都记录；`data/character-artwork-registry.json` 的 `status` 与 `docs/assets-inventory.tsv` 只记录可核对事实。
- 本模板是**抽取整理**，不是对历史每条提示词的逐字替代；已生成的图仍以各自 `generation.json` 的原文为准。
