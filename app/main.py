from shutil import copy


def copy_file(command: str) -> None:
    _, filename1, filename2 = command.split()
    if filename1 != filename2:
        copy(filename1, filename2)
