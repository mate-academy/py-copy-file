def copy_file(command: str) -> None:
    command_parts = command.split()

    if len(command_parts) != 3:
        return

    action, source_file, destination_file = command_parts
    if action != "cp" or source_file == destination_file:
        raise

    with (open(source_file, "r") as source,
          open(destination_file, "r") as file):
        file.write(source.read())
