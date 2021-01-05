#! /bin/bash -l
set -e

echo "::group::Build Packages"
mkdir -p output
conda build sentencepiece --output-folder output
echo "::endgroup::"

echo "::group::Upload Packages"
anaconda -t $ANACONDA_TOKEN upload --skip -u fastai output/*/sentencepiece-*.tar.bz2 || true
echo "::endgroup::"
