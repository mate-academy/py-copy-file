def copy_file(command: str) -> None:
    command_parts = command.split()

    if len(command_parts) != 3 or command_parts[0] != "cp":
        raise ValueError("Invalid command format. "
                         "Use 'cp <source_file> <destination_file>'.")

    source_file, destination_file = command_parts[1], command_parts[2]

    if source_file == destination_file:
        return

    try:
        with open(source_file, "r") as file_in:
            with open(destination_file, "w") as file_out:
                file_out.write(file_in.read())
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: {source_file} does not exist.")
