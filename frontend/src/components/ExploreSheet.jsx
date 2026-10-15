import { useEffect, useRef } from 'react';
import { createPortal } from 'react-dom';
import { useLocale } from '../i18n';

export default function ExploreSheet({ title, onClose, children, returnFocus, initialFocus, className = '' }) {
  const { t } = useLocale();
  const sheet = useRef(null);
  useEffect(() => {
    const trigger = returnFocus || document.activeElement;
    const root = document.getElementById('root');
    const previous = [document.documentElement.style.overflow, document.body.style.overflow, root.inert];
    root.inert = true;
    document.documentElement.style.overflow = document.body.style.overflow = 'hidden';
    (initialFocus && sheet.current.querySelector(initialFocus) || sheet.current.querySelector('button'))?.focus({ preventScroll: true });
    return () => {
      [document.documentElement.style.overflow, document.body.style.overflow, root.inert] = previous;
      if (trigger?.isConnected) trigger.focus({ preventScroll: true });
    };
  }, []);
  const keydown = event => {
    if (event.key === 'Escape') { event.stopPropagation(); onClose(); }
    if (event.key !== 'Tab') return;
    const controls = [...sheet.current.querySelectorAll('button:not(:disabled), a[href], input, select, summary, [tabindex="0"]')].filter(node => node.checkVisibility());
    const first = controls[0], last = controls.at(-1);
    if (event.shiftKey && document.activeElement === first) { event.preventDefault(); last?.focus(); }
    if (!event.shiftKey && document.activeElement === last) { event.preventDefault(); first?.focus(); }
  };
  return createPortal(<div className="explore-sheet-scrim" onClick={onClose}>
    <section ref={sheet} className={`explore-sheet ${className}`} role="dialog" aria-modal="true" aria-label={title} onClick={event => event.stopPropagation()} onKeyDown={keydown}>
      <header><h2>{title}</h2><button onClick={onClose} aria-label={t('关闭')}>×</button></header>
      {children}
    </section>
  </div>, document.body);
}
