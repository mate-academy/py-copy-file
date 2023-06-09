def copy_file(command: str) -> None:
    current_command, source_file, destination_file = command.split()
    if len(current_command) == 2 and source_file != destination_file:
        with (
                open(source_file) as source_file,
                open(destination_file, "w") as destination_file
                ):
            destination_file.write(source_file.read())
