def copy_file(command: str) -> None:
    command_parts = command.split()

    if command_parts[0] == "cp" and len(command_parts) == 3:
        with open(
                command_parts[1], "r"
        ) as file, open(
            command_parts[2], "a"
        ) as file_copy:

            if file.name != file_copy.name:
                file_copy.write(file.read())
