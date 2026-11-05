import { Children, createContext, useContext, useLayoutEffect, useRef, useState } from 'react';
import './blur-reveal.css';

const REVEAL_EASING_MS = 1500;
const roots = new Map();
const active = new Set();
const RevealVisibility = createContext(true);

export function BlurRevealScope({ active = true, children }) {
  const parentVisible = useContext(RevealVisibility);
  return <RevealVisibility.Provider value={parentVisible && active}>{children}</RevealVisibility.Provider>;
}

export function RevealDetails({ children, onToggle, ...props }) {
  const parentVisible = useContext(RevealVisibility);
  const [open, setOpen] = useState(Boolean(props.open));
  const [summary, ...body] = Children.toArray(children);
  return <details {...props} onToggle={event => { setOpen(event.currentTarget.open); onToggle?.(event); }}>
    {summary}<RevealVisibility.Provider value={parentVisible && open}>{body}</RevealVisibility.Provider>
  </details>;
}

function scrollRoot(node) {
  for (let parent = node.parentElement; parent && parent !== document.body; parent = parent.parentElement) {
    if (/(auto|scroll)/.test(getComputedStyle(parent).overflowY)) return parent;
  }
  return null;
}

function contentKey(value) {
  return Children.toArray(value).map(child => typeof child === 'object' ? contentKey(child.props?.children) : String(child)).join('');
}

