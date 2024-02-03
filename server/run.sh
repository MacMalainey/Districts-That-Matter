#!/usr/bin/env bash

BASEDIR=$(dirname "$0")
cd $BASEDIR
if [[ -z "${VIRTUAL_ENV}" ]]; then
	source ./.venv/bin/activate
fi

flask --app main run
