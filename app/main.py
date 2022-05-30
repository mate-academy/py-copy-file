from shutil import copy


def copy_file(command: str):
    copy(command.split()[1], command.split()[2])
