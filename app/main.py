def copy_file(command: str) -> None:
    command, file_initial, file_copy = command.split()
    if command != "cd":
        raise ValueError("Wrong command!")
    if not file_initial == file_copy:
        with open(file_initial, "r") as original, open(file_copy, "w") as copy:
            copy.write(original.read())
