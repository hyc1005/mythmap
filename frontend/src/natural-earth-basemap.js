import GeoJSON from 'ol/format/GeoJSON';
import VectorSource from 'ol/source/Vector';
import { Fill, Stroke, Style, Text } from 'ol/style';
import { assetUrl } from './asset-url';

export const naturalEarthPath = '/data/geography/natural-earth-50m-v5.1.2.geojson';
export const naturalEarthFeatureCount = 2293;
const format = new GeoJSON();
const land = new Style({ fill: new Fill({ color: 'rgba(243,235,216,.94)' }), stroke: new Stroke({ color: '#756e59', width: .85 }) });
const lake = new Style({ fill: new Fill({ color: '#b5c2b4' }), stroke: new Stroke({ color: '#7c9690', width: .6 }) });
const majorRiver = new Style({ stroke: new Stroke({ color: '#78958d', width: 1.25 }) });
const river = new Style({ stroke: new Stroke({ color: '#78958d', width: .85 }) });
const labelStyles = new Map();
const zoomAt = resolution => Math.log2(156543.033928 / resolution);

export function naturalEarthStyle(feature, resolution) {
  if (feature.get('kind') === 'land') return land;
  if (zoomAt(resolution) < Number(feature.get('min_zoom') || 0)) return null;
  return feature.get('kind') === 'lake' ? lake : feature.get('scalerank') < 3 ? majorRiver : river;
}

export function naturalEarthLabelStyle(feature, resolution, locale) {
  if (feature.get('kind') === 'land' || zoomAt(resolution) < Number(feature.get('min_label') || 6)) return null;
  const text = locale === 'zh' ? feature.get('name_zh') || feature.get('name_en') : feature.get('name_en');
  if (!text) return null;
  const key = `${locale}:${feature.get('kind')}:${text}`;
  if (!labelStyles.has(key)) labelStyles.set(key, new Style({ text: new Text({ text, placement: feature.get('kind') === 'river' ? 'line' : 'point', font: '12px sans-serif', overflow: false,
    fill: new Fill({ color: '#53756d' }), stroke: new Stroke({ color: '#f3ebd8', width: 3 }) }) }));
  return labelStyles.get(key);
}

export function createNaturalEarthSource(signal, onLoad, onError) {
  const source = new VectorSource({ attributions: '<a href="https://www.naturalearthdata.com/" target="_blank" rel="noreferrer">Natural Earth</a>' });
  source.setLoader((extent, resolution, projection, success, failure) => {
    fetch(assetUrl(naturalEarthPath), { signal }).then(response => {
      if (!response.ok) throw new Error('Local basemap unavailable');
      return response.json();
    }).then(data => {
      if (signal.aborted) return;
      if (data.type !== 'FeatureCollection' || data.features?.length !== naturalEarthFeatureCount) throw new Error('Local basemap data mismatch');
      const features = format.readFeatures(data, { dataProjection: 'EPSG:4326', featureProjection: projection });
      if (features.length !== naturalEarthFeatureCount) throw new Error('Local basemap geometry mismatch');
      source.addFeatures(features); success(features); onLoad(features.length);
    }).catch(error => {
      failure();
      if (!signal.aborted) onError(error);
    });
  });
  return source;
}
