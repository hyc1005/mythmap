from datetime import date, datetime
import json
from typing import Any

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from sqlalchemy.orm import Session

from .config import settings
from .db import get_db
from .filters import CONFIDENCES, THEMES, validate_confidence, validate_theme
from .atlas import router as atlas_router

app = FastAPI(title="山海寻踪 API", version="1.0.0")
app.include_router(atlas_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_origin_regex=r"http://(localhost|127\.0\.0\.1):517[3-9]",
    allow_credentials=False,
    allow_methods=["GET"],
    allow_headers=["*"],
)

EPS_M = 250_000
MIN_POINTS = 3
PROJECTION = "+proj=aeqd +lat_0=35 +lon_0=105 +datum=WGS84 +units=m +no_defs +type=crs"
PROJECTION_LABEL = "local azimuthal equidistant centered at 105E,35N"


def rows(db: Session, sql: str, params: dict[str, Any] | None = None) -> list[dict[str, Any]]:
    return [dict(row) for row in db.execute(text(sql), params or {}).mappings().all()]


def row(db: Session, sql: str, params: dict[str, Any] | None = None) -> dict[str, Any] | None:
    result = db.execute(text(sql), params or {}).mappings().first()
    return dict(result) if result is not None else None


def clean(value: Any) -> Any:
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    if isinstance(value, dict):
        return {key: clean(item) for key, item in value.items()}
    if isinstance(value, list):
        return [clean(item) for item in value]
    return value


def source_records(db: Session, link_table: str, entity_column: str, entity_id: str) -> list[dict[str, Any]]:
    allowed = {"story_sources": "story_id", "person_sources": "person_id", "place_sources": "place_id", "candidate_sources": "candidate_id"}
    if allowed.get(link_table) != entity_column:
        raise ValueError("unsupported source relation")
    return rows(db, f"""
        SELECT s.id, s.title, s.creator, s.url, s.citation, s.accessed_on
        FROM sources s JOIN {link_table} link ON link.source_id = s.id
        WHERE link.{entity_column} = :entity_id ORDER BY s.title, s.id
    """, {"entity_id": entity_id})


def story_list_filters(q: str | None, theme: str | None, person_id: str | None,
                      place_id: str | None, confidence: str | None) -> tuple[str, dict[str, Any]]:
    theme = validate_theme(theme)
    confidence = validate_confidence(confidence)
    clauses: list[str] = []
    params: dict[str, Any] = {}
    if q and q.strip():
        clauses.append("(s.title ILIKE :q OR s.summary ILIKE :q OR s.chapter ILIKE :q OR s.quote ILIKE :q)")
        params["q"] = f"%{q.strip()}%"
    if theme:
        clauses.append("s.theme = :theme")
        params["theme"] = theme
    if person_id:
        clauses.append("EXISTS (SELECT 1 FROM story_people sx WHERE sx.story_id=s.id AND sx.person_id=:person_id)")
        params["person_id"] = person_id
    if place_id or confidence:
        place_conditions = ["sx.story_id=s.id"]
        if place_id:
            place_conditions.append("sx.place_id=:place_id")
            params["place_id"] = place_id
        if confidence:
            place_conditions.append("px.confidence=:confidence")
            params["confidence"] = confidence
        clauses.append("EXISTS (SELECT 1 FROM story_places sx JOIN places px ON px.id=sx.place_id WHERE " + " AND ".join(place_conditions) + ")")
    return (" WHERE " + " AND ".join(clauses) if clauses else ""), params


