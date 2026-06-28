def copy_file(command: str) -> None:
    parts = command.split()

    if not parts or parts[0] != "cp" or len(parts) != 3:
        return

    source_file_name = parts[1]
    destination_file_name = parts[2]

    if source_file_name == destination_file_name:
        return

    try:
        with open(source_file_name, "r") as source_file_object:
            file_content = source_file_object.read()
    except FileNotFoundError:
        return

    with open(destination_file_name, "w") as destination_file_object:
        destination_file_object.write(file_content)
