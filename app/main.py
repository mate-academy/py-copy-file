def cope_file(command: str) -> None:
    new_command = command.split()
    if (
        len(new_command) == 3
        and new_command[0] == "cp"
        and new_command[1] != new_command[2]
    ):
        with (
            open(new_command[1], "r") as file_in,
            open(new_command[2], "w") as file_out
        ):
            file_out.write(file_in.read())
