def copy_file(command: str) -> None:
    com_list = command.split
    old_file = com_list[1]
    new_file = com_list[2]

    if com_list[0] != 'cp' or old_file == new_file:
        return

    with open(old_file, 'r') as original, open(new_file, 'w') as file_copy:
        file_copy.write(original.read())
