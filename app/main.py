def copy_file(command):
    with open(command.split(' ')[1], "r") as f1:
        with open(command.split(' ')[2], "w") as f2:
            f2.write(f1.read())
