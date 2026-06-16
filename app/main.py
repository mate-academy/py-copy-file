def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) < 3:
        return
    if parts[0] != "cp":
        return
    if parts[1] == parts[2]:
        return

    try:
        with open(parts[1], "r") as file_read:
            content = file_read.read()

        with open(parts[2], "w") as file_write:
            file_write.write(content)

    except FileNotFoundError:
        return
