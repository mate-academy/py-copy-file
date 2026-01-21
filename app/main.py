def copy_file(command: str) -> None:
    command, old_file, new_file = command.split()
    if old_file == new_file or command != "cp":
        return
    with (open(old_file, "r") as read_file,
          open(new_file, "w") as write_file):
        write_file.write(read_file.read())
