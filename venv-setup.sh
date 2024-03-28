#!/usr/bin/env bash

BASEDIR=$(dirname "$0")
cd $BASEDIR
if [[ -d .venv ]]; then
    echo "Virtual environment already exists"
    echo "To perform a fresh install remove $(pwd)/.venv"
    echo ""
else 
    python3 -m venv .venv
fi

if [[ -z "${VIRTUAL_ENV}" ]]; then
	source ./.venv/bin/activate
fi

python3 -m pip install -r parser/requirements.txt
python3 -m pip install -r server/requirements.txt