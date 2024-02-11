def copy_file(command: str) -> None:
    if command.startswith("cp") and len(command.split()) == 3:
        command_parts, file_source, new_file = command.split()
        if file_source != new_file:
            with open(file_source, "r") as source, open(new_file, "w") as copy:
                copy.write(source.read())
