from __future__ import annotations


def copy_file(command: str) -> None:
    try:
        cmd, arg1, arg2 = command.split(" ")
    except ValueError:
        return None
    if cmd != "cp" or arg1 == arg2:
        return None
    try:
        with open(arg1, "r") as file_in, open(arg2, "w") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        return None
