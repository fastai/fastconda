#!/usr/bin/env bash

parallel ./get_specs.sh ::: 3.6 3.7 3.8

