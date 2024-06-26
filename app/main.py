def copy_file(command: str) -> None:
    cmd_ls = command.split(" ")
    if cmd_ls[1] == cmd_ls[2]:
        return None
    with open(cmd_ls[1], "r") as file_in, open(cmd_ls[2], "w") as file_out:
        file_out.write(file_in.read())
