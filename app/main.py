def copy_file(command: str) -> None:
    files = command.split(" ")
    if len(files) != 3 or files[0] != "cp":
        return

    _, file1, file2 = files

    if file1 == file2:
        return
    with open(file1, "r") as f, open(file2, "w") as f2:
        f2.write(f.read())
