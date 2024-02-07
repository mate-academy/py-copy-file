def copy_file(command: str) -> bool:
    command_name, source_file, destination_file, *_ = command.split()

    if command_name != "cp" or source_file == destination_file:
        return False

    with (open(source_file, "r") as file_in,
          open(destination_file, "w") as file_out):
        file_out.write(file_in.read())
