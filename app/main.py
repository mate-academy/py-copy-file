def copy_file(command: str) -> None:
    if len(command.split()) != 3:
        return
    command, file1, file2 = command.split(" ")
    if file1 == file2 or command != "cp":
        return
    with open(file1, "r") as f1, open(file2, "w") as f2:
        f2.write(f1.read())
