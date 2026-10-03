import { createPortal } from 'react-dom';
import { useEffect, useRef, useState } from 'react';
import Feature from 'ol/Feature';
import Point from 'ol/geom/Point';
import LineString from 'ol/geom/LineString';
import Polygon from 'ol/geom/Polygon';
import VectorLayer from 'ol/layer/Vector';
import VectorSource from 'ol/source/Vector';
import { Circle as CircleStyle, Fill, Icon, Stroke, Style, Text } from 'ol/style';
import animations from '../public/data/atlas/story-animations.json';
import catalog from '../public/data/atlas/catalog.json';
import { assetUrl } from './asset-url';

const smooth = value => value * value * (3 - 2 * value);
const clamp = value => Math.max(0, Math.min(1, value));
const imageStyles = new WeakMap();
function showImage(feature, image, zIndex) {
  let style = imageStyles.get(feature);
  if (!style) { style = new Style(); imageStyles.set(feature, style); }
  style.setImage(image); style.setZIndex(zIndex); feature.setStyle(style);
}

function pointAlong(route, fraction) {
  const lengths = route.slice(1).map((point, index) => Math.hypot(point[0] - route[index][0], point[1] - route[index][1]));
  let distance = clamp(fraction) * lengths.reduce((sum, length) => sum + length, 0);
  for (let index = 0; index < lengths.length; index++) {
    if (distance <= lengths[index] || index === lengths.length - 1) {
      const progress = lengths[index] ? distance / lengths[index] : 0;
      return route[index].map((value, axis) => value + (route[index + 1][axis] - value) * progress);
    }
    distance -= lengths[index];
  }
  return route[0];
}

async function spritesFor(sheet) {
  if (!sheet.sheet) {
    if (sheet.actor_art) {
      const image = new Image();
      image.src = assetUrl(sheet.actor_art.startsWith('/') ? sheet.actor_art : `/data/atlas/myth-icons/${sheet.actor_art}`);
      await image.decode();
      const canvas = document.createElement('canvas');
      canvas.width = canvas.height = 160;
      const context = canvas.getContext('2d');
      if (sheet.kind === 'journey') {
        context.fillStyle = '#e4d3ad'; context.strokeStyle = '#765238'; context.lineWidth = 5;
        context.beginPath(); context.arc(80, 80, 50, 0, Math.PI * 2); context.fill(); context.stroke();
        context.fillStyle = '#765238'; context.textAlign = 'center'; context.textBaseline = 'middle'; context.font = '54px serif'; context.fillText('王', 80, 82);
      } else {
        const scale = 146 / Math.max(image.naturalWidth, image.naturalHeight);
        context.drawImage(image, (160 - image.naturalWidth * scale) / 2, 154 - image.naturalHeight * scale, image.naturalWidth * scale, image.naturalHeight * scale);
      }
      const icon = new Icon({ img: canvas, anchor: [.5, 1], declutterMode: 'none' });
      return [[icon, icon]];
    }
    const canvas = document.createElement('canvas'); canvas.width = canvas.height = 160;
    const context = canvas.getContext('2d'); context.fillStyle = '#a44431'; context.strokeStyle = '#f0e4c9'; context.lineWidth = 6;
    context.beginPath(); context.arc(80, 80, 42, 0, Math.PI * 2); context.fill(); context.stroke();
    return [[new Icon({ img: canvas, anchor: [.5, .5], declutterMode: 'none' }), new Icon({ img: canvas, anchor: [.5, .5], declutterMode: 'none' })]];
  }
  const image = new Image();
  image.src = assetUrl(sheet.sheet.url);
  await image.decode();
  const scale = 146 / Math.max(...sheet.sheet.frames.flatMap(frame => frame.slice(2)));
  return sheet.sheet.frames.map(([x, y, width, height], index) => [false, true].map(mirrored => {
    const canvas = document.createElement('canvas');
    canvas.width = canvas.height = 160;
    const context = canvas.getContext('2d');
    if (mirrored) { context.translate(160, 0); context.scale(-1, 1); }
    const baseline = sheet.sheet.baselines?.[index] ?? height;
    context.drawImage(image, x, y, width, height, (160 - width * scale) / 2, (sheet.sheet.baselines ? 133 : 153) - baseline * scale, width * scale, height * scale);
    return new Icon({ img: canvas, anchor: [.5, 1], declutterMode: 'none' });
  }));
}

async function imageFor(url) {
  const image = new Image();
  image.src = assetUrl(url);
  await image.decode();
  return image;
}

function imageStyleFor(feature) {
  const style = feature.getStyle();
  return style instanceof Style ? style.getImage() : null;
}

