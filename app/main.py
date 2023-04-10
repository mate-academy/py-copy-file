def copy_file(command: str) -> None:
    command_split = command.split()
    if len(command_split) != 3:
        return
    command, source_path, destination_path = command_split
    if command != "cp" or source_path == destination_path:
        return
    with \
            open(source_path, "r") as file_in, \
            open(destination_path, "w") as file_out:
        file_out.write(file_in.read())
