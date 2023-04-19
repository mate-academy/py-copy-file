def copy_file(command: str) -> None:
    command_type = command.split()[0]
    file_in = command.split()[1]
    file_out = command.split()[2]
    if command_type == "cp" and file_in != file_out:
        with open(file_in, "r") as file_orig, open(file_out, "w") as file_copy:
            file_copy.write(file_orig.read())
