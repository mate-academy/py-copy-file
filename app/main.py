def copy_file(command: str) -> None:
    command_split = command.split()
    if len(command_split) == 3 and command_split[0] == "cp":
        old_file = command_split[1]
        new_file = command_split[2]

        if old_file != new_file:
            with open(old_file, "r") as origin, open(new_file, "w") as copied:
                copied.write(origin.read())
