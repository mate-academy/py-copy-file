def copy_file(command: str) -> None:

    command_parts = command.split(" ")

    if len(command_parts) != 3 or command_parts[0] != "cp":
        return

    _, source_filename, destination_filename = command_parts

    if source_filename == destination_filename:
        return

    try:
        with open(source_filename, "r", encoding="utf-8") as source_file, \
                open(destination_filename, "w", encoding="utf-8") as destination_file:
            destination_file.write(source_file.read())
    except FileNotFoundError:
        pass