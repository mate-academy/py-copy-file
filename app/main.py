def copy_file(command: str) -> None:
    arguments = command.split()

    if len(arguments) != 3 or arguments[0] != "cp":
        return

    source = arguments[1]
    destination = arguments[2]

    if source == destination:
        return

    try:
        with open(source, "rb") as file_in:
            content = file_in.read()

        with open(destination, "wb") as file_out:
            file_out.write(content)

    except FileNotFoundError:
        return
