def copy_file(command: str) -> None:
    cmd, old_file, new_file = command.split()
    if old_file != new_file:
        with open(old_file, "r") as file_one, open(new_file, "w") as file_two:
            file_two.write(file_one.read())
