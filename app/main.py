def copy_file(command: str) -> None:
    parts = command.split()
    source_file, dest_file = parts[1], parts[2]

    if source_file != dest_file:
        with (open(source_file, "r") as file_in,
             open(dest_file, "w") as file_out):
            file_out.write(file_in.read())
