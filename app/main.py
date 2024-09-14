def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3:
        raise ValueError(
            "Invalid command format."
            " Expected format: 'cp <source> <destination>'."
        )

    if parts[0] != "cp":
        raise ValueError("Unknown command. Only 'cp' is supported.")

    source_file, dest_file = parts[1], parts[2]

    if source_file == dest_file:
        raise ValueError("Source and destination files must be different.")

    with open(source_file, "r") as file_in, open(dest_file, "w") as file_out:
        file_out.write(file_in.read())
