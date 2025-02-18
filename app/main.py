def copy_file(command: str) -> None:
    cmd_list = command.split(' ')
    if cmd_list[1] != cmd_list[2] and cmd_list[0] == "cp":
        with open(cmd_list[1], "r") as f_in, open(cmd_list[2], "w") as f_out:
            f_out.write(f_in.read())
