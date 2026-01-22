def copy_file(command: str) -> None:
    com_d = command.split()
    if com_d[0] != "cp" or com_d[1] == com_d[2]:
        return None
    else:
        with open(com_d[1], "r") as o_file, open(com_d[2], "w") as n_file:
            n_file.write(o_file.read())
