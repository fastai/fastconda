#!/bin/bash
while true; do
    echo "Saving container $(date)"
    docker commit compassionate_cerf hamelsmu/linux-conda-dev 
    sleep 60
done
