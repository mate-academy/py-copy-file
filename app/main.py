def copy_file(command: str) -> None:
    old_file = command.split()
    com, old_file, new_file = old_file
    if old_file[1] == new_file[2] or com[0] != "cp":
        return
    with (open(old_file[1], "r") as file_in,
          open(new_file[2], "w") as file_out):
        file_out.writelines(file_in.read())
