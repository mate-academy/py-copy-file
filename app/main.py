def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        return

    if parts[0] != "cp":
        return

    _, file1, file2 = parts

    if file1 == file2:
        return

    try:
        with open(file1, "r") as f1, open(file2, "w") as f2:
            f2.write(f1.read())
    except FileNotFoundError:
        return
