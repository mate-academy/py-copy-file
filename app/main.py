def copy_file(command: str):
    copy_command = command.split(" ")[0]
    file1 = command.split(" ")[1]
    file2 = command.split(" ")[2]
    if file1 != file2 and copy_command == "cp":
        with open(file1, "r") as file_in, open(file2, "w") as file_out:
            file_out.write(file_in.read())
