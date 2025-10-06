def copy_file(command: str) -> None:
    # Split the command into parts
    parts = command.split()

    # Check if it's a valid cp command with exactly 3 parts
    if len(parts) != 3 or parts[0] != "cp":
        return

    # Extract source and destination filenames
    source_file = parts[1]
    dest_file = parts[2]

    # Do nothing if source and destination are the same
    if source_file == dest_file:
        return

    try:
        # Copy the file content with error handling
        with open(source_file, "r") as file_in, \
                open(dest_file, "w") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        # Do nothing if source file doesn't exist
        return
    except Exception:
        # Handle any other file-related errors gracefully
        return
