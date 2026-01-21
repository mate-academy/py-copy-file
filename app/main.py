def copy_file(command: str) -> None:
    """
    Copies a file's content to another file based on a 'cp' command.

    Example: "cp source.txt destination.txt"
    Does nothing if the source and destination file names are the same.
    """
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    source_file = parts[1]
    dest_file = parts[2]

    if source_file == dest_file:
        return

    try:
        with open(source_file, "r") as file_in:
            with open(dest_file, "w") as file_out:
                content = file_in.read()
                file_out.write(content)

    except FileNotFoundError:
        error_message = f"Error: File '{source_file}' not found."
        print(error_message)
    except IOError as e:
        print(f"Error copying file: {e}")
