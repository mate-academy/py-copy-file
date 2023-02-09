def copy_file(command: str) -> None:
    command = command.split()
    with (
        open(command[1], "r") as file_to_copy,
        open(command[2], "w") as new_file
    ):
        if file_to_copy.name != new_file.name:
            new_file.write(file_to_copy.read())
