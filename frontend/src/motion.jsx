import { useEffect, useState } from 'react';

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

export function ChapterNotice({ change, title }) {
  return <div key={`${change}-${title}`} className={`chapter-transition-veil ${change ? 'is-visible' : ''}`} role="status" aria-live="polite">{Boolean(change) && <span>{title}</span>}</div>;
}
