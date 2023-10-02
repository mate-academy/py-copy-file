def copy_file(command: str) -> None:
    separate = command.split()
    if len(separate) == 3:
        cp, old_file, new_file = separate
        if cp == "cp":
            if old_file == new_file:
                return
            with open(old_file, "r") as old_f, open(new_file, "w") as new_f:
                new_f.writelines(old_f.readlines())
