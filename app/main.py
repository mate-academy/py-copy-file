def copy_file(command: str):
    new_com = command.strip().split()
    if new_com[0] != "cp" and len(new_com) != 3:
        return "Wrong command"
    if new_com[1] == new_com[2]:
        return
    with open(new_com[1], "r") as one, open(new_com[2], "w") as two:
        two.write(one.read())
