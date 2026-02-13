import os


def copy_file(command: str) -> None:

    if command == "":
        return
    parts = command.split()
    if len(parts) < 3:
        return
    if parts[0] != "cp":
        return
    source = parts[1]
    destination = parts[2]

    if not os.path.exists(source) or source == destination:
        return
    with open(source, "r") as file_in, open(destination, "w") as file_out:
        file_out.write(file_in.read())
