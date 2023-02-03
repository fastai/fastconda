#!/usr/bin/env python
from fastcore.all import *
import platform

def inst(s, bin='mamba'):
    cmd = f'{bin} install --json -qy {s}'
    #cmd = f'{bin} install --strict-channel-priority --json -qy {s}'
    print('***', cmd)
    out = run(cmd)
    try: res = dict2obj(loads(out))
    except:
        print(out)
        raise
    #print('---', out)
    return nested_attr(res, 'actions.LINK')

tok = os.getenv('FASTCHAN')
def anacopy(nm):
    if nm.startswith('python'): return
    code,out = run(f'anaconda -t {tok} copy {nm}', ignore_ex=True)
    if out.strip(): print(out.strip())

if __name__=='__main__':
    chans = '-c pytorch -c fastai -c conda-forge'
    links = L([]) #L(inst('mamba', 'conda'))
    if platform.system() in ('Linux','Windows'):
        links += inst(f"{chans} 'cudatoolkit>=11'")
    #    links += inst("-c rapidsai -c nvidia -c defaults -c conda-forge 'cudf>=0.17' 'cudatoolkit>=11' mamba")
    links += L(
        f"{chans} mamba boa rich anaconda-client",
        f"{chans} 'pytorch>=1.7' torchaudio 'torchvision>0.7' pynvml",
        f"{chans} 'transformers>4.12' datasets accelerate",
        f"{chans} sentencepiece 'spacy>=3.1' fastai timm",
        f"{chans} nbdev fastrelease ghapi fastcgi fastbook",
        f"{chans} albumentations",
        # f"{chans} setuptools-conda"
        # "-c labscript-suite -c defaults setuptools-conda"
    ).map(inst).concat()

    nms = L(f'{o.channel}/{o.name}/{o.version}' for o in links if o.channel != 'pkgs/main')
    print('***',nms)
    parallel(anacopy, nms, n_workers=4)
