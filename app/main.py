def copy_file(command: str) -> None:
    separate = command.split()
    if len(separate) == 3:
        cp, old_file, new_file = separate
        if cp == "cp" and old_file != new_file:
            with open(old_file, "r") as old_file, open(new_file, "w") as new_file:
                new_file.writelines(old_file.readlines())
