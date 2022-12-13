import os

from app_utils import merge_files

path = "files"
content_upload = []

# with open(path, encoding="utf-8") as file:
#     for line in file.readlines():
#         line_modify = line.strip()
#         if len(line_modify):
#             content_upload.append(line_modify)
#             print(line_modify)
count = 0
for filename in os.scandir(path):
    count += 1
    merge_files(filename.path)
    print(count)
