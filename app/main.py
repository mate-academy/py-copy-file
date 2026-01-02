def copy_file(command: str) -> None:
    files = command.split()
    if len(files) != 3 or files[0] != "cp":
        return
    _, file, file_copy = files
    if file == file_copy:
        return
    try:
        with open(file, "r") as file1, open(file_copy, "w") as file2:
            file2.write(file1.read())
    except FileNotFoundError:
        return
