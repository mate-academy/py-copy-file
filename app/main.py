def copy_file(command: str) -> None:
    parts = command.split()
    source_file, destination_file = parts[1:]
    if len(parts) != 3 or parts[0] != "cp" or source_file == destination_file:
        return

    with (open(source_file, "r") as file_in,
          open(destination_file, "w") as file_out):
        file_out.write(file_in.read())
