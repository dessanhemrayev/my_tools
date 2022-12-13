import os


ignore_files = ['.git', '.gitignore','README.md','i18n']
ignore_types = ['jpg','png','mp4','pyc','OTF','ttf','webm']


def find_files(path_module:str, file_name):
    """ Find all files """
    for filename in os.scandir(path_module):
        if filename.name not in ignore_files:
            if filename.is_file():
                print(filename.path)
                if check_file(filename.path):
                    with open(file_name, encoding="utf-8", mode='a') as fp:
                        opened_file = ''
                        with open(filename.path,encoding="utf-8",mode='r') as file:
                            opened_file= file.read()
                        fp.write(filename.path + '\n')
                        fp.write(opened_file + '\n')
            else:
                find_files(filename,file_name)
def check_file(file):
    return file.split('.')[-1] not in ignore_types



