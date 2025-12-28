def copy_file(command : str) -> None:
    if "/" in command or "\\" in command:
        return

    parts = command.split()
    if len(parts) == 3:
        cmd, source_file, copied_file = parts
    else:
        return

    if cmd != "cp" or source_file == copied_file:
        return

    try:
        with open(source_file, "r") as source, open(copied_file, "w") as copy:
            copy.write(source.read())
    except FileNotFoundError:
        return
