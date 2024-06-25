def copy_file(command: str) -> None:
    files = command.split(" ")
    if len(files) != 3 or files[0] != "cp":
        return

    file1 = files[1]
    file2 = files[2]

    if file1 == file2:
        return
    else:
        with open(file1, "r") as f, open(file2, "w") as f2:
            content = f.read()
            f2.write(content)