async function effectAssetsFor(assets = {}) {
  const entries = await Promise.all(Object.entries(assets).map(async ([name, asset]) => {
    try {
      const image = await imageFor(asset.url);
      if (!asset.grid) {
        const icon = new Icon({ img: image, imgSize: [image.naturalWidth, image.naturalHeight], anchor: asset.anchor || [.5, 1], declutterMode: 'none' });
        return [name, { image, icon }];
      }
      const [columns, rows] = asset.grid;
      const cellWidth = image.naturalWidth / columns, cellHeight = image.naturalHeight / rows;
      const scale = 146 / Math.max(cellWidth, cellHeight);
      const frames = Array.from({ length: columns * rows }, (_, index) => {
        const canvas = document.createElement('canvas'); canvas.width = canvas.height = 160;
        const context = canvas.getContext('2d');
        const x = index % columns * cellWidth, y = Math.floor(index / columns) * cellHeight;
        context.drawImage(image, x, y, cellWidth, cellHeight, (160 - cellWidth * scale) / 2, 153 - cellHeight * scale, cellWidth * scale, cellHeight * scale);
        return new Icon({ img: canvas, anchor: asset.anchor || [.5, 1], declutterMode: 'none' });
      });
      return [name, { image, frames }];
    } catch (error) {
      if (asset.optional) return [name, null];
      throw error;
    }
  }));
  return Object.fromEntries(entries);
}

