def copy_file(command: str) -> None:
    cmd_list = command.split()
    if (
        len(cmd_list) != 3
        or cmd_list[0] != "cp"
        or cmd_list[1] == cmd_list[2]
    ):
        return

    try:
        with (open(cmd_list[1], "r") as original,
              open(cmd_list[2], "w") as copy):
            copy.write(original.read())
    except (FileNotFoundError, PermissionError):
        return
