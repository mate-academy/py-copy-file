import os


def copy_file(command: str) -> None:
    name = command.split()
    if not command or len(name) != 3:
        return
    elif not os.path.exists(name[1]):
        return
    elif name[0] != "cp":
        return
    elif name[1] == name[2]:
        return
    with open(name[1], "r") as file_in, open(name[2], "w") as file_out:
        file_out.write(file_in.read())
