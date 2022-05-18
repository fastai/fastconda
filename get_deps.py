#!/usr/bin/env python
from fastcore.all import *
import platform

def inst(s, bin='mamba'):
    cmd = f'{bin} install --json -qy {s}'
    #cmd = f'{bin} install --strict-channel-priority --json -qy {s}'
    print(cmd)
    out = run(cmd)
    try: res = dict2obj(loads(out))
    except:
        print(out)
        raise
    #print(out)
    return nested_attr(res, 'actions.LINK')

tok = os.getenv('FASTCHAN')
def anacopy(nm):
    if nm.startswith('python') or 'mutex' in nm: return
    code,out = run(f'anaconda -t {tok} copy {nm}', ignore_ex=True)
    if out.strip(): print(out.strip())

if __name__=='__main__':
    links = L(inst('mamba', 'conda'))
    #if sys.version_info[:2] not in ((3,6),(3,9)) and platform.system()=='Linux':
    #    links += inst("-c rapidsai -c nvidia -c defaults -c conda-forge 'cudf>=0.17' 'cudatoolkit>=11' mamba")
    links += L(
        "boa rich anaconda-client",
        "'pytorch>=1.7' torchaudio 'torchvision>0.7' pynvml",
        "-c huggingface -c pytorch -c nvidia -c defaults -c conda-forge transformers datasets accelerate",
        "sentencepiece 'spacy>=3.1' fastai timm",
        "nbdev fastrelease ghapi fastcgi fastbook"
        # "-c fastai -c defaults --override-channels albumentations",
        # "-c cbillington -c defaults setuptools-conda"
    ).map(inst).concat()

    nms = L(f'{o.channel}/{o.name}/{o.version}' for o in links if o.channel != 'pkgs/main')
    print('***',nms)
    parallel(anacopy, nms, n_workers=4)
