def copy_file(command: str) -> None:
    command_elements = command.split()

    if len(command_elements) != 3:
        return

    if command_elements[0] != "cp":
        return

    _, source_file_name, file_to_create_name = command_elements

    if source_file_name == file_to_create_name:
        return

    try:
        with open(source_file_name, "r") as source_file:
            content = source_file.read()
            with open(file_to_create_name, "w") as file_to_create:
                file_to_create.write(content)
    except FileNotFoundError:
        return
