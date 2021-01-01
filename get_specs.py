#!/usr/bin/env python
from fastcore.utils import *

txt = Path('dep_data/inst-3.8.json').read_text()
links = concat(o.actions.LINK for o in dict2obj(list(loads_multi(txt))))
for o in links:
    if o.channel != 'pkgs/main' and o.name != 'matplotlib': print(f'{o.channel}/{o.name}/{o.version}')

