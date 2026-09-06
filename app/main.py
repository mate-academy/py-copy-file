def copy_file(command: str) -> None:
    command_list = command.split()
    if not command_list:
        return
    if command_list[0] != "cp":
        return
    if len(command_list) < 3:
        return
    if command_list[1] == command_list[2]:
        return
    if len(command_list) < 3 or command_list[0] != "cp":
        return
    else:
        try:
            with (open(command_list[1], "r") as source,
                  open(command_list[2], "w") as destination):
                destination.write(source.read())
        except FileNotFoundError:
            return
