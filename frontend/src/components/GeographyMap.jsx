import { useEffect, useMemo, useRef, useState } from 'react';
import Map from 'ol/Map';
import View from 'ol/View';
import Feature from 'ol/Feature';
import Point from 'ol/geom/Point';
import LineString from 'ol/geom/LineString';
import { greatCircleArc } from 'ol/geom/flat/geodesic';
import VectorLayer from 'ol/layer/Vector';
import VectorSource from 'ol/source/Vector';
import ScaleLine from 'ol/control/ScaleLine';
import Attribution from 'ol/control/Attribution';
import TileLayer from 'ol/layer/Tile';
import OSM from 'ol/source/OSM';
import { geographyMapConfig } from '../geography-map-config';
import { defaults as interactions } from 'ol/interaction';
import { fromLonLat, toLonLat, transformExtent } from 'ol/proj';
import { getDistance } from 'ol/sphere';
import { unByKey } from 'ol/Observable';
import { Circle, RegularShape, Fill, Stroke, Style, Text } from 'ol/style';
import { useLocale, translate } from '../i18n';
import { ChapterNotice } from '../motion';
import { EMPTY_RECORD_NOTICE_MS } from '../map-timing';
import { groupReferences, referenceCollection, geographicEvents, geographicReferences, defaultGeographicEvent, associationLabel, unlocatedStories } from '../geography';
import GeographicEvidence from './GeographicEvidence';
import GeographyComparison from './GeographyComparison';
import '../styles/geography.css';

const area = transformExtent(geographyMapConfig.nationalExtent, 'EPSG:4326', 'EPSG:3857');
const worldExtent = transformExtent([-180, -85.05112878, 180, 85.05112878], 'EPSG:4326', 'EPSG:3857');
const coordinates = value => value.map(number => number.toFixed(3)).join(', ');

