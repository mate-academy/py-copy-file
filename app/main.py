def copy_file(command: str) -> None:
    command_str_into_list = command.split()
    old_file, new_file = command_str_into_list[1], command_str_into_list[2]
    if old_file != new_file:
        with open(old_file, "r") as file_in, open(new_file, "w") as file_out:
            file_out.write(file_in.read())
