def copy_file(command: str) -> None:
    my_command, old_file, new_file = command.split()
    if my_command == "cp" and old_file != new_file:
        with open(old_file, "r") as origin, open(new_file, "w") as copy:
            copy.write(origin.read())
