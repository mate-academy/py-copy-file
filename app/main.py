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
        with open(source, "r") as file:
            content = file.read()

        with open(destination, "w") as file:

            file.write(content)

    except FileNotFoundError:
        return
