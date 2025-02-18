def copy_file(command: str) -> None:
    command_str = command.split()

    if (
        len(command_str) == 3
        and command_str[0] == "cp"
        and command_str[1] != command_str[2]
    ):
        source_file_name = command_str[1]
        new_file_name = command_str[2]

        with (
            open(source_file_name) as source_file,
            open(new_file_name, "w") as new_file
        ):
            new_file.write(
                source_file.read()
            )
