#! /usr/bin/env bash
set -e

if [[ "$1" = "-h" ]] || [[ "$1" = "--help" ]];then
    echo "optional arguments:"
    echo "--force            Return the github tag no matter what. (default: False)"
    echo "-h, --help         show this help message and exit"
    exit 0;
fi

tag=$(python get_tag.py "$1")
if [ "$tag" ]; then
    mamba install -yq -c cbillington -c defaults setuptools-conda anaconda-client
    mkdir -p tmp && cd tmp
    git clone -b "$tag" --depth 1 https://github.com/rwightman/pytorch-image-models.git .
    setuptools-conda build --conda-name-differences 'torch:pytorch' -c pytorch .
    conda convert -p all -o conda_packages conda_packages/*/*.tar.bz2
    anaconda -t $ANACONDA_TOKEN upload --skip -u fastai conda_packages/*/*.tar.bz2 || true;
fi
