def copy_file(command: str):
    com = command.split()[0]
    if com == "cp":
        file1 = command.split()[1]
        file2 = command.split()[2]
        if file1 != file2:
            with open(file1, "r") as file_in, open(file2, "w") as file_out:
                if not file_in.read() == file_out.read():
                    file_out.write(file_in.read())
