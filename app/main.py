def copy_file(command: str) -> None:
    old_file, new_file = command.split()[1], command.split()[2]
    print(old_file, new_file)
    if old_file != new_file:
        with open(old_file) as old, open(new_file, "w") as new:
            reader = old.read()
            new.write(reader)
