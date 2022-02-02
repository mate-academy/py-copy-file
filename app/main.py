def copy_file(command: str):
    command_list = command.split()

    if command_list[1] == command_list[2]:
        return

    with open(command_list[1], "r") as first_file:
        first_file = first_file.read()

        with open(command_list[2], "w") as second_file:
            second_file.write(first_file)


copy_file("cp file.txt file2.txt")
