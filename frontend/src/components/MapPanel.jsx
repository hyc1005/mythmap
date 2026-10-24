import { useLocale, localize } from '../i18n';
import { Component, lazy, Suspense, useCallback, useEffect, useMemo, useRef, useState } from 'react';
import { createPortal } from 'react-dom';
import OlMap from 'ol/Map';
import View from 'ol/View';
import Feature from 'ol/Feature';
import Point from 'ol/geom/Point';
import LineString from 'ol/geom/LineString';
import Projection from 'ol/proj/Projection';
import VectorLayer from 'ol/layer/Vector';
import VectorSource from 'ol/source/Vector';
import { Circle as CircleStyle, Fill, Icon, Stroke, Style, Text } from 'ol/style';
import { defaults as defaultControls } from 'ol/control';
import { defaults as defaultInteractions } from 'ol/interaction';
import MouseWheelZoom from 'ol/interaction/MouseWheelZoom';
import rawCatalog from '../../public/data/atlas/catalog.json';
import rawAnimationCatalog from '../../public/data/atlas/story-animations.json';
import kuafuJourney from '../../public/data/atlas/kuafu-journey.json';
import { worldEntries } from '../entries';
import { assetUrl, assetDimensions } from '../asset-url';

import { iconFor } from '../artwork';
import { ChapterNotice, InkText, useReducedMotion } from '../motion';
import { prefetchNextChapter } from '../asset-cache';
import ArtworkImage from './ArtworkImage';
import ContentOrigin from './ContentOrigin';
import MapToolbar from './MapToolbar';
import MapPlayback from './MapPlayback';
import ReadingActions from './ReadingActions';
import ChapterEntries from './ChapterEntries';
import { storySummary } from '../story-summaries';
import { chapterStoryIds } from '../chapter-stories';
import { drawMapLayers } from '../map-export';
import { paperLayer } from '../paper-layer';
import GeographyMap from './GeographyMap';
const PanguOpening = lazy(() => import('../animations/PanguOpening'));
const KuafuJourney = lazy(() => import('../animations/KuafuJourney'));
const StoryAnimation = lazy(() => import('../animations/StoryAnimation'));
const readingSeal = 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent('<svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 14 14"><path d="M1.5 1.5h11v11h-11zM4 4h6v6H4zM7 4v6M4 7h6" fill="none" stroke="#a44431" stroke-width="1.3" stroke-linejoin="round"/></svg>');

class PanguLoadBoundary extends Component {
  state = { failed: false };
  static getDerivedStateFromError() { return { failed: true }; }
  componentDidCatch() { this.props.onError(); }
  render() { return this.state.failed ? this.props.fallback : this.props.children; }
}

class AnimationBoundary extends Component {
  state = { failed: false };
  static getDerivedStateFromError() { return { failed: true }; }
  render() { return this.state.failed ? this.props.fallback : this.props.children; }
}

function AnimationFailure({ onStatus, onSkip }) {
  const { t } = useLocale();
  useEffect(() => { onStatus('error'); }, [onStatus]);
  return <div className="animation-failure" role="alert"><p>{t('动画暂不可用，仍可阅读本章条目。')}</p><button onClick={() => window.location.reload()}>{t('重新加载页面')}</button><button onClick={onSkip}>{t('跳过')}</button></div>;
}

function AnimationLoading({ onStatus }) {
  useEffect(() => { onStatus('loading'); }, [onStatus]);
  return null;
}

function PanguPoster({ scene, onRetry, controlContainer }) {
  const { t, locale } = useLocale();
  const controls = <button className="pangu-retry" type="button" onClick={onRetry}>{t("播放动态序章")}</button>;
  return <div className="pangu-loading-poster"><ArtworkImage src={assetUrl(scene)} alt={t("盘古分开混沌，天地初开木刻场景")} />{controlContainer ? createPortal(controls, controlContainer) : controls}</div>;
}

const EXTENT = [0, 0, 1200, 800];
const projection = new Projection({ code: 'mythic-plane', units: 'pixels', extent: EXTENT });

const beastIcons = new Map();
function beastMarker(record, active, resolution = 1) {
  const src = iconFor(record, 'map'), size = active ? 40 : Math.round(Math.max(18, Math.min(34, 65 / resolution))), key = `${src}-${size}`;
  if (!beastIcons.has(key)) {
    const icon = new Icon({ src, scale: 1, anchor: [.5, .9], opacity: active ? 1 : .82 });
    const normalize = () => {
      const dimensions = icon.getImageSize();
      if (!dimensions) return;
      icon.setScale(size / Math.max(...dimensions));
      icon.unlistenImageChange(normalize);
    };
    icon.listenImageChange(normalize);
    normalize();
    icon.load();
    beastIcons.set(key, icon);
  }
  return beastIcons.get(key);
}

