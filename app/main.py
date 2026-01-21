def copy_file(command: str) -> None:
    """Copies a file in the current directory like the Linux cp command."""

    parts = command.strip().split()

    # Validate command format
    if len(parts) != 3 or parts[0] != "cp":
        return

    source_filename, destination_filename = parts[1], parts[2]

    # Do nothing if source and destination are the same
    if source_filename == destination_filename:
        return

    try:
        # Copy file content from source to destination
        with open(source_filename, "r") as source_file, \
             open(destination_filename, "w") as destination_file:
            destination_file.write(source_file.read())
    except FileNotFoundError:
        # Gracefully ignore if source file doesn't exist
        return
