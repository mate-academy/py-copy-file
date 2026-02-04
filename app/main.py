def copy_file(command: str) -> None:
    parts = command.split()
    if not (len(parts) == 3 and parts[0] == "cp"):
        return

    source, destination = parts[1], parts[2]
    if source == destination:
        return

    try:
        with open(source, "r") as src, open(destination, "w") as dst:
            content = src.read()
            dst.write(content)
    except (FileNotFoundError, PermissionError):
        return
