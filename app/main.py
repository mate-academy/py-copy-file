def copy_file(command):
    str_list_command = command.split()
    if str_list_command[0] == "cp" and str_list_command[-1] != str_list_command[-2]:
        with open(f"{str_list_command[-2]}", "r") as file_in, \
                open(f"{str_list_command[-1]}", "w") as file_out:
            file_out.write(f"{file_in.read()}")
