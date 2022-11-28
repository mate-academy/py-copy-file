def copy_file(command: str):
    list_of_commands = command.split()
    old = list_of_commands[1]
    new = list_of_commands[2]

    if old != new:
        with open(old, "r") as old_f:
            with open(new, "w") as new_f:
                new_f.write(old_f.read())
