def copy_file(command: str) -> None:
    params = command.split(" ")
    if len(params) == 3:
        command_name, file_name, file_name_copy = params

        if file_name != file_name_copy and command_name == "cp":
            with (
                open(file_name, "r") as file,
                open(file_name_copy, "w") as file_copy
            ):
                file_copy.write(file.read())
