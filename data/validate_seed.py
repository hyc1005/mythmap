"""Validate seed.json without needing a running PostgreSQL server."""
import json
from pathlib import Path

PATH = Path(__file__).with_name("seed.json")
THEMES = {"山川地理", "神祇", "异兽", "方国", "神话事件"}
CONFIDENCE = {"clear", "disputed", "unlocated"}
DISPLAY = {"point", "area", "illustrative", "none"}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def main():
    data = json.loads(PATH.read_text(encoding="utf-8"))
    for collection in ("sources", "stories", "people", "places", "candidates"):
        ids = [row["id"] for row in data[collection]]
        require(len(ids) == len(set(ids)), f"duplicate IDs in {collection}")
    sources = {row["id"] for row in data["sources"]}
    stories = {row["id"]: row for row in data["stories"]}
    people = {row["id"]: row for row in data["people"]}
    places = {row["id"]: row for row in data["places"]}
    candidates = {row["id"]: row for row in data["candidates"]}
    require(20 <= len(stories) <= 30, f"story count out of range: {len(stories)}")
    require(30 <= len(places) <= 50, f"place count out of range: {len(places)}")
    require(set(row["theme"] for row in stories.values()) == THEMES, "all five exact themes must be used")
    for kind, rows in (("story", stories), ("person", people), ("place", places)):
        for row in rows.values():
            require(row.get("name", row.get("title")), f"{kind} has empty name/title")
            require(row.get("description", row.get("summary")), f"{kind} has empty description/summary")
            require(row.get("source_ids"), f"{kind} {row['id']} has no source")
            require(set(row["source_ids"]) <= sources, f"{kind} {row['id']} has unknown source")
    for story in stories.values():
        require(story["theme"] in THEMES and story["chapter"] and story["quote"], f"invalid story citation: {story['id']}")
        require(set(story["place_ids"]) <= places.keys(), f"unknown place in {story['id']}")
        require(set(story["person_ids"]) <= people.keys(), f"unknown person in {story['id']}")
    for person in people.values():
        require(set(person["source_ids"]) <= sources, f"unknown source for {person['id']}")
    for place in places.values():
        require(place["confidence"] in CONFIDENCE, f"invalid confidence on {place['id']}")
    for candidate in candidates.values():
        require(candidate["place_id"] in places, f"unknown place for {candidate['id']}")
        require(candidate["display_mode"] in DISPLAY and candidate["confidence"] in CONFIDENCE, f"invalid candidate flags: {candidate['id']}")
        require(candidate["reason"].strip() and candidate["source_ids"], f"candidate lacks reason/source: {candidate['id']}")
        require(set(candidate["source_ids"]) <= sources, f"unknown source for {candidate['id']}")
        require(candidate["confidence"] == places[candidate["place_id"]]["confidence"], f"place/candidate confidence mismatch: {candidate['id']}")
        geom = candidate["geometry"]
        mode = candidate["display_mode"]
        require((mode == "none") == (geom is None), f"geometry/display mismatch: {candidate['id']}")
        if geom:
            kind = geom["type"]
            require((kind == "Point" and mode in {"point", "illustrative"}) or
                    (kind in {"Polygon", "MultiPolygon"} and mode == "area"),
                    f"geometry/display mismatch: {candidate['id']}")
            coordinates = geom["coordinates"]
            if kind == "Point":
                positions = [coordinates]
            else:
                polygons = [coordinates] if kind == "Polygon" else coordinates
                require(polygons, f"empty area geometry: {candidate['id']}")
                positions = []
                for polygon in polygons:
                    require(polygon, f"area geometry has no rings: {candidate['id']}")
                    for ring in polygon:
                        require(len(ring) >= 4 and ring[0] == ring[-1], f"invalid polygon ring: {candidate['id']}")
                        positions.extend(ring)
            for position in positions:
                require(len(position) >= 2, f"invalid position: {candidate['id']}")
                lon, lat = position[:2]
                require(-180 <= lon <= 180 and -90 <= lat <= 90, f"invalid coordinate: {candidate['id']}")
        require(not (candidate["display_mode"] == "illustrative" and candidate["is_primary"]), f"illustrative point marked primary: {candidate['id']}")
    for place in places.values():
        if place["confidence"] in {"unlocated", "disputed"}:
            require("project-method" in place["source_ids"], f"missing explicit non-location rationale source: {place['id']}")
    primary_ids = [(c["place_id"], c["id"]) for c in candidates.values()
                   if c["is_primary"] and c["confidence"] == "clear" and c["display_mode"] == "point"]
    require(len({place_id for place_id, _ in primary_ids}) == len(primary_ids), "multiple cluster-eligible candidates for one place")
    for link in data["story_people"]:
        require(link[0] in stories and link[1] in people, f"invalid story-person relation: {link}")
    confidence_counts = {level: sum(1 for place in places.values() if place["confidence"] == level) for level in sorted(CONFIDENCE)}
    display_counts = {mode: sum(1 for candidate in candidates.values() if candidate["display_mode"] == mode) for mode in sorted(DISPLAY)}
    print(f"OK: {len(stories)} stories, {len(places)} places, {len(people)} people, {len(candidates)} candidates, {len(sources)} sources")
    print(f"Place confidence: {confidence_counts}; candidate display modes: {display_counts}; cluster-eligible: {len(primary_ids)}")
    print("Themes: " + ", ".join(sorted(THEMES)))


if __name__ == "__main__":
    main()
