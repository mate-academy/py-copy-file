def copy_file(command: str) -> None:
    command_parts = command.split()
    if len(command_parts) != 3 or command_parts[0] != "cp":
        return

    _, source_file_name, target_file_name = command_parts
    if source_file_name == target_file_name:
        return

    try:
        source_file = open(source_file_name, "r")
    except FileNotFoundError:
        return

    with source_file, open(target_file_name, "w") as target_file:
        target_file.write(source_file.read())
