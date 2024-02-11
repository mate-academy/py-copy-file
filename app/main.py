def copy_file(command: str) -> None:
    command_parts = command.split(" ")
    file_source = command_parts[1]
    new_file = command_parts[2]
    if file_source == new_file:
        return
    with open(file_source, "r") as source, open(new_file, "w") as copy:
        copy.write(source.read())
