def copy_file(command: str) -> None:
    com, old_file, new_file = command.split()
    if old_file != new_file:
        with open(old_file) as old, open(new_file, "w") as new:
            reader = old.read()
            new.write(reader)
