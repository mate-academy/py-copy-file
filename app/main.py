def copy_file(command: str) -> None:
    command, file_from, file_to = command.split()
    if file_from == file_to:
        return
    with open(file_from, "r") as file_from:
        with open(file_to, "w") as file_to:
            file_to.write(file_from.read())
