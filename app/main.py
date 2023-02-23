def copy_file(command: str) -> None:
    name_of_file = command.split()
    if name_of_file[0] != "cp" or name_of_file[1] == name_of_file[2]:
        return

    from shutil import copyfile

    copyfile(name_of_file[1], name_of_file[2])
