import os

import subprocess


content = os.listdir('foor_git')
for module in content:
    # os.system(f'cd foor_git/{module} && git init')
    os.system(f'COPY ".gitignore" foor_git\{module}')