def place_scope(alias: str, q: str | None, theme: str | None, story_id: str | None,
                person_id: str | None, place_id: str | None = None,
                include_candidate_text: bool = False) -> tuple[list[str], dict[str, Any]]:
    theme = validate_theme(theme)
    params: dict[str, Any] = {}
    scope_parts: list[str] = []
    if theme:
        scope_parts.append("fs.theme=:theme")
        params["theme"] = theme
    if story_id:
        scope_parts.append("sp.story_id=:story_id")
        params["story_id"] = story_id
    if person_id:
        scope_parts.append("EXISTS (SELECT 1 FROM story_people spp WHERE spp.story_id=sp.story_id AND spp.person_id=:person_id)")
        params["person_id"] = person_id

    clauses: list[str] = []
    if place_id:
        clauses.append(f"{alias}.id=:place_id")
        params["place_id"] = place_id
    if scope_parts:
        clauses.append(
            "EXISTS (SELECT 1 FROM story_places sp JOIN stories fs ON fs.id=sp.story_id WHERE sp.place_id="
            + alias + ".id AND " + " AND ".join(scope_parts) + ")"
        )
    if q and q.strip():
        params["q"] = f"%{q.strip()}%"
        alternatives = [f"{alias}.name ILIKE :q", f"{alias}.modern_name ILIKE :q"]
        if include_candidate_text:
            alternatives.append(
                "EXISTS (SELECT 1 FROM place_candidates qc WHERE qc.place_id=" + alias
                + ".id AND (qc.label ILIKE :q OR qc.reason ILIKE :q))"
            )
        story_conditions = [
            "qsp.place_id=" + alias + ".id",
            "(qs.title ILIKE :q OR qs.summary ILIKE :q OR qs.chapter ILIKE :q OR qs.quote ILIKE :q)",
        ]
        if theme:
            story_conditions.append("qs.theme=:theme")
        if story_id:
            story_conditions.append("qsp.story_id=:story_id")
        if person_id:
            story_conditions.append("EXISTS (SELECT 1 FROM story_people qpp WHERE qpp.story_id=qsp.story_id AND qpp.person_id=:person_id)")
        alternatives.append(
            "EXISTS (SELECT 1 FROM story_places qsp JOIN stories qs ON qs.id=qsp.story_id WHERE "
            + " AND ".join(story_conditions) + ")"
        )
        clauses.append("(" + " OR ".join(alternatives) + ")")
    return clauses, params


def story_text_expression(place_alias: str, theme: str | None, story_id: str | None,
                         person_id: str | None) -> str:
    conditions = [
        f"qsp.place_id={place_alias}.id",
        "(qs.title ILIKE :q OR qs.summary ILIKE :q OR qs.chapter ILIKE :q OR qs.quote ILIKE :q)",
    ]
    if theme:
        conditions.append("qs.theme=:theme")
    if story_id:
        conditions.append("qsp.story_id=:story_id")
    if person_id:
        conditions.append("EXISTS (SELECT 1 FROM story_people qpp WHERE qpp.story_id=qsp.story_id AND qpp.person_id=:person_id)")
    return "EXISTS (SELECT 1 FROM story_places qsp JOIN stories qs ON qs.id=qsp.story_id WHERE " + " AND ".join(conditions) + ")"


@app.get("/api/stories")
def list_stories(q: str | None = None, theme: str | None = None, person_id: str | None = None,
                 place_id: str | None = None, confidence: str | None = None,
                 db: Session = Depends(get_db)) -> dict[str, Any]:
    where, params = story_list_filters(q, theme, person_id, place_id, confidence)
    items = rows(db, f"""
        SELECT s.id, s.title, s.theme, s.summary, s.chapter, s.quote,
          ARRAY(SELECT ss.source_id FROM story_sources ss WHERE ss.story_id=s.id ORDER BY ss.source_id) AS source_ids,
          ARRAY(SELECT sx.person_id FROM story_people sx JOIN people p ON p.id=sx.person_id
                WHERE sx.story_id=s.id ORDER BY p.name, p.id) AS person_ids,
          ARRAY(SELECT sx.place_id FROM story_places sx JOIN places p ON p.id=sx.place_id
                WHERE sx.story_id=s.id ORDER BY p.name, p.id) AS place_ids,
          COALESCE((SELECT json_agg(json_build_object(
              'id',p.id,'name',p.name,'description',p.description,
              'source_ids',ARRAY(SELECT ps.source_id FROM person_sources ps WHERE ps.person_id=p.id ORDER BY ps.source_id)
            ) ORDER BY p.name,p.id) FROM story_people sx JOIN people p ON p.id=sx.person_id
            WHERE sx.story_id=s.id),'[]'::json) AS people
        FROM stories s {where} ORDER BY s.title, s.id
    """, params)
    return {"items": clean(items), "total": len(items)}


