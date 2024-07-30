def copy_file(command: str) -> None:
    parts = command.split(" ")
    if len(parts) != 3 or parts[0] != "cp" or parts[1] == parts[2]:
        return
    with open(parts[1]) as source, open(parts[2], "w") as copy:
        copy.write(source.read())
