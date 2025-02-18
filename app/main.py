def copy_file(command: str) -> None:
    if len(command.split()) == 3:
        command, source_file_path, destination_file_path = command.split()
        if source_file_path != destination_file_path and command == "cp":
            with (open(destination_file_path, "w") as source_file,
                 open(source_file_path, "r") as destination_file):
                source_file.write(destination_file.read())
