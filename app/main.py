
def copy_file(command: str) -> None:
    command_parts = command.split()
    if len(command_parts) == 3:
        _, main_file_name, new_file_name = command_parts
        if (new_file_name != main_file_name
                and command_parts[0] == "cp"):
            with (
                open(main_file_name, "r") as main_file,
                open(new_file_name, "w") as new_file
            ):
                content_of_general_file = main_file.read()
                new_file.write(content_of_general_file)
    return
