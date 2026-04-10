import os


def copy_file(command: str) -> None:
    command_list = command.split()
    if len(command_list) == 3 and command_list[0] == "cp":
        if command_list[1] != command_list[2] \
                and os.path.isfile(command_list[1]) and \
                os.path.dirname(command_list[1]) == "" and \
                os.path.dirname(command_list[2]) == "":
            with open(f"{command_list[1]}", "r") as file_in, \
                    open(f"{command_list[2]}", "w") as file_out:
                text = file_in.read()
                file_out.write(text)
