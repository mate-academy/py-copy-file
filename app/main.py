# If you're reviewing this code - thank you <3

def copy_file(command: str):
    command_list = command.split()
    if command_list[0] == "cp" and command_list[1] != command_list[2]:
        with open(command_list[1], "r") as file_in, \
                open(command_list[2], "w") as file_out:
            file_out.write(file_in.read())
