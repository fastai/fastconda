#!/usr/bin/env bash

bash get_deps.sh $1
python get_specs.py "dep_data/inst-$1.json" > dep_data/specs-$1.txt
parallel -j4 -a dep_data/specs-$1.txt anaconda -t $FASTCHAN copy || true;

