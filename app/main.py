def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        return

    file_from, file_to = parts[1], parts[2]
    if file_from == file_to:
        return

    try:
        with open(file_from, "r") as file_in, open(file_to, "w") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        pass
