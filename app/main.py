def copy_file(command: str) -> None:
    file_names = command.split(" ")
    if file_names[0] != "cp" or file_names[1] == file_names[2]:
        print("GG")
        return

    with open(file_names[1], "r") as read_file, \
            open(file_names[2], "x") as write_file:
        write_file.writelines(read_file.readlines())
