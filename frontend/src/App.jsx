import { Component, lazy, Suspense, useCallback, useEffect, useMemo, useRef, useState } from 'react';
import { createPortal } from 'react-dom';
import OlMap from 'ol/Map';
import View from 'ol/View';
import Feature from 'ol/Feature';
import Point from 'ol/geom/Point';
import LineString from 'ol/geom/LineString';
import Projection from 'ol/proj/Projection';
import ImageLayer from 'ol/layer/Image';
import VectorLayer from 'ol/layer/Vector';
import ImageStatic from 'ol/source/ImageStatic';
import VectorSource from 'ol/source/Vector';
import { Circle as CircleStyle, Fill, Icon, Stroke, Style, Text } from 'ol/style';
import { defaults as defaultControls } from 'ol/control';
import { defaults as defaultInteractions } from 'ol/interaction';
import MouseWheelZoom from 'ol/interaction/MouseWheelZoom';
import catalog from '../public/data/atlas/catalog.json';
import mythWorld from '../public/data/myth-world.json';
import animationCatalog from '../public/data/atlas/story-animations.json';
import kuafuJourney from '../public/data/atlas/kuafu-journey.json';
import KuafuJourney from './KuafuJourney';
import StoryAnimation from './StoryAnimation';
import './myth-world.css';

const PanguOpening = lazy(() => import('./PanguOpening'));

class PanguLoadBoundary extends Component {
  state = { failed: false };
  static getDerivedStateFromError() { return { failed: true }; }
  render() { return this.state.failed ? this.props.fallback : this.props.children; }
}

function PanguPoster({ scene, onRetry, controlContainer }) {
  const controls = <button className="pangu-retry" type="button" onClick={onRetry}>播放动态序章</button>;
  return <div className="pangu-loading-poster"><img src={scene} alt="盘古分开混沌，天地初开木刻场景" />{controlContainer ? createPortal(controls, controlContainer) : controls}</div>;
}

const EXTENT = [0, 0, 1200, 800];
const projection = new Projection({ code: 'mythic-plane', units: 'pixels', extent: EXTENT });

function iconFor(record) {
  return record.artwork ? record.artwork.startsWith('/') ? record.artwork : `/data/atlas/myth-icons/${record.artwork}` : null;
}

