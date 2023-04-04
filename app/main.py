def copy_file(command: str) -> None:
    if len(command.split()) == 3:
        command_cp, file_name, file_to_copy = command.split()
        if file_name == file_to_copy:
            raise TypeError(f"{file_name} are the same name {file_to_copy}")
        if command_cp == "cp":
            with open(file_name, "r") as parent_file:
                with open(file_to_copy, "w") as file_copy:
                    file_copy.write(parent_file.read())
