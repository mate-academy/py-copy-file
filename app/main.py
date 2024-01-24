def copy_file(command: str) -> None:
    file1, file2 = command[3:].split(" ")

    if file1 == file2:
        return

    with open(file1, "r") as r, open(file2, "a") as a:
        a.write(r.read())


copy_file("cp text1.txt text1.txt")
