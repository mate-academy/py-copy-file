def copy_file(command: str) -> None:
    cmd = command.split()
    with open(cmd[1], "r") as file_in, open(cmd[2], "w") as file_out:
        file_out.write(file_in.read())