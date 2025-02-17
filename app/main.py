def copy_file(command: str) -> None:
    parts = command.split()

    # Check if format is valid and `cp` is the first argument
    if len(parts) != 3 or parts[0] != "cp":
        return

    source_file, target_file = parts[1], parts[2]

    # If source and target are the same, do nothing
    if source_file == target_file:
        return

    try:
        # Use context managers to read and write files
        with (
            open(source_file, "r") as file_in,
            open(target_file, "w") as file_out
        ):
            file_out.write(file_in.read())
    except FileNotFoundError:
        pass
