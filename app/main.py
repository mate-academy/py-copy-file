def copy_file(command: str) -> None:
    command_cp, file_name, file_to_copy = command.split()
    if file_name == file_to_copy:
        raise TypeError(f"{file_name} are the same name {file_to_copy}")
    if command_cp == "cp" and file_name != file_to_copy:
        with open("file.txt", "r") as parent_file, \
                open("new_file.txt", "w") as file_copy:
            recent_file = parent_file.read()
            file_copy.write(recent_file)
