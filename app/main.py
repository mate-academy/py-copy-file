def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        return
    source, dest = parts[1], parts[2]
    if source == dest:
        return
    try:
        with open(source, "r") as src, open(dest, "w") as dst:
            dst.write(src.read())
    except FileNotFoundError:
        return
