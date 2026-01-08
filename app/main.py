def copy_file(command: str) -> None:
    split = command.split(" ")
    if len(split) != 3:
        return
    cp, file1, file2 = split

    if cp != "cp":
        return
    elif file1 == file2:
        return
    else:
        try:
            with open(file1, "r") as original, open(file2, "w") as copy:
                copy.write(original.read())
        except FileNotFoundError:
            pass




