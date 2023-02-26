def copy_file(command: str) -> None:
    if command.split()[1] != command.split()[2]:
        with open(command.split()[1], "r") as original_file:
            with open(command.split()[2], "w") as file_copy:
                file_copy.write(original_file.read())
