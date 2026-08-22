import os


def copy_file(command: str) -> None:
    command_parts = command.split()

    if len(command_parts) != 3:
        return

    operation, source, destination = command_parts

    if (
        operation != "cp"
        or source == destination
        or not os.path.isfile(source)
    ):
        return

    with open(source, "r") as file_in, open(destination, "w") as file_out:
        file_out.write(file_in.read())
