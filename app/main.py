def copy_file(command: str) -> None:
    command_parts = command.split(" ")

    if len(command_parts) != 3 or command_parts[0] != "cp":
        raise ValueError(
            "Invalid command format. "
            "Expected format: 'cp <source_file> <destination_file>'"
        )

    source_file_name, destination_file_name = (
        command_parts[1], command_parts[2]
    )

    # Do nothing if source and destination files are the same
    if source_file_name == destination_file_name:
        return

    # Copy content from source_file to destination_file
    try:
        with open(source_file_name, "r") as source_file, open(
            destination_file_name, "w"
        ) as destination_file:
            destination_file.write(source_file.read())
    except FileNotFoundError:
        raise FileNotFoundError(
            f"The file '{source_file_name}' does not exist."
        )
    except Exception as error:
        raise RuntimeError(
            f"An error occurred while copying the file: {error}"
        )
