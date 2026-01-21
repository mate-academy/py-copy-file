def copy_file(command: str) -> None:
    # Splitting the command into parts
    parts = command.split()

    # Check if the command is correctly formed
    if len(parts) != 3 or parts[0] != "cp":
        print("Invalid command")
        return

    # Extracting file names
    source_file = parts[1]
    destination_file = parts[2]

    # Check if the source and destination files are the same
    if source_file == destination_file:
        # Do nothing if the file names are the same
        return

    # Copying the content from source to destination
    with open(source_file, "r") as file_in,\
            open(destination_file, "w") as file_out:
        file_out.write(file_in.read())
