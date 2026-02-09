def copy_file(command: str) -> None:
    if command:
        token = command.split()
        if len(token) == 3:
            command, file_name_1, file_name_2 = token
            if command == "cp" and file_name_1 != file_name_2:
                try:
                    with (open(file_name_1, "r") as source_file,
                          open(file_name_2, "w") as destination_file):
                        data_copy = source_file.readlines()
                        destination_file.writelines(data_copy)
                except FileNotFoundError:
                    pass
                except PermissionError:
                    pass
