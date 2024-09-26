def copy_file(command):
    file_1 = command.split()[1]
    file_2 = command.split()[2]
    if file_1 != file_2 and command.split()[0] == 'cp':
        with open(file_1, "r") as file_in, open(file_2, "w") as file_out:
            file_out.write(file_in.read())
