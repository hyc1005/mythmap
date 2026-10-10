import { useCallback, useEffect, useMemo, useRef, useState } from 'react';
import { createPortal } from 'react-dom';
import catalog from '../public/data/atlas/catalog.json';
import mythWorld from '../public/data/myth-world.json';
import MapPanel from './components/MapPanel';
import DetailDrawer from './components/DetailDrawer';
import Timeline from './components/Timeline';
import Bestiary from './components/Bestiary';
import './myth-world.css';

export default function App() {
  const [world, setWorld] = useState(mythWorld);
  const [stageIndex, setStageIndex] = useState(0);
  const [playing, setPlaying] = useState(false);
  const [journeyBusy, setJourneyBusy] = useState(false);
  const [chapterTransition, setChapterTransition] = useState(false);
  const [activeLayers, setActiveLayers] = useState({ beasts: false, divine: false });
  const [selectedId, setSelectedId] = useState(null);
  const [fullscreenTarget, setFullscreenTarget] = useState(null);
  const [railExpanded, setRailExpanded] = useState(false);
  const [layoutMetrics, setLayoutMetrics] = useState({ mapHeight: 480, timelineHeight: 150 });
  const [autoPlayChapterId, setAutoPlayChapterId] = useState('00');
  const [reducedMotion, setReducedMotion] = useState(() => window.matchMedia?.('(prefers-reduced-motion: reduce)').matches || false);
  const worldLayout = useRef(null);
  const chapterRail = useRef(null);
  const worldMain = useRef(null);
  const timeline = useRef(null);
  const detailTrigger = useRef(null);
  const detailPageScroll = useRef([0, 0]);
  const detailScrollTop = useRef(0);
  const fullscreenTransitionLock = useRef(false);
  const fullscreenTransitionTimers = useRef([]);
  const stages = world.stages;
  const visitedChapters = useRef(new Set(['00']));
  const previousChapterId = useRef(stages[stageIndex].id);
  const beasts = world.beasts.map((beast, groupIndex) => ({ ...beast, stage: beast.reveal_stage, groupIndex }));
  const places = world.places.map(place => ({ ...place, stage: place.reveal_stage }));
  const domains = world.domains;
  const storyOrder = new Map((catalog.stages.find(stage => stage.id === stages[stageIndex].id)?.event_ids || []).map((id, index) => [id, index]));
  const storyItems = (catalog.events || []).filter(item => item.properties.stage_id === stages[stageIndex].id && !['archive', 'group'].includes(item.properties.presentation))
    .sort((a, b) => (storyOrder.get(a.id) ?? Number.MAX_SAFE_INTEGER) - (storyOrder.get(b.id) ?? Number.MAX_SAFE_INTEGER));
  useEffect(() => {
    const id = stages[stageIndex].id;
    if (previousChapterId.current === id) return;
    previousChapterId.current = id;
    if (visitedChapters.current.has(id) && !playing) setAutoPlayChapterId(null);
    else { visitedChapters.current.add(id); setAutoPlayChapterId(id); }
  }, [stageIndex, stages, playing]);
  const selected = useMemo(() => {
    const domain = domains.find(item => item.id === selectedId);
    if (domain) {
      const place = places.find(item => item.id === domain.place_id);
      return { ...domain, description: domain.quote, region: domain.source, direction: place.direction, kind: 'domain' };
    }
    const creature = beasts.find(item => item.id === selectedId);
    if (creature) return creature;
    const place = places.find(item => item.id === selectedId);
    if (place) return place;
    const raw = (catalog.events || []).find(item => item.id === selectedId);
    if (raw) return { id: raw.id, kind: 'story', name: raw.properties.name, source: raw.properties.source_text, description: raw.properties.source_quote, region: raw.properties.location_label || raw.properties.basis_note, direction: raw.properties.basis_note, url: raw.properties.source_url, artwork: raw.properties.artwork, artworks: raw.properties.artworks, raw };
    return null;
  }, [selectedId, world]);
  const open = (id, trigger) => {
    if (!selectedId) detailPageScroll.current = [window.scrollX, window.scrollY];
    if (trigger) detailTrigger.current = trigger;
    setPlaying(false);
    setSelectedId(id);
  };
  const closeDetail = () => {
    setSelectedId(null);
    requestAnimationFrame(() => {
      if (detailTrigger.current?.isConnected) detailTrigger.current.focus({ preventScroll: true });
      else document.querySelector('.myth-map-canvas .ol-viewport')?.focus({ preventScroll: true });
      window.scrollTo({ left: detailPageScroll.current[0], top: detailPageScroll.current[1], behavior: 'instant' });
    });
  };
  const selectStage = index => { setPlaying(false); setStageIndex(index); setSelectedId(null); };
  const navigateFullscreenStage = useCallback(index => {
    if (fullscreenTransitionLock.current || index < 0 || index >= stages.length || index === stageIndex) return;
    fullscreenTransitionLock.current = true;
    setPlaying(false);
    setSelectedId(null);
    setChapterTransition(true);
    fullscreenTransitionTimers.current.push(window.setTimeout(() => {
      setStageIndex(index);
      requestAnimationFrame(() => fullscreenTransitionTimers.current.push(window.setTimeout(() => {
        setChapterTransition(false);
        fullscreenTransitionLock.current = false;
      }, 12)));
    }, 180));
  }, [stageIndex, stages.length]);
  useEffect(() => () => fullscreenTransitionTimers.current.forEach(window.clearTimeout), []);
  useEffect(() => {
    const query = window.matchMedia?.('(prefers-reduced-motion: reduce)');
    if (!query) return undefined;
    const update = event => setReducedMotion(event.matches);
    query.addEventListener?.('change', update);
    return () => query.removeEventListener?.('change', update);
  }, []);
  useEffect(() => {
    const apiBase = import.meta.env.VITE_API_BASE_URL?.replace(/\/$/, '') || '';
    if (!apiBase) return undefined;
    const controller = new AbortController();
    fetch(`${apiBase}/api/world`, { signal: controller.signal })
      .then(response => response.ok ? response.json() : Promise.reject(new Error('world api unavailable')))
      .then(data => {
        if (data?.revision && ['stages', 'regions', 'terrain', 'places', 'relations', 'domains', 'beasts'].every(key => Array.isArray(data[key]))
          && data.stages.length === mythWorld.stages.length && data.stages.every((stage, index) => stage.id === mythWorld.stages[index].id)) setWorld(data);
      })
      .catch(error => { if (error.name !== 'AbortError') console.info('使用随前端打包的神话地图数据'); });
    return () => controller.abort();
  }, []);
  useEffect(() => {
    if (!playing || journeyBusy) return undefined;
    if (stageIndex >= stages.length - 1) { setPlaying(false); return undefined; }
     const timer = window.setTimeout(() => setStageIndex(current => current + 1), reducedMotion ? 4000 : 1000);
    return () => window.clearTimeout(timer);
  }, [playing, stageIndex, stages.length, journeyBusy, reducedMotion]);
  useEffect(() => {
    const measure = () => {
      const layout = worldLayout.current;
      const rail = chapterRail.current;
      const main = worldMain.current;
      const timelineElement = timeline.current;
      if (!layout || !rail || !main || !timelineElement) return;
      const viewportWidth = window.visualViewport?.width || window.innerWidth;
      const viewportHeight = window.visualViewport?.height || window.innerHeight;
      const mobile = viewportWidth <= 640;
      const styles = getComputedStyle(layout);
      const paddingX = parseFloat(styles.paddingLeft) + parseFloat(styles.paddingRight);
      const paddingY = parseFloat(styles.paddingTop) + parseFloat(styles.paddingBottom);
      const gap = parseFloat(styles.columnGap || styles.gap) || 0;
      const timelineHeight = timelineElement.getBoundingClientRect().height;
      const railHeight = mobile ? rail.getBoundingClientRect().height : 0;
      const headerHeight = document.querySelector(".myth-header")?.getBoundingClientRect().height || 0;
      const availableHeight = viewportHeight - headerHeight - paddingY - timelineHeight - 16 - railHeight - (mobile && railHeight ? gap : 0);
      const availableWidth = mobile
        ? layout.clientWidth - paddingX
        : layout.clientWidth - paddingX - rail.getBoundingClientRect().width - gap;
      const mapHeight = Math.max(180, Math.min(760, availableHeight, availableWidth / 1.5));
      setLayoutMetrics(previous => Math.abs(previous.mapHeight - mapHeight) < 1 && Math.abs(previous.timelineHeight - timelineHeight) < 1
        ? previous
        : { mapHeight, timelineHeight });
    };
    const observer = new ResizeObserver(measure);
    [document.querySelector(".myth-header"), worldLayout.current, chapterRail.current, worldMain.current, timeline.current].filter(Boolean).forEach(element => observer.observe(element));
    const alignWorldAfterResize = () => {
      measure();
      requestAnimationFrame(() => {
        if (document.fullscreenElement || document.querySelector('.is-fallback-fullscreen')) return;
        const top = worldLayout.current?.getBoundingClientRect().top;
        if (window.location.hash === '#world' && Number.isFinite(top) && Math.abs(top) < 80) {
          window.scrollTo({ top: window.scrollY + top, behavior: 'instant' });
        }
      });
    };
    window.addEventListener('resize', alignWorldAfterResize);
    window.visualViewport?.addEventListener('resize', alignWorldAfterResize);
    measure();
    if (window.location.hash === '#world') requestAnimationFrame(() => {
      if (!document.fullscreenElement && !document.querySelector('.is-fallback-fullscreen')) worldLayout.current?.scrollIntoView({ block: 'start', behavior: 'instant' });
    });
    return () => {
      observer.disconnect();
      window.removeEventListener('resize', alignWorldAfterResize);
      window.visualViewport?.removeEventListener('resize', alignWorldAfterResize);
    };
  }, [railExpanded, stageIndex]);
  useEffect(() => {
    setRailExpanded(false);
  }, [stageIndex]);
  useEffect(() => {
    if (!selectedId) return undefined;
    const key = event => {
      const fullscreenActive = document.fullscreenElement || document.querySelector('.myth-map-wrap.is-fallback-fullscreen');
      if (event.key === 'Escape' && !fullscreenActive) closeDetail();
    };
    window.addEventListener('keydown', key);
    return () => window.removeEventListener('keydown', key);
  }, [selectedId, fullscreenTarget]);

  return <main className="myth-app">
    <header id="home" className="myth-header"><a href="#world"><span className="seal" aria-hidden="true">山</span><h1>山海寻踪</h1></a><nav aria-label="网站导航"><a href="#world">地图</a><a href="#creatures">异兽谱</a><a href="#reading-notes">读图与依据</a></nav></header>
     <section ref={worldLayout} className="world-layout" id="world" data-timeline-playing={playing} data-animation-busy={journeyBusy} style={{ '--myth-map-height': `${layoutMetrics.mapHeight}px`, '--myth-timeline-height': `${layoutMetrics.timelineHeight}px` }}>
      <aside ref={chapterRail} className="chapter-rail">
        <span className="chapter-number">{stageIndex === 0 ? "序章" : "第 " + stages[stageIndex].id + " 章"}</span><h2>{stages[stageIndex].title}</h2><p>{stages[stageIndex].subtitle}</p>
        <button className="rail-expand" aria-expanded={railExpanded} onClick={() => setRailExpanded(value => !value)}>{railExpanded ? '收起本章故事 ↑' : '展开本章故事 ↓'}</button>
        <div className="chapter-rail-details" data-expanded={railExpanded}>
          <div className="chapter-rule" /><b>本章故事</b><small>典籍来源沿用已有考据条目</small>
          {storyItems.map(item => <button className="story-entry" key={item.id} onClick={event => open(item.id, event.currentTarget)}><i>✦</i><span><b>{item.properties.name}</b><small>{item.properties.source_text || item.properties.basis_note}</small></span></button>)}
          <a className="best-index-link" href="#creatures">打开全书异兽索引 ↗</a>
        </div>
      </aside>
      <div ref={worldMain} className="world-main">
        <MapPanel world={world} stageIndex={stageIndex} autoPlayChapter={playing || autoPlayChapterId === stages[stageIndex].id} activeLayers={{ ...activeLayers, onBeasts: checked => setActiveLayers(state => ({ ...state, beasts: checked })), onDivine: checked => setActiveLayers(state => ({ ...state, divine: checked })), onGoToFirstBeast: () => { const index = stages.findIndex(stage => world.beasts.some(beast => beast.reveal_chapter === stage.id)); if (index >= 0) selectStage(index); } }} selectedId={selectedId} onSelect={open} onFullscreenTargetChange={setFullscreenTarget} onJourneyBusyChange={setJourneyBusy} onFullscreenStageChange={navigateFullscreenStage} chapterTransition={chapterTransition} />
        <Timeline containerRef={timeline} stages={stages} index={stageIndex} playing={playing} onSelect={selectStage} onPlay={() => { if (stageIndex === stages.length - 1 && !playing) setStageIndex(0); setPlaying(value => !value); }} />
      </div>
    </section>
    <Bestiary beasts={beasts} onOpen={open} />
    <section className="reading-notes" id="reading-notes" aria-labelledby="reading-notes-title"><h2 id="reading-notes-title">读图与依据</h2>          <div className="reading-notes-text"><p>《山海经》依山川和方位展开，不是编年史。序章与七章次序是本项目的叙事编排；各章内部仅在原文或可靠叙事关系可核实处排列先后，不代表精确年代。</p><p>经文距离不按比例绘制；淡墨山形为装饰。重要地点以名称和原文标识，故事示意点不表示真实位置。</p></div><p>各篇神域记载不预设为同一空间体系。异兽图标仅关联有篇目依据的地点锚点；缺少可靠地点依据的条目收录在异兽谱中。</p><p>山海空间与异兽描写以《山海经》正文条目为依据，神话故事沿用各条目所列典籍与出处。插画是本项目依据正文的图像解释，不作为古本插图或新增考据证据。</p></section>
    <footer className="myth-footer"><span>版式：方位关系与叙述次序 · 不设距离比例</span><span>山海空间与异兽描写：以《山海经》正文条目核对</span></footer>
    {selected && createPortal(<DetailDrawer selected={selected} onClose={closeDetail} onOpen={open} scrollTopRef={detailScrollTop} />, fullscreenTarget || document.body)}
  </main>;
}