export default function GeographyMap({ catalog, chapterId, currentEventId, visible, transitioning, snapshot, onSnapshot, onEventChange, onOpen }) {
  const { t, locale } = useLocale();
  const target = useRef(null), map = useRef(null), source = useRef(null), measurement = useRef(null);
  if (!source.current) source.current = new VectorSource();
  if (!measurement.current) measurement.current = new VectorSource();
  const originEventId = defaultGeographicEvent(catalog, chapterId, currentEventId);
  const restore = snapshot.originEventId === originEventId && geographicEvents(catalog).some(event => event.id === snapshot.eventId);
  const [eventId, setEventId] = useState(restore ? snapshot.eventId : originEventId);
  const events = useMemo(() => geographicEvents(catalog), [catalog]);
  const references = useMemo(() => geographicReferences(catalog), [catalog]);
  const [query, setQuery] = useState(restore ? snapshot.query || '' : '');
  const [selectedId, setSelectedId] = useState(restore ? snapshot.selectedId || null : null);
  const [position, setPosition] = useState([105, 35]);
  const [measuring, setMeasuring] = useState(false), measureMode = useRef(false), measurePoints = useRef([]);
  const [distance, setDistance] = useState(null), [loadError, setLoadError] = useState(false), [tilesReady, setTilesReady] = useState(false), [emptyNotice, setEmptyNotice] = useState(false);
  const viewMode = useRef(restore ? snapshot.viewMode || 'national' : 'national');
  const layerRefs = useRef({}), current = useRef({}), latestSnapshot = useRef(snapshot), [ready, setReady] = useState(false);
  const compareTrigger = useRef(null);
  const [compareOpen, setCompareOpen] = useState(restore && Boolean(snapshot.compareOpen));
  const [compareIds, setCompareIds] = useState(restore ? snapshot.compareIds || [] : []);
  const eventRecords = references.filter(item => item.properties.entity_id === eventId);
  const comparisonIds = [...new Set([...compareIds, ...eventRecords.map(item => item.id)])]
    .filter(id => eventRecords.some(item => item.id === id)).slice(0, 2);
  const records = useMemo(() => references.filter(item => item.properties.entity_id === eventId
    && (!query.trim() || `${item.properties.label} ${translate(item.properties.label, 'en')} ${item.properties.originalName || item.properties.name || ''} ${associationLabel(item)} ${translate(associationLabel(item), 'en')}`.toLocaleLowerCase().includes(query.trim().toLocaleLowerCase()))), [references, eventId, query, locale]);
  const selected = records.find(item => item.id === selectedId);
  current.current = { selectedId, records, label: selected ? t(selected.properties.label) : '' };
  latestSnapshot.current = { ...latestSnapshot.current, originEventId, eventId, query, selectedId, viewMode: viewMode.current, compareOpen, compareIds: comparisonIds };

  const takeMeasurement = coordinate => {
    const points = measurePoints.current.length === 2 ? [] : measurePoints.current;
    points.push(coordinate); measurePoints.current = points;
    measurement.current.clear();
    points.forEach(point => measurement.current.addFeature(new Feature(new Point(fromLonLat(point)))));
    if (points.length === 2) {
      const view = map.current.getView();
      const arc = greatCircleArc(...points[0], ...points[1], view.getProjection(), (view.getResolution() / 2) ** 2);
      measurement.current.addFeature(new Feature(new LineString(arc, 'XY')));
      setDistance(getDistance(points[0], points[1]));
    } else setDistance(null);
  };
  const measureAction = useRef(takeMeasurement); measureAction.current = takeMeasurement;

  useEffect(() => {
    let live = true;
    const listeners = [];
    let failed = false;
    const newBasemap = () => {
      failed = false;
      const tileSource = new OSM({ url: geographyMapConfig.tileUrl, crossOrigin: 'anonymous', wrapX: false });
      listeners.push(tileSource.on('tileloaderror', () => { failed = true; if (live) setLoadError(true); }));
      return tileSource;
    };
    const background = new TileLayer({ source: newBasemap(), preload: 0 });
    const points = new VectorLayer({ source: source.current, style: feature => {
      const ids = feature.get('ids'), active = ids.includes(current.current.selectedId);
      const traditional = feature.get('traditional');
      const color = traditional ? '#496d75' : '#983e2c';
      const options = { radius: active ? 10 : 8, fill: new Fill({ color: active ? color : '#f5efdf' }), stroke: new Stroke({ color, width: 2 }) };
      const marker = new Style({ image: traditional ? new RegularShape({ ...options, points: 4 }) : new Circle(options),
        text: new Text({ text: ids.length > 1 ? String(ids.length) : '·', font: 'bold 12px sans-serif', fill: new Fill({ color: active ? '#fff7e5' : color }) }) });
      if (!active) return marker;
      const pixel = map.current?.getPixelFromCoordinate(feature.getGeometry().getCoordinates()) || [150, 100];
      const width = map.current?.getSize()?.[0] || 300;
      const align = pixel[0] < 100 ? 'left' : pixel[0] > width - 100 ? 'right' : 'center';
      return [marker, new Style({ text: new Text({ text: current.current.label, font: '14px sans-serif', textAlign: align,
        offsetX: align === 'left' ? 12 : align === 'right' ? -12 : 0, offsetY: pixel[1] < 30 ? 22 : -20,
        fill: new Fill({ color: '#702f24' }), stroke: new Stroke({ color: '#f5efdf', width: 4 }) }) })];
    } });
    const ruler = new VectorLayer({ source: measurement.current, style: new Style({ stroke: new Stroke({ color: '#496d75', width: 2, lineDash: [6, 4] }), image: new Circle({ radius: 5, fill: new Fill({ color: '#496d75' }) }) }) });
    const instance = new Map({ target: target.current, layers: [background, points, ruler], controls: [new ScaleLine({ units: 'metric' }), new Attribution({ collapsible: false })],
      interactions: interactions({ doubleClickZoom: false }), view: new View({ projection: 'EPSG:3857', center: restore && snapshot.center || fromLonLat([105, 35]), zoom: restore ? snapshot.zoom ?? 4 : 4, minZoom: 1, maxZoom: geographyMapConfig.maxZoom, extent: worldExtent, constrainOnlyCenter: false, smoothExtentConstraint: false, smoothResolutionConstraint: false, enableRotation: false }) });
    map.current = instance; layerRefs.current = { background, newBasemap };
    instance.on('rendercomplete', () => { if (live && !failed) setTilesReady(true); });
    instance.on('movestart', () => { if (instance.getView().getInteracting()) viewMode.current = 'local'; });
    instance.on('pointermove', event => { if (!event.dragging) setPosition(toLonLat(event.coordinate)); });
    instance.on('singleclick', event => {
      const coordinate = toLonLat(event.coordinate); setPosition(coordinate);
      if (measureMode.current) { measureAction.current(coordinate); return; }
      const hit = instance.forEachFeatureAtPixel(event.pixel, feature => feature, { layerFilter: layer => layer === points, hitTolerance: 10 });
      if (hit) setSelectedId(hit.get('ids')[0]);
    });
    instance.on('moveend', () => {
      target.current.dataset.extent = JSON.stringify(transformExtent(instance.getView().calculateExtent(instance.getSize()), 'EPSG:3857', 'EPSG:4326'));
      latestSnapshot.current = { ...latestSnapshot.current, center: instance.getView().getCenter(), zoom: instance.getView().getZoom() };
      setPosition(toLonLat(instance.getView().getCenter()));
    });
    const observer = new ResizeObserver(() => {
      if (!target.current?.clientWidth || !target.current?.clientHeight) return;
      instance.updateSize();
      if (viewMode.current === 'national') instance.getView().fit(area, { padding: [24, 24, 24, 24], duration: 0 });
    }); observer.observe(target.current);
    setReady(true);
    return () => { live = false; unByKey(listeners); onSnapshot({ ...latestSnapshot.current, center: instance.getView().getCenter(), zoom: instance.getView().getZoom() }); observer.disconnect(); instance.setTarget(undefined); instance.dispose(); map.current = null; };
  }, []);

  useEffect(() => {
    if (!ready) return;
    const instance = map.current;
    if (!visible) { instance.setTarget(undefined); return; }
    instance.setTarget(target.current);
    const frame = requestAnimationFrame(() => {
      instance.updateSize();
      if (viewMode.current === 'national') instance.getView().fit(area, { padding: [24, 24, 24, 24], duration: 0 });
      else instance.render();
    });
    return () => cancelAnimationFrame(frame);
  }, [ready, visible]);

  const changeEvent = id => {
    setEventId(id); setQuery(''); setSelectedId(null); setCompareOpen(false); setCompareIds([]);
    measurement.current.clear(); measurePoints.current = []; setDistance(null);
    measureMode.current = false; setMeasuring(false);
  };
  useEffect(() => { if (originEventId !== eventId) changeEvent(originEventId); }, [originEventId]);
  useEffect(() => {
    setEmptyNotice(false);
    if (!visible || transitioning || eventRecords.length) return;
    setEmptyNotice(true);
    const timer = window.setTimeout(() => setEmptyNotice(false), EMPTY_RECORD_NOTICE_MS);
    return () => window.clearTimeout(timer);
  }, [visible, transitioning, eventId, eventRecords.length]);

  useEffect(() => {
    source.current.clear();
    source.current.addFeatures(groupReferences(records).map(group => new Feature({ geometry: new Point(fromLonLat(group[0].geometry.coordinates)), ids: group.map(item => item.id), traditional: group.some(item => item.properties.association_type === 'local_tradition') })));
  }, [records, ready]);
  useEffect(() => { source.current.changed(); }, [selectedId]);
  const nationwide = () => {
    viewMode.current = 'national';
    map.current?.getView().fit(area, { padding: [24, 24, 24, 24], duration: 0 });
  };
  const fit = () => {
    if (!map.current || !records.length) return;
    viewMode.current = 'local';
    map.current.getView().fit(source.current.getExtent(), { padding: [48, 48, 48, 48], maxZoom: 9, duration: 0 });
  };
  const locate = record => {
    setSelectedId(record.id); viewMode.current = 'local';
    map.current?.getView().setCenter(fromLonLat(record.geometry.coordinates));
    map.current?.getView().setZoom(Math.max(7, map.current.getView().getZoom()));
  };
  const retryBasemap = () => {
    setLoadError(false); setTilesReady(false);
    layerRefs.current.background.setSource(layerRefs.current.newBasemap());
  };
  const exportData = () => {
    const url = URL.createObjectURL(new Blob([JSON.stringify(referenceCollection(records), null, 2)], { type: 'application/geo+json' }));
    const link = document.createElement('a'); link.href = url; link.download = `shanhai-${eventId}-references.geojson`; link.click();
    window.setTimeout(() => URL.revokeObjectURL(url), 1000);
  };
  const unlocated = unlocatedStories(catalog);
  return <div className="geography-atlas" data-ready={ready} data-event-id={eventId} data-basemap-state={loadError ? 'error' : tilesReady ? 'ready' : 'loading'}>
    <p className="geo-note">{t('每次探索一个事件：地点表示地方传说或地理考证关联，不证明事件发生。')}</p>
    <div className="geo-tools"><label>{t('事件')}<select aria-label={t('地理事件')} value={eventId} onChange={event => { changeEvent(event.target.value); onEventChange(event.target.value); }}>{catalog.stages.map(stage => <optgroup key={stage.id} label={`${stage.id} ${t(stage.title)}`}>{events.filter(event => event.properties.stage_id === stage.id).map(event => <option key={event.id} value={event.id}>{t(event.properties.name)}</option>)}</optgroup>)}</select></label>
      <input aria-label={t('搜索地理参考点')} placeholder={t('搜索本事件地点或类型')} value={query} maxLength={100} onChange={event => setQuery(event.target.value)} />
      <button onClick={nationwide}>{t('全国总览')}</button><button onClick={fit} disabled={!records.length}>{t('查看本事件地点')}</button><button onClick={() => { viewMode.current = 'local'; map.current?.getView().setZoom(map.current.getView().getZoom() + 1); }} aria-label={t('地理地图放大')}>＋</button><button onClick={() => { viewMode.current = 'local'; map.current?.getView().setZoom(map.current.getView().getZoom() - 1); }} aria-label={t('地理地图缩小')}>−</button>
    </div>
    <p className="geo-legend"><span>◆ {t('地方传说')}</span><span>● {t('地理考证')}</span><span>{t('重合点显示数量，详情按条目区分类型。')}</span></p>
    <div className="geo-map-stage"><div className="geo-map" ref={target} tabIndex={0} onKeyDown={event => { if (['ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', '+', '-'].includes(event.key)) viewMode.current = 'local'; }} role="region" aria-label={t('真实地理参考地图')} /><span className="geo-north" aria-label={t('地图北向')}>{t('北 ↑')}</span><ChapterNotice change={transitioning} title={catalog.stages.find(stage => stage.id === chapterId)?.title} />{emptyNotice && <div className="geo-empty-notice" role="status"><b>{t('暂无记录')}</b><span>{t('当前资料尚未提供可靠关联地点')}</span></div>}</div>
    <div className="geo-readout"><span>{t('经度、纬度')} · {coordinates(position)}°</span><span>WGS84 · EPSG:4326 / 3857</span></div>
    <div className="geo-tools geo-secondary">
      <button aria-pressed={measuring} onClick={() => { measureMode.current = !measuring; setMeasuring(!measuring); }}>{t('两点测距')}</button>
      {measuring && <button onClick={() => measureAction.current(toLonLat(map.current.getView().getCenter()))}>{t('以视图中心取点')}</button>}
      {(measuring || distance !== null) && <button onClick={() => { measurement.current.clear(); measurePoints.current = []; setDistance(null); }}>{t('清除量测')}</button>}
      <button ref={compareTrigger} aria-expanded={compareOpen && comparisonIds.length === 2} aria-controls="geo-comparison" disabled={eventRecords.length < 2} onClick={() => setCompareOpen(value => !value)}>{t('对照本事件资料')}</button>
      <button onClick={exportData} disabled={!records.length}>{t('导出参考点 GeoJSON')}</button>
    </div>
    {measuring && <p className="geo-note">{t('在地图点选两个位置，或移动地图后用视图中心取点。量测为现代参考点之间的球面距离，不是古代行程。')}</p>}
    {distance !== null && <p className="geo-distance" role="status">{t('球面距离')} · {(distance / 1000).toFixed(2)} km</p>}
    {loadError && <p role="alert">{t('在线底图加载失败，部分区域可能未显示；关联资料仍可查询。')} <button onClick={retryBasemap}>{t('重试地理底图')}</button></p>}
    <div className="geo-results"><section aria-label={t('地理查询结果')}><p role="status">{t('参考点')} · {records.length}　{t('关联故事')} · {new Set(records.map(item => item.properties.entity_id)).size}</p>
      <div className="geo-result-list">{records.map(record => <button key={record.id} data-candidate-id={record.id} aria-pressed={selected?.id === record.id} onClick={() => locate(record)}><b>{t(record.properties.label)}</b><small>{t(associationLabel(record))}</small></button>)}</div>
      {!records.length && <p>{t(query ? '本事件没有匹配的参考点，请清除搜索。' : '本事件暂无可靠地点资料；保留故事阅读，不推测坐标。')}</p>}
    </section><section className="geo-reference" aria-label={t('参考点依据')}>
      {selected ? <><h3>{t(selected.properties.label)}</h3><GeographicEvidence record={selected} />
        <button onClick={() => onOpen(selected.properties.entity_id)}>{t('查看关联故事与出处')}</button>
      </> : <p>{t('选择地图标记或列表条目，查看传说版本、地理考证与位置精度。')}</p>}
    </section></div>
    {compareOpen && comparisonIds.length === 2 && <GeographyComparison records={eventRecords} ids={comparisonIds} onChange={(index, id) => setCompareIds(comparisonIds.map((value, position) => position === index ? id : value))} onClose={() => { setCompareOpen(false); compareTrigger.current?.focus({ preventScroll: true }); }} />}
    <details className="geo-unlocated"><summary>{t('尚无地理参考点的条目')} · {unlocated.length}</summary>{unlocated.map(event => <button key={event.id} onClick={() => onOpen(event.id)}>{t(event.properties.name)}</button>)}</details>
    <p className="geo-attribution">{t('底图：OpenStreetMap；地点为传说或考证关联，不是历史事件定位证明。')} <a href="https://www.openstreetmap.org/copyright" target="_blank" rel="noreferrer">© OpenStreetMap contributors</a></p>
  </div>;
}
