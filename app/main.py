def copy_file(command: str) -> None:
    command = command.split()
    com_from = command[1]
    com_to = command[2]
    if com_from[1] == com_to[2]:
        pass
    with open(com_from, "r") as file_incom, open(com_to, "a") as file_out:
        file_out.write(file_incom.read())