@app.get("/api/stories/{story_id}")
def get_story(story_id: str, db: Session = Depends(get_db)) -> dict[str, Any]:
    item = row(db, """
        SELECT s.id, s.title, s.theme, s.summary, s.chapter, s.quote,
          ARRAY(SELECT source_id FROM story_sources WHERE story_id=s.id ORDER BY source_id) AS source_ids,
          ARRAY(SELECT person_id FROM story_people WHERE story_id=s.id ORDER BY person_id) AS person_ids,
          ARRAY(SELECT place_id FROM story_places WHERE story_id=s.id ORDER BY place_id) AS place_ids
        FROM stories s WHERE s.id=:id
    """, {"id": story_id})
    if item is None:
        raise HTTPException(404, "story not found")
    item["people"] = rows(db, """
        SELECT p.id, p.name, p.description,
          ARRAY(SELECT ps.source_id FROM person_sources ps WHERE ps.person_id=p.id ORDER BY ps.source_id) AS source_ids
        FROM people p JOIN story_people sp ON sp.person_id=p.id WHERE sp.story_id=:id ORDER BY p.name, p.id
    """, {"id": story_id})
    item["places"] = rows(db, """
        SELECT p.id, p.name, p.modern_name, p.description, p.confidence,
          ARRAY(SELECT c.id FROM place_candidates c WHERE c.place_id=p.id ORDER BY c.label, c.id) AS candidate_ids,
          ARRAY(SELECT sp.story_id FROM story_places sp WHERE sp.place_id=p.id ORDER BY sp.story_id) AS story_ids,
          ARRAY(SELECT ps.source_id FROM place_sources ps WHERE ps.place_id=p.id ORDER BY ps.source_id) AS source_ids
        FROM places p JOIN story_places sp ON sp.place_id=p.id WHERE sp.story_id=:id ORDER BY p.name, p.id
    """, {"id": story_id})
    item["sources"] = source_records(db, "story_sources", "story_id", story_id)
    return clean(item)


def place_list_filters(q: str | None, theme: str | None, story_id: str | None, person_id: str | None,
                       confidence: str | None, include_unlocated: bool) -> tuple[str, dict[str, Any]]:
    theme = validate_theme(theme)
    confidence = validate_confidence(confidence)
    clauses: list[str] = []
    params: dict[str, Any] = {}
    if confidence:
        clauses.append("p.confidence = :confidence")
        params["confidence"] = confidence
    if not include_unlocated:
        clauses.append("p.confidence <> 'unlocated' AND EXISTS (SELECT 1 FROM place_candidates uc WHERE uc.place_id=p.id AND uc.geometry IS NOT NULL AND uc.display_mode<>'none')")
    scope, scope_params = place_scope("p", q, theme, story_id, person_id)
    clauses.extend(scope)
    params.update(scope_params)
    return (" WHERE " + " AND ".join(clauses) if clauses else ""), params


def place_rows(db: Session, where: str, params: dict[str, Any]) -> list[dict[str, Any]]:
    return rows(db, f"""
        SELECT p.id, p.name, p.modern_name, p.description, p.confidence,
          ARRAY(SELECT c.id FROM place_candidates c WHERE c.place_id=p.id ORDER BY c.label, c.id) AS candidate_ids,
          ARRAY(SELECT sp.story_id FROM story_places sp JOIN stories s ON s.id=sp.story_id
                WHERE sp.place_id=p.id ORDER BY s.title, s.id) AS story_ids,
          ARRAY(SELECT ps.source_id FROM place_sources ps WHERE ps.place_id=p.id ORDER BY ps.source_id) AS source_ids
        FROM places p {where} ORDER BY p.name, p.id
    """, params)


@app.get("/api/places")
def list_places(q: str | None = None, theme: str | None = None, story_id: str | None = None, person_id: str | None = None,
                confidence: str | None = None, include_unlocated: bool = True,
                db: Session = Depends(get_db)) -> dict[str, Any]:
    where, params = place_list_filters(q, theme, story_id, person_id, confidence, include_unlocated)
    items = place_rows(db, where, params)
    return {"items": clean(items), "total": len(items)}


