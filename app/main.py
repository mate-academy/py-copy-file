def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        return

    _, file_name_from, file_name_to = parts

    if file_name_from == file_name_to:
        return

    try:
        with open(file_name_from, "r") as file_in, \
                open(file_name_to, "w") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        pass
