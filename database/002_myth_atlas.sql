CREATE TABLE IF NOT EXISTS myth_atlas_features (
  revision_id text NOT NULL,
  id text NOT NULL,
  stage_id text CHECK (stage_id IN ('01','02','03','04','05','06','07')),
  entity_id text NOT NULL,
  layer_role text NOT NULL,
  geometry geometry(Geometry,4326),
  properties jsonb NOT NULL,
  PRIMARY KEY (revision_id, id),
  CHECK (layer_role <> 'spatial_reference' OR geometry IS NULL),
  CHECK (NOT COALESCE((properties->>'analysis_eligible')::boolean, false))
);
CREATE INDEX IF NOT EXISTS myth_atlas_geometry_gix ON myth_atlas_features USING gist (geometry);
CREATE INDEX IF NOT EXISTS myth_atlas_stage_idx ON myth_atlas_features(revision_id, stage_id, layer_role);
CREATE TABLE IF NOT EXISTS myth_atlas_catalog (
  revision_id text PRIMARY KEY,
  catalog jsonb NOT NULL,
  divine_space jsonb NOT NULL
);
