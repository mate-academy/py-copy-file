def copy_file(command: str) -> None:
    command = command.strip()
    parts = command.split(maxsplit=2)
    if len(parts) != 3:
        return
    if parts[0] != "cp":
        return
    old_file = parts[1]
    new_file = parts[2]
    if old_file == new_file:
        return
    try:
        with open(old_file, "r") as files, open(new_file, "w") as new_files:
            new_files.write(files.read())
    except FileNotFoundError:
        return
