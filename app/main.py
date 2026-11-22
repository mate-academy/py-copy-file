def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    _, file_in_name, file_out_name = parts

    if file_in_name == file_out_name:
        return

    try:
        with open(file_in_name, "r") as file_in, \
                open(file_out_name, "w") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
