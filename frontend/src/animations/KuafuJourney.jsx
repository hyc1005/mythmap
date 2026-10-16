import { useLocale } from '../i18n';
import { createPortal } from 'react-dom';
import { useEffect, useLayoutEffect, useRef, useState } from 'react';
import Feature from 'ol/Feature';
import Point from 'ol/geom/Point';
import LineString from 'ol/geom/LineString';
import Polygon from 'ol/geom/Polygon';
import VectorLayer from 'ol/layer/Vector';
import VectorSource from 'ol/source/Vector';
import { Circle as CircleStyle, Fill, Icon, Stroke, Style, Text } from 'ol/style';
import journey from '../../public/data/atlas/kuafu-journey.json';
import catalog from '../../public/data/atlas/catalog.json';
import { loadImage, cachedSprites } from '../asset-cache';
import { InkText, useReducedMotion } from '../motion';
import { playbackState } from '../playback';

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
  const sprites = await cachedSprites('kuafu:' + JSON.stringify([sheet, poses]), () => decodeSprites(sheet, poses));
  return sprites.map(icon => icon.clone());
}

async function decodeSprites(sheet, poses) {
  const image = await loadImage(sheet.url);
  return sheet.frames.map(([x, y, width, height], index) => {
    const canvas = document.createElement('canvas');
    canvas.width = canvas.height = 160;
    const poseScale = poses ? [.68, .92, .62, 1][index] : 1;
    const scale = Math.min(146 / width, 146 / height) * poseScale;
    canvas.getContext('2d').drawImage(image, x, y, width, height, (160 - width * scale) / 2, 155 - height * scale, width * scale, height * scale);
    return new Icon({ img: canvas, anchor: [.5, 1], declutterMode: 'none' });
  });
}

