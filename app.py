import os

from app_utils import clone_module

path = ""
content_upload = []

with open(path, encoding="utf-8") as file:
    for line in file.readlines():
        line_modify = line.strip()
        if len(line_modify):
            content_upload.append(line_modify)
            print(line_modify)
count = 0
for module in content_upload:
    count += 1
    clone_module('iert_project',module)
    print(count)
