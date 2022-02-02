def copy_file(command):
    file1, file2 = command.split(' ')[1], command.split(' ')[2]
    with open(file1, "r") as f1:
        with open(file2, "w") as f2:
            f2.write(f1.read())
