def copy_file(command: str) -> None:
    command_attr = command.split()

    if len(command_attr) != 3 or command_attr[0] != "cp":
        return

    file_name = (command_attr[1] if command_attr[1].endswith(".txt")
                 else f"{command_attr[1]}.txt")
    file_name_new = (command_attr[2] if command_attr[2].endswith(".txt")
                     else f"{command_attr[2]}.txt")

    if file_name == file_name_new:
        return

    with open(file_name, "r") as file_in, open(file_name_new, "w") as file_out:
        file_out.write(file_in.read())
