def copy_file(command : str) -> None:
    command_list = command.split(" ")
    if len(command_list) != 3:
        return
    if command_list[1] == command_list[2]:
        return
    if command_list[0] != "cp":
        return
    try:
        with (open(command_list[1], "r") as file_to_copy,
              open(command_list[2], "w") as file_to_save):
            file_to_save.write(file_to_copy.read())
    except FileNotFoundError:
        return
