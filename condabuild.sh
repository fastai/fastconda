#! /usr/bin/env bash
set -e
: ${1?"Usage: $0 version"}

eval "$(conda shell.bash hook)"
conda create -yqn tmpbuild python=$1 anaconda-client conda-build
conda activate tmpbuild
conda build sentencepiece
conda build purge
anaconda -t $ANACONDA_TOKEN upload --skip -u fastai $CONDA_PREFIX/conda-bld/*/sentencepiece-*.tar.bz2

