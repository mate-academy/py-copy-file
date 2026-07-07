import os


def copy_file(cmd: str) -> None:
    cmd_split = cmd.split(" ")
    if cmd_split == [""]:
        return
    if not os.path.exists(cmd_split[1]):
        return
    if len(cmd_split) != 3:
        return
    if cmd_split[0] != "cp":
        return
    if cmd_split[1] == cmd_split[2]:
        return
    with open(cmd_split[1], "r") as in_file:
        with open(cmd_split[2], "w") as out_file:
            out_file.write(in_file.read())
