def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    source_file_name = parts[1]
    destination_file_name = parts[2]

    if source_file_name == destination_file_name:
        return

    try:
        with open(source_file_name, "r") as source_file, \
                open(destination_file_name, "w") as destination_file:
            destination_file.write(source_file.read())
    except FileNotFoundError:
        return
