def copy_file(command: str) -> None:
    command_parts = command.split()
    if len(command_parts) == 3:
        command, source_file, target_file = command.split()

        if (
                command == "cp"
                and source_file != target_file
        ):

            with (open(source_file, "r") as file,
                    open(target_file, "w") as new_file):
                new_file.write(file.read())
