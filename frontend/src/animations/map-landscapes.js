import Feature from 'ol/Feature';
import Point from 'ol/geom/Point';
import { Fill, Icon, Stroke, Style, Text } from 'ol/style';
import { loadImage } from '../asset-cache';

const DEFAULT_OPACITY = .9;

export async function loadLandscapes(definitions = []) {
  const loaded = await Promise.all(definitions.map(async definition => {
    if (!definition?.image) return null;
    try {
      const image = await loadImage(definition.image);
      if (!image.naturalWidth || !image.naturalHeight) return null;
      return { ...definition, image };
    } catch {
      return null;
    }
  }));
  return loaded.filter(Boolean);
}

export function createLandscapeFeature(asset, { font } = {}) {
  const icon = new Icon({
    img: asset.image,
    imgSize: [asset.image.naturalWidth, asset.image.naturalHeight],
    anchor: asset.anchor || [.5, .5],
    opacity: asset.opacity ?? DEFAULT_OPACITY,
    declutterMode: 'none',
  });
  const styles = [new Style({ image: icon, zIndex: asset.zIndex ?? 2 })];
  if (asset.label) {
    styles.push(new Style({
      text: new Text({
        text: asset.label,
        offsetX: asset.label_offset?.[0] ?? 0,
        offsetY: asset.label_offset?.[1] ?? 18,
        font,
        padding: [2, 5, 2, 5],
        fill: new Fill({ color: '#66543c' }),
        stroke: new Stroke({ color: '#f4ead2', width: 3 }),
      }),
      zIndex: (asset.zIndex ?? 2) + 2,
    }));
  }
  const feature = new Feature({ geometry: new Point(asset.position || [0, 0]) });
  feature.setStyle(styles);
  return { feature, icon, asset };
}

export function sizeLandscape(icon, width) {
  const naturalWidth = icon.getImageSize()[0];
  if (!naturalWidth || !width) return;
  const scale = width / naturalWidth;
  if (Math.abs(icon.getScale() - scale) > .0005) icon.setScale(scale);
}
