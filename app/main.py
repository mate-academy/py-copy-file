def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        return

    _, source, result = parts

    if _ != "cp":
        return

    try:
        with open(source, "r") as read_file:
            content = read_file.read()
    except FileNotFoundError:
        return

    with open(result, "w") as write_file:
        write_file.write(content)
