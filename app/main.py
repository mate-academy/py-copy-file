def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    _, src, dst = parts

    if src == dst:
        return

    try:
        with open(src, "r", encoding="utf-8") as file_in, \
             open(dst, "w", encoding="utf-8") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
