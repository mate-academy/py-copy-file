def copy_file(command: str) -> None:
    if not command.strip():
        return
    command_parts = command.split()
    if len(command_parts) != 3 or command_parts[0] != "cp":
        return
    _, source_file, destination_file = command_parts
    if source_file == destination_file:
        return
    try:
        with (
            open(source_file, "r") as file_in,
            open(destination_file, "w") as file_out
        ):
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
