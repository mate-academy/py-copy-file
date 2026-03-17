def copy_file(command: str) -> None:
    command_split = command.split()
    if len(command_split) == 3 and command_split[0] == "cp":
        if command_split[1] == command_split[2]:
            return None
        try:
            with (
                open(command_split[1], "r") as file_in,
                open(command_split[2], "w") as file_out
            ):
                content_to_copy = file_in.read()
                file_out.write(content_to_copy)
        except FileNotFoundError:
            return None
