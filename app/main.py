def copy_file(command: str) -> None:
    command = command.split()
    file_copy = command[1]
    file_paste = command[2]
    if file_copy == file_paste:
        return
    with open(file_copy, "r") as file_in, open(file_paste, "w") as file_out:
        file_out.write(file_in.read())
