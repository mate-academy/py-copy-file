def copy_file(command: str) -> None:
    command_arr = command.split()
    if command == "":
        return
    if len(command_arr) != 3:
        return
    cp, file, file_copy = command_arr
    if cp != "cp":
        return
    if file == file_copy:
        return
    try:
        with open(file, "r") as file1, open(file_copy, "w") as file_copy1:
            file_copy1.write(file1.read())
    except FileNotFoundError:
        return
