def copy_file(command: str) -> bool:
    try:
        command, file, new_file = command.split(" ")
        if file != new_file and command == "cp":
            with open(file) as file, open(new_file, "a+") as new_file:
                new_file.write(file.read())
        else:
            return False
    except (ValueError, FileNotFoundError, PermissionError):
        return False
    else:
        return True
