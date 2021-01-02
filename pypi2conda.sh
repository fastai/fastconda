#!/usr/bin/env bash
set -e

: "${CONDA:=$CONDA_PREFIX}"
PATH=$CONDA/condabin:$PATH
eval "$(conda shell.bash hook)"

python pypi2conda.py

