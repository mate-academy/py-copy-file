def copy_file(command: str) -> None:
    command = command.split()
    if command[1] != command[2]:
        with open(command[1], "r") as origin, open(command[2], "w") as copy:
            lines = origin.readlines()
            copy.writelines(lines)
