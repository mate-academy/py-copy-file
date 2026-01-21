def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) == 3 or parts[0] == "cp":
        first_file = parts[1]
        copied_file = parts[2]

        if first_file != copied_file:
            with open(first_file, "r") as start, open(copied_file, "w") as end:
                start.write(end.read())
