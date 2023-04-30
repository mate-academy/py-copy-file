def copy_file(command: str) -> None:
    old_file, new_file = command.split(" ")[1:]
    if old_file != new_file:
        with open(old_file, "r") as old, open(new_file, "w") as new:
            new.write(old.read())
