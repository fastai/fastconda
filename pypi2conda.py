#!/usr/bin/env python
from fastrelease.conda import *
from fastcore.all import *

@call_parse
def main(name:Param("Name of pypi lib",str)):
    ver = update_meta(name, f'{name}/meta.yaml.tmpl', f'{name}/meta.yaml')
    print(run('conda mambabuild timm'))
    print('-----------------------------------')
    print(anaconda_upload(name, ver, 'fastai'))

