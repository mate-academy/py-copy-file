def copy_file(command: str) -> None:
    if len(command) == 3:
        command = command.split()[1:]

        if command[0] != command[1]:
            with (
                open(command[0, "r"]) as file_origin,
                open(command[1], "w") as file_copy,
            ):
                file_copy.write(file_origin.read())
