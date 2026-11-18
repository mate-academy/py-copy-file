def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        return
    current_file = parts[1]
    copied_file = parts[2]

    if current_file == copied_file:
        return
    try:
        with open(current_file, "r") as f:
            file_content = f.read()
    except FileNotFoundError:
        return

    with open(copied_file, "w") as f:
        f.write(file_content)
