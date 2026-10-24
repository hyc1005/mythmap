import { useId, useLayoutEffect, useRef, useState } from 'react';
import { createPortal } from 'react-dom';
import { useLocale } from '../i18n';
import '../styles/onboarding.css';

const steps = [
  { id: 'read', title: '先读一段原文', body: '从亮起的入口打开介绍、原文与出处。其他章节里，也可以点地图名称旁的小朱印。', selectors: ['.prologue-source', '.mobile-explore-nav button:last-child', '.chapter-rail .chapter-story-list button'] },
  { id: 'chapters', title: '章节由你选择', body: '从这里切换章节。可以顺着看，也可以停在感兴趣的一章，不必跟随播放。', selectors: ['.mobile-explore-nav button:first-child', '.world-main > .myth-timeline .timeline-current button:not(:disabled)'] },
  { id: 'search', title: '想找什么，就搜什么', body: '故事名、异兽名和现代地名都能搜索。现代地名先带你读故事，真实地理资料由你主动打开。', selectors: ['.global-search-trigger'] },
  { id: 'modes', title: '两种地图，自由切换', body: '木刻叙事看故事与方位，真实地理看传说关联的现代地点。初次进入以木刻地图为主，真实地理由你选择。', selectors: ['.map-mode-switch'] },
];
const controls = 'button:not(:disabled), a[href], input:not(:disabled), select:not(:disabled), summary, [tabindex="0"]';
const visible = node => node.checkVisibility() && node.getBoundingClientRect().width > 0;
const findTarget = step => steps[step]?.selectors.flatMap(selector => [...document.querySelectorAll(selector)]).find(visible);
const clamp = (value, min, max) => Math.max(min, Math.min(max, value));

