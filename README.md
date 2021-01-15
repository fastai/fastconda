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



# Build Process

We are using three different ways for sourcing a conda package into an Ancaconda repo:

1. [conda build](#conda-build): When there are C dependencies.
2. [setuptools-conda](#setuptools-conda): For pure python packages.
3. [anaconda copy](#anaconda-copy): When a maintaiend anconda package already exists.

## conda build

_When there are C dependencies._

Build a conda package by first installing the appropriate pip package(s) in a fresh conda environment, and then use `conda build` to build a package based on this environment.  We do this for packages that have C dependencies and need thus need binaries created for different platforms. This build process is specified in [condabuild.yml](.github/workflows/condabuild.yml).  This type of build requires a specific directory structure with several metadata files which amounts to a fair amount of biolerplate. For this reason, we dynamically generate all of this boilerplate based on the configuration file [build.yaml](./build.yaml)

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

##  setuptools-conda

_For pure python packages._

For python packages that are pure-python that do not require binaries, we can instead create a cross-platform conda package using `setuptools-conda`.  This build process is specified in [setupconda.yaml](.github/workflows/setupconda.yaml).  

You can run this locally with:

> ./setupconda.sh {args}

_see [setupconda.yaml](.github/workflows/setupconda.yaml) for example of args_

##  anaconda copy

_When a maintaiend anconda package already exists._

In situations where there is a relaiable and maintained conda package already present in another channel, we can copy this package and all its dependencies to another channel.  This is desirable when you want to simplify and speed up the installation of packages by placing all dependencies in a single channel.  This process is carried out via [anacopy.yml](.github/workflows/anacopy.yml).  We find all dependencies for a particular package by doing a conda installation, which uses the conda solver to find all the dependencies with appropriate version numbers, and then copy the appropriate packages using `anaconda copy`.

You can run this locally:

>  python get_deps.py

_See [anacopy.yml](.github/workflows/anacopy.yml) for the full workflow._



---

TODO: relate these to the table above?
TODO: mention this?

Copies the following (and their dependencies) from conda-forge, nvidia, rapids, and fastai channels to the fastchan channel: cudf cudatoolkit mamba pytorch torchvision transformers rich sentencepiece fastai timm conda-forge nbdev fastrelease ghapi fastcgi.

