#!/bin/bash

# Full update dependencies using poetry

SCRIPT_DIR="$( cd "$( dirname "$0" )" && pwd )"
CURRENT_DIR=$PWD

_poetry () {
    echo
    echo ">>= $@"
    poetry $@
    RETVAL=$?
    if [ $RETVAL -ne 0 ]; then
        echo "ERROR: Return code was not zero but $RETVAL"
        cd $CURRENT_DIR
        exit $RETVAL
    fi
}

cd $SCRIPT_DIR

_poetry lock --no-update
_poetry install --with docs --sync
_poetry update --with docs

cd $CURRENT_DIR
