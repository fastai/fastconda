#! /usr/bin/env bash
set -e

rm -rf tmp
python get_release.py $1 --force

if [ -d "tmp" ]; then  
  cd tmp
  setuptools-conda build --license-file 'None' $2
  anaconda -t $ANACONDA_TOKEN upload --skip -u fastai conda_packages/*/*.tar.bz2 || true;
else
  echo "no new release available"
fi
