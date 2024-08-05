def copy_file(command: str) -> None:
    command_split = command.split()
    command_to_read, command_to_write = command_split
    if command_to_read != command_to_write:
        with (
            open(command_to_read, "r") as file_in,
            open(command_to_write, "w") as file_out
        ):
            file_out.write(file_in.read())
