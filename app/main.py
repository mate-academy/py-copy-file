def copy_file(command: str) -> None:
    # Split the command into components
    parts = command.split()
    # Validate that there are exactly 3 elements and starts with "cp"
    if len(parts) != 3 or parts[0] != "cp":
        return
    source_name = parts[1]
    destination_name = parts[2]
    # Do nothing if the source and destination names are the same
    if source_name == destination_name:
        return
    try:
        with open(source_name, "r") as file_in, open(destination_name, "w") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
