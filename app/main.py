def copy_file(command: str):
    file = command.split()
    if file[1] != file[2] and file[0] == "cp":
        with open(file[1], "r") as file1, open(file[2], "w") as file2:
            file2.write(file1.read())
