def copy_file(command: str) -> None:
    parts = command.split(" ")

    if len(parts) != 3 or parts[0] != "cp" or parts[1] == parts[2]:
        return

    origin_file = parts[1]
    file_copy = parts[2]

    try:
        with open(origin_file, "r") as origin, open(file_copy, "w") as copy:
            copy.write(origin.read())
    except FileNotFoundError:
        return
