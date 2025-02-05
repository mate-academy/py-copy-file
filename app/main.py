def copy_file(command: str) -> None:
    parts = command.split()

    # Validate command structure
    if len(parts) != 3 or parts[0] != "cp":
        return  # Invalid command format

    source, destination = parts[1], parts[2]

    # Do nothing if source and destination are the same
    if source == destination:
        return

    try:
        with open(source, "r") as file_in, open(destination, "w") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        pass  # Handle missing file silently (or log an error if needed)
