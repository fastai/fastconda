#! /bin/bash -i
set -eou pipefail
get_setting() {
   section=$1
   var=$2
   echo `sed -nr "/^\[$section\]/ { :l /^$var[ ]*=/ { s/.*=[ ]*//; p; q;}; n; b l;}" ./settings.ini`
}

channel_cmd() {
    channels="$@"
    cmd=""
    for c in $channels; do
        cmd="$cmd -c $c"
    done;
    echo $cmd
}

deps=`get_setting DEFAULT deps`
channels=`get_setting DEFAULT install_channels`
conda_channels=`channel_cmd $channels`

py=$1
cenv=tmp-$py
dest="dep_data/inst-$py.json"
logs="dep_data/logs-$cenv.txt"

echo "Copying dependencies for: $deps"
echo "Channels searched: $conda_channels"
echo "Python version: $py"
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
    mamba install $conda_channels -d $deps --json > $dest
echo "Copying conda packages from $dest to fastai channel..."
    python copydeps.py $dest
