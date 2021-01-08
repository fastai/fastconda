#!/usr/bin/env python
from fastcore.all import *

def inst(s, bin='mamba'):
    print('***', bin, s)
    out = run(f'{bin} install --strict-channel-priority --json -qy {s}')
    try: res = dict2obj(loads(out))
    except:
        print(res)
        raise
    return nested_attr(res, 'actions.LINK')

tok = os.getenv('FASTCHAN')
def anacopy(nm):
    code,out = run(f'anaconda -t {tok} copy {nm}', ignore_ex=True)
    if out.strip(): print(out.strip())

links = L(inst('defaults -c conda-forge mamba', 'conda'))
if sys.version_info[:2]!=(3,6):
    links += inst("-c rapidsai -c nvidia -c defaults -c conda-forge 'cudf>=0.17' 'cudatoolkit>=11' mamba")
links += L(
    "boa rich",
    "'pytorch>=1.7' torchvision transformers",
    "sentencepiece fastai timm",
    "nbdev fastrelease ghapi fastcgi"
).map(inst).concat()

nms = L(f'{o.channel}/{o.name}/{o.version}' for o in links if o.channel != 'pkgs/main')
print('***',nms)
inst('defaults -c conda-forge anaconda-client')
parallel(anacopy, nms, n_workers=4)

