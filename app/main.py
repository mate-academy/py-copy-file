class FileNotFound(Exception):
    pass


def copy_file(command: str) -> None:
    parts_of_command = command.split()

    if len(parts_of_command) != 3:
        return

    command_name, source, destination = command.split()

    if command_name != "cp":
        return

    if source == destination:
        return

    try:
        with open(source, "r") as file_in, open(destination, "w") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
