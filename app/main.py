def copy_file(command):
    command_list = command.split(" ")
    with open(f"{command_list[1]}", "r") as file_in, \
            open(f"{command_list[2]}", "w") as file_out:

        if command_list[1] == command_list[2]:
            pass
        else:
            file_out.write(f"{file_in.read()}")
    pass
