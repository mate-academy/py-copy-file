def copy_file(command: str) -> None:
    cmd_ls = command.split(" ")
    if len(cmd_ls) != 3 or cmd_ls[1] != "cp":
        raise ValueError(
            "Invalid command. "
            "Command must look like \'cp file.txt file-copy.txt\'"
        )
    if cmd_ls[1] == cmd_ls[2]:
        return None
    with open(cmd_ls[1], "r") as file_in, open(cmd_ls[2], "w") as file_out:
        file_out.write(file_in.read())
