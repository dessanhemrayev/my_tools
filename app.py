import os
path = ""
content = os.listdir(path)
for module in content:
    # os.system(f'cd foor_git/{module} && git init')
    os.system(f'COPY ".gitignore" foor_git\{module}')
