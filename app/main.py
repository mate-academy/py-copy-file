def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        return
    source_file = parts[1]
    destination_file = parts[2]
    if source_file == destination_file:
        return
    try:
        with open(source_file, "r") as source, \
                open(destination_file, "w") as destination:
            content = source.read()
            destination.write(content)
    except FileNotFoundError:
        return
