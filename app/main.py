def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    source = parts[1]
    destination = parts[2]

    if source == destination:
        return

    try:
        with open(source, "rb") as file_in:
            content = file_in.read()

        with open(destination, "wb") as file_out:
            file_out.write(content)

    except FileNotFoundError:
        return
