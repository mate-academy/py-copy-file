def copy_file(command: str) -> None:
    command_list = command.split()
    if command_list[1] != command_list[2]:
        with (open(command_list[1], "r") as file_read,
              open(command_list[2], "a") as file_write):
            file_write.write(file_read.read())
