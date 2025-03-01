def copy_file(command: str) -> None:
    cmd = command.split()
    if len(cmd) == 3 and cmd[0] == "cp" and cmd[1] != cmd[2]:
        try:
            with open(cmd[1], "r") as file_in, open(cmd[2], "w") as file_out:
                txt = file_in.readlines()
                for i in txt:
                    file_out.write(i)
        except FileNotFoundError:
            pass
