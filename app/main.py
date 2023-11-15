def copy_file(command: str) -> None:
    command, old_file, new_file = command.split()
    if old_file == new_file or command != "cp":
        return

    with open(old_file, "r") as file_to_copy, open(new_file, "w") as new_file:
        new_file.write(file_to_copy.read())
