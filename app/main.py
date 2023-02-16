def copy_file(command: str) -> None:
    try:
        command, file_original, file_copy = command.split()
        if command != "cd":
            raise ValueError
    except ValueError:
        print("Wrong command!")
        return None
    if file_original == file_copy:
        print("Files must have different names.")
        return None
    with open(file_original, "r") as original, open(file_copy, "w") as copy:
        copy.write(original.read())
