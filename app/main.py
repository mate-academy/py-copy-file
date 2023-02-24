def copy_file(command: str) -> None:
    parts = command.split(" ")
    if len(parts) == 3:
        command_name, source_file_path, destination_file_path = parts
        if source_file_path != destination_file_path and command_name == "cd":
            with (
                open(source_file_path, "r") as source_file,
                open(destination_file_path, "w") as destination_file
            ):
                destination_file.write(source_file.read())