export default function OnboardingGuide({ blocked, contextKey, onFinish, returnFocus }) {
  const { t, locale, setLocale } = useLocale();
  const [step, setStep] = useState(-1), [geometry, setGeometry] = useState(null);
  const card = useRef(null), target = useRef(null), finish = useRef(onFinish);
  const initialFocus = useRef(returnFocus);
  const maskId = `onboarding-${useId().replaceAll(':', '')}`;
  finish.current = onFinish;
  const advance = () => step === steps.length - 1 ? finish.current() : setStep(value => value + 1);

  useLayoutEffect(() => () => {
    requestAnimationFrame(() => {
      const node = initialFocus.current?.isConnected ? initialFocus.current : document.querySelector('.map-mode-switch button[aria-pressed="true"]');
      node?.focus({ preventScroll: true });
    });
  }, []);

  useLayoutEffect(() => {
    if (blocked) return undefined;
    const root = document.getElementById('root'), previousInert = root.inert;
    if (step < 0) root.inert = true;
    let frame, alive = true, unbind = () => {};
    const observer = new ResizeObserver(() => schedule());
    const waiting = new MutationObserver(() => { if (findTarget(step)) { align(); waiting.disconnect(); } });
    const next = () => step === steps.length - 1 ? finish.current() : setStep(value => value + 1);
    const clicked = event => { if (event.target.closest(controls)) next(); };
    const bind = node => {
      if (target.current === node) return;
      unbind(); target.current = node;
      if (!node) return;
      const description = node.getAttribute('aria-describedby'), marker = node.getAttribute('data-onboarding-target');
      node.setAttribute('aria-describedby', [description, 'onboarding-description'].filter(Boolean).join(' '));
      node.setAttribute('data-onboarding-target', steps[step].id);
      node.addEventListener('click', clicked); observer.observe(node);
      unbind = () => {
        observer.unobserve(node); node.removeEventListener('click', clicked);
        for (const [name, value] of [['aria-describedby', description], ['data-onboarding-target', marker]]) {
          if (value === null) node.removeAttribute(name); else node.setAttribute(name, value);
        }
        target.current = null;
      };
    };
    const measure = () => {
      if (!card.current) return;
      const node = findTarget(step); bind(node);
      const width = document.documentElement.clientWidth, height = window.innerHeight;
      const cardWidth = card.current.offsetWidth, naturalHeight = card.current.scrollHeight + 2;
      const bounds = node?.getBoundingClientRect();
      const hole = bounds ? { left: clamp(Math.floor(bounds.left - 6), 0, width), top: clamp(Math.floor(bounds.top - 6), 0, height), right: clamp(Math.ceil(bounds.right + 6), 0, width), bottom: clamp(Math.ceil(bounds.bottom + 6), 0, height) } : null;
      let maxHeight = height - 24, top = Math.max(12, (height - Math.min(naturalHeight, maxHeight)) / 2), left = (width - cardWidth) / 2;
      if (hole) {
        const below = height - hole.bottom - 20, above = hole.top - 20;
        const useBelow = below >= naturalHeight || below >= above;
        maxHeight = Math.max(100, Math.min(height - 24, useBelow ? below : above));
        top = useBelow ? hole.bottom + 12 : hole.top - Math.min(naturalHeight, maxHeight) - 12;
        left = clamp((hole.left + hole.right - cardWidth) / 2, 12, width - cardWidth - 12);
      }
      const nextGeometry = { hole, width, height, left: Math.round(left), top: Math.round(clamp(top, 12, height - Math.min(naturalHeight, maxHeight) - 12)), maxHeight: Math.floor(maxHeight) };
      setGeometry(previous => JSON.stringify(previous) === JSON.stringify(nextGeometry) ? previous : nextGeometry);
    };
    const schedule = () => { if (!alive) return; cancelAnimationFrame(frame); frame = requestAnimationFrame(measure); };
    const align = () => {
      const node = findTarget(step);
      node?.scrollIntoView({ block: 'center', inline: 'nearest', behavior: 'instant' });
      if (node && card.current) {
        const box = node.getBoundingClientRect(), available = Math.max(box.top - 20, innerHeight - box.bottom - 20);
        if (available < card.current.scrollHeight + 2) window.scrollBy({ top: box.top - 68, behavior: 'instant' });
      }
      measure();
    };
    const allowed = () => [...(target.current?.matches(controls) ? [target.current] : target.current?.querySelectorAll(controls) || []), ...card.current.querySelectorAll(controls)].filter(visible);
    const keydown = event => {
      if (event.key === 'Escape') { event.preventDefault(); event.stopImmediatePropagation(); finish.current(); }
      if (event.key !== 'Tab') return;
      const nodes = allowed(), index = nodes.indexOf(document.activeElement);
      event.preventDefault(); nodes[(index + (event.shiftKey ? -1 : 1) + nodes.length) % nodes.length]?.focus({ preventScroll: true });
    };
    const focus = event => {
      if (!card.current.contains(event.target) && !target.current?.contains(event.target)) card.current.querySelector('.onboarding-next')?.focus({ preventScroll: true });
    };
    const wheel = event => { if (!event.ctrlKey && !card.current.contains(event.target) && !target.current?.contains(event.target)) event.preventDefault(); };
    align(); observer.observe(card.current);
    if (step >= 0 && !target.current) waiting.observe(document.getElementById('root'), { subtree: true, childList: true });
    card.current.querySelector('.onboarding-next')?.focus({ preventScroll: true });
    window.addEventListener('resize', schedule); window.addEventListener('scroll', schedule, true);
    window.visualViewport?.addEventListener('resize', schedule);
    document.addEventListener('keydown', keydown, true); document.addEventListener('focusin', focus, true);
    document.addEventListener('wheel', wheel, { capture: true, passive: false });
    document.fonts.ready.then(schedule);
    return () => {
      alive = false; cancelAnimationFrame(frame); observer.disconnect(); waiting.disconnect(); unbind();
      root.inert = previousInert;
      window.removeEventListener('resize', schedule); window.removeEventListener('scroll', schedule, true);
      window.visualViewport?.removeEventListener('resize', schedule);
      document.removeEventListener('keydown', keydown, true); document.removeEventListener('focusin', focus, true);
      document.removeEventListener('wheel', wheel, true);
    };
  }, [step, blocked, contextKey, locale]);

  if (blocked) return null;
  const hole = geometry?.hole;
  const blockers = hole ? [
    { left: 0, top: 0, width: '100%', height: hole.top },
    { left: 0, top: hole.bottom, width: '100%', bottom: 0 },
    { left: 0, top: hole.top, width: hole.left, height: hole.bottom - hole.top },
    { left: hole.right, top: hole.top, right: 0, height: hole.bottom - hole.top },
  ] : [{ inset: 0 }];
  return createPortal(<div className="onboarding-guide" data-step={step < 0 ? 'welcome' : steps[step].id}>
    <svg className="onboarding-shade" aria-hidden="true" width="100%" height="100%"><defs><mask id={maskId} maskUnits="userSpaceOnUse"><rect width="100%" height="100%" fill="white" />{hole && <rect x={hole.left} y={hole.top} width={hole.right - hole.left} height={hole.bottom - hole.top} rx="6" fill="black" />}</mask></defs><rect width="100%" height="100%" fill="rgba(0,0,0,.64)" mask={`url(#${maskId})`} /></svg>
    {blockers.map((style, index) => <div key={index} className="onboarding-blocker" style={style} />)}
    {hole && <div className="onboarding-ring" aria-hidden="true" style={{ left: hole.left, top: hole.top, width: hole.right - hole.left, height: hole.bottom - hole.top }} />}
    <section ref={card} className="onboarding-card" role="dialog" aria-modal={step < 0 ? true : undefined} aria-label={t('操作引导')} aria-describedby="onboarding-description" style={geometry ? { left: geometry.left, top: geometry.top, maxHeight: geometry.maxHeight } : undefined}>
      <header><span>{t('操作引导')}{step >= 0 && ` · ${step + 1} / ${steps.length}`}</span><button type="button" className="onboarding-skip" onClick={() => onFinish()}>{t('跳过引导')}</button></header>
      <h2 aria-live="polite">{t(step < 0 ? '从一段故事，走进山海' : steps[step].title)}</h2>
      <p id="onboarding-description">{t(step < 0 ? '四个小步骤，认识原文、章节、搜索与地图。随时跳过，也能从“操作引导”重新打开。' : steps[step].body)}</p>
      {step >= 0 && step < 3 && <p className="onboarding-note">{t('打开的内容关闭后，引导会接着进行。')}</p>}
      <footer>{step < 0 ? <div className="onboarding-language" role="group" aria-label={t('语言')}><button type="button" lang="zh-CN" aria-pressed={locale === 'zh'} onClick={() => setLocale('zh')}>中文</button><button type="button" lang="en" aria-pressed={locale === 'en'} onClick={() => setLocale('en')}>EN</button></div> : <button type="button" onClick={() => setStep(value => value - 1)}>{t('上一步')}</button>}<button type="button" className="onboarding-next" onClick={advance}>{t(step < 0 ? '开始引导' : step === steps.length - 1 ? '开始探索' : '下一步')}</button></footer>
    </section>
  </div>, document.body);
}
