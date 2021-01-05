# fastconda

> Get packages onto your conda channel faster

## Status

 | GitHub | Conda
-- | -- | --
timm | ![](https://img.shields.io/github/v/release/rwightman/pytorch-image-models) | ![](https://img.shields.io/conda/vn/fastai/timm)


## condabuild

Builds a conda package that simply installs a pip package (currently just does sentencepiece).

## build_timm

Creates a conda package from a source repo using `setuptools-conda` (currently just does timm).

## get_deps

Copies the following (and their dependencies) from conda-forge, nvidia, rapids, and fastai channels to the fastchan channel: cudf cudatoolkit mamba pytorch torchvision transformers rich sentencepiece fastai timm conda-forge nbdev fastrelease ghapi fastcgi.
