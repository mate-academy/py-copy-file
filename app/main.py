def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    _, file_1, file_2 = parts

    if file_1 == file_2:
        return

    try:
        with open(file_1, "r") as file_in, open(file_2, "w") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
