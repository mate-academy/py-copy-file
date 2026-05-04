def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3:
        return

    if parts[0] != "cp":
        return
    source = parts[1]
    destination = parts[2]

    if source == destination:
        return

    try:
        with open(source, "r") as source_file, \
                open(destination, "w") as dest_file:
            dest_file.write(source_file.read())

    except FileNotFoundError:
        return
