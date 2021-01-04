#! /usr/bin/env bash
set -e

tag=$(python get_tag.py --force)
if [ "$tag" ]; then
    eval "$(conda shell.bash hook)"
    conda create -yqn tmp-buildconda -c cbillington -c defaults python=3.8 setuptools-conda anaconda-client
    conda activate tmp-buildconda
    mkdir -p tmp && cd tmp

    git clone -b $tag --depth 1 https://github.com/rwightman/pytorch-image-models.git .
    setuptools-conda build --conda-name-differences 'torch:pytorch' -c pytorch .
    conda convert -p all -o conda_packages conda_packages/*/*.tar.bz2
    anaconda -t $ANACONDA_TOKEN upload --skip -u fastai conda_packages/*/*.tar.bz2
fi
