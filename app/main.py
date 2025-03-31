from typing import Any


def copy_file(command: str) -> Any:
    parts = command.split()

    if len(parts) != 3:
        return

    if parts[0] != "cp":
        return

    _, old_file, new_file = parts
    if old_file == new_file:
        return True
    try:
        with (open(old_file, "r") as file_in,
              open(new_file, "w") as file_out):
            content = file_in.read()
            file_out.write(content)
    except FileNotFoundError:
        return
