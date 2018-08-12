#!/usr/bin/env bash
SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)

cd $SCRIPT_DIR

. ./venv/bin/activate

echo "start ngrok"

ngrok start ssh --log=stdout --config=$SCRIPT_DIR/ngrok.yml &

sudo pigpiod

python romaine.py &