@app.get("/api/places/{place_id}")
def get_place(place_id: str, db: Session = Depends(get_db)) -> dict[str, Any]:
    item = row(db, """
        SELECT p.id, p.name, p.modern_name, p.description, p.confidence,
          ARRAY(SELECT c.id FROM place_candidates c WHERE c.place_id=p.id ORDER BY c.label,c.id) AS candidate_ids,
          ARRAY(SELECT sp.story_id FROM story_places sp WHERE sp.place_id=p.id ORDER BY sp.story_id) AS story_ids,
          ARRAY(SELECT ps.source_id FROM place_sources ps WHERE ps.place_id=p.id ORDER BY ps.source_id) AS source_ids
        FROM places p WHERE p.id=:id
    """, {"id": place_id})
    if item is None:
        raise HTTPException(404, "place not found")
    candidates = rows(db, """
        SELECT c.id, c.place_id, c.label,
          CASE WHEN c.geometry IS NULL THEN NULL ELSE ST_AsGeoJSON(c.geometry)::json END AS geometry,
          c.display_mode, c.confidence, c.is_primary, c.reason,
          ARRAY(SELECT cs.source_id FROM candidate_sources cs WHERE cs.candidate_id=c.id ORDER BY cs.source_id) AS source_ids
        FROM place_candidates c WHERE c.place_id=:id ORDER BY c.is_primary DESC, c.label, c.id
    """, {"id": place_id})
    item["candidates"] = candidates
    item["stories"] = rows(db, """
        SELECT s.id, s.title, s.theme, s.summary, s.chapter, s.quote,
          ARRAY(SELECT ss.source_id FROM story_sources ss WHERE ss.story_id=s.id ORDER BY ss.source_id) AS source_ids,
          ARRAY(SELECT spp.person_id FROM story_people spp WHERE spp.story_id=s.id ORDER BY spp.person_id) AS person_ids,
          ARRAY(SELECT spl.place_id FROM story_places spl JOIN places pl ON pl.id=spl.place_id
                WHERE spl.story_id=s.id ORDER BY pl.name,pl.id) AS place_ids,
          sp.relation_type, sp.quote AS relation_quote, sp.sequence
        FROM stories s JOIN story_places sp ON sp.story_id=s.id WHERE sp.place_id=:id
        ORDER BY s.title, s.id, sp.sequence
    """, {"id": place_id})
    item["sources"] = source_records(db, "place_sources", "place_id", place_id)
    return clean(item)


def parse_bbox(bbox: str | None) -> tuple[float, float, float, float] | None:
    if bbox is None or not bbox.strip():
        return None
    try:
        values = tuple(float(value) for value in bbox.split(","))
    except ValueError as exc:
        raise HTTPException(422, "bbox must be min_lon,min_lat,max_lon,max_lat") from exc
    if len(values) != 4:
        raise HTTPException(422, "bbox must be min_lon,min_lat,max_lon,max_lat")
    minx, miny, maxx, maxy = values
    if not (-180 <= minx < maxx <= 180 and -90 <= miny < maxy <= 90):
        raise HTTPException(422, "bbox must be a valid EPSG:4326 extent")
    return values  # type: ignore[return-value]


def spatial_filters(theme: str | None, story_id: str | None, person_id: str | None,
                    place_id: str | None, confidence: str | None, q: str | None,
                    include_candidate_text: bool) -> tuple[list[str], dict[str, Any]]:
    theme = validate_theme(theme)
    confidence = validate_confidence(confidence)
    clauses = ["c.geometry IS NOT NULL", "c.display_mode <> 'none'"]
    scoped, params = place_scope("p", q, theme, story_id, person_id, place_id, include_candidate_text)
    clauses.extend(scoped)
    if confidence:
        clauses.append("p.confidence=:confidence")
        params["confidence"] = confidence
    return clauses, params


