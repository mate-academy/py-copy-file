def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3:
        return

    if parts[0] != "cp":
        return

    old_name = parts[1]
    new_name = parts[2]

    if old_name == new_name:
        return

    try:
        with open(old_name, "r") as old_file:
            text = old_file.read()

        with open(new_name, "w") as new_file:
            new_file.write(text)
    except FileNotFoundError:
        return
