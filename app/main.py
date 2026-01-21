def copy_file(command: str):
    file1_name, file2_name = command.split(" ")[1:]
    if file1_name != file2_name:
        with open(file1_name, "r") as file_in, \
                open(file2_name, "w") as file_out:
            file_out.write(file_in.read())
