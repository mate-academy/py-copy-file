def copy_file(command: str) -> None:
    command_elements = command.split()

    if len(command_elements) != 3:
        return

    if command_elements[0] != "cp":
        return

    command, source_file_name, file_to_create = command_elements

    if source_file_name == file_to_create:
        return

    try:
        with open(source_file_name, "r") as f1:
            content = f1.read()
            if content:
                with open(file_to_create, "w") as f2:
                    f2.write(content)
    except FileNotFoundError:
        return
