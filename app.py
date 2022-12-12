import os

path = ""
content = os.listdir(path)
content_upload = []

with open("not_inst.txt") as file:
    for line in file.readlines():
        line_modify = line.strip()
        if len(line_modify):
            content_upload.append(line_modify)
            print(line_modify)
count = 0
for module in content_upload:
    # os.system(f'cd foor_git/{module} && git init')
    # os.system(f'COPY ".gitignore" foor_git\{module}')
    # os.system(f'MOVE foor_git\{module} upload')
    print(f"Download {module}")
    # os.system(f'cd upload_git && git clone git@gitlab.com:{repo}/{module}.git')
    if module in content:
        count += 1
        os.system(f"mv {path}/{module} new_add/{module}")
        print(count)
