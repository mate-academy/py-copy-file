def copy_file(command: str) -> None:
    update_command = command.split()
    if len(update_command) == 3:
        command_flag, current_file, file_copy = update_command
        if current_file == file_copy:
            return
        if command_flag == "cp":
            with (open(current_file, "r") as parent_file,
                  open(file_copy, "w") as file_copy):
                file_copy.write(parent_file.read())
