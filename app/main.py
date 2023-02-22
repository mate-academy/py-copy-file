def copy_file(command: str) -> None:
    command_name, base_filename, new_filename = command.split()
    if base_filename == new_filename:
        return
    if command_name == "cp":
        with open(base_filename, "r") as source:
            content = source.read()

        with open(new_filename, "w") as destination:
            destination.write(content)
