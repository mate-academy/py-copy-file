def copy_file(command: str) -> None:
    files = command.split()
    if files[1] != files[2] and files[0] == "cp":
        with open(files[1], "r") as file_1, open(files[2], "w") as file_2:
            file_2.write(file_1.read())
