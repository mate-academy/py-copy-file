def copy_file(command: str) -> None:
    command_parts = command.split()
    com, source_file, target_file = (command_parts[0],
                                     command_parts[1],
                                     command_parts[2])

    if (
            com == "cp"
            and source_file != target_file
            and len(command_parts) == 3
    ):

        with (open(source_file, "r") as file,
                open(target_file, "w") as new_file):
            new_file.write(file.read())
