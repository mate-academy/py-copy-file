def copy_file(command):
    command_ls = command.split()
    file_name = command_ls[1]
    copy_name = command_ls[2]
    if file_name != copy_name:
        with open(f"{file_name}", "r") as file:
            with open(f"{copy_name}", "w") as copy:
                data = file.read()
                copy.write(data)
