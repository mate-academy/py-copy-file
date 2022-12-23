def copy_file(command: str) -> None:
    cp, file, file_copy = command.split()
    if cp != "cp":
        return
    if file == file_copy:
        return
    with open(file, "r") as f1, open(file, "w") as f2:
        for line in f1:
            f2.write(line)
