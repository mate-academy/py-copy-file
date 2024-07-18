from typing import Any


def copy_file(command: str) -> Any:
    if len(command.split()) != 3 or command.split()[0] != "cp":
        return

    cp, old_file, new_file = command.split()

    if old_file == new_file:
        return
    elif old_file != new_file:
        with open(old_file, "r") as file_in, open(new_file, "w") as file_out:
            lines = file_in.read()
            file_out.write(lines)
