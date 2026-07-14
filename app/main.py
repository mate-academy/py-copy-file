def copy_file(command: str) -> None:
    parts = command.split(" ")

    if len(parts) < 3 or parts[0] != "cp":
        return

    if parts[1] == parts[2]:
        return

    try:
        with open(
            parts[1],
            "r"
        ) as origin_file, open(
            parts[2],
            "w"
        ) as copy_file:
            copy_file.write(origin_file.read())
    except FileNotFoundError:
        return
