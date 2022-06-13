def copy_file(command):
    file = command.split()
    if file[1] != file[2]:
        with open(file[1], "r") as file1:
            with open(file[2], "w") as file2:
                file2.write(file1.read())
