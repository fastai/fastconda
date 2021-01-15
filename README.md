# fastconda

> Get packages onto your conda channel faster

## Status

 ![CI](https://github.com/fastai/fastconda/workflows/setupconda/badge.svg) ![CI](https://github.com/fastai/fastconda/workflows/condabuild/badge.svg) ![anacopy](https://github.com/fastai/fastconda/workflows/anacopy/badge.svg)

### Builds

Package Name | Pypi | GitHub | Conda [fastai channel](https://anaconda.org/fastai/repo)
-- | -- | -- | -- 
sentencepiece | ![](https://img.shields.io/pypi/v/sentencepiece) |  ![](https://img.shields.io/github/v/release/google/sentencepiece) | ![](https://img.shields.io/conda/vn/fastai/sentencepiece)
opencv-python-headless | ![](https://img.shields.io/pypi/v/opencv-python-headless) |  N/A | ![](https://img.shields.io/conda/vn/fastai/opencv-python-headless)
timm |  ![](https://img.shields.io/pypi/v/timm) | ![](https://img.shields.io/github/v/release/rwightman/pytorch-image-models) | ![](https://img.shields.io/conda/vn/fastai/timm)
albumentations | ![](https://img.shields.io/pypi/v/albumentations) |  ![](https://img.shields.io/github/v/release/albumentations-team/albumentations) | ![](https://img.shields.io/conda/vn/fastai/albumentations) 
imgaug | ![](https://img.shields.io/pypi/v/imgaug) |  ![](https://img.shields.io/github/v/release/aleju/imgaug) | ![](https://img.shields.io/conda/vn/fastai/imgaug)


### Copies

Package | Pypi | Conda [fastchan channel](https://anaconda.org/fastai/repo)
-- | -- | -- 
cudf | ![](https://img.shields.io/pypi/v/cudf ) | ![](https://img.shields.io/conda/vn/fastchan/cudf )
cudatoolkit | N/A | ![](https://img.shields.io/conda/vn/fastchan/cudatoolkit )
mamba | ![](https://img.shields.io/pypi/v/mamba ) | ![](https://img.shields.io/conda/vn/fastchan/mamba )
pytorch | ![](https://img.shields.io/pypi/v/pytorch ) | ![](https://img.shields.io/conda/vn/fastchan/pytorch)
torchvision | ![](https://img.shields.io/pypi/v/torchvision ) | ![](https://img.shields.io/conda/vn/fastchan/torchvision)
transformers | ![](https://img.shields.io/pypi/v/transformers ) | ![](https://img.shields.io/conda/vn/fastchan/transformers)
rich | ![](https://img.shields.io/pypi/v/rich ) | ![](https://img.shields.io/conda/vn/fastchan/rich )
sentencepiece | ![](https://img.shields.io/pypi/v/sentencepiece) | ![](https://img.shields.io/conda/vn/fastchan/sentencepiece)
fastai | ![](https://img.shields.io/pypi/v/fastai ) | ![](https://img.shields.io/conda/vn/fastchan/fastai )
timm | ![](https://img.shields.io/pypi/v/timm ) | ![](https://img.shields.io/conda/vn/fastchan/timm )
nbdev | ![](https://img.shields.io/pypi/v/nbdev ) | ![](https://img.shields.io/conda/vn/fastchan/nbdev )
fastrelease | ![](https://img.shields.io/pypi/v/fastrelease) | ![](https://img.shields.io/conda/vn/fastchan/fastrelease)
ghapi | ![](https://img.shields.io/pypi/v/ghapi ) | ![](https://img.shields.io/conda/vn/fastchan/ghapi )
fastcgi | ![](https://img.shields.io/pypi/v/fastcgi) | ![](https://img.shields.io/conda/vn/fastchan/fastcgi)


# Build Process

We are using three different ways for sourcing a Conda package into an Anaconda repo:

1. [conda build](#conda-build): When there are C dependencies.
2. [setuptools-conda](#setuptools-conda): For pure python packages.
3. [anaconda copy](#anaconda-copy): When a maintained Anaconda package already exists.

## conda build

_When there are C dependencies._

Build a Conda package by first installing the appropriate pip package(s) in a fresh Conda environment, and then use `conda build` to build a package based on this environment.  We do this for packages that have C dependencies and need thus need binaries created for different platforms. This build process is specified in [condabuild.yml](.github/workflows/condabuild.yml).  This type of build requires a specific directory structure with several metadata files which amounts to a fair amount of boilerplate. For this reason, we dynamically generate all of this boilerplate based on the configuration file [build.yaml](./build.yaml)

The schema of [build.yaml](./build.yaml) is as follows:

```yaml
- pypinm: opencv-python-headless
  import_nm: cv2 # Optional: if not specified will default to the same as pypinm
  deps: [numpy]  # Optional: if not specified will just be python
  path: destination_dir # Optional: if not specified, files will be placed in a directory named after `pypinm`
- pypinm: sentencepiece # This second package, `sentencepiece`, uses all of the defaults.
```

In the above example, we specify two packages to built, `opencv-python-headless` and `sentencepiece`.  Here is a description of all fields:

- `pypinm`: this field is required and is the name of the package on pypi.
- `import_nm`: You only need to supply this field when the import name of the pypi package is different than the package name.  For example the import name of `opencv-python-headless` is `cv2`.
- `deps`: This is a list of all dependencies.  If this is not supplied, no dependencies beyond python are assumed.
- `path`: You should usually ignore this field completely and rely on the default behavior. This optional parameter allows you to specify the directory where the metadata files will be placed.  If not specified, files will be placed in a directory named after `pypinm`.

You can run this locally with:

> python build.py

_see [condabuild.yml](.github/workflows/condabuild.yml) for necessary environment setup._

## setuptools-conda

_For pure python packages._

For python packages that are pure-python that do not require binaries, we can instead create a cross-platform Conda package using `setuptools-conda`.  This build process is specified in [setupconda.yaml](.github/workflows/setupconda.yaml).  

You can run this locally with:

> ./setupconda.sh {args}

_see [setupconda.yaml](.github/workflows/setupconda.yaml) for example of args_

## anaconda copy

_When a maintained Anaconda package already exists._

In situations where there is a reliable and maintained conda package already present in another channel, we can copy this package and all its dependencies to another channel.  This is desirable when you want to simplify and speed up the installation of packages by placing all dependencies in a single channel.  This process is carried out via [anacopy.yml](.github/workflows/anacopy.yml).  We find all dependencies for a particular package by doing a Conda installation, which uses the Conda solver to find all the dependencies with appropriate version numbers, and then copy the appropriate packages using `anaconda copy`.

You can run this locally:

> python get_deps.py

_See [anacopy.yml](.github/workflows/anacopy.yml) for the full workflow._
