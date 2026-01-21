def copy_file(command: str) -> None:
    old_file_name, new_file_name = command.split()[1:]
    if old_file_name != new_file_name:
        with open(old_file_name, "r") as old, open(new_file_name, "w") as new:
            new.write(f"{old.read()}")
