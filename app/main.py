def copy_file(command: str):
    com_ls = command.split(" ")
    current_name = com_ls[1]
    copy_name = com_ls[2]
    if current_name != copy_name:
        with open(current_name, "r") as file_in, \
                open(copy_name, "w") as file_out:
            file_out.write(file_in.read())
