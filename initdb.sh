#!/usr/bin/env bash

BASEDIR=$(dirname "$0")
cd "$BASEDIR"
CENSUS_DATA=".local/98-401-X2021006_English_CSV_data_Ontario.csv"
BOUNDARY_DATA=".local/lda_000a21a_e.shp"

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

fatal () {
	if [[ -f ".local/dtmTORO.db" ]]; then
		rm ".local/dtmTORO.db"
	fi
	exit 1
}

spatialite -bail -silent -batch ".local/dtmTORO.db" "" || fatal
python3 parser/main.py "$CENSUS_DATA" --schema "parser/characteristics.csv" --filter "parser/GTA_CSD_LIST.txt" --output ".local/dtmTORO.db" || fatal
echo "Loading boundary data..."
spatialite -bail -silent -batch ".local/dtmTORO.db" < "parser/load_boundary.sql" || fatal
echo "Database initialized!!! Execute run.sh to start the server!"

