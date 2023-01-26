def copy_file(command: str) -> None:
    old_file_name, new_file_name = command.split()[1:]
    with open(old_file_name, "r") as old_file, open(new_file_name, "w") as new_file:
        new_file.write(old_file.read())
