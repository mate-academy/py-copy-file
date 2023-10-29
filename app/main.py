def copy_file(command: str) -> None:
    command_parts = command.split()

    if len(command_parts) != 3:
        return

    source_file, destination_file, action = command_parts

    with (open(source_file, "r") as source,
          open(destination_file, "r") as f):
        f.write(source.read())
