import { useLocale, localize } from './i18n';
import brandMark from './assets/shanhai-mark.svg?raw';
import { useCallback, useEffect, useMemo, useRef, useState } from 'react';
import { createPortal } from 'react-dom';
import rawCatalog from '../public/data/atlas/catalog.json';
import mythWorld from '../public/data/myth-world.json';
import animations from '../public/data/atlas/story-animations.json';
import kuafu from '../public/data/atlas/kuafu-journey.json';
import { chapterStoryIds } from './chapter-stories';
import MapPanel from './components/MapPanel';
import Timeline from './components/Timeline';
import ExploreSheet from './components/ExploreSheet';
import ChapterEntries from './components/ChapterEntries';
import Bestiary from './components/Bestiary';
import DetailDrawer from './components/DetailDrawer';
import GlobalSearch from './components/GlobalSearch';
import { assetUrl } from './asset-url';
import { CHAPTER_TRANSITION_MS, InkText, useReducedMotion } from './motion';
import { itemChapter, readExploration, explorationUrl } from './exploration';
import { validateWorld } from './world-validation';
import { useReading, useLastReading } from './reading';
import './styles/myth-world.css';
import './styles/exploration.css';
import './styles/atlas-layout.css';

export default function App() {
  const { t, locale, setLocale } = useLocale();
  const catalog = useMemo(() => localize(rawCatalog, locale), [locale]);
  const [rawWorld, setWorld] = useState(mythWorld);
  const world = useMemo(() => localize(rawWorld, locale), [rawWorld, locale]);
  const [initial] = useState(() => readExploration(window.location.search, mythWorld, rawCatalog));
  const [stageIndex, setStageIndex] = useState(initial.stageIndex);
  const [playing, setPlaying] = useState(false);
  const [journeyBusy, setJourneyBusy] = useState(false);
  const [playbackStatus, setPlaybackStatus] = useState('loading');
  const [tourActive, setTourActive] = useState(false);
  const [chapterTransition, setChapterTransition] = useState(0);
  const [titleAnimating, setTitleAnimating] = useState(false);
  const [activeLayers, setActiveLayers] = useState({ beasts: false, divine: false });
  const [selectedId, setSelectedId] = useState(initial.item);
  const [detailSequence, setDetailSequence] = useState(null);
  const reading = useReading();
  const lastReading = useLastReading();
  const [restoreReading, setRestoreReading] = useState(() => performance.getEntriesByType('navigation')[0]?.type === 'reload' && lastReading.resume?.id === initial.item ? lastReading.resume : null);
  const [fullscreenTarget, setFullscreenTarget] = useState(null);
  const [mapRecords, setMapRecords] = useState([]);
  const [mobile, setMobile] = useState(() => window.matchMedia('(max-width: 768px)').matches);
  const [panel, setPanel] = useState(null);
  const [searchOpen, setSearchOpen] = useState(false);
  const searchTrigger = useRef(null);
  useEffect(() => {
    const query = window.matchMedia('(max-width: 768px)');
    const change = event => { setMobile(event.matches); setPanel(null); };
    query.addEventListener('change', change);
    return () => query.removeEventListener('change', change);
  }, []);
  const [storyRequest, setStoryRequest] = useState({ chapterId: mythWorld.stages[initial.stageIndex].id, id: null, serial: 0 });
  const reducedMotion = useReducedMotion();
  const [guideVisible, setGuideVisible] = useState(() => {
    try { return localStorage.getItem('shanhai-guide-dismissed') !== '1'; } catch { return true; }
  });
  const [shareStatus, setShareStatus] = useState('');
  const [locateId, setLocateId] = useState(null);
  const worldLayout = useRef(null);
  const panelTrigger = useRef(null);
  const openPanel = (name, event) => { panelTrigger.current = event.currentTarget; setPanel(name); };
  const detailTrigger = useRef(null);
  const detailPageScroll = useRef([0, 0]);
  const transitionTimer = useRef(null);
  const titleTimer = useRef(null);
  const previousAnimatedChapter = useRef(initial.stageIndex);
  const transitionCount = useRef(0);
  const stages = world.stages;
  useEffect(() => {
    document.documentElement.lang = locale === 'en' ? 'en' : 'zh-CN';
    document.title = t('山海寻踪') + ' · ' + t('一卷山海，七章神话');
    document.querySelector('meta[name="description"]')?.setAttribute('content', locale === 'en'
      ? 'An illustrated atlas of Chinese mythology: explore seven narrative chapters, mythical creatures and their textual sources.'
      : '由《山海经》篇目方位关系和七章神话叙事构成的互动山海图。');
  }, [locale, t]);
  const beasts = useMemo(() => world.beasts.map((beast, groupIndex) => ({ ...beast, stage: beast.reveal_stage, groupIndex })), [world.beasts]);
  const places = useMemo(() => world.places.map(place => ({ ...place, stage: place.reveal_stage })), [world.places]);
  const domains = world.domains;
  const entryIndex = useMemo(() => new Map([
    ...world.beasts, ...world.places, ...world.domains,
    ...catalog.events.map(item => ({ id: item.id, name: item.properties.name, source: item.properties.source_text })),
  ].map(item => [item.id, item])), [world, catalog]);
  const collectionItems = reading.favorites.map(id => entryIndex.get(id)).filter(Boolean);
  const resumeEntry = lastReading.resume && entryIndex.get(lastReading.resume.id);
  const storyOrder = new Map((catalog.stages.find(stage => stage.id === stages[stageIndex].id)?.event_ids || []).map((id, index) => [id, index]));
  const storyItems = (catalog.events || []).filter(item => item.properties.stage_id === stages[stageIndex].id && !['archive', 'group'].includes(item.properties.presentation))
    .sort((a, b) => (storyOrder.get(a.id) ?? Number.MAX_SAFE_INTEGER) - (storyOrder.get(b.id) ?? Number.MAX_SAFE_INTEGER));
  const chapterId = stages[stageIndex].id;
  const storyIds = useMemo(() => chapterStoryIds(chapterId, rawCatalog, animations, kuafu), [chapterId]);
  const readingChapter = tourActive && storyIds.length === 0;
  const storyNumber = storyIds.indexOf(storyRequest.id);
  const requestStory = (id, chapter = chapterId) => setStoryRequest(previous => ({ chapterId: chapter, id, serial: previous.serial + 1 }));
  const selected = useMemo(() => {
    const domain = domains.find(item => item.id === selectedId);
    if (domain) {
      const place = places.find(item => item.id === domain.place_id);
      return { ...domain, description: domain.quote, region: domain.source, direction: place.direction, kind: 'domain' };
    }
    const creature = beasts.find(item => item.id === selectedId);
    if (creature) return { ...creature, direction: creature.place_basis };
    const place = places.find(item => item.id === selectedId);
    if (place) return place;
    const raw = (catalog.events || []).find(item => item.id === selectedId);
    if (raw) return { id: raw.id, kind: 'story', name: raw.properties.name, source: raw.properties.source_text, description: raw.properties.source_quote, region: raw.properties.location_label || raw.properties.basis_note, direction: raw.properties.basis_note, url: raw.properties.source_url, artwork: raw.properties.artwork, artworks: raw.properties.artworks, raw };
    return null;
  }, [selectedId, world, catalog, beasts, places]);
  const open = (id, trigger, sequence) => {
    setRestoreReading(null);
    setPanel(null);
    if (!selectedId) detailPageScroll.current = [window.scrollX, window.scrollY];
    if (!selectedId) detailTrigger.current = trigger || null;
    if (sequence || !selectedId) setDetailSequence(sequence || null);
    setSelectedId(id);
  };
  const fallbackSequence = selected?.kind === 'story'
    ? (catalog.events || []).filter(item => item.properties.stage_id === selected.raw.properties.stage_id && (!['archive', 'group'].includes(item.properties.presentation) || item.id === selectedId))
      .sort((a, b) => {
        const order = catalog.stages.find(stage => stage.id === selected.raw.properties.stage_id)?.event_ids || [];
        const rank = id => order.includes(id) ? order.indexOf(id) : Number.MAX_SAFE_INTEGER;
        return rank(a.id) - rank(b.id);
      }).map(item => item.id)
    : selected?.kind === 'domain' ? domains.map(item => item.id)
      : beasts.some(item => item.id === selectedId) ? beasts.map(item => item.id) : places.map(item => item.id);
  const detailIds = detailSequence?.includes(selectedId) ? detailSequence : fallbackSequence;
  const detailIndex = detailIds.indexOf(selectedId);
  const detailNavigation = { index: detailIndex, total: detailIds.length, previous: entryIndex.get(detailIds[detailIndex - 1]), next: entryIndex.get(detailIds[detailIndex + 1]) };
  const chapterForLink = () => {
    const related = selectedId && itemChapter(selectedId, world, catalog);
    return selected?.kind === 'story' || related && Number(related) > Number(chapterId) ? related : chapterId;
  };
  const closeDetail = () => {
    setSelectedId(null);
    requestAnimationFrame(() => {
      if (detailTrigger.current?.isConnected) detailTrigger.current.focus({ preventScroll: true });
      else if (panelTrigger.current?.isConnected) panelTrigger.current.focus({ preventScroll: true });
      else document.querySelector('.myth-map-wrap')?.focus({ preventScroll: true });
      window.scrollTo({ left: detailPageScroll.current[0], top: detailPageScroll.current[1], behavior: 'instant' });
    });
  };
  const selectStage = index => { requestStory(null, stages[index].id); setPlaying(false); setTourActive(false); if (index !== stageIndex) setPlaybackStatus('loading'); setStageIndex(index); setSelectedId(null); setLocateId(null); setPanel(null); };
  const navigateFullscreenStage = useCallback(index => {
    if (index < 0 || index >= stages.length) return;
    setStoryRequest(previous => ({ chapterId: stages[index].id, id: null, serial: previous.serial + 1 }));
    setPlaying(false); setTourActive(false); setPlaybackStatus('loading'); setSelectedId(null); setStageIndex(index); setLocateId(null);
  }, [stages]);
  const continueReading = event => {
    const record = lastReading.resume;
    if (!record || !resumeEntry) return;
    const index = stages.findIndex(stage => stage.id === record.chapter);
    if (index !== stageIndex) selectStage(index);
    open(record.id, event.currentTarget);
    setRestoreReading(record);
  };
  const relatedChapter = selected && itemChapter(selected.id, world, catalog);
  const mapPlace = selected && (places.find(place => place.id === selected.id) || places.find(place => place.id === selected.place_id));
  const canLocate = Boolean(mapPlace || selected?.raw?.properties.map_visible && selected.raw.properties.layout_hint?.every(Number.isFinite));
  const navigateDetail = (chapter, locate = false) => {
    const id = selectedId;
    setPlaying(false); setTourActive(false); requestStory(null, chapter);
    setStageIndex(Math.max(0, stages.findIndex(stage => stage.id === chapter)));
    if (locate) setActiveLayers(value => ({ ...value, beasts: value.beasts || beasts.some(beast => beast.id === id), divine: value.divine || domains.some(domain => domain.id === id) }));
    closeDetail(); setLocateId(locate ? id : null);
    requestAnimationFrame(() => worldLayout.current?.scrollIntoView({ block: 'start', behavior: reducedMotion ? 'instant' : 'smooth' }));
  };
  useEffect(() => {
    if (previousAnimatedChapter.current === stageIndex) return;
    previousAnimatedChapter.current = stageIndex;
    window.clearTimeout(transitionTimer.current);
    window.clearTimeout(titleTimer.current);
    setTitleAnimating(true);
    setChapterTransition(++transitionCount.current);
    transitionTimer.current = window.setTimeout(() => setChapterTransition(0), CHAPTER_TRANSITION_MS);
    titleTimer.current = window.setTimeout(() => setTitleAnimating(false), 700);
  }, [stageIndex]);
  useEffect(() => {
    window.clearTimeout(titleTimer.current);
    setTitleAnimating(false);
  }, [locale]);
  useEffect(() => () => { window.clearTimeout(transitionTimer.current); window.clearTimeout(titleTimer.current); }, []);
  useEffect(() => {
    const url = explorationUrl(window.location.href, chapterForLink(), selectedId, locale);
    url.hash = window.location.hash;
    window.history.replaceState(null, '', url);
    setShareStatus('');
  }, [stageIndex, selectedId, locale, stages]);
  useEffect(() => {
    const restore = () => {
      const next = readExploration(window.location.search, mythWorld, rawCatalog);
      setPlaying(false); setTourActive(false); setLocateId(null); setDetailSequence(null); setRestoreReading(null); setSearchOpen(false);
      setStoryRequest(previous => ({ chapterId: mythWorld.stages[next.stageIndex].id, id: null, serial: previous.serial + 1 }));
      setStageIndex(next.stageIndex); setSelectedId(next.item);
    };
    window.addEventListener('popstate', restore);
    return () => window.removeEventListener('popstate', restore);
  }, []);
  const dismissGuide = () => {
    setGuideVisible(false);
    try { localStorage.setItem('shanhai-guide-dismissed', '1'); } catch {}
  };
  const enterTourChapter = index => {
    const id = stages[index].id;
    const sequence = chapterStoryIds(id, rawCatalog, animations, kuafu);
    setPlaybackStatus('loading'); setStageIndex(index); setSelectedId(null); setLocateId(null);
    requestStory(sequence[0] || null, id); setPlaying(sequence.length > 0);
  };
  const toggleTour = () => {
    dismissGuide(); setPanel(null);
    if (readingChapter) {
      if (stageIndex === stages.length - 1) { setPlaying(false); setTourActive(false); }
      else enterTourChapter(stageIndex + 1);
      return;
    }
    if (tourActive) { setPlaying(value => !value); return; }
    setTourActive(true);
    enterTourChapter(stageIndex === stages.length - 1 ? 0 : stageIndex);
  };
  const manualStory = () => { setTourActive(false); setPlaying(false); };
  const share = async () => {
    const url = explorationUrl(window.location.href, chapterForLink(), selectedId, locale);
    try { await navigator.clipboard.writeText(url.href); setShareStatus('链接已复制'); }
    catch { setShareStatus(url.href); }
  };
  useEffect(() => {
    const apiBase = import.meta.env.VITE_API_BASE_URL?.replace(/\/$/, '') || '';
    if (!import.meta.env.DEV && !apiBase) return undefined;
    const controller = new AbortController();
    fetch(`${apiBase}/api/world`, { signal: controller.signal })
      .then(response => response.ok ? response.json() : Promise.reject(new Error('world api unavailable')))
      .then(data => {
        validateWorld(data, mythWorld);
        setWorld(data);
      })
      .catch(error => { if (error.name !== 'AbortError') console.info(t("使用随前端打包的神话地图数据"), error.message); });
    return () => controller.abort();
  }, []);
  useEffect(() => {
    if (!tourActive || !playing || selectedId || searchOpen || !storyIds.length || !['completed', 'idle'].includes(playbackStatus) || storyRequest.chapterId !== chapterId) return undefined;
    const timer = window.setTimeout(() => {
      const next = storyIds.indexOf(storyRequest.id) + 1;
      if (next < storyIds.length) { setPlaybackStatus('loading'); requestStory(storyIds[next]); }
      else if (stageIndex < stages.length - 1) enterTourChapter(stageIndex + 1);
      else { setPlaying(false); setTourActive(false); }
    }, 1000);
    return () => window.clearTimeout(timer);
  }, [tourActive, playing, selectedId, searchOpen, playbackStatus, storyRequest, chapterId, storyIds, stageIndex, stages]);
  useEffect(() => {
    if (!selectedId) return undefined;
    const key = event => {
      const fullscreenActive = document.fullscreenElement || document.querySelector('.myth-map-wrap.is-fallback-fullscreen');
      if (event.key === 'Escape' && !fullscreenActive) closeDetail();
    };
    window.addEventListener('keydown', key);
    return () => window.removeEventListener('keydown', key);
  }, [selectedId, fullscreenTarget]);

  const chapterEntries = <ChapterEntries stories={storyItems} records={mapRecords} onOpen={open} reading={reading} collectionItems={collectionItems} />;
  const chapterNavigation = <Timeline stages={stages} index={stageIndex} onSelect={selectStage} />;
  const tourLabel = readingChapter ? stageIndex === stages.length - 1 ? '结束游历' : '阅读完毕，下一章' : tourActive ? playing ? '暂停游历' : '继续游历' : '连续游历';
  const readingNote = readingChapter ? <div className="tour-reading"><p>{t('本章以文字为主，请阅读条目后继续。')}</p><button type="button" onClick={toggleTour}>{t(tourLabel)}</button></div> : null;
  return <main className="myth-app" lang={locale === "en" ? "en" : "zh-CN"}>
    <header id="home" className="myth-header"><a href="#world"><span className="seal" aria-hidden="true" dangerouslySetInnerHTML={{ __html: brandMark }} /><h1>{t("山海寻踪")}</h1></a><nav aria-label={t("网站导航")}><a href="#world">{t("地图")}</a><a href="#creatures">{t("异兽谱")}</a><a href="#reading-notes">{t("读图与依据")}</a><button ref={searchTrigger} className="global-search-trigger" type="button" aria-label={t("搜索故事、异兽与出处")} onClick={() => setSearchOpen(true)}>{t("搜索")}</button><div className="language-switch" role="group" aria-label={locale === "en" ? "Language" : "语言"}><button type="button" lang="zh-CN" aria-pressed={locale === "zh"} onClick={() => setLocale("zh")}>中文</button><button type="button" lang="en" aria-pressed={locale === "en"} onClick={() => setLocale("en")}>EN</button></div></nav></header>
     <section ref={worldLayout} className="world-layout" id="world" data-chapter={stages[stageIndex].id} data-timeline-playing={playing} data-animation-busy={journeyBusy} data-tour-active={tourActive} data-tour-reading={readingChapter}>
      <aside className="chapter-rail">
        <span className="chapter-number">{stageIndex === 0 ? t("序章") : t("第 ") + stages[stageIndex].id + t(" 章")}</span><h2><InkText key={stages[stageIndex].id} text={stages[stageIndex].title} animate={previousAnimatedChapter.current !== stageIndex || titleAnimating} /></h2><p><InkText key={stages[stageIndex].id} text={stages[stageIndex].subtitle} variant="subtitle" animate={previousAnimatedChapter.current !== stageIndex || titleAnimating} /></p>
        <div className="rail-exploration">
          {!selectedId && resumeEntry && <button className="resume-reading" type="button" onClick={continueReading}><span>{t("继续上次阅读")}</span><small>{resumeEntry.name}</small></button>}
          <button className="begin-journey" type="button" aria-pressed={tourActive && playing} onClick={toggleTour}>{t(tourLabel)}</button>
          {tourActive && <p className="tour-progress" role="status">{readingChapter ? t('本章以文字为主，请阅读条目后继续。') : t('本章故事') + ` ${Math.max(1, storyNumber + 1)} / ${storyIds.length}`}</p>}
          {guideVisible && <div className="exploration-guide"><p>{t('章节 → 标记 → 原文')}</p><button type="button" aria-label={t('关闭引导')} onClick={dismissGuide}>×</button></div>}
        </div>
        <div className="chapter-rail-details">{!mobile && <><h3>{t('本章条目')}</h3>{chapterEntries}</>}</div>
      </aside>
      <div className="world-main">
        <MapPanel pausedForOverlay={searchOpen} reading={reading} collectionItems={collectionItems} tourPlaying={tourActive ? playing : null} onTourPlaybackChange={setPlaying} onPlaybackChange={setPlaybackStatus} storyItems={storyItems} onRecordsChange={setMapRecords} onShare={share} shareStatus={shareStatus} locateId={locateId} world={world} stageIndex={stageIndex} storyRequest={storyRequest} onManualStoryChange={manualStory} readingNote={readingNote} activeLayers={{ ...activeLayers, onBeasts: checked => setActiveLayers(state => ({ ...state, beasts: checked })), onDivine: checked => setActiveLayers(state => ({ ...state, divine: checked })), onGoToFirstBeast: () => { const index = stages.findIndex(stage => world.beasts.some(beast => beast.reveal_chapter === stage.id)); if (index >= 0) selectStage(index); } }} selectedId={selectedId} onSelect={open} onFullscreenTargetChange={setFullscreenTarget} onJourneyBusyChange={setJourneyBusy} onFullscreenStageChange={navigateFullscreenStage} chapterTransition={chapterTransition} />
        {!mobile && chapterNavigation}
        <nav className="mobile-explore-nav" aria-label={t('探索面板')}>
          <button onClick={event => openPanel('chapters', event)}>{t('章节')}</button>
          <button onClick={event => openPanel('entries', event)}>{t('本章条目')}</button>
        </nav>

      </div>
    </section>
    {mobile && panel && <ExploreSheet returnFocus={panelTrigger.current} title={t({ chapters: '章节', entries: '本章条目' }[panel])} onClose={() => setPanel(null)}>{panel === 'chapters' ? chapterNavigation : chapterEntries}</ExploreSheet>}
    <Bestiary beasts={beasts} onOpen={open} reading={reading} />
    <section className="reading-notes" id="reading-notes" aria-labelledby="reading-notes-title"><h2 id="reading-notes-title">{t("读图与依据")}</h2><div className="reading-notes-body"><div className="reading-notes-copy"><div className="reading-notes-text"><p>{t("《山海经》依山川和方位展开，不是编年史。序章与七章次序是本项目的叙事编排；各章内部仅在原文或可靠叙事关系可核实处排列先后，不代表精确年代。")}</p><p>{t("经文距离不按比例绘制；淡墨山形为装饰。重要地点以名称和原文标识，故事示意点不表示真实位置。")}</p></div><p>{t("各篇神域记载不预设为同一空间体系。异兽图标仅关联有篇目依据的地点锚点；缺少可靠地点依据的条目收录在异兽谱中。")}</p><p>{t("山海空间与异兽描写以《山海经》正文条目为依据，神话故事沿用各条目所列典籍与出处。插画是本项目依据正文的图像解释，不作为古本插图或新增考据证据。")}</p></div><figure className="reading-bookplate"><span className="bookplate-mark" aria-hidden="true" style={{ maskImage: `url(${assetUrl('/data/atlas/optimized/shanhai-bookplate.webp')})` }} /><figcaption>{t("山海寻踪")}<small>{t("藏书印")}</small></figcaption></figure></div></section>
    <footer className="myth-footer"><span>{t("版式：方位关系与叙述次序 · 不设距离比例")}</span><span>{t("山海空间与异兽描写：以《山海经》正文条目核对")}</span></footer>
    <GlobalSearch open={searchOpen} onClose={() => setSearchOpen(false)} returnFocus={searchTrigger.current} world={world} catalog={catalog} onChoose={(id, ids) => { setSearchOpen(false); open(id, searchTrigger.current, ids); }} />
    {selected && createPortal(<DetailDrawer reading={reading} navigation={detailNavigation} selected={selected} onClose={closeDetail} onOpen={open} restoreReading={restoreReading} onSaveReading={lastReading.save} readingChapter={chapterForLink()} resumeSaveFailed={lastReading.saveFailed} relatedChapter={relatedChapter} canLocate={canLocate} onNavigate={navigateDetail} onShare={share} shareStatus={shareStatus} />, fullscreenTarget || document.body)}
  </main>;
}
