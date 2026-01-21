def copy_file(command: str) -> None:
    command, origin, copy = command.split()
    if command == "cp" and ".txt" in (origin, copy):
        if origin != copy:
            with open(origin, "r") as origin, open(copy, "w") as copy:
                lines = origin.readlines()
                copy.writelines(lines)
