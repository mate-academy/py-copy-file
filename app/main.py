def copy_file(command: str) -> bool:
    if len(command.split(" ")) != 3:
        return False

    if not command.startswith("cp"):
        return False

    file, new_file = command.split(" ")[1:]

    if file != new_file:
        try:
            with open(file) as file, open(new_file, "a+") as new_file:
                for line in file:
                    new_file.write(line)
        except (FileNotFoundError, PermissionError):
            return False
        else:
            return True