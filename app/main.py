def copy_file(command: str) -> None:
    parts = command.split()

    # Expect command format: cp source dest
    if len(parts) != 3:
        return

    cmd, src, dst = parts

    # Do nothing if it's not cp
    if cmd != "cp":
        return

    # Do nothing if names are the same
    if src == dst:
        return

    try:
        with open(src, "r") as file_in, open(dst, "w") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        # Silently do nothing if source file doesn't exist
        return
