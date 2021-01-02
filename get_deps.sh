#! /usr/bin/env bash
set -e

py=$1
eval "$(conda shell.bash hook)"

dest="dep_data/inst-$py.json"
logs="dep_data/logs-$py.txt"

conda create -yn tmp-$py python==$py > $logs
conda activate tmp-$py
conda install -yq --json -c defaults -c conda-forge mamba > $dest
mamba install -yq --json -c pytorch -c rapidsai -c nvidia -c defaults -c conda-forge 'pytorch>=1.7' 'cudf>=0.17' 'cudatoolkit>=11' \
    transformers sentencepiece rich timm ipython albumentations mamba >> $dest
mamba install -yq --json -c fastai -c pytorch -c defaults -c conda-forge fastai nbdev >> $dest

