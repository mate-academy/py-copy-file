def copy_file(command: str):
    names = command.split()
    cp = names[0]
    original_name = names[-2]
    file_copy = names[-1]
    if original_name == file_copy or cp != "cp":
        pass
    else:
        with open(original_name, "r") as file_in, \
                open(file_copy, "w") as file_out:
            [file_out.write(line) for line in file_in]
