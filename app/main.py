def copy_file(command: str) -> None:
    command_parts = command.split()

    if len(command_parts) != 3 or command_parts[0] != "cp":
        return

    _, source_name, copy_name = command_parts

    with open(source_name, "r") as source_file,\
            open(copy_name, "w") as copy_file:
        content = source_file.read()
        copy_file.write(content)
