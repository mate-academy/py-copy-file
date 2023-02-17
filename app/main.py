def copy_file(command: str) -> None:
    command = command.split()
    file_name = command[1]
    file_copy_name = command[2]
    if len(command) == 3 and file_name != file_copy_name:
        with open(file_name) as file1:
            file1 = file1.read()
            if len(file1) != 0:
                with open(file_copy_name, "w") as file_copy:
                    file_copy.write(file1)
