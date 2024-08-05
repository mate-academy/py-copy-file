def copy_file(command: str) -> None:
    command_list = command.split()
    if (
            len(command_list) != 3
            or command_list[0] != "cp"
            or command_list[1] == command_list[2]
    ):
        return

    file1_name = command_list[1]
    file2_name = command_list[2]
    with open(file1_name) as file1, open(file2_name, "w") as file2:
        for line in file1:
            file2.write(line)
