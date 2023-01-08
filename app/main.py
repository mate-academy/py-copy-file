def copy_file(command: str) -> None:
    command_list = command.split()
    if command_list[1] != command_list[2]:
        with open(command_list[1], "r") as file_get, \
                open(command_list[2], "w") as file_write:
            info = file_get.read()
            file_write.write(info)
