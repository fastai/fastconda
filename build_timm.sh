#! /usr/bin/env bash
set -e

tag=$(python get_tag.py "$1")
if [ "$tag" ]; then
  rm -rf tmp && mkdir -p tmp && cd tmp
  git clone -b "$tag" --depth 1 https://github.com/rwightman/pytorch-image-models.git .
  setuptools-conda build --noarch .
  anaconda -t $ANACONDA_TOKEN upload --skip -u fastai conda_packages/*/*.tar.bz2 || true;
else
  echo no new release available
fi

