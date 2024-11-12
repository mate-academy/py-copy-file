def copy_file(command: str) -> None:
    # Split the command string into parts
    parts = command.split()

    # Validate command structure
    if len(parts) != 3 or parts[0] != "cp":
        raise ValueError("Command must be in format: "
                         "'cp source_file destination_file'")

    source_file, destination_file = parts[1], parts[2]

    # Check if source and destination are the same
    if source_file == destination_file:
        return  # Do nothing if trying to copy to the same file name

    # Copy content from source to destination
    with open(source_file, "r") as file_in, open(
            destination_file, "w") as file_out:
        file_out.write(file_in.read())
