def copy_file(command: str) -> None:
    param, file_source, new_file = command.split()
    if param == "cp" and file_source != new_file:
        with open(file_source, "r") as source, open(new_file, "w") as copy:
            copy.write(source.read())
