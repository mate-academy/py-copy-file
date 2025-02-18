def copy_file(command: str) -> None:
    command, source_file, destination_file = command.split()

    if command != "cp":
        raise ValueError("Invalid command format. "
                         "Use: 'cp source_file destination_file'")

    if source_file == destination_file:
        return

    with (open(source_file, "r") as file_in,
          open(destination_file, "w") as file_out):
        file_out.write(file_in.read())
