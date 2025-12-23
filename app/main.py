def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp" or parts[1] == parts[2]:
        return

    try:
        with open(parts[1], "r") as src, open(parts[2], "w") as dst:
            dst.write(src.read())
    except FileNotFoundError:
        pass
