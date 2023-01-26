def copy_file(command: str) -> None:
    old_name, new_name = command.split()[1:]
    with open(old_name, "r") as old_file, open(new_name, "w") as new_file:
        new_file.write(old_file.read())
