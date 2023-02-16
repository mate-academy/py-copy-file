def copy_file(command: str) -> None:
    command, old_name, new_name = command.split()
    if command == "cp" and old_name != new_name:
        with open(old_name, "r") as old, open(new_name, "w") as new:
            new.write(old.read())
