def copy_file(command: str) -> None:
    parts_of_command = command.split()
    if len(parts_of_command) == 3 and "cp" in parts_of_command:
        _, file_source, file_new = parts_of_command
    if file_source != file_new:
        with open(file_source, "r") as source, open(file_new, "w") as copied:
            copied.write(source.read())
