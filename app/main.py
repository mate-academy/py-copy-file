def copy_file(command: str) -> None:
    """
    Copy a file from source to destination.

    Args:
        command(str): The command string
        containing the source and destination paths.
    """
    try:
        parts = command.split()
        if len(parts) != 3 or parts[0] != "cp":
            print("Invalid command format. Use: cp <source> <destination>")
            return

        source = parts[1]
        destination = parts[2]

        if source == destination:
            print("Source and destination cannot be the same.")
            return

        with open(source, "rb") as src_file:
            with open(destination, "wb") as dest_file:
                dest_file.write(src_file.read())

        print(f"File copied from {source} to {destination}")

    except FileNotFoundError:
        print(f"Source file '{source}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
