def copy_file(command: str) -> None:
    elements = command.split()

    if len(elements) != 3:
        return

    if elements[0] != "cp":
        return

    source = elements[1]
    destination = elements[2]

    if source == destination:
        return

    try:
        with open(source, "r") as file_in:
            content = file_in.read()
    except FileNotFoundError:
        return

    with open(destination, "w") as file_out:
        file_out.write(content)
