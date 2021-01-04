from ghapi.all import *
from fastcore.all import *
from packaging import version

@call_parse
def get_new_gh_tag(ghowner:Param('GitHub Owner', str)='rwightman', 
                   ghrepo:Param('GitHub Repo', str)='pytorch-image-models', 
                   achan:Param('Anaconda Channel', str)='fastai', 
                   apkg:Param('Anaconda Package', str)='timm',
                   force:Param('Return the github tag no matter what.', store_true)=False):
    "Returns GitHub tag only if a newer release exists compared to an Anaconda Repo."
    ghtagnm = GhApi().repos.get_latest_release(ghowner, repo=ghrepo).tag_name
    ghtag = version.parse(ghtagnm)
    condavs = L(loads(run(f'mamba repoquery search {apkg} -c {achan} --json'))['result']['pkgs'])
    condatag = max(condavs.attrgot('version').map(version.parse))
    if ghtag > condatag or force: print(ghtagnm)
