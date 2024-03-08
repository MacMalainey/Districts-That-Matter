#!/usr/bin/env bash

BASEDIR=$(dirname "$0")
CENSUS_DATA="$BASEDIR/.local/98-401-X2021006_English_CSV_data_Ontario.csv"
BOUNDARY_DATA="$BASEDIR/.local/lda_000a21g_e.gml"

if [[ ! -f "$CENSUS_DATA" ]]; then
	echo "Unable to find census data at: $CENSUS_DATA"
	echo "Please import data there and rerun"
	exit 1
fi

if [[ ! -f "$BOUNDARY_DATA" ]]; then
	echo "Unable to find boundary data at: $BOUNDARY_DATA"
	echo "Please import data there and rerun"
	exit 1
fi

if [[ -f "$BASEDIR/.data/dtmTORO.db" ]]; then
	echo "Database ($BASEDIR/.data/dtmTORO.db) already exists!"
	echo "To perform a fresh install please remove the file and rerun"
	exit 1
fi

if [[ -z "${VIRTUAL_ENV}" ]]; then
	cd "$BASEDIR"
	source ./.venv/bin/activate
	if [[ $? -ne 0 ]]; then
		exit 1
	fi
fi

cd $BASEDIR/utility
python3 main.py "$CENSUS_DATA" "$BOUNDARY_DATA" --filter GTA_CSD_LIST.txt --output "$BASEDIR/.local/dtmTORO.db"

