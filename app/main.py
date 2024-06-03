def copy_file(command: str) -> None:
    parts = command.split()
    old_file, new_file = parts[1], parts[2]
    if old_file != new_file:
        with (open(old_file, "r") as file_in,
              open(new_file, "w") as file_out):
            file_out.write(file_in.read())
