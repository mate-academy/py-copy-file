def copy_file(cp_command: str) -> None:
    command = cp_command.split()
    try:
        new_file = command[2]
        old_file = command[1]
        cp = command[0]
        try:
            if cp == "cp" and len(command) == 3 and old_file != new_file:
                with open(old_file, "r") as old, open(new_file, "w") as new:
                    new.write(old.read())
        except FileNotFoundError:
            pass
    except IndexError:
        pass
