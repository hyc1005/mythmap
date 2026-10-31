import { useLocale } from '../i18n';

export default function MapToolbar({ isFullscreen, chapterStoryOptions, activeJourneyId, onStoryChange, activeLayers, fitStage, exportStage, exportStatus }) {
  const { t } = useLocale();
  return <div className="map-overlay-controls">{isFullscreen && <span className="fullscreen-orientation" aria-label={t("示意北向")}>{t("示意北向 ↑")}</span>}
    {chapterStoryOptions.length > 0 && <label className="map-animation-choice">{t("故事动画")}<select aria-label={t("选择地图故事动画")} value={activeJourneyId || ''} onChange={event => onStoryChange(event.target.value || null)}><option value="">{t("关闭动画")}</option>{chapterStoryOptions.map(story => <option key={story.id} value={story.id}>{story.name}</option>)}</select></label>}
    <button className="map-fit restore-view" onClick={() => fitStage()}>{t("恢复视野")}</button>
    <details className="map-tools"><summary>{t("图具")}</summary><div>
      <div className="myth-layer-switches" aria-label={t("专题图层")}>
        <label><input type="checkbox" checked={activeLayers.beasts} onChange={event => activeLayers.onBeasts(event.target.checked)} />{t("异兽谱")}</label>
        <label><input type="checkbox" checked={activeLayers.divine} onChange={event => activeLayers.onDivine(event.target.checked)} />{t("神域")}</label>
      </div>
      <button className="map-fit" onClick={exportStage} disabled={exportStatus === '正在生成 PNG…'}>{t("存为本章 PNG")}</button>
    </div></details>
    {exportStatus && <span className="map-export-status" role="status">{t(exportStatus)}</span>}
  </div>;
}
