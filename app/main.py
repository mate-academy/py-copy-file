def copy_file(command: str) -> None:
    file_name = command.split()[1]
    copy_name = command.split()[2]
    if file_name != copy_name:
        with open(file_name, "r") as file, open(copy_name, "w") as copy:
            copy.write(file.read())
