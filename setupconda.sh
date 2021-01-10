#! /usr/bin/env bash
set -e

tag=$(python get_tag.py "$2" --pre "$4")
if [ "$tag" ]; then
  rm -rf tmp
  git clone -b "$tag" --depth 1 https://github.com/"$1".git tmp
  cd tmp
  setuptools-conda build $3
  anaconda -t $ANACONDA_TOKEN upload --skip -u fastai conda_packages/*/*.tar.bz2 || true;
else
  echo no new release available
fi

