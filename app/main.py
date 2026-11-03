def copy_file(command: str) -> None:
    part = command.split()

    if len(part) < 3:
        return

    source = part[1]
    destination = part[2]
    if source == destination:
        return

    with open(source, "r") as file_in, open(destination, "w") as file_out:
        file_out.write(file_in.read())
