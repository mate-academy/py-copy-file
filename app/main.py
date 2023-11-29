def copy_file(command: str) -> None:
    command_elements = command.split()
    if len(command_elements) == 3:
        if (
                command_elements[0] == "cp"
                and command_elements[1] != command_elements[2]
        ):
            with (
                open(
                    command_elements[1], "r"
                ) as file_in,
                open(
                    command_elements[2], "w"
                ) as file_out
            ):
                file_out.write(file_in.read())
