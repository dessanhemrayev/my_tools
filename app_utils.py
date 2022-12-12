import os
 # os.system(f'cd foor_git/{module} && git init')
# os.system(f'COPY ".gitignore" foor_git\{module}')
# os.system(f'MOVE foor_git\{module} upload')

def clone_module(path,repo,module):
    """ Clones a module from github """
    os.system(f'cd {path} && git clone git@gitlab.com:{repo}/{module}.git')
