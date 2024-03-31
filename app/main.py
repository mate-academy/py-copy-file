def copy_file(command: str) -> None:
    command_separate = command.split()
    file_name1 = command_separate[1]
    file_name2 = command_separate[2]
    if file_name1 != file_name2:
        with open(file_name1, "r") as file1, open(file_name2, "w") as file2:
            file2.write(file1.read())
