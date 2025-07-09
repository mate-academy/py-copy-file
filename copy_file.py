def copy_file(command: str) -> None:
    """
    Copy a file in current directory like Linux cp command.

    Args:
        command (str): String with command 'cp', source file name and
                      destination file name, separated by spaces.

    Example:
        copy_file("cp file.txt file-copy.txt")
    """
    # Split the command into parts
    parts = command.split()

    # Validate command format
    if len(parts) != 3 or parts[0] != "cp":
        return

    source_file = parts[1]
    destination_file = parts[2]

    # Do nothing if trying to copy file to itself
    if source_file == destination_file:
        return

    # Copy the file content
    try:
        with open(source_file, "r") as file_in, \
                open(destination_file, "w") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        # If source file doesn't exist, do nothing (like cp command)
        pass
    except Exception:
        # Handle any other potential errors silently
        pass
