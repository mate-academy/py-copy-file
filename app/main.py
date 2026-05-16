import os


def copy_file(command: str) -> None:

    parts = command.split()
    if len(parts) != 3:
        return

    command_name, source_file, destination_file = parts

    if source_file == destination_file:
        return
    if command_name != "cp":
        return
    if not os.path.exists(source_file):
        return

    with (open(source_file, "r") as file_in,
          open(destination_file, "w") as file_out):
        source_file_data = file_in.read()
        file_out.write(source_file_data)
