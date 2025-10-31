def copy_file(command: str) -> None:
    """Copies a file like the Linux 'cp' command.
    Does nothing if command is invalid, filenames are identical,
    or source file does not exist.
    """
    # Split the command only once
    parts = command.split()

    # Validate format: must be exactly three parts and start with 'cp'
    if len(parts) != 3 or parts[0] != "cp":
        return

    source_file_name, target_file_name = parts[1], parts[2]

    # Do nothing if source and destination are the same
    if source_file_name == target_file_name:
        return

    # Try to copy file content
    try:
        with open(source_file_name, "r", encoding="utf-8") as source_file, \
             open(target_file_name, "w", encoding="utf-8") as target_file:
            target_file.write(source_file.read())
    except FileNotFoundError:
        # Gracefully ignore missing source file
        return
