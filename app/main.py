from __future__ import annotations


def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3:
        return

    operation, source, destination = parts

    if operation != "cp":
        return

    if source == destination:
        return

    with open(source, "r", encoding="utf-8") as file_in, open(
        destination, "w", encoding="utf-8"
    ) as file_out:
        file_out.write(file_in.read())
