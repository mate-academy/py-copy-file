def copy_file(command: str) -> None:
    command, file_original, file_copy = command.split()
    if command != "cd":
        raise ValueError("Wrong command!")
    if file_original == file_copy:
        return
    with open(file_original, "r") as original, open(file_copy, "w") as copy:
        copy.write(original.read())
