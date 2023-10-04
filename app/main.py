def copy_file(command: str) -> str:
    command_list = command.split()
    if command_list[1] != command_list[2]:
        with (open(command_list[1], "r") as file_in,
              open(command_list[2], "w") as file_out):
            for line in file_in:
                file_out.write(line)
