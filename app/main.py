def copy_file(command: str) -> None:
    command_list = command.split()

    if command_list[0] != "cp" or len(command_list) != 3:
        raise ValueError("The command is specified incorrectly")

    if command_list[1] != command_list[2]:
        with (open(command_list[1], "r") as file_in,
              open(command_list[2], "w") as file_out):
            for line in file_in:
                file_out.write(line)
