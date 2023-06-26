def copy_file(command: str) -> None:
    _, source_file, dest_file = command.split()
    if source_file == dest_file:
        return
    with (open(source_file, "r") as file_in,
          open(dest_file, "w") as file_out):
        file_out.write(file_in.read())
