def copy_file(command: str) -> None:
    list_from_command = command.split(" ")
    command_name, file_name, copy_file_name = list_from_command
    is_name_valid = file_name != copy_file_name
    is_command_valid = command_name == "cp"
    is_all_params = len(list_from_command) == 3

    print(is_name_valid, is_command_valid, is_all_params)

    if is_name_valid and is_command_valid and is_all_params:
        with (
            open(file_name, "rb") as original,
            open(copy_file_name, "wb") as copy
        ):
            copy.write(original.read())


copy_file("cp mango.txt file-copy.txt")
