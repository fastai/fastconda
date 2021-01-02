#!/usr/bin/env python
from fastrelease.conda import *
from fastcore.all import *

@call_parse
def main(name:Param("Name of pypi lib",str)):
    ver = update_meta(name, f'{name}/meta.yaml.tmpl', f'{name}/meta.yaml')
    with open('timm/build.log', 'w') as f:
        f.write(run('conda mambabuild timm'))
        f.write('-----------------------------------')
        f.write(anaconda_upload(name, ver, 'fastai'))

