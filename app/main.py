def copy_file(command: str) -> None:
    commands = command.split()

    command_name, source_file, destination_file = commands

    if source_file == destination_file:
        return

    with (open(source_file, "r") as file_in,
          open(destination_file, "w") as file_out):
        file_out.write(file_in.read())
