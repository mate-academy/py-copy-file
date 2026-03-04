def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        return

    src = parts[1]
    dst = parts[2]

    if src == dst:
        return

    try:
        with open(src, "r", encoding="utf-8") as f_src, \
                open(dst, "w", encoding="utf-8") as f_dst:
            f_dst.write(f_src.read())
    except (FileNotFoundError, PermissionError):
        return
