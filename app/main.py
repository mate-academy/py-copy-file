def copy_file(command: str) -> None:
    parts_command = command.split()

    if len(parts_command) != 3:
        return

    cp, source, destination = parts_command

    if cp != "cp":
        return

    if source == destination:
        return

    try:
        with open(source, "r") as src_file:
            content = src_file.read()

    except FileNotFoundError:
        return

    with open(destination, "w") as dest_file:
        dest_file.write(content)
