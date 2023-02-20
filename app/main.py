def copy_file(command: str) -> None:
    name_of_file = command.split()
    if name_of_file[1] == name_of_file[2] or name_of_file[1][-4:] != ".txt":
        return

    from shutil import copyfile

    copyfile('first.txt', 'second.txt')
