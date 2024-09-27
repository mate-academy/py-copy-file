def copy_file(command: str):
    list_name = command.split()
    if list_name[1] == list_name[2]:
        return
    if list_name[0] != "cp":
        print("Wrong command!")
    with open(list_name[1], "r") as file_orig,\
            open(list_name[2], "w") as file_copy:
        file_copy.write(file_orig.read())
