#! /usr/bin/env bash
set -e

py=$1
dest="dep_data/inst-$py.json"
logs="dep_data/logs-$py.txt"

eval "$(conda shell.bash hook)"
conda create -yn tmp-$py python=$py > $logs
conda activate tmp-$py

conda install -yq --json -c defaults -c conda-forge mamba > $dest
inst () { mamba install -yq --json "$@"; }
if [[ $py != 3.6 ]]; then
  inst -c rapidsai -c nvidia -c defaults -c conda-forge 'cugraph>=0.17' 'cudf>=0.17' 'cuml>=0.17' 'cudatoolkit>=11' >> $dest
fi
inst -c pytorch -c defaults -c conda-forge 'pytorch>=1.7' torchvision >> $dest
inst -c defaults -c conda-forge transformers sentencepiece rich albumentations mamba >> $dest
inst -c fastai -c defaults -c conda-forge fastai timm >> $dest
inst -c fastai -c defaults -c conda-forge nbdev fastbook fastgpu fastrelease ghapi fastcgi fastdot >> $dest

