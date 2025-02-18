def copy_file(command: str) -> None:
    cmd = command.split()
    if cmd[0] != "cp" or cmd[1] == cmd[2]:
        return

    with open(cmd[1], "r") as file_in, open(cmd[2], "w") as file_out:
        for line in file_in:
            file_out.write(line)
