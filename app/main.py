def copy_file(command: str):
    cmd = command.split()
    if cmd[0] == "cp" and cmd[1] != cmd[2]:
        with open(cmd[1], "r") as file_in, open(cmd[2], "w") as file_out:
            file_out.write(file_in.read())
        print("Successful")
