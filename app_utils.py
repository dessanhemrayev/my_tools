import os
 # os.system(f'cd foor_git/{module} && git init')
# os.system(f'COPY ".gitignore" foor_git\{module}')
# os.system(f'MOVE foor_git\{module} upload')

def clone_module(path,repo,module):
    """ Clones a module from github """
    os.system(f'cd {path} && git clone git@gitlab.com:{repo}/{module}.git')

def merge_files(files):
    with open('file', encoding="utf-8", mode='a') as fp:
        opened_file = ''
        with open(files,encoding="utf-8",mode='r') as file:
            opened_file= file.read()
        fp.write(opened_file + '\n')