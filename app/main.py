def copy_file(command: str) -> None:
    parts = command.strip().split()
    if len(parts) != 3:
        return
    cmd, src, dest = parts
    if cmd != "cp" or src == dest:
        return
    try:
        with open(src, "r") as file_in, open(dest, "w") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
