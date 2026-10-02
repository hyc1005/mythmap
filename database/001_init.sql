CREATE EXTENSION IF NOT EXISTS postgis;

CREATE TABLE sources (
  id text PRIMARY KEY,
  title text NOT NULL,
  creator text NOT NULL,
  url text,
  citation text NOT NULL,
  accessed_on date
);

CREATE TABLE stories (
  id text PRIMARY KEY,
  title text NOT NULL,
  theme text NOT NULL CHECK (theme IN ('山川地理','神祇','异兽','方国','神话事件')),
  summary text NOT NULL,
  chapter text NOT NULL,
  quote text NOT NULL
);
CREATE TABLE people (
  id text PRIMARY KEY,
  name text NOT NULL,
  description text NOT NULL
);
CREATE TABLE places (
  id text PRIMARY KEY,
  name text NOT NULL,
  modern_name text,
  description text NOT NULL,
  confidence text NOT NULL CHECK (confidence IN ('clear','disputed','unlocated'))
);
CREATE TABLE place_candidates (
  id text PRIMARY KEY,
  place_id text NOT NULL REFERENCES places(id) ON DELETE CASCADE,
  label text NOT NULL,
  geometry geometry(Geometry,4326),
  display_mode text NOT NULL CHECK (display_mode IN ('point','area','illustrative','none')),
  confidence text NOT NULL CHECK (confidence IN ('clear','disputed','unlocated')),
  is_primary boolean NOT NULL DEFAULT false,
  reason text NOT NULL,
  CHECK ((display_mode='none' AND geometry IS NULL) OR
         (display_mode <> 'none' AND geometry IS NOT NULL AND
          ((display_mode='point' AND GeometryType(geometry)='POINT') OR
           (display_mode='area' AND GeometryType(geometry) IN ('POLYGON','MULTIPOLYGON')) OR
           (display_mode='illustrative' AND GeometryType(geometry)='POINT')))),
  CHECK (display_mode <> 'illustrative' OR NOT is_primary)
);
CREATE TABLE story_places (
  story_id text NOT NULL REFERENCES stories(id) ON DELETE CASCADE,
  place_id text NOT NULL REFERENCES places(id) ON DELETE CASCADE,
  relation_type text NOT NULL,
  quote text NOT NULL,
  sequence integer NOT NULL CHECK (sequence >= 1),
  PRIMARY KEY (story_id, place_id)
);
CREATE TABLE story_people (
  story_id text NOT NULL REFERENCES stories(id) ON DELETE CASCADE,
  person_id text NOT NULL REFERENCES people(id) ON DELETE CASCADE,
  PRIMARY KEY (story_id, person_id)
);
CREATE TABLE story_sources (
  story_id text NOT NULL REFERENCES stories(id) ON DELETE CASCADE,
  source_id text NOT NULL REFERENCES sources(id),
  PRIMARY KEY (story_id, source_id)
);
CREATE TABLE person_sources (
  person_id text NOT NULL REFERENCES people(id) ON DELETE CASCADE,
  source_id text NOT NULL REFERENCES sources(id),
  PRIMARY KEY (person_id, source_id)
);
CREATE TABLE place_sources (
  place_id text NOT NULL REFERENCES places(id) ON DELETE CASCADE,
  source_id text NOT NULL REFERENCES sources(id),
  PRIMARY KEY (place_id, source_id)
);
CREATE TABLE candidate_sources (
  candidate_id text NOT NULL REFERENCES place_candidates(id) ON DELETE CASCADE,
  source_id text NOT NULL REFERENCES sources(id),
  PRIMARY KEY (candidate_id, source_id)
);

CREATE INDEX place_candidates_geom_gix ON place_candidates USING gist (geometry);
CREATE INDEX story_places_place_idx ON story_places(place_id);
CREATE INDEX place_candidates_place_idx ON place_candidates(place_id);

-- A primary, clear point must be unique per place. Illustrative points are excluded.
CREATE UNIQUE INDEX place_one_clear_primary_idx ON place_candidates(place_id)
  WHERE is_primary AND confidence='clear' AND display_mode='point';