function controller(root) {
  if (roots.has(root)) return roots.get(root);
  const items = new Set();
  const scrollTargets = root ? [root] : [];
  for (let parent = root?.parentElement; parent && parent !== document.body; parent = parent.parentElement) {
    if (/(auto|scroll)/.test(getComputedStyle(parent).overflowY)) scrollTargets.push(parent);
  }
  scrollTargets.push(window);
  const motion = matchMedia('(prefers-reduced-motion: reduce)');
  let frame = 0;
  const scrollPosition = () => scrollTargets.reduce((sum, target) => sum + (target === window ? window.scrollY : target.scrollTop), 0);
  let previous = scrollPosition();
  let bypass = false;
  const clear = (item, ease = false) => {
    clearTimeout(item.release);
    if (ease) item.release = setTimeout(() => { active.delete(item); item.node.dataset.revealState = 'clear'; }, REVEAL_EASING_MS);
    else active.delete(item);
    item.node.style.removeProperty('--reveal-blur');
    if (!ease) item.node.style.removeProperty('--reveal-duration');
    item.node.dataset.revealState = ease ? 'revealing' : 'clear';
    item.state = 'clear';
  };
  const show = item => clear(item);
  const visible = (box, bounds) => box.height > 0 && box.width > 0 && bounds.height > 0 && box.bottom > bounds.top && box.top < bounds.bottom;
  const bounds = () => {
    if (!root) return { top: 0, bottom: innerHeight, height: innerHeight };
    const box = root.getBoundingClientRect();
    let top = Math.max(0, box.top + root.clientTop);
    let bottom = Math.min(innerHeight, box.top + root.clientTop + root.clientHeight);
    for (let parent = root.parentElement; parent && parent !== document.body; parent = parent.parentElement) {
      if (!/(auto|scroll|hidden|clip)/.test(getComputedStyle(parent).overflowY)) continue;
      const clip = parent.getBoundingClientRect();
      top = Math.max(top, clip.top + parent.clientTop);
      bottom = Math.min(bottom, clip.top + parent.clientTop + parent.clientHeight);
    }
    return { top, bottom, height: Math.max(0, bottom - top) };
  };
  const tick = () => {
    frame = 0;
    const viewport = bounds();
    const position = scrollPosition();
    const delta = position - previous;
    previous = position;
    const measurements = [...items].map(item => [item, item.node.getBoundingClientRect()]);
    for (const [item, box] of measurements) {
      if (bypass || motion.matches || document.hidden || root?.dataset.readingRestoring === 'true') {
        if (visible(box, viewport)) show(item); else clear(item);
        continue;
      }
      const outside = box.bottom < viewport.top - 24 || box.top > viewport.bottom + 24;
      if (outside) {
        clearTimeout(item.release);
        active.delete(item);
        item.state = 'waiting';
        item.node.dataset.revealState = 'waiting';
        item.node.style.removeProperty('--reveal-blur');
        item.node.style.removeProperty('--reveal-duration');
        continue;
      }
      if (!visible(box, viewport) || item.state === 'clear') continue;
      if (item.state === 'waiting') {
        if (!delta) continue;
        // Large jumps and navigation land directly in the reading position.
        if (Math.abs(delta) > innerHeight / 2 || active.size >= 3
          || (box.top >= viewport.top + viewport.height / 4 && box.bottom <= viewport.bottom - viewport.height / 4)) {
          clear(item); continue;
        }
        const inset = Math.min(50, viewport.height / 4);
        if (delta > 0 && box.top > viewport.bottom - inset) continue;
        if (delta < 0 && box.bottom < viewport.top + inset) continue;
        active.add(item);
        item.node.style.setProperty('--reveal-duration', `${REVEAL_EASING_MS}ms`);
        clear(item, true);
      }
    }
  };
  const schedule = () => { if (!frame && !document.hidden) frame = requestAnimationFrame(tick); };
  const showAll = () => {
    const viewport = bounds();
    items.forEach(item => { if (visible(item.node.getBoundingClientRect(), viewport)) show(item); else clear(item); });
  };
  const navigation = () => { showAll(); schedule(); };
  let navigationFrame = 0;
  const contentChange = () => {
    if (navigationFrame) cancelAnimationFrame(navigationFrame);
    navigationFrame = requestAnimationFrame(() => { navigationFrame = 0; navigation(); });
  };
  const findKey = event => { if ((event.ctrlKey || event.metaKey) && event.key.toLowerCase() === 'f') { bypass = true; showAll(); } };
  const selection = () => { if (!getSelection()?.isCollapsed) { bypass = true; showAll(); } };
  const visibility = () => { if (document.hidden) { cancelAnimationFrame(frame); frame = 0; showAll(); } else navigation(); };
  const reduce = () => { if (motion.matches) showAll(); schedule(); };
  const observer = new IntersectionObserver(schedule, { root, rootMargin: '24px' });
  const resize = new ResizeObserver(contentChange);
  for (const type of ['click', 'input', 'change', 'toggle']) document.addEventListener(type, contentChange, true);
  scrollTargets.forEach(target => target.addEventListener('scroll', schedule, { passive: true }));
  window.addEventListener('resize', navigation);
  window.addEventListener('hashchange', navigation);
  window.addEventListener('popstate', navigation);
  window.addEventListener('beforeprint', showAll);
  document.addEventListener('visibilitychange', visibility);
  document.addEventListener('keydown', findKey);
  document.addEventListener('selectionchange', selection);
  document.addEventListener('focusin', showAll);
  motion.addEventListener('change', reduce);
  document.fonts?.addEventListener('loadingdone', navigation);
  const value = {
    add(node) {
      const item = { node, state: 'waiting' };
      items.add(item);
      if (visible(node.getBoundingClientRect(), bounds()) || motion.matches || bypass) show(item);
      observer.observe(node); resize.observe(node);
      return () => {
        clear(item); items.delete(item); observer.unobserve(node); resize.unobserve(node);
        if (items.size) return;
        cancelAnimationFrame(frame); cancelAnimationFrame(navigationFrame); observer.disconnect(); resize.disconnect();
        for (const type of ['click', 'input', 'change', 'toggle']) document.removeEventListener(type, contentChange, true);
        scrollTargets.forEach(target => target.removeEventListener('scroll', schedule));
        window.removeEventListener('resize', navigation);
        window.removeEventListener('hashchange', navigation);
        window.removeEventListener('popstate', navigation);
        window.removeEventListener('beforeprint', showAll);
        document.removeEventListener('visibilitychange', visibility);
        document.removeEventListener('keydown', findKey);
        document.removeEventListener('selectionchange', selection);
        document.removeEventListener('focusin', showAll);
        motion.removeEventListener('change', reduce);
        document.fonts?.removeEventListener('loadingdone', navigation);
        roots.delete(root);
      };
    },
  };
  roots.set(root, value);
  return value;
}

export default function BlurRevealText({ text, revealKey, variant = 'title', rootRef, active: enabledProp = true, ...props }) {
  const ref = useRef(null);
  const enabled = useContext(RevealVisibility) && enabledProp;
  const content = contentKey(text);
  useLayoutEffect(() => {
    const node = ref.current;
    if (!enabled) { node.dataset.revealState = 'clear'; return; }
    let cleanup, frame;
    const initialize = () => {
      try {
        if (!window.IntersectionObserver || !window.ResizeObserver || !window.requestAnimationFrame) return;
        cleanup = controller(rootRef?.current || scrollRoot(node)).add(node);
      } catch {
        node.style.removeProperty('--reveal-blur');
        node.style.removeProperty('--reveal-duration');
      }
    };
    if (rootRef && !rootRef.current && window.requestAnimationFrame) frame = requestAnimationFrame(initialize);
    else initialize();
    return () => { if (frame) cancelAnimationFrame(frame); cleanup?.(); };
  }, [revealKey, content, rootRef, enabled]);
  return <span {...props} ref={ref} className={`blur-reveal-text blur-reveal-${variant}${props.className ? ` ${props.className}` : ''}`} data-reveal-key={revealKey}>{text}</span>;
}
