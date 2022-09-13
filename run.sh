#! /bin/sh
export PYTHONPATH=/usr/src/app
export FLASK_APP=${PYTHONPATH}/main.py
source ./venv/bin/activate
python3 ./main.py