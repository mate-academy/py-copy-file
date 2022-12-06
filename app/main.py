import shutil


def copy_file(command: str) -> None:
    command = command.split()
    with open(command[1], "r"), open(command[2], "a"):
        if f"{command[1]}" != f"{command[2]}" and command[0] == "cp":
            shutil.copyfile(f"{command[1]}", f"{command[2]}")
