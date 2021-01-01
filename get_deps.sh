#! /bin/bash -i
set -eou pipefail
deps=`echo $(cat conda_deps.txt)`

py=$1
cenv=tmp-$py
conda create -yn $cenv python==$py
conda activate $cenv
conda install -y -c conda-forge mamba
mamba install -c defaults -c conda-forge -d $deps --json > "dep_data/inst-$py.json"

# for py in 3.7; do
#     cenv=tmp-$py
#     conda create -yn $cenv python==$py
#     conda activate $cenv
#     conda install -y -c conda-forge mamba
#     mamba install -c defaults -c conda-forge -d $deps --json > inst-$py.json
# done

