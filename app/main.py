def copy_file(command: str) -> None:
    parts = command.split()

    # Validate command structure
    if len(parts) != 3 or parts[0] != "cp":
        raise ValueError(
            "Command must be in format: cp <source> <destination>"
        )

    source, destination = parts[1], parts[2]

    # Do nothing if source and destination are the same
    if source == destination:
        return

    # Copy content from source to destination
    with open(source, "r") as file_in, open(destination, "w") as file_out:
        file_out.write(file_in.read())
