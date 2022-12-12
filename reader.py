
from read_directory import find_files

files_directory = ''


with open(files_directory,encoding='utf-8') as file:
    for line in file.readlines():
        line_modify = line.strip()
        if len(line_modify):
            find_files(line_modify)
            print(line_modify)
