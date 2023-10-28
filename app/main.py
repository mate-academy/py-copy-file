def copy_file(command: str) -> None:
    command_parts = command.split()

    command, source, destination = command_parts
    if command != "cp" or source == destination:
        return

    with (open(command_parts[1], "r") as file_in,
          open(command_parts[2], "w") as file_out):
        file_out.write(file_in.read())
