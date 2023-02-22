def copy_file(command: str) -> None:
    command_name, file_name, file_name_copy = command.split()
    if command_name == "cp" and file_name != file_name_copy:
        with open(file_name, "r") as file_in, \
                open(file_name_copy, "w") as file_out:
            file_out.write(file_in.read())
