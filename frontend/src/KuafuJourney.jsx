import { createPortal } from 'react-dom';
import { useEffect, useRef, useState } from 'react';
import Feature from 'ol/Feature';
import Point from 'ol/geom/Point';
import LineString from 'ol/geom/LineString';
import Polygon from 'ol/geom/Polygon';
import VectorLayer from 'ol/layer/Vector';
import VectorSource from 'ol/source/Vector';
import { Circle as CircleStyle, Fill, Icon, Stroke, Style, Text } from 'ol/style';
import journey from '../public/data/atlas/kuafu-journey.json';
import catalog from '../public/data/atlas/catalog.json';

function curvedPath(points) {
  if (points.length < 3) return points;
  const result = [];
  for (let i = 0; i < points.length - 1; i++) {
    const [a, b, c, d] = [points[Math.max(0, i - 1)], points[i], points[i + 1], points[Math.min(points.length - 1, i + 2)]];
    for (let step = 0; step < 16; step++) {
      const t = step / 16;
      result.push([0, 1].map(axis => .5 * (2 * b[axis] + (-a[axis] + c[axis]) * t + (2 * a[axis] - 5 * b[axis] + 4 * c[axis] - d[axis]) * t * t + (-a[axis] + 3 * b[axis] - 3 * c[axis] + d[axis]) * t * t * t)));
    }
  }
  return [...result, points.at(-1)];
}

const phases = journey.phases.map(phase => {
  const path = curvedPath(phase.path);
  const distances = [0];
  for (let i = 1; i < path.length; i++) distances.push(distances.at(-1) + Math.hypot(path[i][0] - path[i - 1][0], path[i][1] - path[i - 1][1]));
  return { ...phase, path, distances, length: distances.at(-1) };
});
const route = phases.filter(phase => phase.path.length > 1).flatMap(phase => phase.path);
const raw = catalog.events.find(event => event.id === journey.event_id);
const record = { id: raw.id, name: raw.properties.name, kind: 'story', raw };

function positionAt(phase, ratio) {
  if (!phase.length) return phase.path[0];
  const distance = ratio * phase.length;
  const index = Math.max(1, phase.distances.findIndex(value => value >= distance));
  const a = phase.path[index - 1], b = phase.path[index];
  const t = (distance - phase.distances[index - 1]) / (phase.distances[index] - phase.distances[index - 1] || 1);
  return [a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t];
}

async function loadSprites(sheet, poses = false) {
  const image = new Image();
  image.src = sheet.url;
  await image.decode();
  return sheet.frames.map(([x, y, width, height], index) => {
    const canvas = document.createElement('canvas');
    canvas.width = canvas.height = 160;
    const poseScale = poses ? [.68, .92, .62, 1][index] : 1;
    const scale = Math.min(146 / width, 146 / height) * poseScale;
    canvas.getContext('2d').drawImage(image, x, y, width, height, (160 - width * scale) / 2, 155 - height * scale, width * scale, height * scale);
    return new Icon({ img: canvas, anchor: [.5, 1], declutterMode: 'none' });
  });
}

