import shutil


def copy_file(command: str) -> None:
    command_new = command.split(" ")
    if command_new[1] == command_new[2]:
        pass
    with open(command_new[1], "r"), open(command_new[2], "w"):
        shutil.copy(command_new[1], command_new[2])
