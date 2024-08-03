def copy_file(command: str) -> None:
    cmd, source_filename, destination_filename = command.split()
    if source_filename == destination_filename:
        return
    with (open(source_filename, "r") as file,
          open(destination_filename, "w") as file_copy):
        file_out.write(file_in.read())
