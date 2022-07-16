def copy_file(command):
    copy_list = list(command)
    if copy_list[1] != copy_list[2] and copy_list[0] == "cp":
        with open(copy_list[1], "r") as file_in, \
                open(copy_list[2], "w") as file_out:
            file_out.write(file_in.read())
    else:
        return 0
