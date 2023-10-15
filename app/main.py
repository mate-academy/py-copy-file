def copy_file(command: str) -> None:
    command_list = command.split()
    if command_list[1] == command_list[2] or command_list[0] != "cp":
        return
    with (open(command_list[1], "r") as read_file,
          open(command_list[2], "w") as write_file):
        write_file.write(read_file.read())
