def copy_file(command: str) -> None:
    command_list = command.split(" ")
    old_file = command_list[1]
    new_file = command_list[2]
    if old_file == new_file:
        return
    with open(old_file, "r") as file_from, open(new_file, "w") as file_to:
        for line in file_from:
            file_to.write(line)
