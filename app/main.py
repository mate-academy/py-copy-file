def copy_file(command: str):
    cmd_list = command.split()
    cmd = cmd_list[0]
    old_file = cmd_list[1]
    new_file = cmd_list[2]

    if old_file != new_file and cmd == "cp":
        with open(old_file, "r") as file, open(new_file, "w") as new_file:
            new_file.write(file.read())
    else:
        return
