def copy_file(command: str):
    cmd_list = command.split()
    if cmd_list[1] == cmd_list[2]:
        print("Same file")
    else:
        with open(cmd_list[1], "r") as fin, open(cmd_list[2], "w+") as fout:
            fout.write(fin.read())
