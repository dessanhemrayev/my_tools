import os


ignore_files = ['.git', '.gitignore','README.md']

def find_files(path_module:str):
    """ Find all files """
    for filename in os.scandir(path_module):
        if filename.name not in ignore_files:
            if filename.is_file():
                print(filename.path)
                with open(f'{path_module}.txt', encoding="utf-8", mode='a') as fp:
                    opened_file = ''
                    with open(filename.path,encoding="utf-8",mode='r') as file:
                        opened_file= file.read()
                    fp.write(filename.path + '\n')
                    fp.write(opened_file + '\n')
            else:
                find_files(filename)
