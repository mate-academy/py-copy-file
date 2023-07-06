def copy_file(command: str) -> None:
    cmd_1 = command.split()
    if cmd_1[1] != cmd_1[2]:
        with open(cmd_1[1], "r") as file_in, open(cmd_1[2], "w") as file_out:
            file_out.write(file_in.read())
