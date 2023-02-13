def copy_file(command: str) -> None:
    command, file_source, file_copy = command.split()
    if command == "cd" and file_copy != file_source:
        with open(file_source, "r") as source, open(file_copy, "w") as copy:
            copy.write(source.read())
