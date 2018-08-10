#!/usr/bin/env bash
SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)

sudo pigpiod

cd $SCRIPT_DIR
python romaine.py &