def copy_file(command: str) -> None:
    command_parts = command.split()
    if len(command_parts) != 3 or command_parts[0] != 'cp':
        return

    _, source_file, dest_file = command_parts

    if source_file == dest_file:
        return

    with open(source_file, "r") as file_in, open(dest_file, "w") as file_out:
        file_out.write(file_in.read())
