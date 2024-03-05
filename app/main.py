def copy_file(command: str) -> None:
    cmd_split = command.split()
    if len(cmd_split) == 3:
        if cmd_split[0] == "cp" and (cmd_split[1] != cmd_split[2]):
            with (open(cmd_split[1], "r") as file_in,
                  open(cmd_split[2], "w") as file_out):
                file_out.write(file_in.read())
