import { useLayoutEffect, useRef } from 'react';
import './blur-reveal.css';

const REVEAL_EASING_MS = 1500;
const roots = new Map();
const active = new Set();

function controller(root) {
  if (roots.has(root)) return roots.get(root);
  const items = new Set();
  const scrollTarget = root || window;
  const motion = matchMedia('(prefers-reduced-motion: reduce)');
  let frame = 0;
  let previous = root ? root.scrollTop : window.scrollY;
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
  const visible = (box, bounds) => box.bottom > bounds.top && box.top < bounds.bottom;
  const bounds = () => root ? root.getBoundingClientRect() : { top: 0, bottom: innerHeight, height: innerHeight };
  const tick = () => {
    frame = 0;
    const viewport = bounds();
    const position = root ? root.scrollTop : window.scrollY;
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
        if (Math.abs(delta) > viewport.height / 2 || active.size >= 3
          || (box.top >= viewport.top + viewport.height / 4 && box.bottom <= viewport.bottom - viewport.height / 4)) {
          clear(item); continue;
        }
        if (delta > 0 && box.top > viewport.bottom - 50) continue;
        if (delta < 0 && box.bottom < viewport.top + 50) continue;
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
  const findKey = event => { if ((event.ctrlKey || event.metaKey) && event.key.toLowerCase() === 'f') { bypass = true; showAll(); } };
  const selection = () => { if (!getSelection()?.isCollapsed) { bypass = true; showAll(); } };
  const visibility = () => { if (document.hidden) { cancelAnimationFrame(frame); frame = 0; showAll(); } else navigation(); };
  const reduce = () => { if (motion.matches) showAll(); schedule(); };
  const observer = new IntersectionObserver(schedule, { root, rootMargin: '24px' });
  const resize = new ResizeObserver(schedule);
  scrollTarget.addEventListener('scroll', schedule, { passive: true });
  window.addEventListener('resize', schedule);
  window.addEventListener('hashchange', navigation);
  window.addEventListener('popstate', navigation);
  window.addEventListener('beforeprint', showAll);
  document.addEventListener('visibilitychange', visibility);
  document.addEventListener('keydown', findKey);
  document.addEventListener('selectionchange', selection);
  document.addEventListener('focusin', showAll);
  motion.addEventListener('change', reduce);
  document.fonts?.addEventListener('loadingdone', schedule);
  const value = {
    add(node) {
      const item = { node, state: 'waiting' };
      items.add(item);
      if (visible(node.getBoundingClientRect(), bounds()) || motion.matches || bypass) show(item);
      observer.observe(node); resize.observe(node);
      return () => {
        clear(item); items.delete(item); observer.unobserve(node); resize.unobserve(node);
        if (items.size) return;
        cancelAnimationFrame(frame); observer.disconnect(); resize.disconnect();
        scrollTarget.removeEventListener('scroll', schedule);
        window.removeEventListener('resize', schedule);
        window.removeEventListener('hashchange', navigation);
        window.removeEventListener('popstate', navigation);
        window.removeEventListener('beforeprint', showAll);
        document.removeEventListener('visibilitychange', visibility);
        document.removeEventListener('keydown', findKey);
        document.removeEventListener('selectionchange', selection);
        document.removeEventListener('focusin', showAll);
        motion.removeEventListener('change', reduce);
        document.fonts?.removeEventListener('loadingdone', schedule);
        roots.delete(root);
      };
    },
  };
  roots.set(root, value);
  return value;
}

export default function BlurRevealText({ text, revealKey, variant = 'title', rootRef, ...props }) {
  const ref = useRef(null);
  useLayoutEffect(() => {
    const node = ref.current;
    let cleanup, frame;
    const initialize = () => {
      try {
        if (!window.IntersectionObserver || !window.ResizeObserver || !window.requestAnimationFrame) return;
        cleanup = controller(rootRef?.current || null).add(node);
      } catch {
        node.style.removeProperty('--reveal-blur');
        node.style.removeProperty('--reveal-duration');
      }
    };
    if (rootRef && !rootRef.current && window.requestAnimationFrame) frame = requestAnimationFrame(initialize);
    else initialize();
    return () => { if (frame) cancelAnimationFrame(frame); cleanup?.(); };
  }, [revealKey, rootRef]);
  return <span {...props} ref={ref} className={`blur-reveal-text blur-reveal-${variant}${props.className ? ` ${props.className}` : ''}`} data-reveal-key={revealKey}>{text}</span>;
}
