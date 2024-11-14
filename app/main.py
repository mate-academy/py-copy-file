def copy_file(command: str) -> None:
    com_list = command.split()
    if len(com_list) != 3 or com_list[0] != "cp" or com_list[1] == com_list[2]:
        return
    with open(com_list[1], "r") as file_in, open(com_list[2], "w") as file_out:
        file_out.write(file_in.read())
