def copy_file(command: str):
    command_list = command.split()

    if command_list[1] == command_list[2]:
        return

    with open(command_list[1], "r") as source:
        source = source.read()

        with open(command_list[2], "w") as destination:
            destination.write(source)


copy_file("cp file.txt file2.txt")
