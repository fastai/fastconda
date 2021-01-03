#! /usr/bin/env bash
set -e
: ${1?"Usage: $0 version"}

eval "$(conda shell.bash hook)"
conda create -yqn tmp-$1 python=$1
conda activate tmp-$1
pip install -Uq fastcore

python get_deps.py

