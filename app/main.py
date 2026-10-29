import os


def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    _, file_in, file_out = parts

    if file_in == file_out or not os.path.exists(file_in):
        return

    with open(file_in, "r") as file_in, open(file_out, "w") as file_out:
        file_out.write(file_in.read())
