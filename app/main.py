def copy_file(command: str) -> None:
    command, old_file, new_file = command.split()
    if command == "cp":
        if old_file == new_file:
            pass
        with open(old_file) as old, open(new_file, "w") as new:
            reader = old.read()
            new.write(reader)
