def copy_file(command: str) -> None:
    split_command = command.split()
    old_file, new_file = split_command[1], split_command[2]
    if old_file != new_file:
        with open(old_file) as old, open(new_file, "w") as new:
            reader = old.read()
            new.write(reader)
