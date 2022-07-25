def copy_file(command):
    file_names = command.split()
    if file_names[1] == file_names[2]:
        return
    with open(file_names[1], "r") as file_out, \
            open(file_names[2], "w") as file_in:
        context = file_out.read()
        file_in.write(context)
