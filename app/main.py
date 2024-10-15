import os


def copy_file(command: str) -> None:
    command_parts = command.split()
    source_file = str(command_parts[1])
    destination_file = str(command_parts[2])
    if not os.path.exists(source_file):
        return
    if source_file == destination_file:
        return
    with open(source_file, "r") as file_in, open(destination_file, "w") as file_out:
        file_out.write(file_in.read())
