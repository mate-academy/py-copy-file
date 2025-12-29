def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        return

    ma_file = parts[1]
    copied_file = parts[2]

    try:
        with open(ma_file, "r") as file1, open(copied_file, "w") as file2:
            data = file1.read()
            file2.write(data)
    except FileNotFoundError:
        return
