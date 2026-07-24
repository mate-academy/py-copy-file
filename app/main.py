def copy_file(copy_command: str) -> None:
    command_list = copy_command.split()
    if len(command_list) != 3 or command_list[0] != "cp":
        return

    old_file = command_list[1]
    new_file = command_list[2]

    if old_file == new_file:
        return

    try:
        with open(old_file, "r") as read_only_file:
            with open(new_file, "w") as copied_file:
                copied_file.write(read_only_file.read())
    except FileNotFoundError:
        return
