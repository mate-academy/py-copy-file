def copy_file(command: str) -> None:
    command_list = command.split()
    if len(command_list) == 3:
        command, old_file, new_file = command_list
        if command == "cp" and old_file != new_file:
            with (
                open(old_file, "r") as file_in,
                open(new_file, "w") as file_out
            ):
                file_out.write(file_in.read())
