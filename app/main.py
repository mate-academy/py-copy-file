def copy_file(text: str) -> None:
    command, file_name_1, file_name_2 = text.split()
    print(command, file_name_1, file_name_2)
    if command == "cd" and file_name_1 != file_name_2:
        with open(file_name_1, "r") as source, open(file_name_2, "w") as copy:
            copy.write(source.read())


copy_file("cd ark.txt beke.txt")
