import { useEffect, useState } from 'react';
import { useLocale } from './i18n';

export { CHAPTER_TRANSITION_MS } from './map-timing';

export function useReducedMotion() {
  const [reduced, setReduced] = useState(() => window.matchMedia('(prefers-reduced-motion: reduce)').matches);
  useEffect(() => {
    const query = window.matchMedia('(prefers-reduced-motion: reduce)');
    const change = event => setReduced(event.matches);
    query.addEventListener('change', change);
    return () => query.removeEventListener('change', change);
  }, []);
  return reduced;
}

export function InkText({ text, variant = 'title', animate = true }) {
  const { locale } = useLocale();
  const words = locale === 'en' ? text.match(/\S+\s*/g) || [text] : text.match(/.{1,2}/gu) || [text];
  return <span className={`ink-text ink-${variant} ${animate ? 'ink-animate' : ''}`} aria-label={text}>
    <span aria-hidden="true">{words.map((word, index) => <span className="ink-word" style={{ '--ink-delay': `${Math.min(index * 25, 100)}ms` }} key={index}>{word}</span>)}</span>
  </span>;
}

export function ChapterNotice({ change, title }) {
  return <div key={`${change}-${title}`} className={`chapter-transition-veil ${change ? 'is-visible' : ''}`} role="status" aria-live="polite">{change && <span>{title}</span>}</div>;
}
