def copy_file(command: str) -> None:
    command_parts = command.split()

    if len(command_parts) != 3:
        return

    action, source_filename, destination_filename = command_parts
    if action != "cp" or source_filename == destination_filename:
        raise f"You have an error"

    with (open(source_filename, "r") as source_file,
          open(destination_filename, "r") as destination_file):
        destination_file.write(source_file.read())
