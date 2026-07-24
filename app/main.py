def copy_file(command: str) -> None:
    command_list = command.split()
    if len(command_list) != 3 or command_list[0] != "cp":
        return

    old_file = command_list[1]
    new_file = command_list[2]

    if old_file == new_file:
        return

    try:
        with open(old_file, "r") as file_in, open(new_file, "w") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
