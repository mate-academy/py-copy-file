def copy_file(command: str) -> None:
    action, file_name1, file_name2 = command.split()
    if action == "cp" and file_name1 != file_name2:
        with open(file_name1, "r") as file1, open(file_name2, "w") as file2:
            file2.write(file1.read())
