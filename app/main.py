def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        return
    _, file_in, file_out = parts
    if file_in == file_out:
        return
    try:
        with open(file_in, "r") as f_in, open(file_out, "w") as f_out:
            f_out.write(f_in.read())
    except FileNotFoundError:
        return
