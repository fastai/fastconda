#! /usr/bin/env bash
set -e

eval "$(conda shell.bash hook)"
conda create -yqn tmp-buildconda -c cbillington -c defaults python=3.8 setuptools-conda anaconda-client
conda activate tmp-buildconda
mkdir -p tmp && cd tmp

git clone https://github.com/rwightman/pytorch-image-models.git --depth 1
cd pytorch-image-models
setuptools-conda build --conda-name-differences 'torch:pytorch' -c pytorch .
conda convert -p all -o conda_packages conda_packages/linux-64/timm-0.3.3-py38_0.tar.bz2
anaconda -t $ANACONDA_TOKEN upload --skip -u fastai conda_packages/*/*.tar.bz2 || true

