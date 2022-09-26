def copy_file(command):
    command, file1, file2 = command.split()

    with open(file1, "r") as file_in, open(file2, "w") as file_out:
        if file_in.name != file_out.name:
            file_out.write(file_in.read())
