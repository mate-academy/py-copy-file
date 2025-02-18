def copy_file(command: str) -> None:
    args = command.split()

    if len(args) < 3:
        return

    cmd, file1, file2 = args

    if cmd != "cp":
        return

    if file1 == file2:
        return

    try:
        with open(file1, "r") as file_in, open(file2, "w") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
