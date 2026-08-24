def copy_file(command: str) -> None:
    parts = command.split(" ")

    if len(parts) != 3:
        return None

    cmd, source, destination = parts

    if cmd != "cp":
        return None

    if source == destination:
        return None

    try:
        with open(source, "r") as file_in, open(destination, "w") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        return None
