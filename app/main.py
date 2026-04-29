def copy_file(command: str) -> None:
    if command == "":
        return

    parts = command.split()
    if not parts[0] == "cp":
        return
    if not len(parts) == 3:
        return

    source_file_name = parts[1]
    try:
        with open(source_file_name):
            pass
    except FileNotFoundError:
        return

    destination_file_name = parts[2]

    if source_file_name == destination_file_name:
        return

    with (
        open(source_file_name, "r") as source_file_object,
        open(destination_file_name, "w") as destination_file_object
    ):
        destination_file_object.write(source_file_object.read())
