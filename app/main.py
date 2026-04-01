def copy_file(command: str) -> None:
    parts = (command.split())
    if len(parts) != 3:
        return

    cp, file_txt, file_copy = parts
    if cp != "cp":
        return

    if file_txt == file_copy:
        return

    try:
        with open(file_txt, "r") as file_in, open(file_copy, "w") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
