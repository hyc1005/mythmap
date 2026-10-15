import assert from 'node:assert/strict';
import { access, readFile } from 'node:fs/promises';
import { readExploration, explorationUrl } from '../src/exploration.js';
import { validateWorld } from '../src/world-validation.js';
import { playbackState } from '../src/playback.js';

const read = async path => JSON.parse(await readFile(new URL(path, import.meta.url), 'utf8'));
const world = await read('../public/data/myth-world.json');
const catalog = await read('../public/data/atlas/catalog.json');
const animations = await read('../public/data/atlas/story-animations.json');
const journey = await read('../public/data/atlas/kuafu-journey.json');
const optimized = await read('../src/optimized-assets.json');
const previews = await read('../src/preview-assets.json');
validateWorld(world, world);
for (const mutate of [data => data.domains[0].place_id = 'missing', data => data.places[0].x = NaN,
  data => data.stages[1].extent = [20, 0, 10, 50], data => data.beasts[0].name = '', data => data.revision = 'incompatible']) {
  const invalid = structuredClone(world); mutate(invalid);
  assert.throws(() => validateWorld(invalid, world), /Invalid world/);
}
assert.equal(playbackState({ error: true, ready: true }), 'error');
assert.equal(playbackState({ ready: true, reduced: true }), 'manual');
assert.equal(playbackState({ ready: true, complete: true, reduced: true }), 'completed');
assert.equal(playbackState({ ready: true, blocked: true }), 'paused');

function unique(items, name) {
  const ids = items.map(item => item.id).filter(Boolean);
  assert.equal(new Set(ids).size, ids.length, `${name}: duplicate ID`);
}
for (const [name, items] of Object.entries(world)) if (Array.isArray(items)) unique(items, name);
for (const [name, items] of Object.entries(catalog)) if (Array.isArray(items)) unique(items, name);
unique(animations.stories, 'animations');
const stages = new Set(world.stages.map(stage => stage.id));
const events = new Set(catalog.events.map(event => event.id));
const places = new Set(world.places.map(place => place.id));
const people = new Set(catalog.people.map(person => person.id));
const sources = new Set(catalog.sources.map(source => source.id));
for (const stage of catalog.stages) for (const id of stage.event_ids) {
  assert.ok(events.has(id), `${stage.id}: unknown event ${id}`);
  assert.equal(catalog.events.find(event => event.id === id).properties.stage_id, stage.id);
}
for (const event of catalog.events) {
  const props = event.properties;
  if (props.map_visible) assert.ok(Array.isArray(props.layout_hint) && props.layout_hint.length === 2
    && props.layout_hint.every((n, i) => Number.isFinite(n) && n >= 0 && n <= [1200, 800][i]), `${event.id}: layout coordinates`);
  assert.ok(props.stage_id === null || stages.has(props.stage_id), `${event.id}: invalid chapter`);
  assert.equal(props.id, event.id);
  for (const id of props.person_ids || []) assert.ok(people.has(id), `${event.id}: unknown person ${id}`);
  for (const id of props.source_ids || []) assert.ok(sources.has(id), `${event.id}: unknown source ${id}`);
  if (props.parent_event_id) assert.ok(events.has(props.parent_event_id), `${event.id}: invalid parent`);
}
for (const item of [...world.beasts, ...world.places, ...world.domains]) {
  assert.ok(stages.has(item.reveal_chapter), `${item.id}: invalid reveal chapter`);
  if (item.place_id) assert.ok(places.has(item.place_id), `${item.id}: unknown place`);
}
for (const relation of world.relations) assert.ok(places.has(relation.from) && places.has(relation.to), 'Unknown relation endpoint');
for (const story of [...animations.stories, journey]) {
  assert.ok(stages.has(story.stage_id), `${story.id}: invalid chapter`);
  assert.ok(events.has(story.source_event_id || story.event_id || story.id), `${story.id}: unknown event`);
  assert.ok(Number.isFinite(story.duration_ms) && story.duration_ms > 0);
  assert.equal(story.phases[0].from_ms, 0, `${story.id}: initial phase starts at zero`);
  story.phases.forEach((phase, index) => {
    assert.ok(phase.from_ms >= 0 && phase.from_ms < story.duration_ms, `${story.id}: phase outside duration`);
    if (index) assert.ok(phase.from_ms > story.phases[index - 1].from_ms, `${story.id}: phases must be ordered`);
    if (phase.to_ms !== undefined) {
      assert.ok(phase.to_ms > phase.from_ms && phase.to_ms <= story.duration_ms);
      if (index) assert.equal(phase.from_ms, story.phases[index - 1].to_ms, 'Phase intervals must be contiguous');
    }
  });
}

const assets = new Set();
function collect(value, key = '') {
  if (typeof value === 'string') {
    if (value.startsWith('/data/')) assets.add(value);
    else if (['artwork', 'artworks', 'actor_art'].includes(key) && /\.(webp|png|svg|jpg)$/.test(value)) assets.add(`/data/atlas/myth-icons/${value}`);
  } else if (Array.isArray(value)) value.forEach(item => collect(item, key));
  else if (value && typeof value === 'object') Object.entries(value).forEach(([name, item]) => collect(item, name));
}
[world, catalog, animations, journey].forEach(data => collect(data));
for (const path of assets) await access(new URL(`../public${path}`, import.meta.url));
for (const [original, item] of Object.entries(optimized)) {
  await access(new URL(`../public${item.path}`, import.meta.url));
  if (original !== 'bookplate') await access(new URL(`../public${original}`, import.meta.url));
  assert.ok(item.optimized_bytes < item.original_bytes, `${original}: optimized asset must be smaller`);
}
for (const [original, variants] of Object.entries(previews)) {
  await access(new URL(`../public${original}`, import.meta.url));
  for (const [variant, item] of Object.entries(variants)) {
    await access(new URL(`../public${item.path}`, import.meta.url));
    assert.ok(Math.max(...item.dimensions) <= (variant === 'card' ? 320 : 480));
  }
}
const before = Object.values(optimized).reduce((sum, item) => sum + item.original_bytes, 0);
const after = Object.values(optimized).reduce((sum, item) => sum + item.optimized_bytes, 0);
assert.ok(after <= before * .7, 'Publishing images reduce total bytes by at least 30%');
assert.deepEqual(readExploration('?chapter=invalid&item=03-05', world, catalog), { stageIndex: 0, item: null, shared: true });
assert.equal(readExploration('?chapter=03&item=invalid', world, catalog).item, null);
assert.equal(readExploration('?item=03-05', world, catalog).stageIndex, 3);
assert.equal(readExploration('?chapter=01&item=03-05', world, catalog).item, null);
assert.equal(readExploration('?chapter=03&item=03-05', world, catalog).item, '03-05');
assert.equal(readExploration('?item=08-01', world, catalog).item, null, 'Unassigned archive records do not become public links');
const url = explorationUrl('https://example.com/mythmap/?lang=en', '03', '03-05', 'zh');
assert.equal(url.pathname, '/mythmap/');
assert.equal(url.searchParams.get('item'), '03-05');
assert.equal(explorationUrl(url, '04', null, 'en').searchParams.has('item'), false);
console.log(`PASS: IDs, chapter/source/place references, ${assets.size} assets, phase ordering and share parameters; publishing images ${(100 * (1 - after / before)).toFixed(1)}% smaller.`);
