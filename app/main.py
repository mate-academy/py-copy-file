import os


def copy_file(command: str) -> None:
    command_parts = command.split()

    if len(command_parts) != 3:
        return

    cp_command, source_file, destination_file = command_parts

    if cp_command != "cp":
        return

    if source_file == destination_file:
        return

    if not os.path.exists(source_file):
        return

    with open(source_file, "r") as file_in, \
            open(destination_file, "w") as file_out:
        file_out.write(file_in.read())
