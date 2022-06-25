def copy_file(command: str):
    file1 = command.split()[1]
    file2 = command.split()[2]
    if file1 == file2:
        return
    else:
        with open(file1, "r") as file_in, open(file2, "w") as file_out:
            if file_in.read() == file_out.read():
                return
            else:
                file_out.write(file_in.read())
