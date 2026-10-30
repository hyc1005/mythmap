import { useLocale, localize } from './i18n';
import brandMark from './assets/shanhai-mark.svg?raw';
import { useCallback, useEffect, useLayoutEffect, useMemo, useRef, useState } from 'react';
import { createPortal } from 'react-dom';
import rawCatalog from '../public/data/atlas/catalog.json';
import mythWorld from '../public/data/myth-world.json';
import animations from '../public/data/atlas/story-animations.json';
import kuafu from '../public/data/atlas/kuafu-journey.json';
import { defaultGeographicEvent, geographicReferences } from './geography';
import { animationForEvent, chapterStoryIds } from './chapter-stories';
import { relatedEntries } from './entry-relations';
import { worldEntries } from './entries';
import MapPanel from './components/MapPanel';
import Timeline from './components/Timeline';
import ExploreSheet from './components/ExploreSheet';
import ChapterEntries from './components/ChapterEntries';
import Bestiary from './components/Bestiary';
import DetailDrawer from './components/DetailDrawer';
import GlobalSearch from './components/GlobalSearch';
import OnboardingGuide from './components/OnboardingGuide';
import { assetUrl } from './asset-url';
import { CHAPTER_TRANSITION_MS, InkText, useReducedMotion } from './motion';
import { itemChapter, readExploration, readGeography, explorationUrl } from './exploration';
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
  const [initialGeography] = useState(() => readGeography(window.location.search, mythWorld.stages[initial.stageIndex].id, rawCatalog, geographicReferences(rawCatalog)));
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
  const [searchState, setSearchState] = useState({ query: '', kind: 'all', limit: 40, scrollTop: 0, focusKey: null });
  const [detailFromSearch, setDetailFromSearch] = useState(false);
  const [detailParentId, setDetailParentId] = useState(null);
  const [detailReturnFocusKey, setDetailReturnFocusKey] = useState(null);
  const [playbackReturnId, setPlaybackReturnId] = useState(null);
  const historySnapshot = useRef(null), historyIntent = useRef(null), incomingMapEvent = useRef(undefined);
  const searchTrigger = useRef(null);
  const geographySnapshot = useRef({});
  const [geographyOpen, setGeographyOpen] = useState(initialGeography.open);
  const [geographyEventId, setGeographyEventId] = useState(initialGeography.eventId || (rawCatalog.events.some(event => event.id === initial.item) ? initial.item : null));
  const [geographyReferenceId, setGeographyReferenceId] = useState(initialGeography.referenceId);
  const [geographyFromSearch, setGeographyFromSearch] = useState(false);
  const [geographyLocateRequest, setGeographyLocateRequest] = useState(null);
  const geographyEventRef = useRef(geographyEventId);
  geographyEventRef.current = geographyEventId;
  const mapEventChanged = useCallback(id => {
    if (incomingMapEvent.current === id) return;
    const first = incomingMapEvent.current === undefined;
    incomingMapEvent.current = id;
    if (id && id !== geographyEventRef.current && !(first && initialGeography.eventId)) {
      setGeographyEventId(id); setGeographyReferenceId(null);
    }
  }, []);
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
  const [onboardingOpen, setOnboardingOpen] = useState(() => {
    if (initial.shared || initialGeography.open || lastReading.resume) return false;
    try { return localStorage.getItem('shanhai-onboarding-v1') !== '1'; } catch { return true; }
  });
  const guideTrigger = useRef(null);
  const [locateId, setLocateId] = useState(null);
  const worldLayout = useRef(null);
  const panelTrigger = useRef(null);
  const openPanel = (name, event) => { panelTrigger.current = event.currentTarget; setPanel(name); };
  const detailTrigger = useRef(null);
  const pendingDetailFocus = useRef(false);
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
    ...worldEntries(world),
    ...catalog.events.map(item => ({ id: item.id, name: item.properties.name, source: item.properties.source_text, entryType: '故事' })),
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
    if (creature) return { ...creature, kind: 'beast', direction: creature.place_basis };
    const place = places.find(item => item.id === selectedId);
    if (place) return { ...place, kind: 'place' };
    const natural = world.natural_features.find(item => item.id === selectedId);
    if (natural) return natural;
    const passage = world.passages.find(item => item.id === selectedId);
    if (passage) return passage;
    const textEntity = world.text_entities.find(item => item.id === selectedId);
    if (textEntity) return textEntity;
    const raw = (catalog.events || []).find(item => item.id === selectedId);
    if (raw) return { id: raw.id, kind: 'story', name: raw.properties.name, source: raw.properties.source_text, description: raw.properties.source_quote, region: raw.properties.location_label || raw.properties.basis_note, direction: raw.properties.basis_note, url: raw.properties.source_url, artwork: raw.properties.artwork, artworks: raw.properties.artworks, raw };
    return null;
  }, [selectedId, world, catalog, beasts, places]);
  const open = (id, trigger, sequence) => {
    setRestoreReading(null);
    setDetailReturnFocusKey(null);
    if (!selectedId) setDetailParentId(null);
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
    : selected?.kind === 'passage' ? world.passages.filter(item => (item.source_book || 1) === (selected.source_book || 1)).map(item => item.id)
      : selected?.kind === 'domain' ? domains.map(item => item.id)
      : beasts.some(item => item.id === selectedId) ? beasts.map(item => item.id)
        : worldEntries(world).filter(item => item.kind === selected?.kind).map(item => item.id);
  const detailIds = detailSequence?.includes(selectedId) ? detailSequence : fallbackSequence;
  const detailIndex = detailIds.indexOf(selectedId);
  const detailNavigation = { index: detailIndex, total: detailIds.length, previous: entryIndex.get(detailIds[detailIndex - 1]), next: entryIndex.get(detailIds[detailIndex + 1]) };
  const chapterForLink = () => {
    const related = selectedId && itemChapter(selectedId, world, catalog);
    const contextChapter = selected?.context_place_id && itemChapter(selected.context_place_id, world, catalog);
    if (contextChapter && Number(contextChapter) <= Number(chapterId)) return chapterId;
    return selected?.kind === 'story' || related && Number(related) > Number(chapterId) ? related : chapterId;
  };
  const closeDetail = (returnToOrigin = true) => {
    pendingDetailFocus.current = true;
    if (returnToOrigin !== false && window.history.state?.shanhai?.detailEntry) { window.history.back(); return; }
    historyIntent.current = 'replace';
    setSelectedId(null);
    setDetailParentId(null); setDetailReturnFocusKey(null);
    if (returnToOrigin !== false && detailFromSearch) setSearchOpen(true);
    setDetailFromSearch(false);
  };
  useLayoutEffect(() => {
    if (selectedId || !pendingDetailFocus.current) return;
    pendingDetailFocus.current = false;
    if (detailTrigger.current?.isConnected) detailTrigger.current.focus({ preventScroll: true });
    else if (panelTrigger.current?.isConnected) panelTrigger.current.focus({ preventScroll: true });
    else document.querySelector('.myth-map-wrap')?.focus({ preventScroll: true });
    window.scrollTo({ left: detailPageScroll.current[0], top: detailPageScroll.current[1], behavior: 'instant' });
  }, [selectedId]);
  const selectStage = index => { requestStory(null, stages[index].id); setPlaying(false); setTourActive(false); setPlaybackReturnId(null); if (index !== stageIndex) setPlaybackStatus('loading'); setStageIndex(index); setSelectedId(null); setLocateId(null); setPanel(null); setGeographyEventId(defaultGeographicEvent(catalog, stages[index].id)); setGeographyReferenceId(null); };
  const navigateFullscreenStage = useCallback(index => {
    if (index < 0 || index >= stages.length) return;
    setStoryRequest(previous => ({ chapterId: stages[index].id, id: null, serial: previous.serial + 1 }));
    setPlaying(false); setTourActive(false); setPlaybackStatus('loading'); setSelectedId(null); setStageIndex(index); setLocateId(null);
    setPlaybackReturnId(null);
    setGeographyEventId(defaultGeographicEvent(rawCatalog, stages[index].id)); setGeographyReferenceId(null);
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
  const selectedAnimationId = selected?.kind === 'story' ? animationForEvent(selected.id, rawCatalog, animations, kuafu) : null;
  const rememberDetail = (record, focusKey) => {
    lastReading.save(record);
    const saved = { ...window.history.state?.shanhai, readingPosition: record, detailFocusKey: focusKey };
    window.history.replaceState({ ...window.history.state, shanhai: saved }, '', window.location.href);
    historySnapshot.current = saved;
  };
  const openRelated = (id, record) => {
    rememberDetail(record, id); historyIntent.current = 'push';
    setDetailParentId(selectedId); setDetailReturnFocusKey(null); setRestoreReading(null); setDetailSequence(null); setSelectedId(id);
  };
  const playDetail = record => {
    if (!selectedAnimationId) return;
    rememberDetail(record, 'play'); historyIntent.current = 'push';
    pendingDetailFocus.current = false;
    setPlaybackReturnId(record.id); setDetailParentId(null); setDetailReturnFocusKey(null); setSelectedId(null); setDetailFromSearch(false);
    setStageIndex(stages.findIndex(stage => stage.id === record.chapter)); setGeographyOpen(false); setGeographyEventId(record.id); setGeographyReferenceId(null); setLocateId(null);
    setTourActive(false); setPlaying(true); setPlaybackStatus('loading'); requestStory(selectedAnimationId, record.chapter);
    requestAnimationFrame(() => { worldLayout.current?.scrollIntoView({ block: 'start', behavior: 'instant' }); document.querySelector('.myth-map-wrap')?.focus({ preventScroll: true }); });
  };
  const navigateDetail = (chapter, locate = false) => {
    const id = selectedId;
    setPlaying(false); setTourActive(false); requestStory(null, chapter);
    setStageIndex(Math.max(0, stages.findIndex(stage => stage.id === chapter)));
    if (locate) setActiveLayers(value => ({ ...value, beasts: value.beasts || beasts.some(beast => beast.id === id), divine: value.divine || domains.some(domain => domain.id === id) }));
    if (rawCatalog.events.some(event => event.id === id)) { setGeographyEventId(id); setGeographyReferenceId(null); }
    closeDetail(false); setDetailFromSearch(false); setLocateId(locate ? id : null);
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
  const currentGeographyEvent = defaultGeographicEvent(catalog, chapterId, geographyEventId);
  const detailPlace = detailFromSearch && geographicReferences(catalog).find(record => `geography:${record.id}` === searchState.focusKey && record.properties.entity_id === selectedId);
  const openPlace = () => {
    if (!detailPlace) return;
    const chapter = itemChapter(selectedId, mythWorld, rawCatalog);
    setPlaying(false); setTourActive(false); setPlaybackReturnId(null); setSelectedId(null); setDetailFromSearch(false); setDetailParentId(null); setDetailSequence(null); setLocateId(null);
    setStageIndex(stages.findIndex(stage => stage.id === chapter)); requestStory(null, chapter);
    setGeographyEventId(detailPlace.properties.entity_id); setGeographyReferenceId(detailPlace.id); setGeographyOpen(true); setGeographyFromSearch(true);
    setGeographyLocateRequest(previous => ({ id: detailPlace.id, serial: (previous?.serial || 0) + 1 }));
  };
  const linkChapter = chapterForLink();
  const geographicLink = { open: geographyOpen, eventId: linkChapter === chapterId ? currentGeographyEvent : defaultGeographicEvent(catalog, linkChapter, selectedId), referenceId: linkChapter === chapterId ? geographyReferenceId : null };
  useEffect(() => {
    const previous = historySnapshot.current;
    const next = { stageIndex, item: selectedId, searchOpen, searchState, fromSearch: detailFromSearch, sequence: detailSequence,
      geographyOpen, eventId: currentGeographyEvent, referenceId: geographyReferenceId,
      geographyFromSearch,
      parentId: detailParentId, playbackReturnId,
      readingPosition: previous?.item === selectedId ? previous?.readingPosition : null,
      detailFocusKey: previous?.item === selectedId ? previous?.detailFocusKey : null,
      detailEntry: Boolean(selectedId && previous && (!previous.item || previous.detailEntry || historyIntent.current === 'push')),
      searchEntry: Boolean(searchOpen && previous && (!previous.searchOpen || previous.searchEntry)) };
    const changed = previous && (previous.stageIndex !== stageIndex || Boolean(previous.item) !== Boolean(selectedId)
      || previous.searchOpen !== searchOpen || previous.geographyOpen !== geographyOpen
      || geographyOpen && (previous.eventId !== currentGeographyEvent || previous.referenceId !== geographyReferenceId));
    const url = explorationUrl(window.location.href, chapterForLink(), selectedId, locale, geographicLink);
    url.hash = window.location.hash;
    const method = historyIntent.current === 'push' || changed && historyIntent.current !== 'replace' ? 'pushState' : 'replaceState';
    window.history[method]({ ...window.history.state, shanhai: next }, '', url);
    historySnapshot.current = next; historyIntent.current = null;
  }, [stageIndex, selectedId, locale, searchOpen, searchState, detailFromSearch, detailSequence, geographyOpen, currentGeographyEvent, geographyReferenceId, detailParentId, playbackReturnId, geographyFromSearch]);
  useEffect(() => {
    const restore = () => {
      const language = new URLSearchParams(window.location.search).get('lang');
      if (language === 'zh' || language === 'en') setLocale(language);
      const next = readExploration(window.location.search, mythWorld, rawCatalog);
      const saved = window.history.state?.shanhai;
      const index = saved && mythWorld.stages[saved.stageIndex] ? saved.stageIndex : next.stageIndex;
      const geographicSearch = saved ? new URLSearchParams({ mode: saved.geographyOpen ? 'geography' : '', event: saved.eventId || '', reference: saved.referenceId || '' }).toString() : window.location.search;
      const geo = readGeography(geographicSearch, mythWorld.stages[index].id, rawCatalog, geographicReferences(rawCatalog));
      const previous = historySnapshot.current;
      const sameScene = previous?.stageIndex === index && previous.geographyOpen === geo.open
        && (!geo.open || previous.eventId === (geo.eventId || saved?.eventId));
      historySnapshot.current = saved || null; historyIntent.current = 'replace';
      pendingDetailFocus.current = true;
      if (!sameScene) { setPlaying(false); setTourActive(false); setLocateId(null); }
      setDetailSequence(saved?.sequence || null); setRestoreReading(saved?.readingPosition?.id === next.item ? saved.readingPosition : null);
      setDetailParentId(saved?.parentId || null); setDetailReturnFocusKey(saved?.detailFocusKey || null); setPlaybackReturnId(saved?.playbackReturnId || null);
      setSearchOpen(Boolean(saved?.searchOpen)); setDetailFromSearch(Boolean(saved?.fromSearch));
      if (saved?.searchState) setSearchState(saved.searchState);
      setGeographyOpen(geo.open); setGeographyEventId(geo.eventId || saved?.eventId || null); setGeographyReferenceId(geo.referenceId);
      setGeographyFromSearch(Boolean(saved?.geographyFromSearch));
      setGeographyLocateRequest(null);
      if (!sameScene) setStoryRequest(previous => ({ chapterId: mythWorld.stages[index].id, id: null, serial: previous.serial + 1 }));
      setStageIndex(index); setSelectedId(next.item);
    };
    window.addEventListener('popstate', restore);
    return () => window.removeEventListener('popstate', restore);
  }, []);
  const dismissGuide = () => {
    setGuideVisible(false);
    try { localStorage.setItem('shanhai-guide-dismissed', '1'); } catch {}
  };
  const startGuide = event => { guideTrigger.current = event.currentTarget; setOnboardingOpen(true); };
  const finishGuide = () => {
    setOnboardingOpen(false); dismissGuide();
    try { localStorage.setItem('shanhai-onboarding-v1', '1'); } catch {}
  };
  const enterTourChapter = index => {
    const id = stages[index].id;
    const sequence = chapterStoryIds(id, rawCatalog, animations, kuafu);
    setPlaybackStatus('loading'); setStageIndex(index); setSelectedId(null); setLocateId(null); setPlaybackReturnId(null);
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
  const manualStory = () => { setTourActive(false); setPlaying(false); setPlaybackReturnId(null); };
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
    if (!tourActive || !playing || selectedId || searchOpen || onboardingOpen || geographyOpen || chapterTransition || !storyIds.length || !['completed', 'idle'].includes(playbackStatus) || storyRequest.chapterId !== chapterId) return undefined;
    const timer = window.setTimeout(() => {
      const next = storyIds.indexOf(storyRequest.id) + 1;
      if (next < storyIds.length) { setPlaybackStatus('loading'); requestStory(storyIds[next]); }
      else if (stageIndex < stages.length - 1) enterTourChapter(stageIndex + 1);
      else { setPlaying(false); setTourActive(false); }
    }, 1000);
    return () => window.clearTimeout(timer);
  }, [tourActive, playing, selectedId, searchOpen, onboardingOpen, geographyOpen, playbackStatus, storyRequest, chapterId, storyIds, stageIndex, stages, chapterTransition]);
  useEffect(() => {
    if (!selectedId) return undefined;
    const key = event => {
      const fullscreenActive = document.fullscreenElement || document.querySelector('.myth-map-wrap.is-fallback-fullscreen');
      if (event.key === 'Escape' && !fullscreenActive) closeDetail();
    };
    window.addEventListener('keydown', key);
    return () => window.removeEventListener('keydown', key);
  }, [selectedId, fullscreenTarget]);

  const chapterEntries = <ChapterEntries stories={storyItems} records={mapRecords} passageEntries={world.passages.filter(item => Number(item.reveal_chapter) <= Number(chapterId))} naturalEntries={worldEntries(world).filter(item => (world.natural_features.some(entry => entry.id === item.id) || world.text_entities.some(entry => entry.id === item.id) || item.kind === 'beast' && !item.place_id) && Number(item.reveal_chapter) <= Number(chapterId))} onOpen={open} reading={reading} collectionItems={collectionItems} />;
  const chapterNavigation = <Timeline stages={stages} index={stageIndex} onSelect={selectStage} />;
  const tourLabel = readingChapter ? stageIndex === stages.length - 1 ? '结束游历' : '阅读完毕，下一章' : tourActive ? playing ? '暂停游历' : '继续游历' : '开始游历';
  const readingControls = { resumeEntry, onResume: continueReading, returnEntry: entryIndex.get(playbackReturnId), onReturnToReading: () => window.history.back(), tourLabel, tourActive, playing, readingChapter, progress: `${Math.max(1, storyNumber + 1)} / ${storyIds.length}`, onTour: toggleTour, guideVisible, onDismissGuide: dismissGuide, onGuide: startGuide };
  return <main className="myth-app" lang={locale === "en" ? "en" : "zh-CN"}>
    <header id="home" className="myth-header"><a href="#world"><span className="seal" aria-hidden="true" dangerouslySetInnerHTML={{ __html: brandMark }} /><h1>{t("山海寻踪")}</h1></a><nav aria-label={t("网站导航")}><a href="#world">{t("地图")}</a><a href="#creatures">{t("异兽谱")}</a><a href="#reading-notes">{t("读图与依据")}</a><button ref={searchTrigger} className="global-search-trigger" type="button" aria-label={t("搜索故事、异兽与现代地点")} onClick={() => setSearchOpen(true)}>{t("搜索")}</button><div className="language-switch" role="group" aria-label={locale === "en" ? "Language" : "语言"}><button type="button" lang="zh-CN" aria-pressed={locale === "zh"} onClick={() => setLocale("zh")}>中文</button><button type="button" lang="en" aria-pressed={locale === "en"} onClick={() => setLocale("en")}>EN</button></div></nav></header>
     <section ref={worldLayout} className="world-layout" id="world" data-chapter={stages[stageIndex].id} data-timeline-playing={playing} data-animation-busy={journeyBusy} data-tour-active={tourActive} data-tour-reading={readingChapter}>
      <aside className="chapter-rail">
        <span className="chapter-number">{stageIndex === 0 ? t("序章") : t("第 ") + stages[stageIndex].id + t(" 章")}</span><h2><InkText key={stages[stageIndex].id} text={stages[stageIndex].title} animate={previousAnimatedChapter.current !== stageIndex || titleAnimating} /></h2><p><InkText key={stages[stageIndex].id} text={stages[stageIndex].subtitle} variant="subtitle" animate={previousAnimatedChapter.current !== stageIndex || titleAnimating} /></p>
        <div className="chapter-rail-details">{!mobile && <><h3>{t('本章条目')}</h3>{chapterEntries}</>}</div>
      </aside>
      <div className="world-main">
        <nav className="mobile-explore-nav" aria-label={t('探索面板')}>
          <button onClick={event => openPanel('chapters', event)}>{t('章节')}</button>
          <button onClick={event => openPanel('entries', event)}>{t('本章条目')}</button>
        </nav>
        <MapPanel onActiveEventChange={mapEventChanged} geographyMode={geographyOpen} onGeographyModeChange={value => { setGeographyOpen(value); setPlaybackReturnId(null); }} geographyEventId={currentGeographyEvent} geographyReferenceId={geographyReferenceId} geographyLocateRequest={geographyLocateRequest} geographyFromSearch={geographyFromSearch} onGeographyReturnToSearch={() => { setGeographyFromSearch(false); setSearchOpen(true); }} onGeographyReferenceChange={setGeographyReferenceId} onGeographyEventChange={id => { const event = catalog.events.find(item => item.id === id); if (event.properties.stage_id !== chapterId) selectStage(stages.findIndex(stage => stage.id === event.properties.stage_id)); else { manualStory(); requestStory(null); } setGeographyEventId(id); setGeographyReferenceId(null); }} geographySnapshot={geographySnapshot.current} onGeographySnapshot={value => { geographySnapshot.current = value; }} pausedForOverlay={searchOpen || onboardingOpen} reading={reading} collectionItems={collectionItems} tourPlaying={tourActive ? playing : null} onTourPlaybackChange={setPlaying} onPlaybackChange={setPlaybackStatus} storyItems={storyItems} onRecordsChange={setMapRecords} locateId={locateId} world={world} stageIndex={stageIndex} storyRequest={storyRequest} onManualStoryChange={manualStory} readingNote={readingChapter} readingControls={readingControls} activeLayers={{ ...activeLayers, onBeasts: checked => setActiveLayers(state => ({ ...state, beasts: checked })), onDivine: checked => setActiveLayers(state => ({ ...state, divine: checked })), onGoToFirstBeast: () => { const index = stages.findIndex(stage => world.beasts.some(beast => beast.reveal_chapter === stage.id)); if (index >= 0) selectStage(index); } }} selectedId={selectedId} onSelect={open} onFullscreenTargetChange={setFullscreenTarget} onJourneyBusyChange={setJourneyBusy} onFullscreenStageChange={navigateFullscreenStage} chapterTransition={chapterTransition} />
        {!mobile && chapterNavigation}

      </div>
    </section>
    {mobile && panel && <ExploreSheet returnFocus={panelTrigger.current} title={t({ chapters: '章节', entries: '本章条目' }[panel])} onClose={() => setPanel(null)}>{panel === 'chapters' ? chapterNavigation : chapterEntries}</ExploreSheet>}
    <Bestiary world={world} onOpen={open} reading={reading} />
    <section className="reading-notes" id="reading-notes" aria-labelledby="reading-notes-title"><h2 id="reading-notes-title">{t("读图与依据")}</h2><div className="reading-notes-body"><div className="reading-notes-copy"><div className="reading-notes-text"><p>{t("本项目为选编，并未完整收录《山海经》。故事入口区分《山海经》、其他古籍与地方传说；地点考证另作标识。")}</p><p>{t("《山海经》依山川和方位展开，不是编年史。序章与七章次序是本项目的叙事编排；各章内部仅在原文或可靠叙事关系可核实处排列先后，不代表精确年代。")}</p><p>{t("经文距离不按比例绘制；淡墨山形为装饰。重要地点以名称和原文标识，故事示意点不表示真实位置。")}</p></div><p>{t("各篇神域记载不预设为同一空间体系。异兽图标仅关联有篇目依据的地点锚点；缺少可靠地点依据的条目收录在异兽谱中。")}</p><p>{t("山海空间与异兽描写以《山海经》正文条目为依据，神话故事沿用各条目所列典籍与出处。插画是本项目依据正文的图像解释，不作为古本插图或新增考据证据。英文译文由模型生成，未声明已完成专业审校。")}</p></div><figure className="reading-bookplate"><span className="bookplate-mark" aria-hidden="true" style={{ maskImage: `url(${assetUrl('/data/atlas/optimized/shanhai-bookplate.webp')})` }} /><figcaption>{t("山海寻踪")}<small>{t("藏书印")}</small></figcaption></figure></div></section>
    <footer className="myth-footer"><span>{t("版式：方位关系与叙述次序 · 不设距离比例")}</span><span>{t("山海空间与异兽描写：以《山海经》正文条目核对")}</span><a href="https://github.com/hyc1005/mythmap/blob/main/ASSETS.md" target="_blank" rel="noopener noreferrer" aria-label={t("查看来源与许可")}>{t("来源与许可 ↗")}</a></footer>

    {onboardingOpen && <OnboardingGuide blocked={Boolean(selectedId || panel || searchOpen || fullscreenTarget)} contextKey={`${chapterId}-${mobile}-${geographyOpen}`} onFinish={finishGuide} returnFocus={guideTrigger.current} />}
    <GlobalSearch open={searchOpen} state={searchState} onStateChange={setSearchState} onClose={() => { if (window.history.state?.shanhai?.searchEntry) window.history.back(); else setSearchOpen(false); }} returnFocus={searchTrigger.current} world={world} catalog={catalog} onChoose={(id, ids, savedSearch, result) => {
      const saved = { ...window.history.state?.shanhai, searchState: savedSearch };
      window.history.replaceState({ ...window.history.state, shanhai: saved }, '', window.location.href);
      setSearchState(savedSearch); setSearchOpen(false);
      if (result.kind === 'geography') {
        const record = geographicReferences(rawCatalog).find(item => item.id === result.referenceId && item.properties.entity_id === id);
        if (!record) return;
        setGeographyOpen(false); setGeographyFromSearch(false);
        setDetailFromSearch(true); open(id, searchTrigger.current, [id]);
      } else { setDetailFromSearch(true); open(id, searchTrigger.current, ids); }
    }} />
    {selected && createPortal(<DetailDrawer placeReference={detailPlace} onOpenPlace={openPlace} reading={reading} navigation={detailNavigation} selected={selected} placeContents={worldEntries(world).filter(item => item.context_place_id === selectedId || item.context_place_ids?.includes(selectedId))} contextPlace={entryIndex.get(selected.context_place_id)} fromSearch={detailFromSearch} onClose={() => closeDetail()} onOpen={open} restoreReading={restoreReading} returnFocusKey={detailReturnFocusKey} onSaveReading={lastReading.save} readingChapter={chapterForLink()} resumeSaveFailed={lastReading.saveFailed} relatedChapter={relatedChapter} canLocate={canLocate} onNavigate={navigateDetail} animationId={selectedAnimationId} onPlay={playDetail} relatedItems={relatedEntries(selectedId, entryIndex)} onRelated={openRelated} parentEntry={entryIndex.get(detailParentId)} />, fullscreenTarget || document.body)}
  </main>;
}
