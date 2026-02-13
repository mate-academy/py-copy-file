def copy_file(command: str) -> None:
    command_parts = command.split()

    if len(command_parts) != 3 or command_parts[0] != "cp":
        return

    source_file = command_parts[1]
    destination_file = command_parts[2]

    if source_file == destination_file:
        return

    try:
        with open(source_file, "r") as source_file_object, \
             open(destination_file, "w") as destination_file_object:
            destination_file_object.write(source_file_object.read())
    except FileNotFoundError:
        pass
