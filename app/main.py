def copy_file(command: str) -> None:
    command, old_file, new_file = command.split()
    if old_file != new_file:
        with open(old_file, "r") as copy, open(new_file, "w") as file:
            file.write(copy.read())
