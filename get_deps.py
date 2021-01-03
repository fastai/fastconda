#!/usr/bin/env python
from fastcore.all import *

tok = os.getenv('FASTCHAN')
def inst(s, bin='mamba'): return dict2obj(loads(run(f'{bin} install --json -qyc {s}'))).actions.LINK
def anacopy(nm):
    code,out = run(f'anaconda -t {tok} copy {nm}', ignore_ex=True)
    if out.strip(): print(out.strip())

links = L(inst('defaults -c conda-forge mamba', 'conda'))
if sys.version_info[:2]!=(3,6):
    links += inst("rapidsai -c nvidia -c defaults -c conda-forge 'cugraph>=0.17' 'cudf>=0.17' 'cuml>=0.17' 'cudatoolkit>=11'")
links += L(
    "pytorch -c defaults -c conda-forge 'pytorch>=1.7' torchvision",
    "defaults -c conda-forge transformers sentencepiece rich albumentations mamba",
    "fastai -c defaults -c conda-forge fastai timm",
    "fastai -c defaults -c conda-forge nbdev fastbook fastgpu fastrelease ghapi fastcgi fastdot"
).map(inst).concat()
nms = L(f'{o.channel}/{o.name}/{o.version}' for o in links if o.channel != 'pkgs/main')
parallel(anacopy, nms, n_workers=4)

