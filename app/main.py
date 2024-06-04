def copy_file(command: str) -> None:
    command = command.split()
    com_from = command[1]
    com_to = command[2]
    if com_from[1] == com_to[2]:
        pass
    with open(com_from, "r") as in_, open(com_to, "a") as out_:
        out_.write(in_.read())
