def copy_file(command: str):
    com_list = command.split
    old_name = com_list[1]
    new_name = com_list[2]

    if com_list[0] != 'cp':
        return
    if old_name == new_name:
        return

    with open(old_name, 'r') as original, open(new_name, 'w') as copied:
        copied.write(original.read())
