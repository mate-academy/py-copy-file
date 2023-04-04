def copy_file(command: str) -> None:
    update_command = command.split()
    if len(update_command) == 3:
        if update_command[1] == update_command[2]:
            raise TypeError(
                f"{update_command[1]} are the same name {update_command[2]}"
            )
        if update_command[0] == "cp":
            with open(update_command[1], "r") as parent_file, \
                    open(update_command[2], "w") as file_copy:
                file_copy.write(parent_file.read())
