def copy_file(command: str) -> None:
    cmd, existing_file, new_file = command.split()

    if existing_file == new_file or cmd != "cp":
        return

    with (open(existing_file, "r") as f_read,
          open(new_file, "w") as f_write):
        content = f_read.read()
        f_write.write(content)
