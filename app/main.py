def copy_file(command: str) -> None:
    parts = command.split()

    # Ensure the command is well-formed
    if len(parts) != 3 or parts[0] != "cp":
        return

    source_file = parts[1]
    destination_file = parts[2]

    # Do nothing if the filenames are exactly the same
    if source_file == destination_file:
        return

    # Copy the content from the source to the destination,
    # ignoring missing files
    try:
        with open(source_file, "r") as file_in, \
                open(destination_file, "w") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
