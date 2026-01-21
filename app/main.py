import os.path


def copy_file(command: str):
    command_list = command.split()
    if not os.path.isfile(command_list[2]):
        with (open(command_list[1], "r") as file_in,
             open(command_list[2], "w") as file_out):
            file_out.write(file_in.read())
    return 0