export default function KuafuJourney({ map, selectedId, onSelect, onStatusChange, onSkip, controlContainer, externalPaused = false, tourPlaying = null, onUserPlaybackChange, compactControls = false, storyView = true, closeup = false, cameraRequest = 0 }) {
  const { t, locale } = useLocale();
  const mapFont = locale === 'en' ? '"Source Sans 3 Variable", Arial, sans-serif' : '"Noto Serif SC", SimSun, serif';
  const [sprites, setSprites] = useState(null);
  const [error, setError] = useState(false);
  const [paused, setPaused] = useState(false);
  useEffect(() => { if (tourPlaying === true) setPaused(false); }, [tourPlaying]);
  const [completed, setCompleted] = useState(false);
  const [playbackRate, setPlaybackRate] = useState(1);
  const [following, setFollowing] = useState(true);
  const [hidden, setHidden] = useState(document.hidden);
  const reduced = useReducedMotion();
  const [restart, setRestart] = useState(0);
  const [reload, setReload] = useState(0);
  const [ui, setUi] = useState({ elapsed: 0, phase: phases[0], position: phases[0].path[0], frame: 0 });
  const elapsed = useRef(0);
  const playbackRateRef = useRef(1);
  const panel = useRef(null);
  const features = useRef(null);
  const lastPublished = useRef(0);
  const blocked = paused || externalPaused || Boolean(selectedId) || hidden;
  const playback = playbackState({ error, ready: sprites, complete: completed, blocked, reduced });
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
    const visibility = () => setHidden(document.hidden);
    document.addEventListener('visibilitychange', visibility);
    return () => {
      document.removeEventListener('visibilitychange', visibility);
    };
  }, []);

  useEffect(() => {
    onStatusChange(playback);
  }, [playback, onStatusChange]);

  useLayoutEffect(() => {
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
        text: new Text({ text: t(node.label), offsetX: -12, offsetY: node.id === 'chase' ? 20 : -17, textAlign: 'right', font: `12px ${mapFont}`, fill: new Fill({ color: '#66543c' }), stroke: new Stroke({ color: '#f4ead2', width: 4 }), padding: [3, 3, 3, 3] }),
      }));
      return feature;
    });
    const waters = [t("河"), t("渭")].map((name, index) => {
      const points = Array.from({ length: 22 }, (_, i) => [1010 + i * 5, 341 - index * 19 + Math.sin(i * .55 + index) * 5]);
      const feature = new Feature({ geometry: new LineString(points) });
      feature.setStyle(new Style({ stroke: new Stroke({ color: '#647f84a0', width: 4 - index }), text: new Text({ text: name, placement: 'line', font: `11px ${mapFont}`, fill: new Fill({ color: '#526c72' }), stroke: new Stroke({ color: '#f4ead2', width: 3 }) }), zIndex: 2 }));
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
  }, [map, locale]);

  useEffect(() => {
    if (!sprites || !storyView) return;
    const view = map.getView();
    const resolution = Math.max(view.getMinResolution(), view.getMaxResolution() * (closeup ? .38 : .65));
    const position = elapsed.current === 0 ? positionAt(phases[0], 0) : features.current?.actor.getGeometry().getCoordinates() || positionAt(phases[0], 0);
    setFollowing(true);
    view.animate({ center: cameraCenter(position, resolution), resolution, duration: reduced || blocked ? 0 : 320 });
  }, [sprites, restart, map, reduced, storyView, closeup, cameraRequest]);

  useEffect(() => {
    if (selectedId || hidden) map.getView().cancelAnimations();
  }, [selectedId, hidden, map]);

  useLayoutEffect(() => {
    if (!sprites || !features.current || error) return;
    let frameId, previous;
    const paint = (time, delta = 0) => {
      const mapSize = map.getSize();
      if (!mapSize || !features.current || !map.getTarget()) return;
      const phase = phases.find(item => time < item.to_ms) || phases.at(-1);
      const ratio = Math.max(0, Math.min(1, (time - phase.from_ms) / (phase.to_ms - phase.from_ms)));
      const motionRatio = phase.action === 'tired' ? 1 - (1 - ratio) ** 2 : ratio;
      const position = positionAt(phase, motionRatio);
      const resolution = map.getView().getResolution();
      const step = Math.floor(phase.length * ratio / (resolution * 46) * sprites.run.length) % sprites.run.length;
      const actionIndex = { drink: 0, tired: 1, collapse: 2, forest: 3 }[phase.action];
      const sprite = phase.action === 'run' ? sprites.run[step] : sprites.actions[actionIndex];
      const size = Math.max(48, Math.min(closeup ? 104 : 78, mapSize[0] * .28, mapSize[1] * (closeup ? .25 : .18)));
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
      if (storyView && reduced && following) {
        const view = map.getView(), desired = cameraCenter(position, resolution), center = view.getCenter();
        if (Math.hypot(center[0] - desired[0], center[1] - desired[1]) > .01) view.setCenter(desired);
      }
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
    lastPublished.current = -Infinity;
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
  }, [sprites, map, error, blocked, completed, reduced, following, restart, controlContainer, locale, closeup, storyView]);

  const replay = () => {
    onUserPlaybackChange?.(true);
    elapsed.current = 0;
    lastPublished.current = 0;
    setCompleted(false); setPaused(false); setFollowing(true); setRestart(value => value + 1);
  };
  const nextScene = () => {
    const index = phases.findIndex(phase => phase.id === ui.phase.id);
    elapsed.current = index === phases.length - 1 ? journey.duration_ms : phases[index + 1].from_ms;
    if (elapsed.current === journey.duration_ms) setCompleted(true);
    setRestart(value => value + 1);
  };
  const status = playback === 'manual' ? 'reduced' : playback;
  const replayControl = !reduced && !error && !completed && <button onClick={replay} disabled={!sprites}>{t('重播')}</button>;
  const followControl = !reduced && !error && <button aria-label={following ? t('跟随镜头') : t('恢复跟随')} title={following ? t('停止镜头跟随') : t('恢复镜头跟随')} aria-pressed={following} onClick={() => setFollowing(value => !value)}>{t('跟随')}</button>;
  const controls = <div className="kuafu-journey" ref={panel} data-screen-x={ui.screen?.[0]} data-screen-y={ui.screen?.[1]} data-size={ui.size} role="group" aria-label={t("夸父逐日动态")} data-closeup={closeup} data-status={status} data-phase={ui.phase.id} data-frame={ui.frame} data-elapsed={Math.round(ui.elapsed)} data-playback-rate={playbackRate} data-x={ui.position[0].toFixed(2)} data-y={ui.position[1].toFixed(2)} data-follow={following}>
    <progress value={ui.elapsed} max={journey.duration_ms} aria-label={t("夸父故事进度")} />
    <div className="journey-heading"><b>{t("夸父逐日")}</b><span aria-live="polite"><InkText key={ui.phase.id} variant="phase" text={error ? t("动作图加载失败") : !sprites ? t("正在载入动作图…") : `${t(ui.phase.title)}${status === 'paused' ? t(" · 已暂停") : status === 'completed' ? t(" · 完") : ''}`} /></span></div>
    <p>{t(ui.phase.quote)}</p>
    <div className="journey-actions">
      {error ? <button onClick={() => setReload(value => value + 1)}>{t("重新载入")}</button> : reduced && !completed ? <button onClick={nextScene} disabled={!sprites}>{ui.phase === phases.at(-1) ? t("完成故事") : t("下一幕")}</button> : <button onClick={completed ? replay : () => { const next = !(paused || externalPaused); setPaused(next); onUserPlaybackChange?.(!next); }} disabled={!sprites || Boolean(selectedId) || hidden} aria-label={completed ? t("重播夸父逐日") : (paused || externalPaused) ? t("继续夸父逐日") : t("暂停夸父逐日")}>{completed ? t("重播") : (paused || externalPaused) ? t("继续") : t("暂停")}</button>}
      {!completed && <button onClick={onSkip}>{t('跳过')}</button>}
      {!compactControls && replayControl}
      {!reduced && !error && <button aria-label={t(`播放速度 ${playbackRate}倍`)} aria-pressed={playbackRate === 2} onClick={() => setPlaybackRate(rate => { const next = rate === 1 ? 2 : 1; playbackRateRef.current = next; return next; })}>{playbackRate}×</button>}
      {!compactControls && followControl}
      <button aria-label={t("原文 ↗")} onClick={event => onSelect(journey.event_id, event.currentTarget)}>{t("原文")}</button>
      {compactControls && (replayControl || followControl) && <details className="journey-more"><summary>{t('更多')}</summary><div>{replayControl}{followControl}</div></details>}
      <small title={t(journey.location_note)}>{t("叙事示意 · 大泽未至")}</small>
    </div>
  </div>;
  return controlContainer ? createPortal(controls, controlContainer) : controls;
}
