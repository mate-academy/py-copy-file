def copy_file(command: str) -> None:

    command_list = command.split()

    if command_list[1] == command_list[2] or command_list[0] != "cd":
        print("do nothing")
        return None

    with open(command_list[1], "r") as file_out, open(command_list[2], "w") as file_to:
        print("copy file")
        file_to.write(file_out.read())
