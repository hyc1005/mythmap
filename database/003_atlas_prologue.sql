ALTER TABLE myth_atlas_features DROP CONSTRAINT IF EXISTS myth_atlas_features_stage_id_check;
ALTER TABLE myth_atlas_features ADD CONSTRAINT myth_atlas_features_stage_id_check
  CHECK (stage_id IN ('00','01','02','03','04','05','06','07'));
