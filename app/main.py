def copy_file(command: str) -> None:
    command_list = command.split()
    file_1 = command_list[1]
    file_2 = command_list[2]

    if file_1 == file_2:
        pass
    with open(file_1, "r") as file_out, open(file_2, "w") as file_in:
        for line in file_out.readlines():
            copy_content = line
            file_in.write(copy_content)
