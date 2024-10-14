def copy_file(command: str) -> None:
    if (not isinstance(command, str) or len(command) < 3
            or command[:3] != "cp "):
        return

    cmd_list = command.strip().split(" ")
    if len(cmd_list) < 3 or cmd_list[1] == cmd_list[2]:
        return

    with open(cmd_list[1], "r") as file_in, open(cmd_list[2], "w") as file_out:
        file_out.write(file_in.read())
