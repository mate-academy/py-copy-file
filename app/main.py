def copy_file(command: str) -> None:
    split_command = command.split()

    if len(split_command) != 3:
        return None

    command_name, source_file, destination_file = split_command

    try:
        if command_name != "cp" or source_file == destination_file:
            return None

        with (open(source_file, "r") as current_file,
              open(destination_file, "w") as new_file):
            new_file.write(current_file.read())
    except FileNotFoundError:
        return None
