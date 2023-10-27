def copy_file(command: str) -> None:
    # Split the command into parts
    command_parts = command.split()

    if command_parts[0] != "cp" or command_parts[1] == command_parts[2]:
        return

    with (open(command_parts[1], "r") as file_in,
          open(command_parts[2], "w") as file_out):
        file_out.write(file_in.read())
