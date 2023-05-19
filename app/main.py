def copy_file(command: str) -> None:
    command = command.split()
    if len(command) != 3:
        return
    file_name1, file_name2 = command[1:]
    if file_name1 == file_name2:
        return
    with open(file_name1, "r") as file_in, open(file_name2, "w") as file_out:
        original_file = file_in.read()
        file_out.write(original_file)
