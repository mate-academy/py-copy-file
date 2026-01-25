def copy_file(command: str) -> None:
    command_list = command.split()
    if len(command_list) < 3:
        return None
    if command_list[1] == command_list[2]:
        return None
    if command_list[0] != "cp":
        return None
    try:
        with open(command_list[1],
                  "r") as origin, open(command_list[2], "w") as copy:
            copy.write(origin.read())
    except FileNotFoundError:
        return None
