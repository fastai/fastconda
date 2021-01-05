# fastconda

> Get packages onto your conda channel faster

## Status

Package Name | Pypi | GitHub | Conda [fastai channel](https://anaconda.org/fastai/repo) | Actions |
-- | -- | -- | -- | --
timm |  ![](https://img.shields.io/pypi/v/timm) | ![](https://img.shields.io/github/v/release/rwightman/pytorch-image-models) | ![](https://img.shields.io/conda/vn/fastai/timm) | ![timm](https://github.com/fastai/fastconda/workflows/timm/badge.svg)
sentencepiece | ![](https://img.shields.io/pypi/v/sentencepiece) |  ![](https://img.shields.io/github/v/release/google/sentencepiece) | ![](https://img.shields.io/conda/vn/fastai/sentencepiece) | ![condabuild](https://github.com/fastai/fastconda/workflows/condabuild/badge.svg)


## condabuild

Builds a conda package that simply installs a pip package (currently just does sentencepiece).

## build_timm

Creates a conda package from a source repo using `setuptools-conda` (currently just does timm).

## get_deps

Copies the following (and their dependencies) from conda-forge, nvidia, rapids, and fastai channels to the fastchan channel: cudf cudatoolkit mamba pytorch torchvision transformers rich sentencepiece fastai timm conda-forge nbdev fastrelease ghapi fastcgi.
