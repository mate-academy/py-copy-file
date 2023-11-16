def copy_file(command: str) -> None:
    command_split = command.split()
    if command_split[0] == "cp":
        if command_split[1] != command_split[2]:
            with (
                open(command_split[2], "w") as new_file,
                open(command_split[1], "r") as old_file
            ):
                new_file.write(old_file.read())
