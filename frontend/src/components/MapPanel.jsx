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
import catalog from '../../public/data/atlas/catalog.json';
import animationCatalog from '../../public/data/atlas/story-animations.json';
import kuafuJourney from '../../public/data/atlas/kuafu-journey.json';
import KuafuJourney from '../KuafuJourney';
import StoryAnimation from '../StoryAnimation';
import { assetUrl, iconFor } from '../asset-url';

const PanguOpening = lazy(() => import('../PanguOpening'));

class PanguLoadBoundary extends Component {
  state = { failed: false };
  static getDerivedStateFromError() { return { failed: true }; }
  render() { return this.state.failed ? this.props.fallback : this.props.children; }
}

function PanguPoster({ scene, onRetry, controlContainer }) {
  const controls = <button className="pangu-retry" type="button" onClick={onRetry}>播放动态序章</button>;
  return <div className="pangu-loading-poster"><img src={assetUrl(scene)} alt="盘古分开混沌，天地初开木刻场景" />{controlContainer ? createPortal(controls, controlContainer) : controls}</div>;
}

const EXTENT = [0, 0, 1200, 800];
const projection = new Projection({ code: 'mythic-plane', units: 'pixels', extent: EXTENT });


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
export default function MapPanel({ world, stageIndex, activeLayers, selectedId, onSelect, onFullscreenTargetChange, onJourneyBusyChange, onFullscreenStageChange, chapterTransition, autoPlayChapter }) {
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
    const paper = new ImageLayer({ source: new ImageStatic({ url: assetUrl('/data/atlas/myth-paper.png'), imageExtent: EXTENT, projection, interpolate: true }) });
    const created = new OlMap({
      target: target.current,
      controls: defaultControls({ attribution: false, rotate: false, zoom: false }),
      layers: [
        paper,
        new VectorLayer({ source: areaSource.current, declutter: 'map-labels', style: feature => obscuredLabel(feature.getGeometry().getCoordinates(), feature.get('label')) ? null : new Style({
          text: new Text({ text: feature.get('label'), font: '14px "Noto Serif SC","SimSun",serif', padding: [5, 9, 5, 9], backgroundFill: new Fill({ color: '#eee2c5c9' }), fill: new Fill({ color: '#806d51' }), overflow: true }),
        }) }),
        new VectorLayer({ source: terrainSource.current, style: feature => new Style({ image: new Icon({ src: assetUrl(`/data/atlas/myth-icons/terrain/${feature.get('kind')}.png`), width: feature.get('width'), anchor: [0.5, 1], opacity: feature.get('opacity') }) }) }),
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
    if (isFullscreen && !selectedId) requestAnimationFrame(() => mapFrame.current?.focus({ preventScroll: true }));
  }, [isFullscreen, selectedId]);
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
      {(visiblePortrait.record.artworks?.length ? visiblePortrait.record.artworks : [visiblePortrait.record.artwork]).filter(Boolean).map((artwork, index) => <img key={`${visiblePortrait.id}-${index}`} src={assetUrl(artwork.startsWith('/') ? artwork : `/data/atlas/myth-icons/${artwork}`)} alt="" />)}
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
