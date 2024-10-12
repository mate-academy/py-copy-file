def copy_file(command: str) -> None:
    split_command = command.split()
    if split_command[1] == split_command[2]:
        return

    if split_command[0] == "cp":
        with (
            open(split_command[1], "r") as file_input,
            open(split_command[2], "w") as file_output
        ):
            file_output.write(file_input.read())
