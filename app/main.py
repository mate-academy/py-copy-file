def copy_file(command: str) -> None:
    command, origin, copy = command.split()
    if origin != copy:
        with open(origin, "r") as origin, open(copy, "w") as copy:
            lines = origin.readlines()
            copy.writelines(lines)
