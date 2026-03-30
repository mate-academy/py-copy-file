def copy_file(command: str) -> None:
    list_of_command = command.split()
    if len(list_of_command) == 3 and list_of_command[0] == "cp":
        file_to_copy, file_take_copy = list_of_command[1], list_of_command[2]
        if not file_to_copy == file_take_copy:
            try:
                with (
                    open(file_to_copy) as copied_file,
                    open(file_take_copy, "w") as new_file
                ):
                    new_file.write(copied_file.read())
            except FileNotFoundError:
                return
