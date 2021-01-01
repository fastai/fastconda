from fastcore.all import *
from configparser import ConfigParser

cfg = ConfigParser()
cfg.read('settings.ini')
cfg['DEFAULT']['deps']
ignore_channels = cfg['DEFAULT']['ignore_channels'].split()

def read_dep(f:str):
    "Reads in json output from mamba dry run. Cleans json file of artifacts before reading."
    f = L(Path(f).readlines())
    bidx = f.argwhere(lambda x: x == '{\n')[0]
    eidx = f.argwhere(lambda x: x == '}\n')[0]+1
    deps = dict2obj(loads(''.join(f[bidx:eidx])))
    assert deps.success, "Was not able to determine dependencies."
    return deps

def copy_spec(s):
    print(f'copying {s}')
    run(f'anaconda copy --to-label fastchan {s}', ignore_ex=True)

@call_parse
def main(filename:Param("filename",str)):
    deps = read_dep(filename)
    specs = (deps.actions.LINK.filter(lambda x: x.channel not in ignore_channels)
             .map(lambda x: f'{x.channel}/{x.name}/{x.version}'))
    for s in specs: copy_spec(s)
