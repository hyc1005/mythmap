import { fromLonLat, transformExtent } from 'ol/proj.js';

export const geographyMapConfig = {
  provider: 'tianditu',
  initialCenter: [110.5, 34.5],
  initialZoom: 5,
  nationalCenter: [108.94, 34.34],
  nationalExtent: [73, 3, 136, 54],
  maxZoom: 14,
};

export function nationalView(size) {
  const center = fromLonLat(geographyMapConfig.nationalCenter);
  const bounds = transformExtent(geographyMapConfig.nationalExtent, 'EPSG:4326', 'EPSG:3857');
  return { center, resolution: Math.max(
    2 * Math.max(center[0] - bounds[0], bounds[2] - center[0]) / Math.max(1, size[0] - 48),
    2 * Math.max(center[1] - bounds[1], bounds[3] - center[1]) / Math.max(1, size[1] - 48),
  ) };
}
