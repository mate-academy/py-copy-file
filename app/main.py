def copy_file(command: str) -> None:
    parts = command.strip().split()

    if command == "":
        return

    if len(parts) != 3 or parts[0] != "cp":
        print("Invalid command format. Use: cp <source> <destination>")
        return

    cp, source, destination = parts

    # Do nothing if source and destination names are the same
    if source == destination:
        return

    try:
        with (
            open(source, "r") as source,
                open(destination, "w") as destination):
            destination.write(source.read())
    except FileNotFoundError:
        return
