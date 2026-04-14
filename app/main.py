def copy_file(command: str) -> None:
    try:
        if len(command.split()) < 3:
            return

        command_name, file_input, file_output = command.split()

        if file_input == file_output or command_name != "cp":
            return

        with open(file_input) as file_from, open(file_output, "w") as file_to:
            file_to.write(file_from.read())
    except FileNotFoundError:
        return
