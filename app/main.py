def copy_file(command: str) -> None:
    command_parts = command.split()

    command1, command2, command3 = command_parts
    if command1 != "cp" or command2 == command3:
        return

    with (open(command_parts[1], "r") as file_in,
          open(command_parts[2], "w") as file_out):
        file_out.write(file_in.read())
