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
        with open(source, "r") as file_in, open(destination, "w") as file_out:
            content = file_in.read()
            file_out.write(content)
    except FileNotFoundError:
        return
