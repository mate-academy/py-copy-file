def copy_file(command: str) -> None:
    command_parts = command.split()
    if len(command_parts) != 3:
        raise ValueError("Invalid command format")

    cmd, source_path, destination_path = command_parts

    if source_path == destination_path:
        return
    if command_parts[0] == "cp":
        with (
            open(source_path, "r") as file_in,
            open(destination_path, "w") as file_out
        ):
            file_out.write(file_in.read())
