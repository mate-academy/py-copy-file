def copy_file(command: str) -> None:
    command_parts = command.split(" ")
    file_name = command_parts[1]
    copy_file_name = command_parts[2]
    if command_parts[0] != "cp":
        raise ValueError('There is not "cp" command')
    if file_name == copy_file_name:
        return
    with open(file_name, "r") as original, open(copy_file_name, "w") as copy:
        copy.write(original.read())
