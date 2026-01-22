def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    _, src, dest = parts

    if src == dest:
        return

    try:
        with open(src, "r", encoding="utf-8") as file_in, \
             open(dest, "w", encoding="utf-8") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
