import os


def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3:
        return

    cp_command, source, destination = parts

    if cp_command != "cp":
        return

    if source == destination:
        return

    if not os.path.exists(source):
        return

    with open(source, "r") as file_in, open(destination, "w") as file_out:
        file_out.write(file_in.read())
