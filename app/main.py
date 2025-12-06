def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    _, file_name1, file_name2 = parts

    if file_name1 == file_name2:
        return

    try:
        with open(file_name1, "r") as file1, open(file_name2, "w") as file2:
            file2.write(file1.read())
    except FileNotFoundError:
        pass
