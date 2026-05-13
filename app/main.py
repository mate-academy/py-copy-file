def copy_file(command: str) -> None:
    command_parts = command.split()

    if len(command_parts) != 3:
        return None

    cmd, source_file_name, new_file_name = command_parts

    if cmd != "cp":
        return None

    if source_file_name == new_file_name:
        return None

    try:
        with open(source_file_name, "r") as source_file, \
             open(new_file_name, "w") as new_file:
            for line in source_file:
                new_file.write(line)
    except FileNotFoundError:
        return None