export default function StoryAnimation({ id, map, selectedId, onSelect, onBusyChange, onSkip, onSceneBoundsChange, controlContainer }) {
  const story = animations.stories.find(item => item.id === id);
  const bird = id === '03-04';
  const archer = id === '04-02';
  const [sprites, setSprites] = useState(null);
  const [effects, setEffects] = useState({});
  const [error, setError] = useState(false);
  const [reload, setReload] = useState(0);
  const [paused, setPaused] = useState(false);
  const [playbackRate, setPlaybackRate] = useState(1);
  const [following, setFollowing] = useState(story.follow_camera !== false);
  const [hidden, setHidden] = useState(document.hidden);
  const [reduced, setReduced] = useState(() => matchMedia('(prefers-reduced-motion: reduce)').matches);
  const [ui, setUi] = useState({ time: 0, phase: story.phases[0], position: story.origin, frame: 0 });
  const [restart, setRestart] = useState(0);
  const elapsed = useRef(0), features = useRef(null), panel = useRef(null), frameTransition = useRef({ frame: 0, previous: 0, changedAt: 0 });
  const playbackRateRef = useRef(1);
  const speedControl = ['01-02', '02-04', '03-04', '04-02', '05-01'].includes(id);
  const complete = ui.time >= story.duration_ms;
  const blocked = paused || Boolean(selectedId) || hidden;

  useEffect(() => {
    let cancelled = false;
    setError(false); setSprites(null); setEffects({}); elapsed.current = 0;
    frameTransition.current = { frame: 0, previous: 0, changedAt: 0 };
    setUi({ time: 0, phase: story.phases[0], position: story.origin, frame: 0 });
    Promise.all([spritesFor(story), effectAssetsFor(story.effect_assets)])
      .then(([actors, assets]) => { if (!cancelled) { setEffects(assets); setSprites(actors); } })
      .catch(() => { if (!cancelled) setError(true); });
    return () => { cancelled = true; };
  }, [story, reload]);

  useEffect(() => {
    const preference = matchMedia('(prefers-reduced-motion: reduce)');
    const visibility = () => setHidden(document.hidden);
    const motion = event => setReduced(event.matches);
    document.addEventListener('visibilitychange', visibility);
    preference.addEventListener('change', motion);
    return () => { document.removeEventListener('visibilitychange', visibility); preference.removeEventListener('change', motion); };
  }, []);

  useEffect(() => {
    onBusyChange(!complete);
    return () => onBusyChange(false);
  }, [complete, error, reduced, onBusyChange]);

  useEffect(() => {
    const eventId = story.source_event_id || id;
    const raw = catalog.events.find(item => item.id === eventId);
    const actor = new Feature({ geometry: new Point(story.origin), record: { id: eventId, kind: 'story', name: story.name, raw } });
    const actorTransition = new Feature({ geometry: new Point(story.origin) });
    const arrow = new Feature({ geometry: new LineString([[0, 0], [0, 0]]) });
    const projectile = archer ? new Feature({ geometry: new Point(story.origin) }) : null;
    const streaks = archer ? Array.from({ length: 3 }, () => new Feature({ geometry: new LineString([[0, 0], [0, 0]]) })) : [];
    const payload = new Feature({ geometry: new Point(story.destination || story.origin) });
    const decorations = Array.from({ length: bird ? 4 : story.kind === 'fire' ? 0 : 10 }, () => new Feature({ geometry: new Point(story.origin || story.waypoints?.[0]) }));
    const waypoints = story.waypoints || [story.origin, story.destination].filter(Boolean);
    if (waypoints.length > 1) arrow.getGeometry().setCoordinates(waypoints);
    const waves = Array.from({ length: 5 }, () => new Feature({ geometry: new Point(story.origin || [220, 580]) }));
    const suns = archer ? Array.from({ length: 10 }, () => new Feature({ geometry: new Point(story.origin) })) : [];
    const clouds = archer ? Array.from({ length: 2 }, () => new Feature({ geometry: new Point(story.origin) })) : [];
    const impact = archer ? new Feature({ geometry: new Point(story.origin) }) : null;
     [actor, actorTransition, arrow, projectile, ...streaks, payload, impact, ...waves, ...suns, ...clouds, ...decorations].filter(Boolean).forEach(feature => feature.setStyle([]));
    if (['migration', 'journey'].includes(story.kind) && waypoints.length > 1) arrow.setStyle(new Style({ stroke: new Stroke({ color: '#a4443180', width: 2, lineDash: [7, 6] }) }));
    const landmarks = [];
    if (bird) {
      const sea = new Feature({ geometry: new Polygon([[[880, 195], [940, 210], [980, 245], [935, 275], [885, 265], [880, 195]]]) });
      sea.setStyle(new Style({ fill: new Fill({ color: '#77979924' }), stroke: new Stroke({ color: '#69848885', width: 1.5 }), text: new Text({ text: '东海 · 示意', offsetY: 25, font: '10px serif', fill: new Fill({ color: '#526c72' }), stroke: new Stroke({ color: '#f4ead2', width: 3 }) }) }));
      const mountain = new Feature({ geometry: new LineString([[635, 215], [650, 249], [662, 230], [680, 258], [696, 215]]) });
      mountain.setStyle(new Style({ stroke: new Stroke({ color: '#746748aa', width: 2 }), text: new Text({ text: '西山木石 · 示意', offsetY: 23, font: '10px serif', fill: new Fill({ color: '#66543c' }), stroke: new Stroke({ color: '#f4ead2', width: 3 }) }) }));
      landmarks.push(sea, mountain);
    }
     const source = new VectorSource({ features: [...landmarks, clouds, suns, impact, waves, ...decorations, streaks, projectile, payload, arrow, actorTransition, actor].flat().filter(Boolean) });
    const layer = new VectorLayer({ source, zIndex: 36 });
    map.addLayer(layer);
     features.current = { actor, actorTransition, arrow, projectile, streaks, payload, waves, suns, clouds, impact, decorations, waypoints, shot: null };
    const stop = () => { map.getView().cancelAnimations(); setFollowing(false); };
    map.on('pointerdrag', stop); map.on('journey:user-view', stop);
    map.getViewport().addEventListener('wheel', stop, { passive: true });
    return () => {
      map.un('pointerdrag', stop); map.un('journey:user-view', stop);
      map.getViewport().removeEventListener('wheel', stop);
      map.getView().cancelAnimations(); map.removeLayer(layer); source.clear(); features.current = null;
      onSceneBoundsChange?.(null);
    };
  }, [id, map, story, bird]);

  const centerFor = (position, resolution) => {
    const size = map.getSize();
    const top = panel.current ? panel.current.getBoundingClientRect().top - map.getViewport().getBoundingClientRect().top : size[1];
    return [position[0] - size[0] * resolution * (bird ? .04 : -.10), position[1] + (Math.min(size[1] * .57, top - 12) - size[1] / 2) * resolution];
  };

  useEffect(() => {
    if (!sprites || reduced || !following || story.follow_camera === false) return;
    const size = map.getSize(), view = map.getView();
    const resolution = Math.max(view.getMinResolution(), Math.min(view.getResolution(), view.getMaxResolution() * (size[1] < 280 || size[0] < 500 ? .48 : .72)));
    view.animate({ resolution, center: centerFor(story.origin, resolution), duration: 600 });
  }, [sprites, restart, map, reduced]);

  useEffect(() => {
    if (!sprites || !features.current || error) return;
    if (blocked) map.getView().cancelAnimations();
    let frameId, previous, published = -Infinity;
    const paint = (time, delta = 0) => {
       const { actor, actorTransition, payload, decorations, arrow, projectile, streaks, waves, suns, clouds, impact, waypoints: sourceWaypoints } = features.current;
      let waypoints = sourceWaypoints;
      const phase = story.phases.findLast(item => item.from_ms <= time);
      const view = map.getView(), resolution = view.getResolution(), mapSize = map.getSize();
      const panelTop = panel.current ? panel.current.getBoundingClientRect().top - map.getViewport().getBoundingClientRect().top : mapSize[1];
       const size = Math.max(28, Math.min(bird ? 64 : story.kind === 'fire' ? 166 : archer || story.kind === 'creation' || story.kind === 'flood' ? 144 : 84, mapSize[1] * (bird ? .16 : archer ? .235 : story.kind === 'creation' ? .28 : story.kind === 'fire' ? .25 : story.kind === 'flood' ? .22 : .20), archer ? (mapSize[0] - 64) / 4.4 : mapSize[0] / 3, Math.max(28, (panelTop - 75) / (archer ? 1.8 : 1.4))));
      let position = [...(story.origin || waypoints[0])], frame = 0, mirrored = false, shotState = 'none';
      if (story.follow_camera === false) {
        const pixel = map.getPixelFromCoordinate(position);
        const rightMargin = archer ? size * 3.35 + 24 : story.kind === 'flood' ? Math.min((sourceWaypoints.at(-1)[0] - sourceWaypoints[0][0]) / resolution, mapSize[0] - size * 2) + size * .6 : story.kind === 'fire' ? size * 2 : size * 1.4;
        const x = Math.max(size * (story.kind === 'flood' ? 1.15 : .6) + 12, Math.min(mapSize[0] - rightMargin, pixel[0]));
        const y = Math.max(60 + size * (archer ? 1.6 : 1.25), Math.min(panelTop - 12, pixel[1]));
        position = map.getCoordinateFromPixel([x, y]);
      }
      if (story.kind === 'flood') {
        const offset = position.map((value, axis) => value - story.origin[axis]);
        const routeScale = Math.min(1, (mapSize[0] - size * 2) * resolution / (sourceWaypoints.at(-1)[0] - sourceWaypoints[0][0]));
        waypoints = sourceWaypoints.map(point => point.map((value, axis) => story.origin[axis] + (value - story.origin[axis]) * routeScale + offset[axis]));
      }
      if (bird) {
        const cycle = Math.min(time, story.duration_ms - 1) % 9000;
        const outbound = cycle >= 1500 && cycle < 4700;
        const inbound = cycle >= 5600 && cycle < 8700;
        const progress = outbound ? smooth((cycle - 1500) / 3200) : inbound ? 1 - smooth((cycle - 5600) / 3100) : cycle >= 4700 && cycle < 5600 ? 1 : 0;
        position = [story.origin[0] + (story.destination[0] - story.origin[0]) * progress, story.origin[1] + Math.sin(progress * Math.PI) * 48 + 25];
        mirrored = inbound;
        frame = [0, 1, 2, 1][Math.floor(time / 125) % 4] + (cycle >= 5000 ? 3 : 0);
        const drop = cycle >= 4800 && cycle < 5400 ? (cycle - 4800) / 600 : null;
        payload.getGeometry().setCoordinates([story.destination[0] + 12, story.destination[1] + (drop === null ? 0 : 22 * (1 - drop ** 2))]);
        payload.setStyle(drop === null ? [] : new Style({ image: new CircleStyle({ radius: 3, fill: new Fill({ color: '#6c624b' }), declutterMode: 'none' }) }));
        decorations.forEach((feature, index) => {
          feature.getGeometry().setCoordinates([story.destination[0] + (index - 1.5) * resolution * 8, story.destination[1] - resolution * (6 + index % 2 * 3)]);
          const deposits = time >= 14400 ? 4 : time >= 5400 ? 2 : 0;
          feature.setStyle(index < deposits ? new Style({ image: new CircleStyle({ radius: 2.5, fill: new Fill({ color: '#887254' }), declutterMode: 'none' }) }) : []);
        });
      } else if (archer) {
        frame = time < 2200 ? 0 : time < 4400 ? 1 : time < 5200 ? 2 : time < 6500 ? 3 : time < 8500 ? 4 : 5;
        const solarCenter = [position[0] + size * resolution * 1.9, position[1] + size * resolution * 1.15];
        const gap = size * resolution * .56;
        const [launchAt, impactAt, recoveryAt] = story.shot_timing_ms || [6500, 7600, 9200];
         if (time < impactAt) features.current.hitSunPosition = null;
         suns.forEach((feature, index) => {
          const column = index % 5, row = Math.floor(index / 5);
           const positionAt = age => [solarCenter[0] + (column - 2) * gap + Math.sin(age / 760 + index) * 4 * resolution, solarCenter[1] + (row ? -.42 : .42) * gap + Math.cos(age / 890 + index * .7) * 3 * resolution];
           if (index === 7 && time >= impactAt) {
             features.current.hitSunPosition ||= positionAt(impactAt);
             feature.getGeometry().setCoordinates(features.current.hitSunPosition);
           } else feature.getGeometry().setCoordinates(positionAt(time));
          if (effects.sun && !feature.baseSunIcon) {
            feature.baseSunIcon = new Icon({ img: effects.sun.image, imgSize: [effects.sun.image.naturalWidth, effects.sun.image.naturalHeight], scale: 40 / effects.sun.image.naturalWidth, anchor: [.5, .5], declutterMode: 'none' });
            feature.activeSunIcon = feature.baseSunIcon;
            feature.setStyle(new Style({ image: feature.baseSunIcon, zIndex: 12 }));
          }
          if (effects.sun && feature.baseSunIcon) {
            const age = time - impactAt;
             const hitFrame = index !== 7 || !effects.sunImpact?.frames || age < 0
              ? null
              : age < 120 ? 0 : age < 430 ? 1 : age < 980 ? 2 : 3;
            const nextIcon = hitFrame === null ? feature.baseSunIcon : effects.sunImpact.frames[hitFrame];
            if (feature.activeSunIcon !== nextIcon) {
              feature.activeSunIcon = nextIcon;
              feature.setStyle(new Style({ image: nextIcon, zIndex: 12 }));
            }
            const activeImage = feature.activeSunIcon;
             const heldHit = index === 7 && age >= 0;
             const hit = heldHit && age < 980;
             const impactJolt = hit ? Math.sin(age / 34) * .105 * (1 - clamp(age / 980)) : 0;
             const pulse = heldHit ? 0 : Math.sin(time / 420 + index * .82) * .035 + impactJolt;
             activeImage.setScale((40 / (hitFrame === null ? effects.sun.image.naturalWidth : 160)) * (1 + pulse));
             activeImage.setRotation(heldHit ? 0 : Math.sin(time / 1800 + index) * .018 + (hit ? Math.sin(age / 42) * .035 * (1 - clamp(age / 520)) : 0));
          }
        });
        if (effects.cloud && !imageStyleFor(clouds[0])) clouds.forEach((feature, index) => {
          const image = new Icon({ img: effects.cloud.image, imgSize: [effects.cloud.image.naturalWidth, effects.cloud.image.naturalHeight], scale: 220 / effects.cloud.image.naturalWidth, anchor: [.5, .5], opacity: .64, declutterMode: 'none' });
          feature.setStyle(new Style({ image, zIndex: 8 }));
        });
        clouds.forEach((feature, index) => {
          feature.getGeometry().setCoordinates([solarCenter[0] + Math.sin(time / 2600 + index * Math.PI) * size * resolution * .12, solarCenter[1] + (index ? -.50 : .50) * gap]);
          imageStyleFor(feature)?.setRotation(Math.sin(time / 2200 + index) * .018);
        });
        const target = suns[7].getGeometry().getCoordinates();
        const anchor = story.bow_anchor;
        shotState = time < launchAt ? 'aim' : time < impactAt ? 'flight' : time < recoveryAt ? 'impact' : 'settled';
        if (time < launchAt) features.current.shot = null;
        if (time >= launchAt && !features.current.shot) {
          const start = [position[0] + size * resolution * anchor[0], position[1] + size * resolution * anchor[1]];
          const launchCenter = [position[0] + size * resolution * 1.9, position[1] + size * resolution * 1.15];
          const column = 7 % 5, row = Math.floor(7 / 5);
          const center = [launchCenter[0] + (column - 2) * gap + Math.sin(launchAt / 760 + 7) * 4 * resolution, launchCenter[1] + (row ? -.42 : .42) * gap + Math.cos(launchAt / 890 + 7 * .7) * 3 * resolution];
          const startPixel = map.getPixelFromCoordinate(start), centerPixel = map.getPixelFromCoordinate(center);
          const length = Math.hypot(centerPixel[0] - startPixel[0], centerPixel[1] - startPixel[1]);
          const direction = [(centerPixel[0] - startPixel[0]) / length, (centerPixel[1] - startPixel[1]) / length];
          const impactPixel = [centerPixel[0] - direction[0] * 19, centerPixel[1] - direction[1] * 19];
          features.current.shot = { start, impact: map.getCoordinateFromPixel(impactPixel), direction };
        }
        const shot = features.current.shot;
        const flight = shot && time >= launchAt && time < impactAt ? clamp((time - launchAt) / (impactAt - launchAt)) : 0;
        const progress = 1 - (1 - flight) ** 3;
        const startPixel = shot ? map.getPixelFromCoordinate(shot.start) : null;
        const impactPixel = shot ? map.getPixelFromCoordinate(shot.impact) : null;
        const tipPixel = shot ? startPixel.map((value, axis) => value + (impactPixel[axis] - value) * progress) : null;
        impact.getGeometry().setCoordinates(shot?.impact || target);
        if (flight > 0 && effects.projectile?.image) {
          const icon = features.current.projectileIcon ||= new Icon({ img: effects.projectile.image, imgSize: [effects.projectile.image.naturalWidth, effects.projectile.image.naturalHeight], anchor: [.5, .5], declutterMode: 'none' });
          const arrowLength = Math.min(104, Math.max(60, size * .72));
          icon.setScale([arrowLength / effects.projectile.image.naturalWidth, arrowLength / effects.projectile.image.naturalHeight]);
          icon.setRotation(Math.atan2(impactPixel[1] - startPixel[1], impactPixel[0] - startPixel[0]));
          const centerPixel = [tipPixel[0] - shot.direction[0] * arrowLength * .46, tipPixel[1] - shot.direction[1] * arrowLength * .46];
          projectile.getGeometry().setCoordinates(map.getCoordinateFromPixel(centerPixel));
          showImage(projectile, icon, 15);
          arrow.setStyle([]);
          streaks.forEach((feature, index) => {
            const near = 18 + index * 12, far = near + 9;
            feature.getGeometry().setCoordinates([
              map.getCoordinateFromPixel([tipPixel[0] - shot.direction[0] * far, tipPixel[1] - shot.direction[1] * far]),
              map.getCoordinateFromPixel([tipPixel[0] - shot.direction[0] * near, tipPixel[1] - shot.direction[1] * near])
            ]);
            const fade = 1 - clamp((time - (impactAt - 170)) / 170);
            feature.setStyle(new Style({ stroke: new Stroke({ color: `rgba(164,68,49,${.46 * fade / (index + 1)})`, width: index === 0 ? 1.5 : 1 }), zIndex: 14 }));
          });
        } else {
          projectile?.setStyle([]);
          streaks.forEach(feature => feature.setStyle([]));
          if (flight > 0 && shot) {
            const tailPixel = [tipPixel[0] - shot.direction[0] * 25, tipPixel[1] - shot.direction[1] * 25];
            arrow.getGeometry().setCoordinates([map.getCoordinateFromPixel(tailPixel), map.getCoordinateFromPixel(tipPixel)]);
            arrow.setStyle([new Style({ stroke: new Stroke({ color: '#f0e4c9', width: 4, lineCap: 'round' }) }), new Style({ stroke: new Stroke({ color: '#754c2c', width: 1.5, lineCap: 'round' }) })]);
          } else arrow.setStyle([]);
        }
        const hitPulse = shot && time >= impactAt && time < impactAt + 820 ? clamp((time - impactAt) / 820) : 0;
        const hitPixel = shot ? map.getPixelFromCoordinate(shot.impact) : map.getPixelFromCoordinate(target);
        const rays = Array.from({ length: 7 }, (_, index) => {
          const angle = index * Math.PI * 2 / 7 + Math.atan2(shot?.direction[1] || 0, shot?.direction[0] || 1);
          return [map.getCoordinateFromPixel([hitPixel[0] + Math.cos(angle) * 10, hitPixel[1] + Math.sin(angle) * 10]), map.getCoordinateFromPixel([hitPixel[0] + Math.cos(angle) * (17 + hitPulse * 13), hitPixel[1] + Math.sin(angle) * (17 + hitPulse * 13)])];
        });
        impact.setStyle(hitPulse > 0 ? rays.map(coordinates => new Style({ geometry: new LineString(coordinates), stroke: new Stroke({ color: `rgba(164,68,49,${1 - hitPulse})`, width: 1.7 }), zIndex: 16 })) : []);
      } else if (['migration', 'journey'].includes(story.kind)) {
        const travel = Math.min(waypoints.length - 1, time / story.duration_ms * (waypoints.length - 1));
        const segment = Math.min(waypoints.length - 2, Math.floor(travel));
        const progress = smooth(travel - segment);
        position = waypoints[segment].map((value, axis) => value + (waypoints[segment + 1][axis] - value) * progress);
        frame = Math.max(0, story.phases.indexOf(phase));
        payload.getGeometry().setCoordinates(position);
        payload.setStyle(new Style({ image: new CircleStyle({ radius: 12 + Math.sin(time / 260) * 2, fill: new Fill({ color: '#c0934a50' }), stroke: new Stroke({ color: '#9b5437', width: 1.5 }), declutterMode: 'none' }) }));
      } else {
        frame = Math.max(0, story.phases.indexOf(phase));
        if (story.kind === 'fire') {
          frame = time < 3500 ? [0, 1, 0, 1][Math.floor(time / 260) % 4] : time < 4700 ? 2 : time < 6200 ? 3 : time < 8500 ? 4 : 5;
        } else if (story.kind === 'flood') {
          const channelProgress = clamp((time - 3000) / 4000);
          const routeCount = Math.min(waypoints.length - 1, Math.floor(channelProgress * (waypoints.length - 1)));
          const routeProgress = channelProgress * (waypoints.length - 1) - routeCount;
          const route = waypoints.slice(0, routeCount + 1);
          if (routeCount < waypoints.length - 1) route.push(waypoints[routeCount].map((value, axis) => value + (waypoints[routeCount + 1][axis] - value) * routeProgress));
          const activeRoute = route.length > 1 && Math.hypot(route[1][0] - route[0][0], route[1][1] - route[0][1]) > .01 ? route : [waypoints[0], pointAlong(waypoints, .003)];
          arrow.getGeometry().setCoordinates(activeRoute);
          arrow.setStyle([]);
          const retreat = 1 - clamp((time - 11000) / 3000) * .68;
          const blend = smooth(clamp((time - 3000) / 1200));
          waves.forEach((feature, index) => {
            const distance = ((time - 3000) / 6500 + index / waves.length + 2) % 1;
            const flowing = pointAlong(activeRoute, distance);
            const pool = [position[0] + (index - 2) * size * resolution * .22, position[1] + Math.sin(time / 250 + index * 1.4) * size * resolution * .07];
            const point = pool.map((value, axis) => value + (flowing[axis] - value) * blend);
            feature.getGeometry().setCoordinates(point);
            const waveFrame = (Math.floor(time / 190) + index) % 4;
            const template = effects.waveLoop?.frames?.[waveFrame];
            if (template) {
              feature.waveIcons ||= effects.waveLoop.frames.map(icon => icon.clone());
              const frameIcon = feature.waveIcons[waveFrame];
              frameIcon.setScale(size * (1.3 - blend * .55) * (.55 + retreat * .45) / 160);
              const endFade = Math.min(1, distance / .10, (1 - distance) / .12);
              frameIcon.setOpacity((1 - blend + blend * endFade) * retreat);
              showImage(feature, frameIcon, 10 + index);
            }
          });
        }
      }
      frame = Math.min(frame, sprites.length - 1);
      const icon = sprites[frame][mirrored ? 1 : 0];
      icon.setScale(size / 160);
      if (frameTransition.current.frame !== frame) frameTransition.current = { frame, previous: frameTransition.current.frame, changedAt: time };
      const previousFrame = Math.min(frameTransition.current.previous, sprites.length - 1);
      const previousIcon = sprites[previousFrame][mirrored ? 1 : 0];
      previousIcon.setScale(size / 160);
      const transition = archer && frame === 4 ? 1 : smooth(clamp((time - frameTransition.current.changedAt) / (story.kind === 'fire' && time < 3500 ? 60 : 180)));
      if (frame === previousFrame) icon.setOpacity(1);
      else { icon.setOpacity(transition); previousIcon.setOpacity(1 - transition); }
      actor.getGeometry().setCoordinates(position);
      actorTransition.getGeometry().setCoordinates(position);
      showImage(actor, icon, 22);
      if (frame === previousFrame || transition >= 1) actorTransition.setStyle([]);
      else showImage(actorTransition, previousIcon, 21);
      if (following && story.follow_camera !== false && !reduced && !blocked && !view.getAnimating()) {
        const center = view.getCenter(), desired = centerFor(position, resolution), ease = 1 - Math.exp(-delta / 450);
        view.setCenter(center.map((value, index) => value + (desired[index] - value) * ease));
      }
      if (time - published > 140 || blocked || reduced || time >= story.duration_ms) {
        published = time;
        const occupied = [actor, ...(archer ? [...suns, ...clouds, projectile] : story.kind === 'flood' ? waves : [])];
        const bounds = occupied.filter(feature => imageStyleFor(feature)).map(feature => {
          const pixel = map.getPixelFromCoordinate(feature.getGeometry().getCoordinates());
          const icon = imageStyleFor(feature), dimensions = icon.getSize(), scale = icon.getScaleArray(), anchor = icon.getAnchor();
          return [pixel[0] - anchor[0] * scale[0] - 8, pixel[1] - anchor[1] * scale[1] - 8, pixel[0] + (dimensions[0] - anchor[0]) * scale[0] + 8, pixel[1] + (dimensions[1] - anchor[1]) * scale[1] + 8];
        });
        onSceneBoundsChange?.(bounds);
         const hitSunElapsed = time - (story.shot_timing_ms?.[1] || 7600);
         const hitFrame = hitSunElapsed < 0 ? null : hitSunElapsed < 120 ? 0 : hitSunElapsed < 430 ? 1 : hitSunElapsed < 980 ? 2 : 3;
         setUi({ time, phase, position, frame, screen: map.getPixelFromCoordinate(position), size, bounds, shotState, hitSunPosition: archer ? features.current.hitSunPosition : null, hitFrame: archer ? hitFrame : null, arrow: archer && time >= (story.shot_timing_ms?.[0] || 6500) && time < (story.shot_timing_ms?.[1] || 7600) ? arrow.getGeometry().getCoordinates() : null });
      }
    };
    const refresh = () => {
      if (blocked || reduced || elapsed.current >= story.duration_ms) { published = -Infinity; paint(elapsed.current); }
    };
    map.on('moveend', refresh); map.on('change:size', refresh);
    paint(elapsed.current);
    if (blocked || reduced || elapsed.current >= story.duration_ms) return () => { map.un('moveend', refresh); map.un('change:size', refresh); };
    const tick = () => {
      const now = performance.now();
      const delta = previous === undefined ? 0 : Math.max(0, now - previous) * playbackRateRef.current;
      previous = now;
      const next = Math.min(story.duration_ms, elapsed.current + delta);
      elapsed.current = next;
      paint(elapsed.current, delta);
      if (elapsed.current < story.duration_ms) frameId = requestAnimationFrame(tick);
    };
    frameId = requestAnimationFrame(tick);
    return () => { cancelAnimationFrame(frameId); map.un('moveend', refresh); map.un('change:size', refresh); };
  }, [sprites, effects, story, bird, map, error, blocked, reduced, following, restart, controlContainer]);

  const replay = () => { elapsed.current = 0; frameTransition.current = { frame: 0, previous: 0, changedAt: 0 }; sprites?.flat().forEach(icon => icon.setOpacity(1)); setPaused(false); setFollowing(story.follow_camera !== false); setRestart(value => value + 1); };
  const skip = () => onSkip?.();
  const next = () => {
    const index = story.phases.findLastIndex(phase => phase.from_ms <= elapsed.current);
    elapsed.current = index === story.phases.length - 1 ? story.duration_ms : story.phases[index + 1].from_ms;
    setUi(value => ({ ...value, time: elapsed.current, phase: story.phases[Math.min(index + 1, story.phases.length - 1)] }));
    setRestart(value => value + 1);
  };
  const status = error ? 'error' : !sprites ? 'loading' : complete ? 'completed' : reduced ? 'reduced' : blocked ? 'paused' : 'playing';
  const controls = <div ref={panel} className="kuafu-journey story-animation" role="group" aria-label={`${story.name}动态`} data-story={id} data-status={status} data-frame={ui.frame} data-elapsed={Math.round(ui.time)} data-playback-rate={playbackRate} data-shot-state={ui.shotState || 'none'} data-hit-sun-position={JSON.stringify(ui.hitSunPosition)} data-hit-frame={ui.hitFrame} data-x={ui.position[0]} data-y={ui.position[1]} data-screen-x={ui.screen?.[0]} data-screen-y={ui.screen?.[1]} data-size={ui.size} data-follow={following} data-arrow={JSON.stringify(ui.arrow)} data-scene-bounds={JSON.stringify(ui.bounds)}>
    <progress value={ui.time} max={story.duration_ms} aria-label={`${story.name}进度`} />
    <div className="journey-heading"><b>{story.name}</b><span aria-live="polite">{error ? '动作图加载失败' : !sprites ? '正在载入动作图…' : `${ui.phase.title}${status === 'paused' ? ' · 已暂停' : complete ? ' · 完' : ''}`}</span></div>
    <p>{story.source_quote}</p>
    <div className="journey-actions">
      {error ? <button onClick={() => setReload(value => value + 1)}>重新载入</button> : reduced && !complete ? <button onClick={next} disabled={!sprites}>{ui.phase === story.phases.at(-1) ? '完成故事' : '下一幕'}</button> : <button onClick={complete ? replay : () => setPaused(value => !value)} disabled={!sprites || Boolean(selectedId) || hidden} aria-label={`${complete ? '重播' : paused ? '继续' : '暂停'}${story.name}`}>{complete ? '重播' : paused ? '继续' : '暂停'}</button>}
      {!error && !reduced && !complete && <button onClick={replay} disabled={!sprites}>重播</button>}
      {!complete && <button onClick={skip}>跳过</button>}
      {speedControl && !error && !reduced && <button aria-label={`播放速度 ${playbackRate}倍`} aria-pressed={playbackRate === 2} onClick={() => setPlaybackRate(rate => { const next = rate === 1 ? 2 : 1; playbackRateRef.current = next; return next; })}>{playbackRate}×</button>}
      {!error && !reduced && story.follow_camera !== false && <button aria-label={following ? '跟随镜头' : '恢复跟随'} aria-pressed={following} onClick={() => setFollowing(value => !value)}>跟随</button>}
      <button aria-label="原文 ↗" onClick={event => onSelect(story.source_event_id || id, event.currentTarget)}>原文</button>
      <small title={`${animations.location_note} ${story.note}`}>叙事示意</small>
    </div>
  </div>;
  return controlContainer ? createPortal(controls, controlContainer) : controls;
}
