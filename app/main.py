def copy_file(command: str) -> None:
    parts = command.split()
    file_name = parts[1]
    file_copy_name = parts[2]
    if file_name == file_copy_name:
        return
    with (open(file_name, "r") as file_in,
          open(file_copy_name, "w") as file_out):
        file_out.write(file_in.read())
