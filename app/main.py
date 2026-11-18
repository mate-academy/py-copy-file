def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        return
    current_file = parts[1]
    copied_file = parts[2]

    if current_file == copied_file:
        return
    try:
        with open(current_file, "r") as read_file:
            file_content = read_file.read()
    except FileNotFoundError:
        return

    with open(copied_file, "w") as write_file:
        write_file.write(file_content)
