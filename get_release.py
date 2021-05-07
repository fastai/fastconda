from fastrelease.conda import *
from urllib.request import urlretrieve
from urllib.parse import urlparse
from packaging import version
from fastcore.all import *

def latest_conda(achan:str='', apkg:str=None):
    condavs = L(loads(run(f'mamba repoquery search {apkg} {achan} --json'))['result']['pkgs'])
    vers = condavs.attrgot('version').map(version.parse)
    return max(vers or [0])

@call_parse
def get_pypi_source(pypinm, 
                    dest:Param('Name of directory to place files in', str)=None,
                    achan:Param('Anaconda Channels', str)='',
                    apkg:Param('Anaconda Package', str)=None,
                    force:Param('Return the github tag no matter what.', store_true)=False):
    "Download latest source from pypi and untars to `dest` if a newer release exists on Pypi compared to an Anaconda Repo."
    dest = ifnone(dest,pypinm)
    pypi_ver,url,_ = pypi_details(pypinm)
    conda_ver = latest_conda(achan=achan, apkg=ifnone(apkg, pypinm))
    if force or not conda_ver or version.parse(pypi_ver) > conda_ver:
        with urlopen(url) as f: untar_dir(f, dest)

