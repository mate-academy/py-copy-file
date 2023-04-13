def copy_file(command: str) -> None:
    cmd = command.split(" ")
    if cmd[1] == cmd[2]:
        pass

    f1 = open(cmd[1], "r")
    f2 = open(cmd[2], "w")
    date = f1.read()
    f2.write(str(date))
    f1.close()
    f2.close()
