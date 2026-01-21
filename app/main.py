def copy_file(command: str):
    command_list = command.split()
    if command_list[1] != command_list[2]:
        with open(command_list[1], "r") as file_origin, \
                open(command_list[2], "w") as file_copy:
            file_copy.write(file_origin.read())
