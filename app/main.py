def copy_file(command: str) -> None:
    cmd_list = command.split()
    if cmd_list[1] != cmd_list[2]:
        with (open(cmd_list[1], "r") as old_f,
              open(cmd_list[2], "w") as new_f):
            new_f.write(old_f.read())
