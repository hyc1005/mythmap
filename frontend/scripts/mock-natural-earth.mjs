export async function mockNaturalEarth(context) {
  const network = { requests: 0, fail: false, malformed: false, hold: null, externalRequests: [] };
  context.on('request', request => {
    if (/tianditu\.gov\.cn|openstreetmap\.org/.test(request.url())) network.externalRequests.push(request.url());
  });
  await context.route('**/data/geography/natural-earth-50m-v5.1.2.geojson*', async route => {
    network.requests++;
    if (network.hold) await network.hold;
    if (network.fail) return route.abort();
    if (network.malformed) return route.fulfill({ status: 200, contentType: 'application/json', body: '{"type":"FeatureCollection","features":[]}' });
    try { await route.continue(); } catch (error) { if (!/closed|cancel|abort/i.test(error.message)) throw error; }
  });
  return network;
}
