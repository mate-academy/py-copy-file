def copy_file(command: str) -> None:
    command_list = command.split()
    file1, file2 = command_list[1], command_list[2]
    if file1 == file2:
        return
    with open(file1, "r") as file_in, open(file2, "w") as file_out:
        file_out.write(file_in.read())
