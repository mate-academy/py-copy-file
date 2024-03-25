def copy_file(text: str) -> None:
    if text.split() == 3:
        command, file_name_1, file_name_2 = text.split()
        if command == "cd" and file_name_1 != file_name_2:
            with open(file_name_1, "r") as source, \
                    open(file_name_2, "w") as copy:
                copy.write(source.read())
