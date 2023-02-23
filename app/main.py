from shutil import copyfile


def copy_file(command: str) -> None:
    name_of_file = command.split()
    if not (name_of_file[0] != "cp" or name_of_file[1] == name_of_file[2]):
        copyfile(name_of_file[1], name_of_file[2])
