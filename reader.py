
from read_directory import find_files

files_directory = 'installed.txt'


with open(files_directory,encoding='utf-8') as file:
    for line in file.readlines():
        line_modify = line.strip()
        if len(line_modify):
            find_files(f'test/{line_modify}',f"{line_modify}.txt")
            print(line_modify)
