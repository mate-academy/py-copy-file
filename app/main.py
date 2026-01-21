def copy_file(command: str) -> None:
    parts = command.split(" ")
    if parts[0] != "cp" or len(parts) != 3:
        return
    if parts[1] == parts[2]:
        return
    try:
        with open(parts[1], "r") as inp_f, open(parts[2], "w") as out_f:
            out_f.write(inp_f.read())
    except FileNotFoundError:
        pass