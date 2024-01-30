def copy_file(command: str) -> None:
    command_list = command.split()
    if command_list[1] != command_list[2]:
        with (open(command_list[1], "r") as file_in,
              open(command_list[2], "a") as file_out):
            for line in file_in:
                file_out.write(line)
