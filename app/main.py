def copy_file(command: str) -> None :
    command_list = command.split(" ")
    if len(command_list) != 3:
        return

    command_name, file_to_copy, file_to_paste = command_list

    if command_name != "cp" or file_to_copy == file_to_paste:
        return

    try:
        with (
            open(file_to_copy, "r") as file_from,
            open(file_to_paste, "w") as file_to
        ):
            file_to.write(file_from.read())
    except Exception:
        return
