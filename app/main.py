def copy_file(command: str) -> None:
    command_parts = command.split()

    if len(command_parts) != 3:
        raise ValueError("Command must consist of three parts: action,"
                         " source filename, and destination filename")

    action, source_filename, destination_filename = command_parts
    if action != "cp" or source_filename == destination_filename:
        raise ValueError("The action must be 'cp'")

    with (open(source_filename, "r") as source_file,
          open(destination_filename, "r") as destination_file):
        destination_file.write(source_file.read())
