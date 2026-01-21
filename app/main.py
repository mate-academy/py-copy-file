def copy_file(command: str) -> None:
    command_list = command.split()

    if len(command_list) != 3 or command_list[0] != "cp":
        return

    file_name = command_list[1]
    new_file_name = command_list[2]

    if file_name == new_file_name:
        return

    try:
        src_file = open(file_name, "r")
    except FileNotFoundError:
        return

    dest_file = open(new_file_name, "w")
    dest_file.write(src_file.read())
    src_file.close()
    dest_file.close()
