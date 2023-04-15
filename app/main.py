def copy_file(command_line: str) -> None:
    info = command_line.split()
    if len(info) != 3:
        return
    command, old_file, new_file = info
    if old_file == new_file or command != "cp":
        return
    with open(old_file, "r") as file_in, open(new_file, "w") as file_out:
        file_out.write(file_in.read())
