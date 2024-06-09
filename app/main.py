def copy_file(command: str) -> None:
    cmd_list = command.split()

    if (
        (cmd_list[0] == "cp")
        and (len(cmd_list) == 3)
        and (cmd_list[1] != cmd_list[2])
    ):
        with (open(cmd_list[1], "r") as old_f,
              open(cmd_list[2], "w") as new_f):
            new_f.write(old_f.read())
    else:
        print("Invalid request. "
              "Please use template as: cp 'file to read' 'file to write'")
