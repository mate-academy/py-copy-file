def copy_file(command: str) -> None:
    cmnd, file, new_file = command.split()
    if file == new_file or cmnd != "cp":
        return

    with (open(file, "r") as file_to_read,
          open(new_file, "w") as file_to_write):
        file_to_write.write(file_to_read.read())
