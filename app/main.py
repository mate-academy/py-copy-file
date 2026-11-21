def copy_file(command: str) -> None:
    command = command.split()
    if len(command) != 3 or command[1] == command[2] or command[0] != "cp":
        return
    try:
        with open(command[1], "r") as original, open(command[2], "w") as copy:
            copy.write(original.read())
    except FileNotFoundError:
        return
