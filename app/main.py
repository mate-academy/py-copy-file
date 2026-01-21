def copy_file(command: str) -> None:
    command = command.strip()
    if not command:
        return

    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    source_file_path = parts[1]
    destination_file_path = parts[2]

    if source_file_path == destination_file_path:
        return

    try:
        with open(source_file_path, "r") as source_file, \
             open(destination_file_path, "w") as destination_file:
            destination_file.write(source_file.read())
    except FileNotFoundError:
        return
