.loadshp .local/lda_000a21a_e lda_000a21a_e CP1252 3347 geometry dguid MULTIPOLYGON 2d;
CREATE TABLE boundary_data AS SELECT dguid, Transform(geometry, 4326) FROM lda_000a21a_e JOIN census_data USING (dguid);
SELECT RecoverGeometryColumn('boundary_data', 'geometry', 4326, 'MULTIPOLYGON', 'XY');
DROP TABLE lda_000a21a_e;
.exit