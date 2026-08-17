def copy_file(command: str) -> None:
    result = command.split(" ")

    if len(result) != 3:
        return

    if result[0] != "cp":
        return

    source_file = result[1]
    destination_file = result[2]
    if source_file == destination_file:
        return

    try:
        with open(source_file, "r") as source_file_object:
            content = source_file_object.read()
    except FileNotFoundError:
        return

    with open(destination_file, "w") as destination_file_object:
        destination_file_object.write(content)
