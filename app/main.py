def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        return

    _, source, destination = parts
    if source == destination:
        return

    with open(source, "r") as source_file, \
         open(destination, "w") as dest_file:
        dest_file.write(source_file.read())
