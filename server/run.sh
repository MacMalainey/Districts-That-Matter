#!/usr/bin/env bash

SCRIPTDIR=$(dirname "$0")
cd "$SCRIPTDIR/.."
BASEDIR=$(pwd)
if [[ -z "${VIRTUAL_ENV}" ]]; then
	source .venv/bin/activate
fi

export DTM_SERVER_STATIC_DIR=.../district_tm/build
export DTM_SERVER_SCHEMA=../.local/dtmTORO_schema.json
export DTM_SERVER_DATABASE=../.local/dtmTORO.db

cd server
python3 -m flask --app main run
