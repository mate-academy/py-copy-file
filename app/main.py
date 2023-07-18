def copy_file(command: str) -> None:
    if len(command) != 3:
        return
    command, file_from, file_to = command.split()
    if command != "cp":
        return
    if file_from == file_to:
        return
    with open(file_from, "r") as file_from, open(file_to, "w") as file_to:
        file_to.write(file_from.read())