@app.get("/api/map/features")
def map_features(q: str | None = None, bbox: str | None = None, theme: str | None = None,
                 story_id: str | None = None, person_id: str | None = None, place_id: str | None = None,
                 confidence: str | None = None, db: Session = Depends(get_db)) -> dict[str, Any]:
    extent = parse_bbox(bbox)
    clauses, params = spatial_filters(theme, story_id, person_id, place_id, confidence, None, False)
    if q and q.strip():
        params["q"] = f"%{q.strip()}%"
        story_match = story_text_expression("p", theme, story_id, person_id)
        clauses.append("(p.name ILIKE :q OR p.modern_name ILIKE :q OR c.label ILIKE :q OR c.reason ILIKE :q OR " + story_match + ")")
    if extent:
        clauses.append("ST_Intersects(c.geometry, ST_MakeEnvelope(:minx,:miny,:maxx,:maxy,4326))")
        params.update(dict(zip(("minx", "miny", "maxx", "maxy"), extent)))
    features = rows(db, f"""
        SELECT c.id AS candidate_id, p.id AS place_id, p.name AS place_name,
          p.confidence, c.display_mode, c.is_primary,
          ARRAY(SELECT sp.story_id FROM story_places sp JOIN stories s ON s.id=sp.story_id
                WHERE sp.place_id=p.id ORDER BY s.title,s.id) AS story_ids,
          ST_AsGeoJSON(c.geometry) AS geometry
        FROM place_candidates c JOIN places p ON p.id=c.place_id
        WHERE {' AND '.join(clauses)} ORDER BY p.name,p.id,c.label,c.id
    """, params)
    return {"type": "FeatureCollection", "features": [
        {"type": "Feature", "id": feature["candidate_id"],
         "geometry": json.loads(feature.pop("geometry")), "properties": feature}
        for feature in features
    ]}


def cluster_filter_sql(theme: str | None, story_id: str | None, person_id: str | None,
                       place_id: str | None, confidence: str | None, q: str | None) -> tuple[str, dict[str, Any]]:
    clauses, params = spatial_filters(theme, story_id, person_id, place_id, confidence, q, True)
    clauses = [clause for clause in clauses if clause not in ("c.geometry IS NOT NULL", "c.display_mode <> 'none'")]
    return (" AND ".join(clauses) or "TRUE"), params


