import Layer from 'ol/layer/Layer';
import { loadImage } from './asset-cache';

export function paperLayer(url) {
  const element = document.createElement('div');
  element.className = 'ol-layer';
  Object.assign(element.style, { position: 'absolute', inset: '0', pointerEvents: 'none' });
  const canvas = document.createElement('canvas');
  canvas.style.transformOrigin = '0 0';
  element.append(canvas);
  let image;
  const layer = new Layer({ render: state => {
    const [width, height] = state.size.map(size => Math.round(size * state.pixelRatio));
    if (canvas.width !== width || canvas.height !== height) { canvas.width = width; canvas.height = height; }
    canvas.style.transform = `matrix(${1 / state.pixelRatio}, 0, 0, ${1 / state.pixelRatio}, 0, 0)`;
    const context = canvas.getContext('2d');
    context.globalAlpha = 1;
    context.fillStyle = '#eee2c5'; context.fillRect(0, 0, width, height);
    if (image) {
      const scale = Math.max(width / image.naturalWidth, height / image.naturalHeight);
      const w = image.naturalWidth * scale, h = image.naturalHeight * scale;
      context.globalAlpha = .67; context.drawImage(image, (width - w) / 2, (height - h) / 2, w, h);
    }
    canvas.dataset.paperReady = String(Boolean(image));
    return element;
  } });
  loadImage(url).then(value => { image = value; layer.changed(); }).catch(() => { layer.set('paperError', true); });
  return layer;
}
