def copy_file(command: str) -> None:
    command_parts = command.split()
    if len(command_parts) < 3 and command_parts[0] != "cp":
        return
    try:
        command_name, file_input, file_output = command_parts

        if file_input == file_output:
            return

        with open(file_input) as file_from, open(file_output, "w") as file_to:
            file_to.write(file_from.read())
    except FileNotFoundError:
        return
