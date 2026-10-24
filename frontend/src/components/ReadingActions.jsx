import { useLocale } from '../i18n';

export default function ReadingActions({ resumeEntry, onResume, returnEntry, onReturnToReading, showTour, tourLabel, tourActive, playing, readingChapter, progress, onTour, guideVisible, onDismissGuide, onGuide }) {
  const { t } = useLocale();
  if (!resumeEntry && !showTour && !returnEntry && !onGuide) return null;
  return <div className="map-reading-actions" role="group" aria-label={t('阅读与游历')}>
    {showTour && <button className="begin-journey" type="button" aria-pressed={tourActive && playing} onClick={onTour}>{t(tourLabel)}</button>}
    {onGuide && <button className="guide-replay" type="button" onClick={onGuide}>{t('操作引导')}</button>}
    {returnEntry && <button className="return-to-reading resume-reading" type="button" onClick={onReturnToReading}>{t('返回阅读')} · {returnEntry.name}</button>}
    {resumeEntry && resumeEntry.id !== returnEntry?.id && <button className="resume-reading" type="button" aria-label={`${t('继续上次阅读')} · ${resumeEntry.name}`} onClick={onResume}><span className="resume-full">{t('继续上次阅读')}</span><span className="resume-short" aria-hidden="true">{t('续读')}</span><small>{resumeEntry.name}</small></button>}
    {showTour && tourActive && <p className={readingChapter ? 'tour-reading' : 'tour-progress'} role="status">{readingChapter ? t('本章以文字为主，请阅读条目后继续。') : t('本章故事') + ` ${progress}`}</p>}
    {showTour && guideVisible && <div className="exploration-guide"><p>{t('播放只看当前故事；开始游历按章节连续观看，文字章节由你继续。')}<br />{t('木刻叙事看故事与方位，真实地理查传说关联地点。')}</p><button type="button" aria-label={t('关闭引导')} onClick={onDismissGuide}>×</button></div>}
  </div>;
}