@app.get("/api/analysis/clusters")
def clusters(q: str | None = None, theme: str | None = None, story_id: str | None = None,
             person_id: str | None = None, place_id: str | None = None, confidence: str | None = None,
             db: Session = Depends(get_db)) -> dict[str, Any]:
    where, params = cluster_filter_sql(theme, story_id, person_id, place_id, confidence, q)
    scoped, scope_params = place_scope("p", q, theme, story_id, person_id, place_id, True)
    if confidence:
        scoped.append("p.confidence=:confidence")
        scope_params["confidence"] = confidence
    scoped_sql = " AND ".join(scoped) if scoped else "TRUE"
    inventory = rows(db, f"""
        WITH scoped AS (
          SELECT p.id AS place_id,p.confidence AS place_confidence,
                 count(c.id)::int AS candidate_count,
                 bool_or(c.geometry IS NULL OR c.display_mode='none') AS has_unlocated_candidate,
                 max(c.confidence) AS candidate_confidence,
                 max(c.display_mode) AS display_mode,
                 bool_and(c.is_primary) AS all_primary,
                 max(GeometryType(c.geometry)) AS geometry_type
          FROM places p LEFT JOIN place_candidates c ON c.place_id=p.id
          WHERE {scoped_sql}
          GROUP BY p.id,p.confidence
        )
        SELECT place_id,place_confidence,candidate_confidence,display_mode,all_primary,
               candidate_count,has_unlocated_candidate,
               CASE WHEN candidate_count=0 OR has_unlocated_candidate OR place_confidence='unlocated' THEN 'unlocated'
                    WHEN candidate_count>1 THEN 'multiple_candidates'
                    WHEN place_confidence='disputed' OR candidate_confidence='disputed' THEN 'disputed'
                    WHEN display_mode='area' THEN 'area'
                    WHEN display_mode='illustrative' THEN 'illustrative'
                    WHEN all_primary IS NOT TRUE OR place_confidence<>'clear'
                         OR candidate_confidence<>'clear' OR display_mode<>'point'
                         OR geometry_type<>'POINT' THEN 'unlocated'
                    ELSE 'eligible' END AS classification
        FROM scoped ORDER BY place_id
    """, scope_params)
    exclusions = {"unlocated": 0, "area": 0, "illustrative": 0, "disputed": 0, "multiple_candidates": 0}
    for item in inventory:
        classification = item["classification"]
        if classification in exclusions:
            exclusions[classification] += 1

    result = row(db, f"""
        WITH eligible AS (
          SELECT p.id AS place_id, ST_Transform(c.geometry, :projection) AS geom_m
          FROM places p JOIN place_candidates c ON c.place_id=p.id
          WHERE p.confidence='clear' AND c.confidence='clear' AND c.is_primary IS TRUE
            AND c.display_mode='point' AND GeometryType(c.geometry)='POINT'
            AND (SELECT count(*) FROM place_candidates cx WHERE cx.place_id=p.id)=1
            AND {where}
        ), clustered AS (
          SELECT place_id, geom_m,
                 ST_ClusterDBSCAN(geom_m, eps := :eps_m, minpoints := :min_points)
                   OVER (ORDER BY place_id) AS cluster_no
          FROM eligible
        ), grouped AS (
          SELECT cluster_no, min(place_id) AS first_place_id, count(*)::int AS count,
                 array_agg(place_id ORDER BY place_id) AS place_ids,
                 ST_Transform(ST_ConvexHull(ST_Collect(geom_m)), 4326) AS geometry
          FROM clustered WHERE cluster_no IS NOT NULL GROUP BY cluster_no
        ), numbered AS (
          SELECT row_number() OVER (ORDER BY first_place_id)::int AS id,count,place_ids,
                 ST_AsGeoJSON(geometry)::json AS geometry FROM grouped
        )
        SELECT (SELECT count(*)::int FROM eligible) AS eligible_count,
               COALESCE((SELECT sum(count)::int FROM grouped),0) AS clustered_count,
               COALESCE((SELECT count(*)::int FROM eligible e WHERE NOT EXISTS
                         (SELECT 1 FROM clustered c WHERE c.place_id=e.place_id AND c.cluster_no IS NOT NULL)),0) AS noise_count,
               COALESCE((SELECT json_agg(json_build_object('id',id,'count',count,'geometry',geometry,'place_ids',place_ids)
                         ORDER BY id) FROM numbered),'[]'::json) AS clusters
    """, {**params, "projection": PROJECTION, "eps_m": EPS_M, "min_points": MIN_POINTS, "confidence": confidence})
    return clean({
        "parameters": {"eps_m": EPS_M, "min_points": MIN_POINTS, "projection": PROJECTION_LABEL},
        "eligible_count": result["eligible_count"], "clustered_count": result["clustered_count"],
        "noise_count": result["noise_count"], "clusters": result["clusters"], "excluded": exclusions,
    })


@app.get("/api/stats")
def stats(db: Session = Depends(get_db)) -> dict[str, Any]:
    totals = row(db, """
        SELECT (SELECT count(*)::int FROM stories) AS stories,
               (SELECT count(*)::int FROM places) AS places,
               (SELECT count(*)::int FROM people) AS people,
               (SELECT count(*)::int FROM place_candidates WHERE geometry IS NOT NULL AND display_mode<>'none') AS mapped_candidates,
               (SELECT count(*)::int FROM places p WHERE p.confidence='unlocated'
                 OR NOT EXISTS (SELECT 1 FROM place_candidates c WHERE c.place_id=p.id AND c.geometry IS NOT NULL)) AS unlocated_places
    """)
    theme_rows = rows(db, "SELECT theme,count(*)::int AS story_count FROM stories GROUP BY theme")
    confidence_rows = rows(db, "SELECT confidence,count(*)::int AS place_count FROM places GROUP BY confidence")
    by_theme = {theme: 0 for theme in THEMES}
    by_theme.update({item["theme"]: item["story_count"] for item in theme_rows})
    by_confidence = {confidence: 0 for confidence in CONFIDENCES}
    by_confidence.update({item["confidence"]: item["place_count"] for item in confidence_rows})
    return {**totals, "by_theme": by_theme, "by_confidence": by_confidence}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
