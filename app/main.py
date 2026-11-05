def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    file1 = parts[1]
    file2 = parts[2]

    if file1 == file2:
        return

    try:
        with (open(file1, "r") as f1,
              open(file2, "w") as f2):
            f2.write(f1.read())
    except FileNotFoundError:
        pass
