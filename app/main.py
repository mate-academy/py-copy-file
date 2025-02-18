def copy_file(command: str) -> None:
    command = command.split()
    command_type, file_in, file_out = command
    if command_type == "cp" and file_in != file_out:
        with open(file_in, "r") as file_orig, open(file_out, "w") as file_copy:
            file_copy.write(file_orig.read())
