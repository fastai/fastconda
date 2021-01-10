from ghapi.all import *
from fastcore.all import *
from packaging import version
from fastrelease.conda import *

@call_parse
def new_gh_tag(nm:Param('Package name on pypi', str),
               pre:Param('Tag prefix', str)='',
               achan:Param('Anaconda Channels', str)='',
               apkg:Param('Anaconda Package', str)=None,
               force:Param('Return the github tag no matter what.', store_true)=False):
    "Prints GitHub tag only if a newer release exists on Pypi compared to an Anaconda Repo."
    pypitag = latest_pypi(nm)
    condavs = L(loads(run(f'mamba repoquery search {apkg} {achan} --json'))['result']['pkgs'])
    condatag = condavs.attrgot('version').map(version.parse)
    if force or not condatag or pypitag > max(condatag): print(pre+str(pypitag))

