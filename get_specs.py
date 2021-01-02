#!/usr/bin/env python
from fastcore.all import *

@call_parse
def main(filename:Param("filename",str)):
    txt = Path(filename).read_text()
    links = concat(o.actions.LINK for o in dict2obj(list(loads_multi(txt))))
    for o in links:
        if o.channel != 'pkgs/main': print(f'{o.channel}/{o.name}/{o.version}')
