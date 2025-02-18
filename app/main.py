def copy_file(command: str) -> None:
    new_list = command.split()
    if "cp" in command:
        abr_command, file_needs_copy, new_copy_of_file = new_list
        if file_needs_copy == new_copy_of_file:
            return
        with (
            open(file_needs_copy, "r") as file_1,
            open(new_copy_of_file, "w") as file_2
        ):
            file_2.write(file_1.read())
