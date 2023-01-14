def copy_file(command: str) -> None:
    cp, origin, file_copy = command.split()
    if origin != file_copy:
        with open(origin, "r") as file, open(file_copy, "w") as new_file:
            new_file.write(file.read())
