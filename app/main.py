def copy_file(command: str) -> None:
    _, file1, file2 = command.split(" ")
    if file1 == file2:
        return
    with open(file1, "r") as f1, open(file2, "w") as f2:
        f2.write(f1.read())
