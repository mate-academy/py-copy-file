from __future__ import annotations


def copy_file(command: str) -> None:
    parts = command.split()

    # Expected format: cp <source> <destination>
    if len(parts) != 3:
        return

    cmd, source, destination = parts
    if cmd != "cp":
        return

    if source == destination:
        return

    try:
        with open(source, "r") as file_in, open(destination, "w") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        # Missing source file -> no action
        return
