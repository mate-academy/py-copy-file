def copy_file(command: str) -> None:
    command_parts = command.split()
    source_file, destination_file = command_parts[1], command_parts[2]

    if source_file != destination_file:
        with (
            open(source_file, "r") as source,
            open(destination_file, "w") as destination
        ):
            destination.write(source.read())
