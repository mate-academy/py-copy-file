def copy_file(command: str) -> None:
    if len(command.split()) == 3:
        input_command, source_file_path, destination_file_path \
            = command.split()
        if input_command == "cp" and source_file_path != destination_file_path:
            with open(source_file_path, "r") as original_file, \
                    open(destination_file_path, "w") as file_copy:
                file_copy.write(original_file.read())
