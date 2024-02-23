def copy_file(command: str) -> None:
    command_parts = command.split()

    if (
            len(command_parts) == 3
            and command_parts[0] == "cp"
            and command_parts[1] != command_parts[2]
    ):

        with open(
                command_parts[1], "r"
        ) as file, open(
            command_parts[2], "a"
        ) as file_copy:

            file_copy.write(file.read())
