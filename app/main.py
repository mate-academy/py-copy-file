def copy_file(command: str) -> None:
    command_lst = command.split()
    if len(command_lst) != 3:
        return
    if command_lst[0] != "cp":
        return
    if command_lst[1] == command_lst[2]:
        return

    try:
        with (open(command_lst[1], "r") as file_to_copy,
              open(command_lst[2], "w") as file_to_write):
            file_to_write.write(file_to_copy.read())
    except FileNotFoundError:
        return
