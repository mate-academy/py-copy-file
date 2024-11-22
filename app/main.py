def copy_file(command: str) -> None:
    command_split = command.split(" ")
    if len(command_split) == 3:
        file_name = command_split[1]
        copy_file_name = command_split[2]
        if command_split[0] == "cp" and file_name != copy_file_name:
            with (open(file_name, "r") as file_to_copy,
                    open(copy_file_name, "a") as file_copy):
                file_copy.write(str(file_to_copy.read()))
