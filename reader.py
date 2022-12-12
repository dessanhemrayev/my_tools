with open("list_modules.txt") as file:
    for line in file.readlines():
        line_modify = line.strip()
        if len(line_modify):
            print(line_modify)
