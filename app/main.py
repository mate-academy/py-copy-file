def copy_file(command: str) -> None:
    command_data = command.split()
    if command_data[0] != "cp" or len(command_data) != 3:
        return

    with (open(command_data[1], "r") as file_in,
          open(command_data[2], "w") as file_out):
        file_out.writelines(file_in.readlines())
