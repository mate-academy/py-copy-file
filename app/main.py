def copy_file(command: str) -> None:
    command_part = command.split()

    if command_part[0] == "cp":
        with open(
                command_part[1], "r"
        ) as file, open(
            command_part[2], "a"
        ) as file_copy:

            if file.name != file_copy.name:
                file_copy.write(file.read())
