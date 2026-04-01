def copy_file(command: str) -> None:

    if len(command.split()) != 3:
        return

    cp, file_txt, file_copy = command.split()
    if cp != "cp":
        return

    if file_txt == file_copy:
        return

    try:
        with open(file_txt, "r") as file_in, open(file_copy, "w") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
