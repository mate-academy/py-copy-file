def copy_file(command: str) -> None:
    try:
        command_for_run, source_file, destination = command.split(" ")
    except ValueError:
        return None

    if source_file == destination or command_for_run != "cp":
        return None

    try:
        with open(source_file, "r") as file_in, \
                open(destination, "w") as file_out:
            content = file_in.read()
            file_out.write(content)
    except FileNotFoundError:
        return None
    except PermissionError:
        return None
