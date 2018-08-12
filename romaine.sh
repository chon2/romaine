#!/usr/bin/env bash
SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)

echo "start ngrok"

ngrok start ssh --log=stdout --config=$SCRIPT_DIR/ngrok.yml

#sudo pigpiod
#
#cd $SCRIPT_DIR
#python romaine.py &