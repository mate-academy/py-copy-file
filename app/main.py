def copy_file(command: str) -> None:
    # Handle empty command
    if not command or not command.strip():
        return

    # Validate command format
    parts = command.split()
    if len(parts) != 3:
        return

    action, source_file, destination_file = parts

    # Validate action is "cp"
    if action != "cp":
        return

    # Handle same source and destination
    if source_file == destination_file:
        return

    # Handle missing source file
    try:
        with open(source_file, "r") as file_in, \
                open(destination_file, "w") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
