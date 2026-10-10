def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) == 3 and parts[1] != parts[2] and parts[0] == "cp":
        try:
            with open(parts[1], "r") as origin, open(parts[2], "w") as copy:
                content = origin.read()
                copy.write(content)
        except FileNotFoundError:
            pass
