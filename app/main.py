from typing import Any


def copy_file(command: str) -> Any:
    command_ls = command.split()
    if command_ls[0] != "cp":
        return "Please, write correct command"
    if command_ls[1] == command_ls[2]:
        return
    with open(command_ls[1], "r") as file_in,\
            open(command_ls[2], "w") as file_out:
        file_out.write(file_in.read())
