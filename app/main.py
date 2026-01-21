def copy_file(command: str) -> None:
    if not command:
        return
    split_command = command.split()
    if len(split_command) != 3:
        return
    if split_command[0] != "cp":
        return
    file_og = split_command[1]
    file_copy = split_command[2]
    if file_og == file_copy:
        return
    try:
        with open(file_og, "r") as file_in, \
                open(file_copy, "w") as file_out:
            for line in file_in:
                file_out.write(line)
    except FileNotFoundError:
        return