export default function KuafuJourney({ map, selectedId, onSelect, onBusyChange, controlContainer }) {
  const [sprites, setSprites] = useState(null);
  const [error, setError] = useState(false);
  const [paused, setPaused] = useState(false);
  const [completed, setCompleted] = useState(false);
  const [playbackRate, setPlaybackRate] = useState(1);
  const [following, setFollowing] = useState(true);
  const [hidden, setHidden] = useState(document.hidden);
  const [reduced, setReduced] = useState(() => window.matchMedia('(prefers-reduced-motion: reduce)').matches);
  const [restart, setRestart] = useState(0);
  const [reload, setReload] = useState(0);
  const [ui, setUi] = useState({ elapsed: 0, phase: phases[0], position: phases[0].path[0], frame: 0 });
  const elapsed = useRef(0);
  const playbackRateRef = useRef(1);
  const panel = useRef(null);
  const features = useRef(null);
  const lastPublished = useRef(0);
  const blocked = paused || Boolean(selectedId) || hidden;
  const cameraCenter = (position, resolution) => {
    const size = map.getSize();
    const panelTop = panel.current ? panel.current.getBoundingClientRect().top - map.getViewport().getBoundingClientRect().top : size[1];
    const anchorY = Math.min(size[1] * .55, panelTop - 10);
    return [position[0] - size[0] * resolution * .06, position[1] + (anchorY - size[1] / 2) * resolution];
  };

  useEffect(() => {
    let cancelled = false;
    setError(false);
    Promise.all([loadSprites(journey.sprites.run), loadSprites(journey.sprites.actions, true)])
      .then(([run, actions]) => { if (!cancelled) setSprites({ run, actions }); })
      .catch(() => { if (!cancelled) setError(true); });
    return () => { cancelled = true; };
  }, [reload]);

  useEffect(() => {
    const preference = window.matchMedia('(prefers-reduced-motion: reduce)');
    const visibility = () => setHidden(document.hidden);
    const changeMotion = event => setReduced(event.matches);
    document.addEventListener('visibilitychange', visibility);
    preference.addEventListener('change', changeMotion);
    return () => {
      document.removeEventListener('visibilitychange', visibility);
      preference.removeEventListener('change', changeMotion);
    };
  }, []);

  useEffect(() => {
    onBusyChange(!completed && !error && !reduced);
    return () => onBusyChange(false);
  }, [completed, error, reduced, onBusyChange]);

  useEffect(() => {
    const source = new VectorSource();
    const actor = new Feature({ geometry: new Point(phases[0].path[0]), record });
    const sun = new Feature({ geometry: new Point([835, 220]) });
    const ghost = new Feature({ geometry: new Point([1050, 580]) });
    const trail = new Feature({ geometry: new LineString([route[0], route[0]]) });
    const outline = new Feature({ geometry: new LineString(route) });
    outline.setStyle(new Style({ stroke: new Stroke({ color: '#80694c88', width: 1.5, lineDash: [4, 6] }) }));
    trail.setStyle(new Style({ stroke: new Stroke({ color: '#a44431a6', width: 2 }) }));
    const unreached = new Feature({ geometry: new LineString([[1050, 580], [1060, 690]]) });
    unreached.setStyle(new Style({ stroke: new Stroke({ color: '#6c807377', width: 1, lineDash: [2, 7] }) }));
    const nodes = journey.nodes.map(node => {
      const feature = new Feature({ geometry: new Point(node.position) });
      feature.setStyle(new Style({
        image: new CircleStyle({ radius: 4, fill: new Fill({ color: node.unreached ? '#eee2c5' : '#a44431' }), stroke: new Stroke({ color: node.unreached ? '#6c8073' : '#f4ead2', width: 1.5 }), declutterMode: 'none' }),
        text: new Text({ text: node.label, offsetX: -12, offsetY: node.id === 'chase' ? 20 : -17, textAlign: 'right', font: '11px "Noto Serif SC",serif', fill: new Fill({ color: '#66543c' }), stroke: new Stroke({ color: '#f4ead2', width: 4 }), padding: [3, 3, 3, 3] }),
      }));
      return feature;
    });
    const waters = ['河', '渭'].map((name, index) => {
      const points = Array.from({ length: 22 }, (_, i) => [1010 + i * 5, 341 - index * 19 + Math.sin(i * .55 + index) * 5]);
      const feature = new Feature({ geometry: new LineString(points) });
      feature.setStyle(new Style({ stroke: new Stroke({ color: '#647f84a0', width: 4 - index }), text: new Text({ text: name, placement: 'line', font: '10px serif', fill: new Fill({ color: '#526c72' }), stroke: new Stroke({ color: '#f4ead2', width: 3 }) }), zIndex: 2 }));
      return feature;
    });
    const marsh = new Feature({ geometry: new Polygon([Array.from({ length: 33 }, (_, i) => { const t = i / 32 * Math.PI * 2; return [1060 + Math.cos(t) * (40 + Math.sin(t * 5) * 3), 690 + Math.sin(t) * 18]; })]) });
    marsh.setStyle(new Style({ stroke: new Stroke({ color: '#69848870', width: 1.5 }), fill: new Fill({ color: '#74959a26' }), zIndex: 1 }));
    const ripples = [0, 1, 2].map(() => new Feature({ geometry: new LineString([[0, 0], [0, 0]]) }));
    ripples.forEach(feature => feature.setStyle([]));
    actor.setStyle([]); sun.setStyle([]); ghost.setStyle([]);
    source.addFeatures([marsh, ...waters, ...ripples, outline, unreached, trail, ...nodes, sun, ghost, actor]);
    const layer = new VectorLayer({ source, declutter: 'map-labels', zIndex: 35 });
    map.addLayer(layer);
    features.current = { actor, sun, ghost, trail, ripples };
    const stopFollow = () => { map.getView().cancelAnimations(); setFollowing(false); };
    map.on('pointerdrag', stopFollow);
    map.on('journey:user-view', stopFollow);
    map.getViewport().addEventListener('wheel', stopFollow, { passive: true });
    return () => {
      map.un('pointerdrag', stopFollow);
      map.un('journey:user-view', stopFollow);
      map.getViewport().removeEventListener('wheel', stopFollow);
      map.getView().cancelAnimations();
      map.removeLayer(layer);
      source.clear();
      features.current = null;
    };
  }, [map]);

  useEffect(() => {
    if (!sprites || reduced || !following) return;
    const view = map.getView();
    const size = map.getSize();
    const resolution = Math.max(view.getMinResolution(), Math.min(view.getResolution(), view.getMaxResolution() * (size[1] < 280 || size[0] < 500 ? .55 : .82)));
    view.animate({ center: cameraCenter(positionAt(phases[0], 0), resolution), resolution, duration: 600 });
  }, [sprites, restart, map, reduced]);

  useEffect(() => {
    if (selectedId || hidden) map.getView().cancelAnimations();
  }, [selectedId, hidden, map]);

  useEffect(() => {
    if (!sprites || !features.current || error) return;
    let frameId, previous;
    const paint = (time, delta = 0) => {
      const phase = phases.find(item => time < item.to_ms) || phases.at(-1);
      const ratio = Math.max(0, Math.min(1, (time - phase.from_ms) / (phase.to_ms - phase.from_ms)));
      const motionRatio = phase.action === 'tired' ? 1 - (1 - ratio) ** 2 : ratio;
      const position = positionAt(phase, motionRatio);
      const resolution = map.getView().getResolution();
      const step = Math.floor(phase.length * ratio / (resolution * 46) * sprites.run.length) % sprites.run.length;
      const actionIndex = { drink: 0, tired: 1, collapse: 2, forest: 3 }[phase.action];
      const sprite = phase.action === 'run' ? sprites.run[step] : sprites.actions[actionIndex];
      const size = Math.max(48, Math.min(78, map.getSize()[1] * .18));
      sprite.setScale(size / 160 * (phase.action === 'forest' ? .5 + .5 * ratio : 1));
      sprite.setOpacity(phase.action === 'forest' ? .4 + .6 * ratio : 1);
      const { actor, sun, ghost, trail, ripples } = features.current;
      ripples.forEach((feature, index) => {
        const pulse = (ratio * 2 + index / 3) % 1;
        const radius = (3 + pulse * 10) * resolution;
        feature.getGeometry().setCoordinates(Array.from({ length: 25 }, (_, i) => { const t = i / 24 * Math.PI * 2; return [1053 + Math.cos(t) * radius, 337 + Math.sin(t) * radius * .28]; }));
        feature.setStyle(phase.id === 'drink' ? new Style({ stroke: new Stroke({ color: `rgba(82,108,114,${(1 - pulse) * .65})`, width: 1 }), zIndex: 3 }) : []);
      });
      actor.getGeometry().setCoordinates(position);
      actor.setStyle(new Style({ image: sprite, zIndex: 50 }));
      ghost.setStyle(phase.action === 'forest' && ratio < 1 ? new Style({ image: sprites.actions[2], zIndex: 49 }) : []);
      if (phase.action === 'forest') { sprites.actions[2].setScale(size / 160); sprites.actions[2].setOpacity(1 - ratio); }
      if (phase.id === 'chase') {
        sun.getGeometry().setCoordinates([position[0] + 55, position[1] + 62]);
        sun.setStyle(new Style({ image: new CircleStyle({ radius: 10, fill: new Fill({ color: '#b66a3bb0' }), stroke: new Stroke({ color: '#704b2b', width: 1 }), declutterMode: 'none' }), zIndex: 48 }));
      } else sun.setStyle([]);
      const travelled = phases.filter(item => item.to_ms <= time && item.path.length > 1).flatMap(item => item.path);
      if (phase.length) travelled.push(...phase.path.filter((_, index) => phase.distances[index] < phase.length * motionRatio));
      travelled.push(position);
      trail.getGeometry().setCoordinates(travelled.length > 1 ? travelled : [position, position]);
      if (following && !reduced && !blocked && !map.getView().getAnimating()) {
        const view = map.getView(), center = view.getCenter();
        const desired = cameraCenter(position, resolution);
        const ease = 1 - Math.exp(-delta / 600);
        view.setCenter(center.map((value, index) => value + (desired[index] - value) * ease));
      }
      if (time - lastPublished.current > 140 || reduced || completed || time === journey.duration_ms || time === 0) {
        lastPublished.current = time;
        setUi({ elapsed: time, phase, position, screen: map.getPixelFromCoordinate(position), size, frame: phase.action === 'run' ? step : actionIndex });
      }
    };
    const refresh = () => { lastPublished.current = -Infinity; paint(elapsed.current); };
    map.on("change:size", refresh); map.on("moveend", refresh);
    const cleanup = () => { cancelAnimationFrame(frameId); map.un("change:size", refresh); map.un("moveend", refresh); };
    paint(elapsed.current);
    if (blocked || completed || reduced) return cleanup;
    const tick = timestamp => {
      const delta = previous === undefined ? 0 : Math.max(0, timestamp - previous) * playbackRateRef.current;
      previous = timestamp;
      elapsed.current = Math.min(journey.duration_ms, elapsed.current + delta);
      paint(elapsed.current, delta);
      if (elapsed.current >= journey.duration_ms) { setCompleted(true); return; }
      frameId = requestAnimationFrame(tick);
    };
    frameId = requestAnimationFrame(tick);
    return cleanup;
  }, [sprites, map, error, blocked, completed, reduced, following, restart, controlContainer]);

  const replay = () => {
    elapsed.current = 0;
    lastPublished.current = 0;
    setCompleted(false); setPaused(false); setFollowing(true); setRestart(value => value + 1);
  };
  const nextScene = () => {
    const next = phases[(phases.findIndex(phase => phase.id === ui.phase.id) + 1) % phases.length];
    elapsed.current = next.from_ms;
    setRestart(value => value + 1);
  };
  const status = error ? 'error' : !sprites ? 'loading' : reduced ? 'reduced' : completed ? 'completed' : blocked ? 'paused' : 'playing';
  const controls = <div className="kuafu-journey" ref={panel} data-screen-x={ui.screen?.[0]} data-screen-y={ui.screen?.[1]} data-size={ui.size} role="group" aria-label="夸父逐日动态" data-status={status} data-phase={ui.phase.id} data-frame={ui.frame} data-elapsed={Math.round(ui.elapsed)} data-playback-rate={playbackRate} data-x={ui.position[0].toFixed(2)} data-y={ui.position[1].toFixed(2)} data-follow={following}>
    <progress value={ui.elapsed} max={journey.duration_ms} aria-label="夸父故事进度" />
    <div className="journey-heading"><b>夸父逐日</b><span aria-live="polite">{error ? '动作图加载失败' : !sprites ? '正在载入动作图…' : `${ui.phase.title}${status === 'paused' ? ' · 已暂停' : status === 'completed' ? ' · 完' : ''}`}</span></div>
    <p>{ui.phase.quote}</p>
    <div className="journey-actions">
      {error ? <button onClick={() => setReload(value => value + 1)}>重新载入</button> : reduced ? <button onClick={nextScene} disabled={!sprites}>下一幕</button> : <button onClick={completed ? replay : () => setPaused(value => !value)} disabled={!sprites || Boolean(selectedId) || hidden} aria-label={completed ? '重播夸父逐日' : paused ? '继续夸父逐日' : '暂停夸父逐日'}>{completed ? '重播' : paused ? '继续' : '暂停'}</button>}
      {!reduced && !error && !completed && <button onClick={replay} disabled={!sprites}>重播</button>}
      {!reduced && !error && <button aria-label={`播放速度 ${playbackRate}倍`} aria-pressed={playbackRate === 2} onClick={() => setPlaybackRate(rate => { const next = rate === 1 ? 2 : 1; playbackRateRef.current = next; return next; })}>{playbackRate}×</button>}
      {!reduced && !error && <button aria-label={following ? '跟随镜头' : '恢复跟随'} title={following ? '停止镜头跟随' : '恢复镜头跟随'} aria-pressed={following} onClick={() => setFollowing(value => !value)}>跟随</button>}
      <button aria-label="原文 ↗" onClick={event => onSelect(journey.event_id, event.currentTarget)}>原文</button>
      <small title={journey.location_note}>叙事示意 · 大泽未至</small>
    </div>
  </div>;
  return controlContainer ? createPortal(controls, controlContainer) : controls;
}
