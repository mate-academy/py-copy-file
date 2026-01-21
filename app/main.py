def copy_file(command: str) -> None:
    tokens = command.split()
    if len(tokens) != 3 or tokens[0] != "cp":
        return

    source = tokens[1]
    dest = tokens[2]
    if source == dest:
        return

    try:
        with open(source, "r", encoding="utf-8") as file_in, \
             open(dest, "w", encoding="utf-8") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
