import os


def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) < 3 or parts[0] != "cp":
        return

    _, source, destination = parts[:3]

    if source == destination:
        return

    if not os.path.exists(source):
        return

    with open(source, "r", encoding="utf-8") as file_in, \
            open(destination, "w", encoding="utf-8") as file_out:
        file_out.write(file_in.read())
