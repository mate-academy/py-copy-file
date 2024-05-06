def copy_file(command: str) -> None:
    cmd, source_file, dest_file, *_ = command.split()
    if cmd != "cp" or source_file == dest_file:
        return
    try:
        with (open(source_file, "r") as file_in,
                open(dest_file, "w") as file_out):
            file_out.write(file_in.read())
    except FileNotFoundError:
        print(f"File {source_file} not found.")
