#!/bin/bash
BASE_PATH=$PWD
VENV_NAME=env
VENV_DIR=$BASE_PATH/$VENV_NAME
rm -rf $VENV_NAME && python3 -m venv $VENV_NAME
source $VENV_DIR/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
