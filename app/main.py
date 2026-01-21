def copy_file(command: str) -> None:
    parametrs = command.split()
    if len(parametrs) == 3:
        command_name, file_name, copy_file_name = parametrs
        if file_name != copy_file_name and command_name == "cp":
            with (
                open(file_name, "r") as file,
                open(copy_file_name, "w") as new_file
            ):
                new_file.write(file.read())
