def copy_file(command: str) -> None:
    command_parts = command.split(" ")
    if len(command_parts) == 3 and command_parts[0] == "cp":
        if command_parts[1] == command_parts[2]:
            return
        else:
            with (
                open(command_parts[1], "r") as file_in,
                open(command_parts[2], "w") as file_out
            ):
                for line in file_in:
                    file_out.write(line)
