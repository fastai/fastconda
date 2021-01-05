#! /bin/bash -l
set -e
tag=$(python get_tag.py --nm sentencepiece --apkg sentencepiece)

if [ "$tag" ]; then
    echo "::group::Build Package"
    mkdir -p output
    conda build sentencepiece --output-folder output
    echo "::endgroup::"

    echo "::group::Upload Package"
    anaconda -t $ANACONDA_TOKEN upload --skip -u fastai output/*/sentencepiece-*.tar.bz2 || true
    echo "::endgroup::"
else
    echo "Conda package fastai/sentencepiece already up to date."
fi
