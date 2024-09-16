def copy_file(command: str) -> None:
    command_ls = command.split()
    if len(command_ls) == 3 and \
       command_ls[0] == "cp" and \
       command_ls[1] != command_ls[2]:
        with open(command_ls[1], "r") as file_in, \
             open(command_ls[2], "w") as file_out:
            file_out.writelines(file_in.readlines())
