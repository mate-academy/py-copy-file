def copy_file(command: str) -> None:
    сopy_command, file1, file2 = command.split()
    if сopy_command == "cp":
        if file1 == file2:
            return
        with open(file1, "r") as file_def, open(file2, "w") as file_def2:
            text_file = file_def.read()
            file_def2.write(text_file)
