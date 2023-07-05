def copy_file(command: str) -> None:
    command_parts = command.split()

    if len(command_parts) != 3:
        return

    command_line, source_path, destination_path = command_parts
    if source_path == destination_path or command_line != "cp":
        return

    with open(source_path, "r") as src, open(destination_path, "w") as dst:
        dst.write(src.read())
