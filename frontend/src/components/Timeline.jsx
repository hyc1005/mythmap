import { useEffect, useRef } from 'react';
import { useLocale } from '../i18n';

export default function Timeline({ stages, index, onSelect }) {
  const { t, locale } = useLocale();
  const steps = useRef(null);
  useEffect(() => {
    const row = steps.current, active = row?.children[index];
    if (!active || row.scrollWidth <= row.clientWidth) return;
    const offset = active.getBoundingClientRect().left - row.getBoundingClientRect().left + row.scrollLeft;
    row.scrollTo({ left: offset - (row.clientWidth - active.offsetWidth) / 2, behavior: 'instant' });
  }, [index, locale]);
  const keys = event => {
    if (event.altKey || event.ctrlKey || event.metaKey || event.shiftKey) return;
    const next = { ArrowRight: index + 1, ArrowLeft: index - 1, Home: 0, End: stages.length - 1 }[event.key];
    if (next === undefined) return;
    event.preventDefault();
    onSelect(Math.max(0, Math.min(stages.length - 1, next)));
    requestAnimationFrame(() => steps.current?.querySelector('[aria-current=step]')?.focus({ preventScroll: true }));
  };
  return <nav className="myth-timeline" aria-label={t('章节导航')} onKeyDown={keys}>
    <div className="timeline-current">
      <button type="button" onClick={() => onSelect(index - 1)} disabled={index === 0}>{t('← 上一章')}</button>
      <button type="button" onClick={() => onSelect(index + 1)} disabled={index === stages.length - 1}>{t('下一章 →')}</button>
    </div>
    <div ref={steps} className="timeline-steps">{stages.map((stage, i) => <button type="button" key={stage.id} aria-current={index === i ? 'step' : undefined} onClick={() => onSelect(i)}><i>{stage.id}</i>{stage.title}</button>)}</div>
  </nav>;
}
