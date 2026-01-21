from typing import Any


def copy_file(command: str) -> Any:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    _, source_path, destination_path = parts
    if source_path == destination_path:
        return True
    try:
        with (open(source_path, "r") as file_in,
              open(destination_path, "w") as file_out):
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
