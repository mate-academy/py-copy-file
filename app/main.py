def copy_file(command: str) -> None:
    if len(command) != 3:
        raise ValueError("Invalid command value")
    command_file, source_file_path, destination_file_path = command.split()
    if command_file == "cp" and source_file_path != destination_file_path:
        with (
            open(source_file_path, "r") as file_r,
            open(destination_file_path, "w") as file_w
        ):
            file_w.write(file_r.read())


