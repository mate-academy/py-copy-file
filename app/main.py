def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        return
    source_file_name, destination_file_name = parts[1], parts[2]
    if source_file_name == destination_file_name:
        return
    try:
        with open(source_file_name, "r") as source_file_object, \
             open(destination_file_name, "w") as destination_file_object:
            destination_file_object.write(source_file_object.read())
    except FileNotFoundError:
        return
