def copy_file(command: str) -> None:
    if len(command.strip()) == 3:
        prefix, source_file_path, destination_file_path = command.strip()
        if source_file_path != destination_file_path and prefix == "cp":
            with open(source_file_path, "r") as source_file, \
                    open(destination_file_path, "w") as file:
                file.write(source_file.read())
