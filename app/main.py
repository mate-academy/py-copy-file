def copy_file(command: str):
    lst_command = command.split(" ")
    origin = lst_command[1]
    copy = lst_command[2]
    if origin == copy:
        return
    with open(origin, "r") as file_in, open(copy, "w") as file_out:
        file_out.write(file_in.read())
