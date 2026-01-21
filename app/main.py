def copy_file(command: str) -> None:
    command_list = command.split()
    if len(command_list) == 3:
        if command_list[0] == "cp":
            if command_list[1] != command_list[2]:
                with (open(command_list[1], "r") as file_read,
                      open(command_list[2], "w") as file_write):
                    file_write.write(file_read.read())
