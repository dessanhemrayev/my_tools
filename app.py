import os

path = ""
content = os.listdir(path)
content_upload = []

with open(path) as file:
    for line in file.readlines():
        line_modify = line.strip()
        if len(line_modify):
            content_upload.append(line_modify)
            print(line_modify)
count = 0
for module in content_upload:
    if module in content:
        count += 1
        os.system(f"mv {path}/{module} new_add/{module}")
        print(count)
