def copy_file(command: str) -> None:
    cmd_list = command.split()
    if cmd_list[1] != cmd_list[2]:
        with open(cmd_list[1], "r") as file_in, \
                open(cmd_list[2], "w") as file_out:
            file_out.write(file_in.read())
