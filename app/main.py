def copy_file(command: str) -> None:
    if len(command.split()) < 3:
        return None
    if command.split()[0] != "cp":
        return None
    try:
        with open(command.split()[1],
                  "r") as origin, open(command.split()[2], "w") as copy:
            copy.write(origin.read())
    except FileNotFoundError:
        return None