export default function MapPanel({ world, stageIndex, activeLayers, selectedId, pausedForOverlay = false, onSelect, onFullscreenTargetChange, onJourneyBusyChange, onFullscreenStageChange, chapterTransition, storyRequest, onActiveEventChange, onManualStoryChange, readingNote, readingControls, locateId, storyItems, onRecordsChange, reading, collectionItems, tourPlaying = null, onTourPlaybackChange, onPlaybackChange, geographyMode, onGeographyModeChange, geographyEventId, onGeographyEventChange, geographyReferenceId, onGeographyReferenceChange, geographyLocateRequest, geographyFromSearch, onGeographyReturnToSearch, geographySnapshot, onGeographySnapshot }) {
  const { t, locale } = useLocale();
  const externalPaused = tourPlaying === false || pausedForOverlay || geographyMode || Boolean(chapterTransition);
  const [geographyVisited, setGeographyVisited] = useState(geographyMode);
  useEffect(() => { if (geographyMode) setGeographyVisited(true); }, [geographyMode]);
  const onUserPlaybackChange = tourPlaying === null ? undefined : onTourPlaybackChange;
  const catalog = useMemo(() => localize(rawCatalog, locale), [locale]);
  const animationCatalog = useMemo(() => localize(rawAnimationCatalog, locale), [locale]);
  const reducedMotion = useReducedMotion();
  const [exportStatus, setExportStatus] = useState('');
  const [compactTools, setCompactTools] = useState(() => window.matchMedia('(max-width: 768px), (max-height: 480px)').matches);
  const exportTimer = useRef(null);
  const exportJob = useRef(null);
  const mapFont = locale === 'en' ? '"Source Sans 3 Variable", Arial, sans-serif' : '"Noto Serif SC", SimSun, serif';
  const mapFontRef = useRef(mapFont);
  const labelMeasure = useRef(null), labelWidths = useRef(new Map());
  const labelWidth = (text, font) => {
    const key = `${font}:${text}`;
    if (!labelWidths.current.has(key)) {
      labelMeasure.current ||= document.createElement('canvas').getContext('2d');
      labelMeasure.current.font = font;
      labelWidths.current.set(key, labelMeasure.current.measureText(text).width);
    }
    return labelWidths.current.get(key);
  };
  mapFontRef.current = mapFont;
  useEffect(() => {
    document.fonts.load(`13px ${mapFontRef.current}`).then(() => { labelWidths.current.clear(); map.current?.getLayers().forEach(layer => layer.changed()); });
  }, [locale]);
  const stages = world.stages;
  const chapterId = stages[stageIndex].id;
  useEffect(() => prefetchNextChapter(chapterId, world, rawCatalog, rawAnimationCatalog, kuafuJourney), [chapterId, world]);
  useEffect(() => {
    exportJob.current?.cancel();
    setExportStatus('');
    return () => exportJob.current?.cancel();
  }, [chapterId]);
  useEffect(() => {
    const query = window.matchMedia('(max-width: 768px), (max-height: 480px)');
    const change = event => setCompactTools(event.matches);
    query.addEventListener('change', change);
    return () => query.removeEventListener('change', change);
  }, []);
  const isPrologue = chapterId === '00';
  const revealed = record => Number(record.reveal_chapter) <= Number(chapterId);
  const beasts = useMemo(() => {
    const beastGroupOrders = new Map();
    return world.beasts.map(beast => {
      const groupIndex = beast.place_id ? beastGroupOrders.get(beast.place_id) || 0 : -1;
      if (beast.place_id) beastGroupOrders.set(beast.place_id, groupIndex + 1);
      return { ...beast, stage: beast.reveal_stage, groupIndex };
    });
  }, [world.beasts]);
  const places = useMemo(() => world.places.map(place => ({ ...place, stage: place.reveal_stage })), [world.places]);
  const availableBeasts = useMemo(() => beasts.filter(beast => Number(beast.reveal_chapter) <= Number(chapterId)), [beasts, chapterId]);
  const mappedBeastCount = availableBeasts.filter(beast => beast.place_id && places.some(place => place.id === beast.place_id)).length;
  const mappedPlaceCount = new Set(availableBeasts.filter(beast => beast.place_id && places.some(place => place.id === beast.place_id)).map(beast => beast.place_id)).size;
  const domains = world.domains;
  const relationLines = world.relations;
  const terrain = world.terrain;
  const target = useRef(null);
  const map = useRef(null);
  const [mapInstance, setMapInstance] = useState(null);
  const [journeyId, setJourneyId] = useState(null);
  const chapterStoryOptions = isPrologue ? [] : chapterStoryIds(chapterId, catalog, animationCatalog, kuafuJourney).map(id => animationCatalog.stories.find(story => story.id === id) || { id, name: t('夸父逐日') });
  const [cameraMode, setCameraMode] = useState('overview');
  const [cameraRequest, setCameraRequest] = useState(0);
  const activeJourneyId = chapterStoryOptions.some(story => story.id === journeyId) ? journeyId : null;
  const activeJourneyRef = useRef(activeJourneyId);
  activeJourneyRef.current = animationCatalog.stories.find(story => story.id === activeJourneyId)?.source_event_id || activeJourneyId;
  const activeEventId = isPrologue ? '01-01' : activeJourneyRef.current;
  useEffect(() => { onActiveEventChange(activeEventId); }, [activeEventId, onActiveEventChange]);
  const sceneBounds = useRef(null);
  const handleSceneBounds = useCallback(bounds => {
    const before = JSON.stringify(sceneBounds.current?.map(rect => rect.map(value => Math.round(value / 8))));
    const after = JSON.stringify(bounds?.map(rect => rect.map(value => Math.round(value / 8))));
    sceneBounds.current = bounds;
    if (before !== after) map.current?.getLayers().forEach(layer => layer.changed());
  }, []);
  const obscuredLabel = (coordinate, label, offsetY = 0) => {
    if (!sceneBounds.current || !map.current) return false;
    const pixel = map.current.getPixelFromCoordinate(coordinate);
    const halfWidth = Math.max(20, (label?.length || 0) * 7);
    return sceneBounds.current.some(([left, top, right, bottom]) => pixel[0] + halfWidth > left && pixel[0] - halfWidth < right && pixel[1] + offsetY + 12 > top && pixel[1] + offsetY - 12 < bottom);
  };
  useEffect(() => {
    const id = storyRequest.chapterId === chapterId ? storyRequest.id : null;
    setJourneyId(isPrologue ? null : id);
    setCameraMode(id ? 'story' : 'overview'); setCameraRequest(value => value + 1);
  }, [chapterId, storyRequest, isPrologue]);
  const [journeyBusy, setJourneyBusy] = useState(false);
  const journeyBusyRef = useRef(false);
  journeyBusyRef.current = journeyBusy;
  const handlePlayback = useCallback(status => {
    const busy = !['completed', 'idle'].includes(status);
    setJourneyBusy(busy); onJourneyBusyChange(busy); onPlaybackChange(status);
  }, [onJourneyBusyChange, onPlaybackChange]);
  useEffect(() => { if (!isPrologue && !activeJourneyId) handlePlayback('idle'); }, [chapterId, isPrologue, activeJourneyId, handlePlayback]);
  const areaSource = useRef(new VectorSource());
  const terrainSource = useRef(new VectorSource());
  const relationSource = useRef(new VectorSource());
  const pointSource = useRef(new VectorSource());
  const [hoverId, setHoverId] = useState(null);
  const hoverLeaveTimer = useRef(null);
  const hoverCardActive = useRef(false);
  const keepHover = () => window.clearTimeout(hoverLeaveTimer.current);
  const leaveHover = () => { keepHover(); hoverLeaveTimer.current = window.setTimeout(() => { if (!hoverCardActive.current && !mapFrame.current?.querySelector('.ink-hover-card')?.contains(document.activeElement)) setHoverId(null); }, 180); };
  useEffect(() => () => window.clearTimeout(hoverLeaveTimer.current), []);
  useEffect(() => { if (!hoverId) hoverCardActive.current = false; }, [hoverId]);
  const [pinnedId, setPinnedId] = useState(null);
  const [nativeFullscreen, setNativeFullscreen] = useState(false);
  const [fallbackFullscreen, setFallbackFullscreen] = useState(false);
  const [panguRetry, setPanguRetry] = useState(0);
  const [prologueSkipped, setPrologueSkipped] = useState(false);
  useEffect(() => { setPrologueSkipped(false); }, [chapterId, storyRequest.serial]);
  const [shortMap, setShortMap] = useState(false);
  const [controlContainer, setControlContainer] = useState(null);
  const mapFrame = useRef(null);
  const activeRecordId = useRef(null);
  activeRecordId.current = hoverId || pinnedId || selectedId;
  const visibleRecords = useMemo(() => {
    if (isPrologue) return [];
    const storyRecords = (catalog.events || []).filter(item => item.properties.stage_id === chapterId && item.properties.map_visible).map(item => ({
      id: item.id, name: item.properties.name, kind: 'story', source: item.properties.source_text,
      description: item.properties.source_quote, region: item.properties.location_label, direction: item.properties.basis_note, url: item.properties.source_url,
      x: item.properties.layout_hint?.[0], y: item.properties.layout_hint?.[1], artwork: item.properties.artwork, artworks: item.properties.artworks, raw: item,
    }));
    const domainRecords = activeLayers.divine ? domains.filter(revealed).map(domain => {
      const place = places.find(item => item.id === domain.place_id);
      return { ...domain, kind: 'domain', x: place.x, y: place.y, region: domain.source, direction: place.direction, description: domain.quote, place_id: place.id };
    }) : [];
    const domainPlaceIds = new Set(domainRecords.map(domain => domain.place_id));
    const placeRecords = places.filter(place => revealed(place) && !domainPlaceIds.has(place.id));
    const creatureRecords = activeLayers.beasts ? availableBeasts : [];
    const mappedCreatures = creatureRecords.map(beast => {
      const home = beast.place_id && places.find(place => place.id === beast.place_id);
      if (!home) return null;
      const column = beast.groupIndex % 4;
      const row = Math.floor(beast.groupIndex / 4);
      return { ...beast, x: home.x + (column - 1.5) * 78, y: home.y - 42 - row * 76, kind: 'beast', group_id: home.id, direction: beast.place_basis || home.direction };
    }).filter(Boolean);
    return [...storyRecords, ...placeRecords.map(place => ({ ...place, kind: 'place' })), ...domainRecords, ...mappedCreatures];
  }, [world, stageIndex, activeLayers.beasts, activeLayers.divine]);
  useEffect(() => { onRecordsChange(visibleRecords); }, [visibleRecords, onRecordsChange]);

  useEffect(() => {
    if (!target.current || map.current) return undefined;
    const paper = paperLayer('/data/atlas/myth-paper.webp');
    const created = new OlMap({
      target: target.current,
      controls: defaultControls({ attribution: false, rotate: false, zoom: false }),
      layers: [
        paper,
        new VectorLayer({ source: areaSource.current, declutter: 'map-labels', style: (feature, resolution) => activeJourneyRef.current || resolution > 2.2 || obscuredLabel(feature.getGeometry().getCoordinates(), feature.get('label')) ? null : new Style({
          text: new Text({ text: feature.get('label'), font: `15px ${mapFontRef.current}`, padding: [5, 9, 5, 9], backgroundFill: new Fill({ color: '#eee2c5c9' }), fill: new Fill({ color: '#806d51' }), overflow: true }),
        }) }),
        new VectorLayer({ source: terrainSource.current, style: feature => {
          const path = `/data/atlas/myth-icons/terrain/${feature.get('kind')}.${feature.get('kind') === 'distant' ? 'png' : 'webp'}`;
          const width = assetDimensions(path)?.[0] || 1100;
          return new Style({ image: new Icon({ src: assetUrl(path), scale: feature.get('width') / width, anchor: [0.5, 1], opacity: feature.get('opacity') }) });
        } }),
        new VectorLayer({ source: relationSource.current, style: feature => feature.get('arrow') ? new Style({
          text: new Text({ text: '▲', font: 'bold 12px sans-serif', fill: new Fill({ color: '#a83f2b' }), stroke: new Stroke({ color: '#f4ead2', width: 3 }) }),
        }) : new Style({
          stroke: new Stroke({ color: '#a83f2b', width: 1.5, lineDash: [7, 7] }),
          text: new Text({ text: obscuredLabel(feature.getGeometry().getCoordinateAt(.5), feature.get('label')) ? '' : feature.get('label'), placement: 'line', font: `12px ${mapFontRef.current}`, fill: new Fill({ color: '#943b2b' }), stroke: new Stroke({ color: '#f4ead2', width: 4 }), overflow: true }),
        }) }),
        new VectorLayer({ source: pointSource.current, style: feature => {
          const record = feature.get('record');
          if (record.id === activeJourneyRef.current) return null;
          const active = record.id === activeRecordId.current;
          const chapterRange = record.kind === 'place' && record.map_role === 'chapter-range';
          const image = record.kind === 'beast' ? iconFor(record) : null;
          const symbol = new Style({
            zIndex: active ? 30 : record.kind === 'place' ? 20 : 10,
            image: image ? beastMarker(record, active, map.current?.getView().getResolution()) :
              new CircleStyle({ radius: active ? 8 : 5, fill: new Fill({ color: chapterRange ? 'rgba(83, 124, 134, .64)' : record.kind === 'place' ? '#526052' : record.kind === 'domain' ? '#946737' : '#a44431' }), stroke: new Stroke({ color: '#f0e4c9', width: 2 }) }),
          });
          if (!active || !image) return symbol;
          return [new Style({ zIndex: 29, image: new CircleStyle({ radius: 24, fill: new Fill({ color: '#a4443110' }), stroke: new Stroke({ color: '#a44431', width: 1.5 }) }) }), symbol];
        } }),
        new VectorLayer({ source: pointSource.current, declutter: 'map-labels', renderOrder: (a, b) => {
          const rank = feature => {
            const record = feature.get('record');
            return record.id === activeRecordId.current ? 0 : record.id === activeJourneyRef.current ? 1 : { story: 2, place: 3, domain: 4, beast: 5 }[record.kind];
          };
          return rank(a) - rank(b);
        }, style: (feature, resolution) => {
          const record = feature.get('record');
          if (record.id === activeJourneyRef.current) return null;
          const active = record.id === activeRecordId.current;
          if (!active && resolution > 2.2 && ['beast', 'domain'].includes(record.kind)) return null;
          const dimmed = !active && (Boolean(activeJourneyRef.current) || obscuredLabel(feature.getGeometry().getCoordinates(), record.name, record.kind === 'beast' ? 18 : -20));
          const font = `${active ? 'bold 14px' : '13px'} ${mapFontRef.current}`;
          const offsetY = record.kind === 'beast' ? 18 : -20;
          return new Style({ zIndex: active ? 40 : 1,
            image: new Icon({ src: readingSeal, scale: (active ? 12.5 : 11) / 14, displacement: [-labelWidth(record.name, font) / 2 - 9, -offsetY], opacity: dimmed ? .45 : active ? 1 : .9 }),
            text: new Text({ text: record.name, offsetY, font, fill: new Fill({ color: dimmed ? '#66543c99' : '#392d20' }), stroke: new Stroke({ color: dimmed ? '#f5ecd599' : '#f5ecd5', width: 4 }), padding: [3, 5, 3, 5] }) });
        } }),
      ],
      interactions: defaultInteractions({ mouseWheelZoom: false }).extend([new MouseWheelZoom({ maxDelta: 0.38, duration: 380 })]),
      view: new View({ projection, center: [600, 400], resolution: 1, minResolution: 0.25, maxResolution: 1, extent: EXTENT, constrainOnlyCenter: false, showFullExtent: true, smoothExtentConstraint: false, smoothResolutionConstraint: false, enableRotation: false }),
    });
    created.on('pointermove', event => {
      if (event.dragging) { setHoverId(null); setPinnedId(null); return; }
      if (event.originalEvent?.pointerType === 'touch') return;
      const hit = created.forEachFeatureAtPixel(event.pixel, feature => feature.get('record')?.id, { hitTolerance: 8 });
      if (hit) { keepHover(); setHoverId(hit); } else leaveHover();
      target.current.style.cursor = hit ? 'pointer' : 'grab';
    });
    created.on('postrender', () => {
      const view = created.getView();
      const value = JSON.stringify({ center: view.getCenter(), resolution: view.getResolution(), size: created.getSize() });
      if (target.current && target.current.dataset.view !== value) target.current.dataset.view = value;
    });
    created.on('singleclick', event => {
      const hit = created.forEachFeatureAtPixel(event.pixel, feature => feature.get('record')?.id, { hitTolerance: 8 });
      setPinnedId(hit || null);
    });
    const mapTarget = target.current;
    const clearHover = leaveHover;
    mapTarget.addEventListener('pointerleave', clearHover);
    map.current = created;
    document.fonts.load(`13px ${mapFontRef.current}`).then(() => {
      if (map.current === created) { labelWidths.current.clear(); created.getLayers().forEach(layer => layer.changed()); }
    });
    setMapInstance(created);
    return () => { mapTarget.removeEventListener('pointerleave', clearHover); created.dispose(); map.current = null; };
  }, []);

  useEffect(() => {
    const activeMap = map.current;
    if (!activeMap || !target.current) return undefined;
    let previousSize = null;
    const syncBounds = () => {
      if (!target.current?.clientWidth || !target.current?.clientHeight) return;
      activeMap.updateSize();
      const size = activeMap.getSize();
      if (!size?.[0] || !size?.[1]) return;
      setShortMap(window.innerWidth > 640 && size[1] < 280);
      const maxResolution = Math.max(EXTENT[2] / Math.max(1, size[0] - 100), EXTENT[3] / Math.max(1, size[1] - 100));
      const previous = activeMap.getView();
      const resizeFactor = previousSize ? Math.max(previousSize[0] / size[0], previousSize[1] / size[1]) : 1;
      const unchanged = previousSize && previousSize[0] === size[0] && previousSize[1] === size[1];
      previousSize = [...size];
      if (unchanged && Math.abs(previous.getMaxResolution() - maxResolution) < 0.005) return;
      activeMap.setView(new View({
        projection, center: previous.getCenter() || [600, 400],
        resolution: Math.min((previous.getResolution() || maxResolution) * resizeFactor, maxResolution), rotation: previous.getRotation(),
        minResolution: 0.25, maxResolution, extent: EXTENT, constrainOnlyCenter: false, showFullExtent: true, smoothExtentConstraint: false, smoothResolutionConstraint: false, enableRotation: false,
      }));
    };
    const observer = new ResizeObserver(syncBounds);
    observer.observe(target.current);
    syncBounds();
    return () => observer.disconnect();
  }, []);

  useEffect(() => {
    const activeAreas = world.regions.filter(revealed);
    areaSource.current.clear();
    areaSource.current.addFeatures(activeAreas.map(area => new Feature({
      geometry: new Point(area.label_position), label: area.label,
    })));
    terrainSource.current.clear();
    terrainSource.current.addFeatures(terrain.filter(revealed).map(stamp => new Feature({ geometry: new Point([stamp.x, stamp.y]), kind: stamp.kind, width: stamp.width, opacity: stamp.opacity })));
  }, [stageIndex, world]);

  useEffect(() => {
    setHoverId(null);
    setPinnedId(null);
    map.current?.getView().cancelAnimations();
    map.current?.getInteractions().forEach(interaction => interaction.setActive(!isPrologue));
    if (isPrologue) return;
    let secondFrame;
    const firstFrame = requestAnimationFrame(() => {
      secondFrame = requestAnimationFrame(() => {
        map.current?.updateSize();
        if (map.current && !activeJourneyRef.current) fitStage(false);
      });
    });
    return () => { cancelAnimationFrame(firstFrame); cancelAnimationFrame(secondFrame); };
  }, [chapterId, activeJourneyId, storyRequest.serial]);

  useEffect(() => {
    const selectedPlaceIds = new Set(places.filter(revealed).map(place => place.id));
    relationSource.current.clear();
    relationSource.current.addFeatures(relationLines.filter(link => selectedPlaceIds.has(link.from) && selectedPlaceIds.has(link.to)).map(link => {
      const start = places.find(place => place.id === link.from);
      const end = places.find(place => place.id === link.to);
      return [
        new Feature({ geometry: new LineString([[start.x, start.y], [end.x, end.y]]), id: `link-${link.from}`, label: link.label, source: link.source }),
        new Feature({ geometry: new Point([end.x, end.y]), id: `arrow-${link.from}`, arrow: true }),
      ];
    }).flat());
    pointSource.current.clear();
    pointSource.current.addFeatures(visibleRecords.map(record => new Feature({ geometry: new Point([record.x ?? 1100, record.y ?? 120 + (record.stage || 0) * 40]), record })));
    map.current?.getLayers().forEach(layer => layer.changed());
  }, [visibleRecords, stageIndex]);
  useEffect(() => {
    if (!locateId || !mapInstance) return;
    const record = visibleRecords.find(item => item.id === locateId);
    if (!record) return;
    setJourneyId(null);
    mapInstance.dispatchEvent('journey:user-view');
    mapInstance.getView().animate({ center: [record.x, record.y], duration: reducedMotion ? 0 : 320 });
    setPinnedId(locateId);
    requestAnimationFrame(() => mapFrame.current?.focus({ preventScroll: true }));
  }, [locateId, visibleRecords, mapInstance, reducedMotion]);

  useEffect(() => {
    pointSource.current.changed();
  }, [selectedId, hoverId, pinnedId]);


  useEffect(() => { map.current?.getLayers().forEach(layer => layer.changed()); }, [journeyBusy, activeJourneyId]);

  useEffect(() => {
    if (!selectedId) return;
    setHoverId(null);
    setPinnedId(null);
  }, [selectedId]);

  useEffect(() => {
    const visibleIds = new Set(visibleRecords.map(record => record.id));
    if (hoverId && !visibleIds.has(hoverId)) setHoverId(null);
    if (pinnedId && !visibleIds.has(pinnedId)) setPinnedId(null);
  }, [visibleRecords]);

  useEffect(() => {
    const updateFullscreen = () => {
      setNativeFullscreen(document.fullscreenElement === mapFrame.current);
      requestAnimationFrame(() => map.current?.updateSize());
    };
    document.addEventListener('fullscreenchange', updateFullscreen);
    return () => document.removeEventListener('fullscreenchange', updateFullscreen);
  }, []);

  useEffect(() => {
    if (!fallbackFullscreen) return undefined;
    const previousOverflow = document.body.style.overflow;
    document.body.style.overflow = 'hidden';
    const exitOnEscape = event => {
      if (event.key !== 'Escape') return;
      event.preventDefault();
      event.stopImmediatePropagation();
      setFallbackFullscreen(false);
    };
    window.addEventListener('keydown', exitOnEscape, true);
    return () => {
      document.body.style.overflow = previousOverflow;
      window.removeEventListener('keydown', exitOnEscape, true);
    };
  }, [fallbackFullscreen]);

  useEffect(() => {
    requestAnimationFrame(() => map.current?.updateSize());
  }, [fallbackFullscreen, nativeFullscreen, geographyMode]);

  const isFullscreen = nativeFullscreen || fallbackFullscreen;
  useEffect(() => {
    if (isFullscreen && !selectedId) requestAnimationFrame(() => mapFrame.current?.focus({ preventScroll: true }));
  }, [isFullscreen, selectedId]);
  useEffect(() => {
    if (!isFullscreen) return undefined;
    const handleFullscreenKeys = event => {
      if (geographyMode || selectedId || event.repeat || event.altKey || event.ctrlKey || event.metaKey || event.shiftKey) return;
      if (event.target?.closest?.('input, textarea, select, button, a, [contenteditable="true"], [role="slider"], .detail-scrim')) return;
      if (event.key !== 'ArrowRight' && event.key !== 'ArrowLeft') return;
      event.preventDefault();
      onFullscreenStageChange(stageIndex + (event.key === 'ArrowRight' ? 1 : -1));
    };
    window.addEventListener('keydown', handleFullscreenKeys);
    return () => window.removeEventListener('keydown', handleFullscreenKeys);
  }, [isFullscreen, geographyMode, selectedId, stageIndex, onFullscreenStageChange]);
  useEffect(() => {
    onFullscreenTargetChange?.(isFullscreen ? mapFrame.current : null);
  }, [isFullscreen, onFullscreenTargetChange]);
  useEffect(() => {
    if (!nativeFullscreen) return;
    const escape = event => {
      if (event.key !== 'Escape' || selectedId) return;
      event.preventDefault();
      document.exitFullscreen().catch(() => {});
    };
    window.addEventListener('keydown', escape);
    return () => window.removeEventListener('keydown', escape);
  }, [nativeFullscreen, selectedId]);
  const toggleFullscreen = useCallback(async () => {
    const frame = mapFrame.current;
    if (!frame) return;
    if (fallbackFullscreen) { setFallbackFullscreen(false); return; }
    if (document.fullscreenElement === frame) { await document.exitFullscreen(); return; }
    if (!frame.requestFullscreen) { setFallbackFullscreen(true); frame.focus({ preventScroll: true }); requestAnimationFrame(() => frame.focus({ preventScroll: true })); return; }
    try { await frame.requestFullscreen(); requestAnimationFrame(() => frame.focus({ preventScroll: true })); } catch { setFallbackFullscreen(true); frame.focus({ preventScroll: true }); requestAnimationFrame(() => frame.focus({ preventScroll: true })); }
  }, [fallbackFullscreen]);

  const fitStage = (animate = true) => {
    const activeMap = map.current;
    if (!activeMap) return;
    setCameraMode('overview');
    if (animate) activeMap.dispatchEvent('journey:user-view');
    const bounds = [...stages[stageIndex].extent];
    for (const record of visibleRecords) {
      bounds[0] = Math.min(bounds[0], record.x); bounds[1] = Math.min(bounds[1], record.y);
      bounds[2] = Math.max(bounds[2], record.x); bounds[3] = Math.max(bounds[3], record.y);
    }
    activeMap.getView().fit(bounds, { duration: animate && !reducedMotion && !activeJourneyId ? 320 : 0, padding: [54, 64, 54, 64] });
  };
  const exportStage = async () => {
    if (exportJob.current) return;
    setExportStatus('正在生成 PNG…');
    const activeMap = map.current;
    if (!activeMap) { setExportStatus('导出失败，请重试'); return; }
    const render = () => {
      if (job.cancelled) return;
      job.cancel();
      try {
        const size = activeMap.getSize();
        if (!size) throw new Error('Map size unavailable');
        const output = document.createElement('canvas');
        output.width = size[0];
        output.height = size[1];
        const context = output.getContext('2d');
        context.fillStyle = getComputedStyle(target.current.closest('.map-surface')).backgroundColor;
        context.fillRect(0, 0, output.width, output.height);
        drawMapLayers(context, activeMap.getViewport().querySelectorAll('.ol-layer canvas'));
        context.setTransform(1, 0, 0, 1, 0, 0);
        context.globalAlpha = 1;
        context.filter = 'none';
        context.fillStyle = '#544431';
        context.font = `15px ${mapFontRef.current}`;
        context.fillText(t(`山海寻踪 · ${stages[stageIndex].id} ${stages[stageIndex].title}`), 18, 28);
        context.font = `12px ${mapFontRef.current}`;
        context.fillText(t("方位与篇目关系示意 · 点位间距不表示真实距离"), 18, size[1] - 18);
        const link = document.createElement('a');
        link.download = `shan-hai-stage-${stages[stageIndex].id}.png`;
        link.href = output.toDataURL('image/png');
        link.click();
        setExportStatus('PNG 已生成');
      } catch { setExportStatus('导出失败，请重试'); }
    };
    const job = { cancelled: false, cancel: () => {
      job.cancelled = true;
      window.clearTimeout(exportTimer.current);
      activeMap.un('rendercomplete', render);
      if (exportJob.current === job) exportJob.current = null;
    } };
    exportJob.current = job;
    try {
      await document.fonts.ready;
      if (job.cancelled || map.current !== activeMap) return;
      activeMap.once('rendercomplete', render);
      exportTimer.current = window.setTimeout(() => {
        job.cancel();
        setExportStatus('导出失败，请重试');
      }, 10000);
      activeMap.renderSync();
    } catch { job.cancel(); setExportStatus('导出失败，请重试'); }
  };
  const hoverRecord = !selectedId && visibleRecords.find(record => record.id === (hoverId || pinnedId));
  const hoverStoryId = hoverRecord && chapterStoryOptions.find(story => story.id === hoverRecord.id || story.source_event_id === hoverRecord.id || story.event_id === hoverRecord.id)?.id;


  const mapControls = <MapToolbar isFullscreen={isFullscreen} compactTools={compactTools} chapterStoryOptions={chapterStoryOptions} activeJourneyId={activeJourneyId} onStoryChange={id => { setHoverId(null); setPinnedId(null); onManualStoryChange(); setJourneyId(id); setCameraMode(id ? 'story' : 'overview'); setCameraRequest(value => value + 1); }} activeLayers={activeLayers} fitStage={fitStage} exportStage={exportStage} exportStatus={exportStatus} />;
  const entries = <details className="map-entry-list" key={chapterId}><summary>{t('本章条目')}</summary><ChapterEntries stories={storyItems} records={visibleRecords} passageEntries={world.passages.filter(item => Number(item.reveal_chapter) <= Number(chapterId))} naturalEntries={worldEntries(world).filter(item => (world.natural_features.some(entry => entry.id === item.id) || world.text_entities.some(entry => entry.id === item.id) || item.kind === 'beast' && !item.place_id) && Number(item.reveal_chapter) <= Number(chapterId))} onOpen={onSelect} reading={reading} collectionItems={collectionItems} /></details>;
  const closePreview = () => { keepHover(); hoverCardActive.current = false; setHoverId(null); setPinnedId(null); };
  const preview = hoverRecord && <div className="ink-hover-card" role="region" aria-label={t('地图地点预览')} onPointerEnter={() => { hoverCardActive.current = true; keepHover(); }} onPointerLeave={() => { hoverCardActive.current = false; leaveHover(); }} onFocusCapture={keepHover} onBlurCapture={event => { if (!event.currentTarget.contains(event.relatedTarget)) leaveHover(); }}>
    <button type="button" className="preview-close" aria-label={t('收起地点预览')} onClick={() => { closePreview(); mapFrame.current?.focus({ preventScroll: true }); }}>×</button>
    <span>{hoverRecord.region}</span><b>{hoverRecord.name}</b>
    <ContentOrigin record={hoverRecord} />
    <div className="preview-body">
      {hoverRecord.kind === 'story' && !activeJourneyId && !isFullscreen && iconFor(hoverRecord) && <ArtworkImage key={hoverRecord.id} className="preview-art" src={iconFor(hoverRecord, 'preview')} alt="" interactive={false} />}
      <p>{storySummary(hoverRecord.id, locale) || hoverRecord.description}</p>
    </div>
    <div className="preview-actions">
      <button type="button" className="preview-read" aria-label={t('展开原文与出处 ↗')} onClick={event => onSelect(hoverRecord.id, event.currentTarget)}>{t('展开阅读')}</button>
      {hoverStoryId && <button type="button" onClick={() => { onManualStoryChange(); setJourneyId(hoverStoryId); setCameraMode('story'); setCameraRequest(value => value + 1); closePreview(); }} aria-label={t('播放故事动画')}>{t('播放动画')}</button>}
    </div>
  </div>;
  const legend = <small className="map-range-legend"><i className="legend-story" />{t("故事示意")}<i className="legend-place" />{t("篇目地点")}<i />{t("篇目山列")}<span>{t("兽形图标：异兽")}</span><span className="map-reading-hint"><img src={readingSeal} alt="" />{t('朱印旁的名称可点阅')}</span></small>;
  const layerStatus = <div className="map-layer-summary" role="status">{activeLayers.beasts && <span>{availableBeasts.length ? t("异兽图层 · ") + mappedBeastCount + t(" 条已关联") : t("本章暂无异兽")}{!availableBeasts.length && <button onClick={activeLayers.onGoToFirstBeast}>{t("前往第 3 章 ↗")}</button>}</span>}{activeLayers.divine && <span>{t("神域已显示")}</span>}</div>;
  const fullscreenButton = <button className="map-fullscreen" onClick={toggleFullscreen} aria-pressed={isFullscreen} aria-label={isFullscreen ? t("退出地图全屏") : t("地图全屏")}>{isFullscreen ? t("退出全屏") : t("全屏展示")}</button>;

  const readingActions = <ReadingActions {...readingControls} showTour={!geographyMode} />;
  const modeControls = <div className="map-mode-switch" role="group" aria-label={t('地图模式')}><button type="button" aria-pressed={!geographyMode} onClick={() => onGeographyModeChange(false)}>{t('木刻叙事')}</button><button type="button" aria-pressed={geographyMode} onClick={() => onGeographyModeChange(true)}>{t('真实地理')}</button></div>;

  return <><section ref={mapFrame} tabIndex={-1} data-map-mode={geographyMode ? 'geography' : 'woodcut'} data-camera-mode={cameraMode} className={`myth-map-wrap ${isPrologue ? "is-prologue" : ""} ${geographyMode ? "is-geography" : ""} ${isFullscreen ? "is-map-fullscreen" : ""} ${fallbackFullscreen ? "is-fallback-fullscreen" : ""} ${shortMap ? "is-short-map" : ""} ${activeJourneyId ? "has-journey" : ""} ${activeJourneyId && activeJourneyId !== "03-05" ? "has-local-story" : ""}`} aria-label={geographyMode ? t("真实地理参考地图") : isPrologue ? t("盘古开天序章场景") : t("山海经方位关系地图")}>
    {isFullscreen && <header className="fullscreen-toolbar" aria-label={t("全屏地图工具栏")}><div className="fullscreen-chapter-nav" aria-label={t("全屏章节切换")}>
      <button type="button" onClick={() => { onFullscreenStageChange(stageIndex - 1); mapFrame.current?.focus({ preventScroll: true }); }} disabled={stageIndex === 0}>{t("← 上一章")}</button>
      <span><small>{stages[stageIndex].id} / {String(stages.length - 1).padStart(2, '0')}</small><b><InkText key={chapterId} text={stages[stageIndex].title} animate={Boolean(chapterTransition)} /></b></span>
      <button type="button" onClick={() => { onFullscreenStageChange(stageIndex + 1); mapFrame.current?.focus({ preventScroll: true }); }} disabled={stageIndex >= stages.length - 1}>{t("下一章 →")}</button>
    </div>{modeControls}{!geographyMode && !isPrologue && mapControls}{isFullscreen && !isPrologue && entries}{fullscreenButton}</header>}
    {!isFullscreen && <header className="explore-toolbar">{modeControls}{!geographyMode && !isPrologue && mapControls}{fullscreenButton}</header>}
    <div className="map-surface" hidden={geographyMode}><div ref={target} className="myth-map-canvas" />
{isPrologue && <div className="prologue-scene">
      {prologueSkipped ? <ArtworkImage src={assetUrl(stages[stageIndex].scene)} className="pangu-static-poster" alt={t('盘古开天')} /> : <PanguLoadBoundary key={panguRetry} onError={() => handlePlayback('error')} fallback={<AnimationFailure onStatus={handlePlayback} onSkip={() => { setPrologueSkipped(true); handlePlayback('completed'); }} />}>
        <Suspense fallback={<PanguPoster scene={stages[stageIndex].scene} controlContainer={controlContainer} onRetry={() => setPanguRetry(value => value + 1)} />}>
          <PanguOpening active={isPrologue} key={storyRequest.serial} autoStart={storyRequest.chapterId === chapterId && storyRequest.id === '00-opening'} selected={Boolean(selectedId) || pausedForOverlay} onStatusChange={handlePlayback} externalPaused={externalPaused} tourPlaying={tourPlaying} onUserPlaybackChange={onUserPlaybackChange} onSkip={() => { setPrologueSkipped(true); handlePlayback('completed'); }} controlContainer={controlContainer} />
        </Suspense>
      </PanguLoadBoundary>}

    </div>}
    {!isPrologue && <>
      {!isFullscreen && <><div className="map-orientation" aria-label={t("示意北向")}><span>{t("示意北向")} ↑</span></div></>}
      {!isFullscreen && preview}
    <AnimationBoundary key={chapterId + '-' + activeJourneyId} fallback={<AnimationFailure onStatus={handlePlayback} onSkip={() => setJourneyId(null)} />}>
    <Suspense fallback={<AnimationLoading onStatus={handlePlayback} />}>
      {activeJourneyId === '03-05' && mapInstance && <KuafuJourney key={storyRequest.serial} storyView={cameraMode === 'story'} closeup={cameraMode === 'story' && compactTools} cameraRequest={cameraRequest} compactControls={compactTools && !isFullscreen} map={mapInstance} selectedId={selectedId} onSelect={onSelect} onSkip={() => setJourneyId(null)} onStatusChange={handlePlayback} externalPaused={externalPaused} tourPlaying={tourPlaying} onUserPlaybackChange={onUserPlaybackChange} controlContainer={controlContainer} />}
      {activeJourneyId && activeJourneyId !== '03-05' && mapInstance && <StoryAnimation compactControls={compactTools && !isFullscreen} key={activeJourneyId + '-' + storyRequest.serial} storyView={cameraMode === 'story'} closeup={cameraMode === 'story' && compactTools} cameraRequest={cameraRequest} id={activeJourneyId} map={mapInstance} selectedId={selectedId} onSelect={onSelect} onStatusChange={handlePlayback} externalPaused={externalPaused} tourPlaying={tourPlaying} onUserPlaybackChange={onUserPlaybackChange} onSceneBoundsChange={handleSceneBounds} controlContainer={controlContainer} onSkip={() => setJourneyId(null)} />}
    </Suspense>
    </AnimationBoundary>
      {!isFullscreen && (activeLayers.beasts || activeLayers.divine) && layerStatus}
    </>}
    <ChapterNotice change={chapterTransition} title={stages[stageIndex].title} />
    </div>
    {geographyVisited && <div className="geography-main" hidden={!geographyMode}><GeographyMap readingActions={geographyMode ? readingActions : null} catalog={catalog} chapterId={chapterId} currentEventId={geographyEventId} currentReferenceId={geographyReferenceId} onReferenceChange={onGeographyReferenceChange} locateRequest={geographyLocateRequest} fromSearch={geographyFromSearch} onReturnToSearch={onGeographyReturnToSearch} visible={geographyMode} transitioning={chapterTransition} isFullscreen={isFullscreen} snapshot={geographySnapshot} onSnapshot={onGeographySnapshot} onEventChange={onGeographyEventChange} onOpen={(id, trigger) => onSelect(id, trigger)} /></div>}
    <MapPlayback readingActions={!geographyMode ? readingActions : null} hidden={geographyMode} isFullscreen={isFullscreen} isPrologue={isPrologue} activeJourneyId={activeJourneyId} onSelect={onSelect} controlRef={setControlContainer} preview={preview} legend={legend} layerStatus={layerStatus} readingNote={readingNote} cameraMode={cameraMode} onCloseup={() => { setCameraMode('story'); setCameraRequest(value => value + 1); }} onOverview={() => fitStage()} />
  </section></>;
}
