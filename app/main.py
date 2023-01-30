def copy_file(command: str) -> None:
    command, old_name, new_name = command.split()
    if old_name != new_name and command == "cp":
        with open(old_name, "r") as old_file, open(new_name, "w") as new_file:
            new_file.write(old_file.read())
