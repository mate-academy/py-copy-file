def copy_file(command: str) -> None:
    command_list = command.split(" ")
    original_file = command_list[1]
    file_to_copy = command_list[2]

    if original_file == file_to_copy:
        return

    with open(original_file, "r") as orig, open(file_to_copy, "a") as copy:
        for line in orig.readlines():
            copy.write(line)
