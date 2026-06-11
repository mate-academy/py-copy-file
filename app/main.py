def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        return

    _, source, result = parts

    if _ != "cp":
        return
 
    if source == result:
        return

    try:
        with open(source, "r") as read_file, open(result, "w") as write_file:
            content = read_file.read()
            write_file.write(content)
    except FileNotFoundError:
        return
