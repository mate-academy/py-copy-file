def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        return

    if parts[0] != "cp":
        return
    source = parts[1]
    target = parts[2]
    if source == target:
        return

    try:
        with open(source, "r") as src, open(target, "w") as dst:
            dst.write(src.read())
    except FileNotFoundError:
        return
