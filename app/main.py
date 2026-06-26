def copy_file(command: str) -> None:
    parts = command.split()
    if (not len(parts)
            or parts[0] != "cp"
            or len(parts) != 3
            or parts[1] == parts[2]):
        return
    try:
        with open(parts[1], "r") as old_file:
            new_file = open(parts[2], "w")
            new_file.write(old_file.read())
            new_file.close()
        old_file.close()
    except FileNotFoundError:
        pass
