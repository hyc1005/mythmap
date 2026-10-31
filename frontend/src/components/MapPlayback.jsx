import { useLocale } from '../i18n';

export default function MapPlayback({ hidden, isFullscreen, isPrologue, activeJourneyId, onSelect, controlRef, preview, legend, layerStatus, readingNote, readingActions }) {
  const { t } = useLocale();
  return <footer hidden={hidden} className={isFullscreen ? 'fullscreen-dock' : 'explore-playback'} aria-label={t('地图播放与信息栏')}>
    {isPrologue && <div className="fullscreen-prologue-title"><b>{t('盘古开天')}</b><button className="prologue-source" onClick={event => onSelect('01-01', event.currentTarget)}>{t('原文与出处 ↗')}</button></div>}
    <div className="fullscreen-control-slot playback-control-slot" ref={controlRef} />
    {isFullscreen && !isPrologue && <div className="fullscreen-preview-slot" aria-label={t('地图地点预览')}>{preview}</div>}
    {!isPrologue && !activeJourneyId && !readingNote && <div className="fullscreen-idle-info">{legend}{layerStatus}</div>}
    {readingActions}
  </footer>;
}
