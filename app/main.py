def copy_file(command: str) -> None:
    parts: list[str] = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    source: str = parts[1]
    destination: str = parts[2]

    if source == destination:
        return

    try:
        with open(source, "r", encoding="utf-8") as file_in, \
             open(destination, "w", encoding="utf-8") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        # Source file does not exist -> do nothing
        return
