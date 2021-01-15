# fastconda

> Get packages onto your conda channel faster

## Status

TODO: Update Badges

Package Name | Pypi | GitHub | Conda [fastai channel](https://anaconda.org/fastai/repo) | Actions |
-- | -- | -- | -- | --
timm |  ![](https://img.shields.io/pypi/v/timm) | ![](https://img.shields.io/github/v/release/rwightman/pytorch-image-models) | ![](https://img.shields.io/conda/vn/fastai/timm) | ![timm](https://github.com/fastai/fastconda/workflows/timm/badge.svg)
sentencepiece | ![](https://img.shields.io/pypi/v/sentencepiece) |  ![](https://img.shields.io/github/v/release/google/sentencepiece) | ![](https://img.shields.io/conda/vn/fastai/sentencepiece) | ![condabuild](https://github.com/fastai/fastconda/workflows/condabuild/badge.svg)
albumentations | ![](https://img.shields.io/pypi/v/albumentations) |  ![](https://img.shields.io/github/v/release/albumentations-team/albumentations) | ![](https://img.shields.io/conda/vn/fastai/albumentations) | ![condabuild]()
imgaug | ![](https://img.shields.io/pypi/v/imgaug) |  ![](https://img.shields.io/github/v/release/aleju/imgaug) | ![](https://img.shields.io/conda/vn/fastai/imgaug) | ![condabuild]()


## Build Process

There are three different ways a conda package can be sourced into an Ancaconda repo:

1. Build a conda package by first installing the appropriate pip package(s) in a fresh conda environment, and then use `conda build` to build a package based on this environment.  We do this for packages that have C dependencies and need thus need binaries created for different platforms. This build process is specified in [condabuild.yml](.github/workflows/condabuild.yml)

2. For python packages that are pure-python that do not require binaries, we can instead create a cross-platform conda package using `setuptools-conda`.  This build process is specified in [setupconda.yaml](.github/workflows/condabuild.yaml)

3. In situations where there is a relaiable and maintained conda package already present in another channel, we can copy this package and all its dependencies to another channel.  This is desirable when you want to simplify and speed up the installation of packages by placing all dependencies in a single channel.  This process is carried out via [anacopy.yml](.github/workflows/anacopy.yml)

TODO: Mention how dependencies are determined, perhaps with dryrun?  
TODO: figure out why dryrun is not being used?

TODO: mention this?

Copies the following (and their dependencies) from conda-forge, nvidia, rapids, and fastai channels to the fastchan channel: cudf cudatoolkit mamba pytorch torchvision transformers rich sentencepiece fastai timm conda-forge nbdev fastrelease ghapi fastcgi.

