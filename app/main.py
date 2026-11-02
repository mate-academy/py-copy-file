import os


def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        return

    _, source_file_name, destination_file_name = parts

    if source_file_name == destination_file_name or not \
            os.path.exists(source_file_name):
        return

    with open(source_file_name, "rb") as file_in, \
            open(destination_file_name, "wb") as file_out:
        file_out.write(file_in.read())
