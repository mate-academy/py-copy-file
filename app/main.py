def copy_file(command: str) -> None:
    cmd = command.split(" ")
    if cmd[0] == "cp":
        if cmd[1] != cmd[2]:
            with open(cmd[1], "r") as source, open(cmd[2], "w") as target:
                lines = source.readlines()
                for line in lines:
                    target.write(line)
