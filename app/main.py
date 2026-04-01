def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        return
    parts_command, src, dst = parts[0], parts[1], parts[2]
    if parts_command != "cp":
        return
    if src == dst:
        return
    try:
        with open(src, "r") as fsrc, open(dst, "w") as fdst:
            fdst.write(fsrc.read())
    except FileNotFoundError:
        return
