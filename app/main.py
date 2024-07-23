def copy_file(command: str) -> None:
    cmd, source_filename, destination_filename = command.split()
    if source_filename == destination_filename:
        return
    with (open(source_filename, "r") as file_in,
          open(destination_filename, "w") as file_out):
        content = file_in.read()
        file_out.write(content)
