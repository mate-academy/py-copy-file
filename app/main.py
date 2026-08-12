def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3:
        return

    if parts[0] != "cp":
        return

    if parts[1] == parts[2]:
        return

    try:
        with (
            open(parts[1], "r") as source_file,
            open(parts[2], "w") as destination_file
        ):
            destination_file.write(source_file.read())
    except FileNotFoundError:
        return
