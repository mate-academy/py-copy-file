def copy_file(command: str) -> None:
    new_command = command.split()
    if (
            len(command.split()) == 3
            and new_command[1] != new_command[2]
            and command.split()[0] == "cp"
    ):
        with (
            open(new_command[1], "r") as file_in,
            open(new_command[2], "w") as file_out
        ):
            file_out.write(file_in.read())
