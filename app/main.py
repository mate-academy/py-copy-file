import os


def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        return
    cp, source_file_name, destination_file_name = parts
    if source_file_name == destination_file_name:
        return
    if not os.path.exists(source_file_name):
        return
    with (open(source_file_name, "r") as file_in,
          open(destination_file_name, "w") as file_out):
        file_out.write(file_in.read())
