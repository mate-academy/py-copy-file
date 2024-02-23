def copy_file(command: str) -> None:
    params = command.split(" ")
    command_name = params[0]
    file_name = params[1]
    file_name_copy = params[2]

    if file_name != file_name_copy and command_name == "cp":
        with (
            open(file_name, "r") as file,
            open(file_name_copy, "w") as file_copy
        ):
            file_copy.write(file.read())
