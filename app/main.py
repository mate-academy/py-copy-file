def copy_file(command: str) -> None:
    command_parts = command.split()
    if len(command_parts) != 3 and command_parts[0] != "cp":
        raise ValueError("Bad command")
    if command_parts[1] != command_parts[2]:
        with open(command_parts[1], "r") as file_in, open(
                command_parts[2], "w"
        ) as file_out:
            file_out.write(str(file_in.read()))
