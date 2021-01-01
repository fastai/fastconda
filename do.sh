#!/usr/bin/env bash

bash get_deps.sh
python get_specs.py > dep_data/specs.txt
parallel -a dep_data/specs.txt anaconda -t $FASTCHAN copy

