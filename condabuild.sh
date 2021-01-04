#! /bin/bash -l
set -e

mkdir -p output
conda build sentencepiece --output-folder output
anaconda -t $ANACONDA_TOKEN upload --skip -u fastai output/*/sentencepiece-*.tar.bz2 || true

