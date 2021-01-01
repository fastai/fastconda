#! /bin/bash -i
set -eou pipefail
deps=`sed -nr "/^\[DEFAULT\]/ { :l /^deps[ ]*=/ { s/.*=[ ]*//; p; q;}; n; b l;}" ./settings.ini`
py=$1
cenv=tmp-$py
dest="dep_data/inst-$py.json"
logs="dep_data/logs-$cenv.txt"

echo "Copying dependencies for: $deps"
echo "Logs available in: $logs"
echo "Dependency metadata available in: $dest"
printf "\n============================================\n"

echo "Creating python $py environment..."
    conda create -yn $cenv python==$py > $logs
    conda activate $cenv
echo "Installing mamba & fastcore..."
    conda install -y -c conda-forge mamba >> $logs
    pip install fastcore >> logs
echo "Solving for dependencies and writing to $dest"
    mamba install -c defaults -c conda-forge -d $deps --json > $dest
echo "Copying conda packages from $dest to fastai channel..."
    python copydeps.py $dest
