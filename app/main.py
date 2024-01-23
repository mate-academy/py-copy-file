def copy_file(command: str) -> None:
    command = command.split()
    if command[1] == command[2] or command[0] != "cp":
        return
    with open(command[1], "r") as source, open(command[2], "w") as source_copy:
        source_copy.write(source.read())
