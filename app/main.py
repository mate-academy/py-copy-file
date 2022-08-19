def copy_file(command: str):
    names = command.split()
    original_name = names[1]
    file_copy = names[2]
    if original_name == file_copy:
        pass
    with open(original_name, "r") as file_in, \
            open(file_copy, "w") as file_out:
        [file_out.write(line) for line in file_in]
