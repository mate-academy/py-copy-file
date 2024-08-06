def copy_file(command: str) -> None:
    command, source_file_name, destination_file_name = command.split()
    if command == "cp" and source_file_name != destination_file_name:
        with (
            open(source_file_name) as source_file,
            open(destination_file_name, "w") as destination_file
        ):
            for line in source_file:
                destination_file.write(line)
