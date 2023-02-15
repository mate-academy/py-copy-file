def copy_file(command: str) -> None:
    command = command.split()
    if command[1] != command[2]:
        with (
            open(f"{command[1]}", "r") as file,
            open(f"{command[2]}", "w") as file_copy
        ):
            file_copy.write(file.read())

