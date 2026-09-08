def copy_file(command: str) -> None:
    command_parts = command.split()

    if len(command_parts) != 3 or command_parts[0] != "cp":
        return

    source_file_name = command_parts[1]
    destination_file_name = command_parts[2]

    if source_file_name == destination_file_name:
        return

    try:
        with open(source_file_name, "r") as source_file_object, open(
            destination_file_name, "w"
        ) as destination_file_object:
            destination_file_object.write(source_file_object.read())
    except FileNotFoundError:
        return
