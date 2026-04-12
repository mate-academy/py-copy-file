def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        return
    if parts[0] != "cp":
        return
    if parts[1] == parts[2]:
        return
    try:
        with open(parts[1], "r") as source_file, \
             open(parts[2], "w") as target_file:
            text = source_file.read()
            target_file.write(text)
    except FileNotFoundError:
        return
