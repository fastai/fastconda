#! /usr/bin/env bash
set -e
: ${1?"Usage: $0 version"}

PATH=${CONDA:=$CONDA_PREFIX}/condabin:$PATH
eval "$(conda shell.bash hook)"
conda create -yqn tmpbuild python=$1 anaconda-client conda-build
conda activate tmpbuild
conda build sentencepiece
conda build purge
anaconda -t $ANACONDA_TOKEN upload --skip -u fastai $(conda info --root)/conda-bld/*/sentencepiece-*.tar.bz2

