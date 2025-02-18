def copy_file(command: str) -> None:
    command_cp, command_file, command_new_file = command.split()

    if command_cp == "cp" and command_file != command_new_file:
        with (
            open(command_file, "r") as file_in,
            open(command_new_file, "w") as file_out
        ):
            file_out.write(file_in.read())
