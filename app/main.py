from shutil import copyfileobj


def copy_file(command):
    data = command.split()
    if data[0] == 'cp':
        with open(f"{data[1]}.txt", "r") as file_in, \
             open(f"{data[2]}.txt", "w") as file_out:
            copyfileobj(file_in, file_out)
