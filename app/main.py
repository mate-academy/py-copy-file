def copy_file(command: str) -> None:
    """
    Copies a file to a new file in the current directory, similar to the
    Linux 'cp' command.

    Args:
        command (str): A string with the command 'cp', the source file name,
                       and the new file name, separated by spaces.
                       Example: "cp file.txt new_file.txt"
    """

    parts = command.split()

    # Check for correct command structure and prevent copying a file to itself
    if len(parts) != 3 or parts[0] != "cp" or parts[1] == parts[2]:
        return

    source_file_name = parts[1]
    destination_file_name = parts[2]

    try:
        with open(source_file_name, "r") as source_file, \
             open(destination_file_name, "w") as destination_file:
            content = source_file.read()
            destination_file.write(content)
    except FileNotFoundError:
        print(f"Error: The file '{source_file_name}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
