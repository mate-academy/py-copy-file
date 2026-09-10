import os


def copy_file(command: str) -> None:
    command_parts = command.split()

    if len(command_parts) != 3:
        return

    command_name, source, destination = command_parts

    if (
            command == ""
            or source == ""
            or destination == ""
            or command_name != "cp"
            or not os.path.exists(source)
    ):
        return

    if source == destination:
        return

    with open(source, "r") as file_in, open(destination, "w") as file_out:
        file_out.write(file_in.read())
