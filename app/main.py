def copy_file(command):
    if command.split()[1] == command.split()[2] \
            or command.split()[0] != "cp":
        return
    with open(command.split()[1], "r") as file_in, \
            open(command.split()[2], "w") as file_out:
        content = file_in.read()
        file_out.write(content)
