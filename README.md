# fastconda
Get packages onto your conda channel faster

## Usage

### Step 1: Configure Settings
Configure settings in [settings.ini](settings.ini).

### Step 2: Copy Anaconda Repos

> ./get_deps.sh {python version number}

For example

```
> ./get_deps.sh 3.7

Copying dependencies for: sentencepiece transformers rich timm
Channels searched: -c defaults -c conda-forge
Python version: 3.7
Logs available in: dep_data/logs-tmp-3.7.txt
Dependency metadata available in: dep_data/inst-3.7.json

============================================
Creating python 3.7 environment...
Installing mamba & fastcore...
Solving for dependencies and writing to dep_data/inst-3.7.json
Copying conda packages from dep_data/inst-3.7.json to fastai channel...
    copying conda-forge/gperftools/2.7 to fastai
    copying conda-forge/sentencepiece/0.1.92 to fastai
    copying conda-forge/tokenizers/0.9.4 to fastai
    copying conda-forge/rich/9.6.1 to fastai
    copying conda-forge/sacremoses/0.0.43 to fastai
    copying conda-forge/timm/0.3.2 to fastai
    copying conda-forge/transformers/4.1.1 to fastai
```
