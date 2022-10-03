def copy_file(command: str) -> None:
    cmd = command.split()
    if cmd[0] == "cp" and cmd[1] != cmd[2]:
        with open(cmd[1], "r") as source, open(cmd[2], "w") as copy:
            copy.write(source.read())
