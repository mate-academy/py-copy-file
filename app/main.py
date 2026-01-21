def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        return
    cmd, source_file, dest_file = parts
    if cmd != "cp" or source_file == dest_file:
        return
    with (open(source_file, "r") as file_in,
          open(dest_file, "w") as file_out):
        file_out.write(file_in.read())
