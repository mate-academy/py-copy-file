def copy_file(command: str) -> None:
    arguments_list = command.split()
    if len(arguments_list) != 3:
        return
    if arguments_list[0] == "cp":
        file_name_to_copy = arguments_list[1]
        copied_file_name = arguments_list[2]
        if file_name_to_copy == copied_file_name:
            return
        try:
            with (
                open(file_name_to_copy, "r") as file,
                open(copied_file_name, "w") as copied_file
            ):
                copied_file.write(file.read())
        except FileNotFoundError:
            return
    return
