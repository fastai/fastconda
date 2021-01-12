#!/usr/bin/env python
from pathlib import Path
import yaml
from ghapi.actions import *
from fastrelease.conda import latest_pypi, pypi_json, anaconda_upload
from fastcore.all import ifnone, patch, store_attr , compose, L, call_parse, Param, run


@patch
def wlns(self:Path, lst:list): 
    with self.open('w') as f: f.writelines(lst)

@patch
def d2yml(self:Path, d):
    yaml.SafeDumper.ignore_aliases = lambda *args : True
    # with self.open('w') as f: f.write('---\n')
    with self.open('w') as f: yaml.safe_dump(d, f, sort_keys=False)
        
@patch
def yml2d(self:Path):
    with self.open('r') as f: return yaml.safe_load(f)
        
def _mkdir(path):
    p = Path(path)
    p.mkdir(exist_ok=True, parents=True)
    return p


class CondaBuild:
    def __init__(self, pypinm, deps=None, import_nm=None, path=None):
        store_attr('pypinm,deps')
        self.import_nm = ifnone(import_nm, pypinm)
        try: self.ver = str(latest_pypi(pypinm))
        except: raise ValueError(f'package name: {pypinm} not found on pypi.')
        self.info = pypi_json(f'{pypinm}/{self.ver}')['info']
        self.path = _mkdir(ifnone(path,self.pypinm))
        self.meta ={'package': {'name': self.pypinm, 'version': self.ver},
                    'build':{'number':0, 'binary_relocation':False, 'detect_binary_files_with_prefix':False},
                    'requirements':{'host': ['pip', 'python'], 'run':['python']+list(L(self.deps))},
                    'test':{'imports': [self.import_nm], 'requires':['pip']},
                    'about':{'home':self.info['home_page'], 'summary':self.info['summary'], 'license':self.info['license']},
                    'extra':{'recipe-maintainers': ['jph00']}
                   }
        
    def create_meta(self): (self.path/'meta.yaml').d2yml(self.meta)
            
    def create_sh(self): (self.path/'build.sh').wlns(['#!/usr/bin/env bash\n','PIP_NO_INDEX=False python -m pip install -Uq $PKG_NAME'])
            
    def create_bat(self): (self.path/'bld.bat').wlns(['setlocal\n', 'set PIP_NO_INDEX=False\n','python -m pip install -Uq %PKG_NAME%'])
    
    def create_build_files(self):
        for f in [self.create_meta, self.create_sh, self.create_bat]: f()
    
    @classmethod
    def from_yaml(cls, path): 
        p = Path(path)
        assert p.is_file() and p.exists(), f"Did not find file: {path}."
        cb = L(cls(**d) for d in p.yml2d())
        for c in cb: c.create_build_files()
        return cb

@call_parse  
def main(path:Param('Path to build file', str)='build.yaml',
         args:Param("Extra args to pass to `build`",str)=''): 
    cb = CondaBuild.from_yaml(path)
    for c in cb:
        ver = c.ver
        name = c.path
        with actions_group(f'Build {name}'): print(run(f'conda build {name} {args}'))
        with actions_group(f'Upload {name}'): print(anaconda_upload(name, ver, env_token='ANACONDA_TOKEN'))
