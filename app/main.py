def copy_file(command: str) -> None:
    command_parts = command.split()
    if len(command_parts) != 3:
        raise ValueError("Invalid command format")
    if command_parts[1] == command_parts[2]:
        pass
    if command_parts[0] == "cp":
        with (
            open(command_parts[1], "r") as file_in,
            open(command_parts[2], "w") as file_out
        ):
            file_out.write(file_in.read())
