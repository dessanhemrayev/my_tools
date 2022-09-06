import os
path = ""
content = os.listdir(path)
content_upload = []
for module in content:
    # os.system(f'cd foor_git/{module} && git init')
    # os.system(f'COPY ".gitignore" foor_git\{module}')
    # os.system(f'MOVE foor_git\{module} upload')
    os.system(f'git clone {module}')
