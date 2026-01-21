def copy_file(command: str) -> None:
    command, file_name, file_copy = command.split()
    if command != "cp" or file_name == file_copy:
        pass
    with open(file_name, "r") as file_in, open(file_copy, "w") as file_out:
        content = file_in.read()
        file_out.write(content)
