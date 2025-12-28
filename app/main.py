def copy_file(command: str) -> None:
    command = command.strip()
    parts = command.split()

    if len(parts) != 3:
        return

    cmd, source, destination = parts

    if cmd != "cp":
        return

    if source == destination:
        return

    try:
        with open(source, "r") as source_file:
            content = source_file.read()

    except FileNotFoundError:
        return

    with open(destination, "w") as destination_file:
        destination_file.write(content)
