def copy_file(command: str) -> str:
    try:
        current_command, file, new_file = command.split()
        if file != new_file and current_command == "cp":
            with open(file) as file, open(new_file, "a+") as new_file:
                new_file.write(file.read())
    except (ValueError, FileNotFoundError, PermissionError) as error:
        return str(error)
