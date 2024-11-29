def copy_file(command: str):
    # Split the command string to extract components
    parts = command.split()

    # Validate the command format
    if len(parts) != 3 or parts[0] != "cp":
        raise ValueError(
            "Invalid command format. Use: cp source_file destination_file"
        )

    source, destination = parts[1], parts[2]

    # Do nothing if the source and destination filenames are the same
    if source == destination:
        return

    # Copy content from source to destination
    try:
        with open(source, "r") as file_in, open(destination, "w") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        print(f"Error: The file '{source}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
