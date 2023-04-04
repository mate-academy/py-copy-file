def copy_file(command: str) -> None:
    update_command = command.split()
    command_flag, current_file, file_copy = update_command
    if len(update_command) == 3:
        if current_file == file_copy:
            raise TypeError(
                f"{current_file} are the same name {file_copy}"
            )
        if command_flag == "cp":
            with open(current_file, "r") as parent_file, \
                    open(file_copy, "w") as file_copy:
                file_copy.write(parent_file.read())
