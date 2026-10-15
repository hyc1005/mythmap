import { useState } from 'react';
import { useLocale } from '../i18n';

export default function ArtworkImage({ src, alt = '', className, loading, interactive = true }) {
  const { t } = useLocale();
  const [failed, setFailed] = useState(false);
  const [attempt, setAttempt] = useState(0);
  if (failed) return <span className={`artwork-fallback ${className || ''}`} role="group" aria-label={t('插画暂不可用')}>
    <span aria-hidden="true">✦</span><span>{t('插画暂不可用')}</span>
    {interactive && <button type="button" onClick={event => { event.stopPropagation(); setFailed(false); setAttempt(value => value + 1); }}>{t('重试插画')}</button>}
  </span>;
  return <img key={attempt} src={src} alt={alt} className={className} loading={loading} onError={() => setFailed(true)} />;
}
