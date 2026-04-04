def copy_file(command: str) -> None:
    parts = command.split(maxsplit=2)
    if len(parts) != 3:
        return
    cmd, source, dest = parts
    if cmd != "cp":
        return
    if source == dest:
        return
    try:
        with open(source, "r") as src, open(dest, "w") as dst:
            dst.write(src.read())
    except FileNotFoundError:
        return
