"""Read-only atlas endpoints, available even when the legacy PostGIS service is offline."""
import json
from pathlib import Path

from fastapi import APIRouter, HTTPException

router = APIRouter(prefix='/api/atlas', tags=['seven-stage-atlas'])
DATA = Path(__file__).resolve().parents[2] / 'frontend/public/data'


def catalog():
    file = DATA / 'atlas/catalog.json'
    if not file.exists():
        raise HTTPException(503, 'atlas data has not been built')
    return json.loads(file.read_text(encoding='utf-8'))


def validate_revision(data, revision_id):
    if revision_id and revision_id != data['revision_id']:
        raise HTTPException(409, 'atlas revision is unavailable; refresh the catalog')


def chapter(data, stage_id):
    item = next((stage for stage in data['stages'] if stage['id'] == stage_id), None)
    if item is None:
        raise HTTPException(404, 'stage must be 01 through 07')
    return item


@router.get('')
def get_catalog(revision_id: str | None = None):
    data = catalog()
    validate_revision(data, revision_id)
    return data


@router.get('/stages')
def get_stages():
    data = catalog()
    return {'revision_id': data['revision_id'], 'items': data['stages'], 'total': 7}


@router.get('/stages/{stage_id}/layers/{layer}')
def get_layer(stage_id: str, layer: str, cumulative: bool = False, revision_id: str | None = None):
    data = catalog()
    validate_revision(data, revision_id)
    chapter(data, stage_id)
    if layer not in ('events', 'candidates', 'routes', 'activities'):
        raise HTTPException(404, 'unknown atlas layer')
    available = data.get(layer, [])
    features = [f for f in available if f['properties']['stage_id'] and
                (f['properties']['stage_id'] <= stage_id if cumulative else f['properties']['stage_id'] == stage_id)]
    return {'type': 'FeatureCollection', 'revision_id': data['revision_id'], 'features': features,
            'note': 'No evidence-supported activity polygons are available.' if layer == 'activities' else ''}


@router.get('/entities/{entity_id}')
def get_entity(entity_id: str, revision_id: str | None = None):
    data = catalog()
    validate_revision(data, revision_id)
    event = next((e for e in data['events'] if e['id'] == entity_id), None)
    if event is None:
        raise HTTPException(404, 'atlas entity not found')
    return {'revision_id': data['revision_id'], 'event': event,
            'candidates': [c for c in data['candidates'] if c['properties']['entity_id'] == entity_id],
            'sources': [s for s in data['sources'] if s['id'] in event['properties']['source_ids']]}


@router.get('/divine-space')
def get_divine_space():
    return {**json.loads((DATA / 'divine-space.json').read_text(encoding='utf-8')), 'revision_id': catalog()['revision_id']}