const beastIcons = new Map();
function beastMarker(record, active, resolution = 1) {
  const src = iconFor(record), size = active ? 40 : Math.round(Math.max(18, Math.min(34, 65 / resolution))), key = `${src}-${size}`;
  if (!beastIcons.has(key)) {
    const icon = new Icon({ src, width: size, anchor: [.5, .9], opacity: active ? 1 : .82 });
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

function DetailDrawer({ selected, onClose, onOpen, onToggleFullscreen, fullscreen, scrollTopRef }) {
  const closeButton = useRef(null);
  const drawer = useRef(null);
  useEffect(() => {
    drawer.current?.scrollTo(0, scrollTopRef.current);
    closeButton.current?.focus({ preventScroll: true });
    return () => { scrollTopRef.current = drawer.current?.scrollTop || 0; };
  }, [selected.id]);
  return <div className="detail-scrim" onClick={onClose}>
    <aside ref={drawer} className="detail-drawer" role="dialog" aria-modal="true" aria-label={selected.name} tabIndex={-1} onClick={event => event.stopPropagation()}>
      <div className="drawer-actions"><button className="drawer-fullscreen" type="button" onClick={onToggleFullscreen} aria-label={fullscreen ? '退出地图全屏' : '地图全屏'}>{fullscreen ? '退出全屏' : '地图全屏'}</button>
        <button ref={closeButton} className="drawer-close" onClick={onClose} aria-label="关闭">×</button></div>
      <span className="intro-overline">{selected.region || selected.source}</span>
      <h2>{selected.name}</h2>
      {iconFor(selected) && <img className="drawer-art" src={iconFor(selected)} alt={`${selected.name}版画插画`} />}
      <blockquote>{selected.quote || selected.description || selected.raw?.properties.source_quote}</blockquote>
      {selected.raw?.properties.parent_event_id && <nav className="story-siblings" aria-label="补天四幕">{catalog.events.filter(item => item.properties.parent_event_id === selected.raw.properties.parent_event_id).map(item => <button key={item.id} aria-current={item.id === selected.id ? 'true' : undefined} onClick={event => onOpen(item.id, event.currentTarget)}>{item.properties.name}</button>)}</nav>}
      <h3>原文出处</h3><p>{selected.source || selected.raw?.properties.source_text}</p>
      {selected.url && <a className="source-link" href={selected.url} target="_blank" rel="noreferrer">打开所引篇章 ↗</a>}
      <h3>{selected.kind === 'story' ? '位置说明' : '方位表达'}</h3>
      <p>{selected.direction || selected.raw?.properties.basis_note}</p>
      <p className="source-caution">{selected.kind === 'story' ? '故事点为叙事锚点·示意，不表示真实地点、距离或未经原文支持的因果关系；插画中的器物与场景属于艺术解释。' : '原文未明示的方位不以图面位置补出；淡墨山海纹样仅为装饰。'}</p>
    </aside>
  </div>;
}

function MapPanel({ world, stageIndex, activeLayers, selectedId, onSelect, onFullscreenTargetChange, onFullscreenToggleChange, onJourneyBusyChange, onFullscreenStageChange, chapterTransition, autoPlayChapter }) {
  const stages = world.stages;
  const chapterId = stages[stageIndex].id;
  const isPrologue = chapterId === '00';
  const revealed = record => Number(record.reveal_chapter) <= Number(chapterId);
  const beastGroupOrders = new Map();
  const beasts = world.beasts.map(beast => {
    const groupIndex = beast.place_id ? beastGroupOrders.get(beast.place_id) || 0 : -1;
    if (beast.place_id) beastGroupOrders.set(beast.place_id, groupIndex + 1);
    return { ...beast, stage: beast.reveal_stage, groupIndex };
  });
  const places = world.places.map(place => ({ ...place, stage: place.reveal_stage }));
  const availableBeasts = beasts.filter(revealed);
  const mappedBeastCount = availableBeasts.filter(beast => beast.place_id && places.some(place => place.id === beast.place_id)).length;
  const mappedPlaceCount = new Set(availableBeasts.filter(beast => beast.place_id && places.some(place => place.id === beast.place_id)).map(beast => beast.place_id)).size;
  const domains = world.domains;
  const relationLines = world.relations;
  const terrain = world.terrain;
  const target = useRef(null);
  const map = useRef(null);
  const [mapInstance, setMapInstance] = useState(null);
  const [journeyId, setJourneyId] = useState(null);
  const chapterStoryOptions = animationCatalog.stories.filter(story => story.stage_id === chapterId && !['06-03', '07-journey'].includes(story.id));
  if (chapterId === kuafuJourney.stage_id) chapterStoryOptions.push({ id: kuafuJourney.event_id, stage_id: kuafuJourney.stage_id, name: '夸父逐日' });
  const defaultStoryId = chapterId === kuafuJourney.stage_id ? kuafuJourney.event_id : chapterStoryOptions[0]?.id;
  const activeJourneyId = chapterStoryOptions.some(story => story.id === journeyId) ? journeyId : null;
  const activeJourneyRef = useRef(activeJourneyId);
  activeJourneyRef.current = animationCatalog.stories.find(story => story.id === activeJourneyId)?.source_event_id || activeJourneyId;
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
  useEffect(() => { setJourneyId(autoPlayChapter ? defaultStoryId || null : null); }, [chapterId, autoPlayChapter, defaultStoryId]);
  const [journeyBusy, setJourneyBusy] = useState(false);
  const journeyBusyRef = useRef(false);
  journeyBusyRef.current = journeyBusy;
  const handleJourneyBusy = useCallback(busy => { setJourneyBusy(busy); onJourneyBusyChange(busy); }, [onJourneyBusyChange]);
  const areaSource = useRef(new VectorSource());
  const terrainSource = useRef(new VectorSource());
  const relationSource = useRef(new VectorSource());
  const pointSource = useRef(new VectorSource());
  const [hoverId, setHoverId] = useState(null);
  const [pinnedId, setPinnedId] = useState(null);
  const [touchSelectedId, setTouchSelectedId] = useState(null);
  const [portrait, setPortrait] = useState(null);
  const portraitTimer = useRef(null);
  const desiredPortraitId = useRef(null);
  const [nativeFullscreen, setNativeFullscreen] = useState(false);
  const [fallbackFullscreen, setFallbackFullscreen] = useState(false);
  const [panguRetry, setPanguRetry] = useState(0);
  const [shortMap, setShortMap] = useState(false);
  const [controlContainer, setControlContainer] = useState(null);
  const mapFrame = useRef(null);
  const hasShownWorld = useRef(false);
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

  useEffect(() => {
    if (!target.current || map.current) return undefined;
    const paper = new ImageLayer({ source: new ImageStatic({ url: '/data/atlas/myth-paper.png', imageExtent: EXTENT, projection, interpolate: true }) });
    const created = new OlMap({
      target: target.current,
      controls: defaultControls({ attribution: false, rotate: false, zoom: false }),
      layers: [
        paper,
        new VectorLayer({ source: areaSource.current, declutter: 'map-labels', style: feature => obscuredLabel(feature.getGeometry().getCoordinates(), feature.get('label')) ? null : new Style({
          text: new Text({ text: feature.get('label'), font: '14px "Noto Serif SC","SimSun",serif', padding: [5, 9, 5, 9], backgroundFill: new Fill({ color: '#eee2c5c9' }), fill: new Fill({ color: '#806d51' }), overflow: true }),
        }) }),
        new VectorLayer({ source: terrainSource.current, style: feature => new Style({ image: new Icon({ src: `/data/atlas/myth-icons/terrain/${feature.get('kind')}.png`, width: feature.get('width'), anchor: [0.5, 1], opacity: feature.get('opacity') }) }) }),
        new VectorLayer({ source: relationSource.current, style: feature => feature.get('arrow') ? new Style({
          text: new Text({ text: '▲', font: 'bold 12px sans-serif', fill: new Fill({ color: '#a83f2b' }), stroke: new Stroke({ color: '#f4ead2', width: 3 }) }),
        }) : new Style({
          stroke: new Stroke({ color: '#a83f2b', width: 1.5, lineDash: [7, 7] }),
          text: new Text({ text: obscuredLabel(feature.getGeometry().getCoordinateAt(.5), feature.get('label')) ? '' : feature.get('label'), placement: 'line', font: '11px "Noto Serif SC","SimSun",serif', fill: new Fill({ color: '#943b2b' }), stroke: new Stroke({ color: '#f4ead2', width: 4 }), overflow: true }),
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
            return record.id === activeRecordId.current ? 0 : { story: 1, domain: 2, place: 3, beast: 4 }[record.kind];
          };
          return rank(a) - rank(b);
        }, style: feature => {
          const record = feature.get('record');
          if (record.id === activeJourneyRef.current) return null;
          const active = record.id === activeRecordId.current;
          const dimmed = !active && record.kind !== 'place' && obscuredLabel(feature.getGeometry().getCoordinates(), record.name, record.kind === 'beast' ? 18 : -20);
          return new Style({ zIndex: active ? 40 : 1, text: new Text({ text: record.name, offsetY: record.kind === 'beast' ? 18 : -20, font: `${active ? 'bold 13px' : '12px'} "Noto Serif SC","SimSun",serif`, fill: new Fill({ color: dimmed ? '#392d2020' : '#392d20' }), stroke: new Stroke({ color: dimmed ? '#f5ecd520' : '#f5ecd5', width: 4 }), padding: [3, 5, 3, 5] }) });
        } }),
      ],
      interactions: defaultInteractions({ mouseWheelZoom: false }).extend([new MouseWheelZoom({ maxDelta: 0.38, duration: 380 })]),
      view: new View({ projection, center: [600, 400], resolution: 1, minResolution: 0.25, maxResolution: 1, extent: EXTENT, constrainOnlyCenter: false, smoothExtentConstraint: false, smoothResolutionConstraint: false, enableRotation: false }),
    });
    created.on('pointermove', event => {
      if (event.dragging) { setHoverId(null); setPinnedId(null); setTouchSelectedId(null); return; }
      if (event.originalEvent?.pointerType === 'touch') return;
      const hit = created.forEachFeatureAtPixel(event.pixel, feature => feature.get('record')?.id, { hitTolerance: 8 });
      setHoverId(hit || null);
      setTouchSelectedId(null);
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
      setTouchSelectedId(event.originalEvent?.pointerType === 'touch' ? hit || null : null);
    });
    target.current.addEventListener('pointerleave', () => setHoverId(null));
    map.current = created;
    setMapInstance(created);
    return () => { created.setTarget(undefined); map.current = null; };
  }, []);

  useEffect(() => {
    const activeMap = map.current;
    if (!activeMap || !target.current) return undefined;
    let previousSize = null;
    const syncBounds = () => {
      activeMap.updateSize();
      const size = activeMap.getSize();
      if (!size?.[0] || !size?.[1]) return;
      setShortMap(window.innerWidth > 640 && size[1] < 280);
      const maxResolution = Math.min(EXTENT[2] / size[0], EXTENT[3] / size[1]);
      const previous = activeMap.getView();
      const resizeFactor = previousSize ? Math.max(previousSize[0] / size[0], previousSize[1] / size[1]) : 1;
      const unchanged = previousSize && previousSize[0] === size[0] && previousSize[1] === size[1];
      previousSize = [...size];
      if (unchanged && Math.abs(previous.getMaxResolution() - maxResolution) < 0.005) return;
      activeMap.setView(new View({
        projection, center: previous.getCenter() || [600, 400],
        resolution: Math.min((previous.getResolution() || maxResolution) * resizeFactor, maxResolution), rotation: previous.getRotation(),
        minResolution: 0.25, maxResolution, extent: EXTENT, constrainOnlyCenter: false, smoothExtentConstraint: false, smoothResolutionConstraint: false, enableRotation: false,
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
    setTouchSelectedId(null);
    map.current?.getView().cancelAnimations();
    map.current?.getInteractions().forEach(interaction => interaction.setActive(!isPrologue));
    if (!isPrologue && !hasShownWorld.current && map.current) {
      map.current.getView().fit(stages[stageIndex].extent, { padding: [80, 65, 65, 65], duration: 0 });
      hasShownWorld.current = true;
    }
  }, [chapterId]);

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
  }, [visibleRecords, selectedId, hoverId, pinnedId, stageIndex]);

  useEffect(() => {
    const activeId = hoverId || (touchSelectedId && !hoverId ? touchSelectedId : null);
    const record = visibleRecords.find(item => item.id === activeId);
    const activeMap = map.current;
    const hasPortrait = record?.kind === 'story' && record.raw?.properties.person_ids?.length > 0 && !activeJourneyId && !(journeyBusy && (record.id === activeJourneyId || window.innerWidth <= 640 || shortMap));
    desiredPortraitId.current = hasPortrait && !selectedId ? record.id : null;
    window.clearTimeout(portraitTimer.current);
    if (!activeMap || !record || !hasPortrait || selectedId) { setPortrait(null); return undefined; }
    let armed = !hoverId;
    const update = () => {
      if (!armed || desiredPortraitId.current !== record.id) return;
      const pixel = activeMap.getPixelFromCoordinate([record.x ?? 1100, record.y ?? 120 + (record.stage || 0) * 40]);
      const size = activeMap.getSize();
      if (!pixel || !size) return;
      const narrow = window.matchMedia('(max-width: 640px)').matches;
      const compact = !narrow && size[0] < 560 && size[1] < 260;
      const width = Math.min(narrow ? 142 : compact ? size[0] / 2 - 25 : 185, size[0] - 24);
      let left = Math.max(width / 2 + 12, Math.min(size[0] - width / 2 - 12, pixel[0]));
      let height = narrow ? 128 : 185;
      const frame = target.current.getBoundingClientRect();
      const card = target.current.parentElement.querySelector('.ink-hover-card')?.getBoundingClientRect();
      const controls = target.current.parentElement.querySelector('.map-overlay-controls')?.getBoundingClientRect();
      const minTop = narrow && controls ? controls.bottom - frame.top + 8 : 10;
      const bottom = narrow && card ? card.top - frame.top - 8 : size[1] - 10;
      height = Math.min(height, Math.max(0, bottom - minTop));
      if (height < 36) { setPortrait(null); return; }
      const above = narrow || pixel[1] >= height + minTop + 30;
      const top = above ? Math.max(minTop + height, Math.min(bottom, pixel[1] - 25)) : Math.max(minTop, Math.min(bottom - height, pixel[1] + 15));
      const portraitTop = above ? top - height : top;
      if (!narrow && card && left + width / 2 > card.left - frame.left && portraitTop < card.bottom - frame.top && portraitTop + height > card.top - frame.top) {
        left = Math.max(width / 2 + 12, card.left - frame.left - width / 2 - 14);
      }
      setPortrait({ id: record.id, record, left, top, above, width, height });
    };
    portraitTimer.current = window.setTimeout(() => { armed = true; update(); }, hoverId ? 80 : 0);
    const view = activeMap.getView();
    activeMap.on('moveend', update);
    view.on('change:center', update);
    view.on('change:resolution', update);
    activeMap.on('change:size', update);
    return () => {
      activeMap.un('moveend', update);
      view.un('change:center', update);
      view.un('change:resolution', update);
      activeMap.un('change:size', update);
      window.clearTimeout(portraitTimer.current);
      if (desiredPortraitId.current === record.id) desiredPortraitId.current = null;
    };
  }, [hoverId, touchSelectedId, selectedId, visibleRecords, journeyBusy, shortMap, activeJourneyId]);

  useEffect(() => { map.current?.getLayers().forEach(layer => layer.changed()); }, [journeyBusy, activeJourneyId]);

  useEffect(() => {
    if (!selectedId) return;
    setHoverId(null);
    setPinnedId(null);
    setTouchSelectedId(null);
    setPortrait(null);
  }, [selectedId]);

  useEffect(() => {
    const visibleIds = new Set(visibleRecords.map(record => record.id));
    if (hoverId && !visibleIds.has(hoverId)) setHoverId(null);
    if (pinnedId && !visibleIds.has(pinnedId)) setPinnedId(null);
    if (touchSelectedId && !visibleIds.has(touchSelectedId)) setTouchSelectedId(null);
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
  }, [fallbackFullscreen, nativeFullscreen]);

  const isFullscreen = nativeFullscreen || fallbackFullscreen;
  useEffect(() => {
    if (isFullscreen) requestAnimationFrame(() => mapFrame.current?.focus({ preventScroll: true }));
  }, [isFullscreen]);
  useEffect(() => {
    if (!isFullscreen) return undefined;
    const handleFullscreenKeys = event => {
      if (selectedId || event.repeat || event.altKey || event.ctrlKey || event.metaKey || event.shiftKey) return;
      if (event.target?.closest?.('input, textarea, select, button, a, [contenteditable="true"], [role="slider"], .detail-scrim')) return;
      if (event.key !== 'ArrowRight' && event.key !== 'ArrowLeft') return;
      event.preventDefault();
      onFullscreenStageChange(stageIndex + (event.key === 'ArrowRight' ? 1 : -1));
    };
    window.addEventListener('keydown', handleFullscreenKeys);
    return () => window.removeEventListener('keydown', handleFullscreenKeys);
  }, [isFullscreen, selectedId, stageIndex, onFullscreenStageChange]);
  useEffect(() => {
    onFullscreenTargetChange?.(isFullscreen ? mapFrame.current : null);
  }, [isFullscreen, onFullscreenTargetChange]);
  const toggleFullscreen = useCallback(async () => {
    const frame = mapFrame.current;
    if (!frame) return;
    if (fallbackFullscreen) { setFallbackFullscreen(false); return; }
    if (document.fullscreenElement === frame) { await document.exitFullscreen(); return; }
    if (!frame.requestFullscreen) { setFallbackFullscreen(true); frame.focus({ preventScroll: true }); requestAnimationFrame(() => frame.focus({ preventScroll: true })); return; }
    try { await frame.requestFullscreen(); requestAnimationFrame(() => frame.focus({ preventScroll: true })); } catch { setFallbackFullscreen(true); frame.focus({ preventScroll: true }); requestAnimationFrame(() => frame.focus({ preventScroll: true })); }
  }, [fallbackFullscreen]);
  useEffect(() => { onFullscreenToggleChange(() => toggleFullscreen); }, [toggleFullscreen, onFullscreenToggleChange]);

  const fitStage = () => { map.current?.dispatchEvent('journey:user-view'); map.current?.getView().fit(stages[stageIndex].extent, { duration: 320, padding: [50, 50, 70, 50], maxZoom: 2.4 }); };
  const exportStage = () => {
    const activeMap = map.current;
    if (!activeMap) return;
    activeMap.once('rendercomplete', () => {
      const size = activeMap.getSize();
      if (!size) return;
      const output = document.createElement('canvas');
      output.width = size[0];
      output.height = size[1];
      const context = output.getContext('2d');
      activeMap.getViewport().querySelectorAll('.ol-layer canvas').forEach(canvas => {
        if (!canvas.width) return;
        const opacity = canvas.parentNode.style.opacity;
        context.globalAlpha = opacity === '' ? 1 : Number(opacity);
        const transform = canvas.style.transform.match(/^matrix\((.+)\)$/);
        context.setTransform(...(transform ? transform[1].split(',').map(Number) : [1, 0, 0, 1, 0, 0]));
        context.drawImage(canvas, 0, 0);
      });
      context.setTransform(1, 0, 0, 1, 0, 0);
      context.globalAlpha = 1;
      context.fillStyle = '#544431';
      context.font = '14px "Noto Serif SC", SimSun, serif';
      context.fillText(`山海寻踪 · ${stages[stageIndex].id} ${stages[stageIndex].title}`, 18, 28);
      context.font = '11px "Noto Serif SC", SimSun, serif';
      context.fillText('方位与篇目关系示意 · 点位间距不表示真实距离', 18, size[1] - 18);
      const link = document.createElement('a');
      link.download = `shan-hai-stage-${stages[stageIndex].id}.png`;
      link.href = output.toDataURL('image/png');
      link.click();
    });
    activeMap.renderSync();
  };
  const hoverRecord = !selectedId && visibleRecords.find(record => record.id === (hoverId || pinnedId));
  const hoverStoryId = hoverRecord && chapterStoryOptions.find(story => story.id === hoverRecord.id || story.source_event_id === hoverRecord.id || story.event_id === hoverRecord.id)?.id;
  const visiblePortrait = portrait && portrait.id === (hoverId || touchSelectedId) && !selectedId ? portrait : null;

  const mapControls = <div className="map-overlay-controls">{isFullscreen && <span className="fullscreen-orientation" aria-label="图面北向">北 ↑</span>}
      <div className="myth-layer-switches" aria-label="专题图层">
        <label><input type="checkbox" checked={activeLayers.beasts} onChange={event => activeLayers.onBeasts(event.target.checked)} /> 异兽谱</label>
        <label><input type="checkbox" checked={activeLayers.divine} onChange={event => activeLayers.onDivine(event.target.checked)} /> 神域</label>
      </div>
        {chapterStoryOptions.length > 0 && <label className="map-animation-choice">故事动画 <select aria-label="选择地图故事动画" value={activeJourneyId || ''} onChange={event => { setHoverId(null); setPinnedId(null); setTouchSelectedId(null); setPortrait(null); setJourneyId(event.target.value || null); }}><option value="">关闭动画</option>{chapterStoryOptions.map(story => <option key={story.id} value={story.id}>{story.name}</option>)}</select></label>}
      {isFullscreen ? <details className="map-tools"><summary>地图工具</summary><div><button className="map-fit" onClick={fitStage}>看本章山海</button><button className="map-fit" onClick={exportStage}>存为本章 PNG</button></div></details> : <><button className="map-fit" onClick={fitStage}>看本章山海</button><button className="map-fit" onClick={exportStage}>存为本章 PNG</button></>}
    </div>;
  const preview = hoverRecord && <div className="ink-hover-card" role="status"><span>{hoverRecord.region}</span><b>{hoverRecord.name}</b><p>{hoverRecord.description}</p><small>{hoverRecord.direction}</small><button aria-label="展开原文与出处 ↗" onClick={event => onSelect(hoverRecord.id, event.currentTarget)}>展开原文与出处 ↗</button>{hoverStoryId && <button onClick={() => { setJourneyId(hoverStoryId); setHoverId(null); setPinnedId(null); setTouchSelectedId(null); setPortrait(null); }} aria-label="播放故事动画">播放动画</button>}</div>;
  const legend = <small className="map-range-legend"><i className="legend-story" />故事示意<i className="legend-place" />篇目地点<i />篇目山列<span>兽形图标：异兽</span></small>;
  const layerStatus = <div className="map-layer-summary" role="status">{activeLayers.beasts && <span>{availableBeasts.length ? "异兽图层 · " + mappedBeastCount + " 条已关联" : "本章暂无异兽"}{!availableBeasts.length && <button onClick={activeLayers.onGoToFirstBeast}>前往第 3 章 ↗</button>}</span>}{activeLayers.divine && <span>神域已显示</span>}</div>;
  const fullscreenButton = <button className="map-fullscreen" onClick={toggleFullscreen} aria-pressed={isFullscreen} aria-label={isFullscreen ? '退出地图全屏' : '地图全屏'}>{isFullscreen ? '退出全屏' : '全屏展示'}</button>;

  return <section ref={mapFrame} tabIndex={-1} className={`myth-map-wrap ${isPrologue ? "is-prologue" : ""} ${isFullscreen ? "is-map-fullscreen" : ""} ${fallbackFullscreen ? "is-fallback-fullscreen" : ""} ${shortMap ? "is-short-map" : ""} ${activeJourneyId ? "has-journey" : ""} ${activeJourneyId && activeJourneyId !== "03-05" ? "has-local-story" : ""}`} aria-label={isPrologue ? "盘古开天序章场景" : "山海经方位关系地图"}>
    {isFullscreen && <header className="fullscreen-toolbar" aria-label="全屏地图工具栏"><div className="fullscreen-chapter-nav" aria-label="全屏章节切换">
      <button type="button" onClick={() => { onFullscreenStageChange(stageIndex - 1); mapFrame.current?.focus({ preventScroll: true }); }} disabled={stageIndex === 0}>← 上一章</button>
      <span><small>{stages[stageIndex].id} / {String(stages.length - 1).padStart(2, '0')}</small><b>{stages[stageIndex].title}</b></span>
      <button type="button" onClick={() => { onFullscreenStageChange(stageIndex + 1); mapFrame.current?.focus({ preventScroll: true }); }} disabled={stageIndex >= stages.length - 1}>下一章 →</button>
    </div>{!isPrologue && mapControls}{fullscreenButton}</header>}
    <div className="map-surface"><div ref={target} className="myth-map-canvas" />
{isPrologue && <div className="prologue-scene">
      <PanguLoadBoundary key={panguRetry} fallback={<PanguPoster scene={stages[stageIndex].scene} controlContainer={isFullscreen ? controlContainer : null} onRetry={() => setPanguRetry(value => value + 1)} />}>
        <Suspense fallback={<PanguPoster scene={stages[stageIndex].scene} controlContainer={isFullscreen ? controlContainer : null} onRetry={() => setPanguRetry(value => value + 1)} />}>
          <PanguOpening active={isPrologue} autoStart={autoPlayChapter || false} selected={Boolean(selectedId)} onBusyChange={onJourneyBusyChange} controlContainer={isFullscreen ? controlContainer : null} />
        </Suspense>
      </PanguLoadBoundary>
      {!isFullscreen && <><button className="prologue-source" onClick={event => onSelect('01-01', event.currentTarget)}>盘古开天 · 原文与出处 ↗</button><span className="prologue-caption">混沌初开 · 天地初分</span></>}
    </div>}
    {!isPrologue && <>
      {!isFullscreen && <><div className="map-orientation" aria-label="图面方位示意"><span>北</span><i>↑</i><span>西　中　东</span><i>↓</i><span>南</span></div>{mapControls}</>}
    {visiblePortrait && !isFullscreen && <div key={visiblePortrait.id} className={`map-role-portrait ${visiblePortrait.above ? 'is-above' : 'is-below'} ${visiblePortrait.record.artworks?.length > 1 ? 'has-pair' : ''}`} style={{ left: visiblePortrait.left, top: visiblePortrait.top, width: visiblePortrait.width, height: visiblePortrait.height }} aria-hidden="true">
      {(visiblePortrait.record.artworks?.length ? visiblePortrait.record.artworks : [visiblePortrait.record.artwork]).filter(Boolean).map((artwork, index) => <img key={`${visiblePortrait.id}-${index}`} src={artwork.startsWith('/') ? artwork : `/data/atlas/myth-icons/${artwork}`} alt="" />)}
    </div>}
      {!isFullscreen && preview}
    {activeJourneyId === '03-05' && mapInstance && <KuafuJourney map={mapInstance} selectedId={selectedId} onSelect={onSelect} onBusyChange={handleJourneyBusy} controlContainer={isFullscreen ? controlContainer : null} />}
    {activeJourneyId && activeJourneyId !== '03-05' && mapInstance && <StoryAnimation key={activeJourneyId} id={activeJourneyId} map={mapInstance} selectedId={selectedId} onSelect={onSelect} onBusyChange={handleJourneyBusy} onSceneBoundsChange={handleSceneBounds} controlContainer={isFullscreen ? controlContainer : null} onSkip={() => setJourneyId(null)} />}
      {!isFullscreen && <><span className="map-rule-note">{legend}</span>{(activeLayers.beasts || activeLayers.divine) && layerStatus}</>}
    </>}
    {!isFullscreen && fullscreenButton}
    <div className={`chapter-transition-veil ${chapterTransition ? "is-visible" : ""}`} aria-hidden="true" />
    </div>
    {isFullscreen && <footer className="fullscreen-dock" aria-label="地图播放与信息栏">
      {isPrologue && <div className="fullscreen-prologue-title"><b>盘古开天</b><button className="prologue-source" onClick={event => onSelect("01-01", event.currentTarget)}>原文与出处 ↗</button></div>}
      <div className="fullscreen-control-slot" ref={setControlContainer} />
      {!isPrologue && <div className="fullscreen-preview-slot" aria-label="地图地点预览">{preview}</div>}
      {!isPrologue && !activeJourneyId && <div className="fullscreen-idle-info"><span className="fullscreen-orientation">北 ↑</span>{legend}{layerStatus}</div>}
    </footer>}
  </section>;
}

function Timeline({ stages, index, onSelect, playing, onPlay, containerRef }) {
  const slider = useRef(null);
  const lastIndex = stages.length - 1;
  const setFromPointer = event => {
    const rect = slider.current.getBoundingClientRect();
    const value = Math.round(Math.max(0, Math.min(1, (event.clientX - rect.left) / rect.width)) * (stages.length - 1));
    onSelect(value);
  };
  return <section ref={containerRef} className="myth-timeline" aria-label="序章与七章神话时间轴">
    <div className="timeline-current"><button onClick={() => onSelect(Math.max(0, index - 1))} disabled={!index}>‹</button><button onClick={onPlay} aria-label={playing ? '暂停' : '播放'}>{playing ? 'Ⅱ' : '▶'}</button><button onClick={() => onSelect(Math.min(stages.length - 1, index + 1))} disabled={index === stages.length - 1}>›</button><span><small>第 {stages[index].id} 章</small><b>{stages[index].title}</b></span></div>
    <div className="timeline-steps">{stages.map((stage, i) => <button key={stage.id} aria-current={index === i ? 'step' : undefined} onClick={() => onSelect(i)}><i>{stage.id}</i>{stage.title}</button>)}</div>
    <div className="chapter-slider" ref={slider} tabIndex={0} role="slider" aria-valuemin={0} aria-valuemax={lastIndex} aria-valuenow={index} aria-valuetext={`第 ${stages[index].id} 章 ${stages[index].title}`}
      onPointerDown={event => { if (event.button !== 0) return; event.currentTarget.setPointerCapture(event.pointerId); onSelect(index); setFromPointer(event); }}
      onPointerMove={event => { if (event.currentTarget.hasPointerCapture(event.pointerId)) setFromPointer(event); }}
      onPointerUp={event => { if (event.currentTarget.hasPointerCapture(event.pointerId)) { setFromPointer(event); event.currentTarget.releasePointerCapture(event.pointerId); } }}
      onPointerCancel={event => { if (event.currentTarget.hasPointerCapture(event.pointerId)) event.currentTarget.releasePointerCapture(event.pointerId); onSelect(index); }}
      onKeyDown={event => { const next = { ArrowRight: index + 1, ArrowUp: index + 1, ArrowLeft: index - 1, ArrowDown: index - 1, Home: 0, End: lastIndex }[event.key]; if (next !== undefined) { event.preventDefault(); onSelect(Math.max(0, Math.min(lastIndex, next))); } }}>
      <i style={{ width: `${index / lastIndex * 100}%` }} /><span style={{ left: `${index / lastIndex * 100}%` }} />
    </div>
  </section>;
}

function Bestiary({ beasts, onOpen }) {
  const grid = useRef(null);
  const [columns, setColumns] = useState(2);
  const [expanded, setExpanded] = useState(false);
  const [search, setSearch] = useState('');
  const [bookFilter, setBookFilter] = useState('全部篇目');
  const hasFilter = Boolean(search.trim()) || bookFilter !== '全部篇目';
  const list = beasts.filter(beast => (bookFilter === '全部篇目' || beast.region === bookFilter) && (!search.trim() || `${beast.name} ${beast.region} ${beast.description}`.includes(search.trim())));
  const showAll = expanded || hasFilter;
  useEffect(() => {
    const measure = () => setColumns(getComputedStyle(grid.current).gridTemplateColumns.split(' ').length);
    const observer = new ResizeObserver(measure);
    observer.observe(grid.current);
    measure();
    return () => observer.disconnect();
  }, []);
  useEffect(() => setExpanded(false), [search, bookFilter]);
  return <section className="best-page" id="creatures">
    <div className="best-page-heading"><h2>山海经异兽谱</h2><p>收录32项异兽 · 同名异篇分开呈现</p></div>
    <div className="bestiary-tools"><input value={search} onChange={event => setSearch(event.target.value)} placeholder="搜索异兽或形貌" aria-label="搜索异兽" /><select value={bookFilter} onChange={event => setBookFilter(event.target.value)} aria-label="按篇目筛选"><option>全部篇目</option>{Array.from(new Set(beasts.map(item => item.region))).map(item => <option key={item}>{item}</option>)}</select><span>{list.length} 项索引 · {showAll ? '全部匹配条目' : '首行预览'}</span></div>
    <div className="beast-grid" id="beast-cards" ref={grid} data-expanded={showAll}>{(showAll ? list : list.slice(0, columns)).map(beast => <button className="beast-card" key={beast.id} onClick={event => onOpen(beast.id, event.currentTarget)}><div className="beast-art">{iconFor(beast) ? <img src={iconFor(beast)} alt="" loading="lazy" /> : <div className="beast-placeholder" aria-hidden="true"><span>異</span><i>山海经</i></div>}<span>{beast.region}</span></div><b>{beast.name}</b><p>{beast.description}</p><small>{beast.source} · 第 {beast.reveal_chapter} 章起可见（非诞生年代）</small></button>)}</div>
    {!list.length && <p className="bestiary-empty">没有找到匹配的异兽，请换一个名称或篇目。</p>}
    <button className="bestiary-toggle" aria-controls="beast-cards" aria-expanded={showAll} onClick={() => { if (hasFilter) { setSearch(''); setBookFilter('全部篇目'); setExpanded(false); } else setExpanded(value => !value); }}>{hasFilter ? '清除筛选并收起' : expanded ? '收起异兽谱 ↑' : `展开全部 ${beasts.length} 项 ↓`}</button>
  </section>;
}

export default function App() {
  const [world, setWorld] = useState(mythWorld);
  const [stageIndex, setStageIndex] = useState(0);
  const [playing, setPlaying] = useState(false);
  const [journeyBusy, setJourneyBusy] = useState(false);
  const [chapterTransition, setChapterTransition] = useState(false);
  const [activeLayers, setActiveLayers] = useState({ beasts: false, divine: false });
  const [selectedId, setSelectedId] = useState(null);
  const [fullscreenTarget, setFullscreenTarget] = useState(null);
  const [fullscreenToggle, setFullscreenToggle] = useState(() => () => {});
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
    if (!import.meta.env.DEV && !apiBase) return undefined;
    const controller = new AbortController();
    fetch(`${apiBase}/api/world`, { signal: controller.signal })
      .then(response => response.ok ? response.json() : Promise.reject(new Error('world api unavailable')))
      .then(data => { if (data.revision && Array.isArray(data.stages) && Array.isArray(data.beasts)) setWorld(data); })
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
        const top = worldLayout.current?.getBoundingClientRect().top;
        if (window.location.hash === '#world' && Number.isFinite(top) && Math.abs(top) < 80) {
          window.scrollTo({ top: window.scrollY + top, behavior: 'instant' });
        }
      });
    };
    window.addEventListener('resize', alignWorldAfterResize);
    window.visualViewport?.addEventListener('resize', alignWorldAfterResize);
    measure();
    if (window.location.hash === '#world') requestAnimationFrame(() => worldLayout.current?.scrollIntoView({ block: 'start', behavior: 'instant' }));
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
        <MapPanel world={world} stageIndex={stageIndex} autoPlayChapter={playing || autoPlayChapterId === stages[stageIndex].id} activeLayers={{ ...activeLayers, onBeasts: checked => setActiveLayers(state => ({ ...state, beasts: checked })), onDivine: checked => setActiveLayers(state => ({ ...state, divine: checked })), onGoToFirstBeast: () => { const index = stages.findIndex(stage => world.beasts.some(beast => beast.reveal_chapter === stage.id)); if (index >= 0) selectStage(index); } }} selectedId={selectedId} onSelect={open} onFullscreenTargetChange={setFullscreenTarget} onFullscreenToggleChange={setFullscreenToggle} onJourneyBusyChange={setJourneyBusy} onFullscreenStageChange={navigateFullscreenStage} chapterTransition={chapterTransition} />
        <Timeline containerRef={timeline} stages={stages} index={stageIndex} playing={playing} onSelect={selectStage} onPlay={() => { if (stageIndex === stages.length - 1 && !playing) setStageIndex(0); setPlaying(value => !value); }} />
      </div>
    </section>
    <Bestiary beasts={beasts} onOpen={open} />
    <section className="reading-notes" id="reading-notes" aria-labelledby="reading-notes-title"><h2 id="reading-notes-title">读图与依据</h2>          <div className="reading-notes-text"><p>《山海经》依山川和方位展开，不是编年史。序章与七章次序是本项目的叙事编排；各章内部仅在原文或可靠叙事关系可核实处排列先后，不代表精确年代。</p><p>经文距离不按比例绘制；淡墨山形为装饰。重要地点以名称和原文标识，故事示意点不表示真实位置。</p></div><p>各篇神域记载不预设为同一空间体系。异兽图标仅关联有篇目依据的地点锚点；缺少可靠地点依据的条目收录在异兽谱中。</p><p>山海空间与异兽描写以《山海经》正文条目为依据，神话故事沿用各条目所列典籍与出处。插画是本项目依据正文的图像解释，不作为古本插图或新增考据证据。</p></section>
    <footer className="myth-footer"><span>版式：方位关系与叙述次序 · 不设距离比例</span><span>山海空间与异兽描写：以《山海经》正文条目核对</span></footer>
    {selected && createPortal(<DetailDrawer selected={selected} onClose={closeDetail} onOpen={open} onToggleFullscreen={fullscreenToggle} fullscreen={Boolean(fullscreenTarget)} scrollTopRef={detailScrollTop} />, fullscreenTarget || document.body)}
  </main>;
}
