def copy_file(command: str) -> None:
    command_split = command.split()

    with (
        open(command_split[1], "r") as file_in,
        open(command_split[2], "w") as file_out
    ):
        if command_split[1] != command_split[2]:
            original_file = file_in.read()
            file_out.write(original_file)
