def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    source = parts[1]
    destination = parts[2]

    if source == destination:
        return

    try:
        with open(source, "r") as f:
            content = f.read()
    except FileNotFoundError:
        return

    with open(destination, "w") as f:
        f.write(content)
