def copy_file(command: str) -> None:
    parts = command.split()
    source_filename = parts[1]
    destination_filename = parts[2]
    if source_filename == destination_filename:
        return
    with (open(source_filename, "r") as file_in,
          open(destination_filename, "w") as file_out):
        content = file_in.read()
        file_out.write(content)
