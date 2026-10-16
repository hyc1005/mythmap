import { useLocale } from '../i18n';

export default function ReadingActions({ resumeEntry, onResume, showTour, tourLabel, tourActive, playing, readingChapter, progress, onTour, guideVisible, onDismissGuide }) {
  const { t } = useLocale();
  if (!resumeEntry && !showTour) return null;
  return <div className="map-reading-actions" role="group" aria-label={t('阅读与游历')}>
    {showTour && <button className="begin-journey" type="button" aria-pressed={tourActive && playing} onClick={onTour}>{t(tourLabel)}</button>}
    {resumeEntry && <button className="resume-reading" type="button" aria-label={`${t('继续上次阅读')} · ${resumeEntry.name}`} onClick={onResume}><span className="resume-full">{t('继续上次阅读')}</span><span className="resume-short" aria-hidden="true">{t('续读')}</span><small>{resumeEntry.name}</small></button>}
    {showTour && tourActive && <p className={readingChapter ? 'tour-reading' : 'tour-progress'} role="status">{readingChapter ? t('本章以文字为主，请阅读条目后继续。') : t('本章故事') + ` ${progress}`}</p>}
    {showTour && guideVisible && <div className="exploration-guide"><p>{t('章节 → 标记 → 原文')}</p><button type="button" aria-label={t('关闭引导')} onClick={onDismissGuide}>×</button></div>}
  </div>;
}
