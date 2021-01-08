#!/usr/bin/env python
from fastrelease.conda import *
from fastcore.all import *
from ghapi.actions import *
import shutil

@call_parse
def main(name:Param("Name of pypi lib",str),
         args:Param("Extra args to pass to `build`",str)=''):
    if not chk_conda_rel(name): return print('Package already up to date')
    ver = update_meta(name, f'{name}/meta.yaml.tmpl', f'{name}/meta.yaml')
    with actions_group(f'Build {name}'): print(run(f'conda mambabuild {name} {args}'))
    with actions_group(f'Upload {name}'): print(anaconda_upload(name, ver, env_token='ANACONDA_TOKEN'))

