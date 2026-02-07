def copy_file(command: str) -> None:
    command_in_list = command.split()
    if len(command_in_list) != 3 or command_in_list[0] != "cp":
        return
    if command_in_list[1] == command_in_list[2]:
        return
    try:
        with (open(command_in_list[1], "r") as file_in,
              open(command_in_list[2], "w") as file_out):
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
