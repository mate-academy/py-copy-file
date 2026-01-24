def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) < 2 or parts[0] != "cp":
        return

    if len(parts) != 3:
        return

    if parts[1] == parts[2]:
        return 

    try:
        with open(parts[1], "r") as source_f, open(parts[2], "w") as dst_f:
            dst_f.write(source_f.read())
    except FileNotFoundError:
        pass