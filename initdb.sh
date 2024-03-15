#!/usr/bin/env bash

BASEDIR=$(dirname "$0")
cd "$BASEDIR"
CENSUS_DATA=".local/98-401-X2021006_English_CSV_data_Ontario.csv"
BOUNDARY_DATA=".local/lda_000a21g_e.gml"

if [[ ! -f "$CENSUS_DATA" ]]; then
	echo "Unable to find census data at: $BASEDIR/$CENSUS_DATA"
	echo "Please import data there and rerun"
	exit 1
fi

if [[ ! -f "$BOUNDARY_DATA" ]]; then
	echo "Unable to find boundary data at: $BASEDIR/$BOUNDARY_DATA"
	echo "Please import data there and rerun"
	exit 1
fi

if [[ -f ".local/dtmTORO.db" ]]; then
	echo "Database ($BASEDIR/.local/dtmTORO.db) already exists!"
	echo "To perform a fresh install please remove the file and rerun"
	exit 1
fi

if [[ -z "${VIRTUAL_ENV}" ]]; then
	source ./.venv/bin/activate
	if [[ $? -ne 0 ]]; then
		exit 1
	fi
fi


python3 parser/main.py "$CENSUS_DATA" --schema "parser/characteristics.csv" --filter "parser/GTA_CSD_LIST.txt" --output ".local/dtmTORO.db" || exit 1
# spatialite_tool -i -shp .local/lda_000a21a_e.shp -d .local/dtmTORO.db -c CP1252 -s 3347 -t tempgeom -g geom
spatialite -bail ".local/dtmTORO.db" < "parser/load_boundary.sql" || exit 1

