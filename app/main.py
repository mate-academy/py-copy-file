def copy_file(command: str) -> None:

    parts = command.split()

    if len(parts) != 3:
        return

    if parts[0] != "cp":
        return

    source_file_name = parts[1]
    destination_file_name = parts[2]

    if source_file_name == destination_file_name:
        return
    try:
        with (
            open(source_file_name, "r") as original_file,
            open(destination_file_name, "w") as copy_file
        ):
            copy_file.write(original_file.read())
    except FileNotFoundError:
        return
