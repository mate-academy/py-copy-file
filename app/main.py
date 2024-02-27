def copy_file(command: str) -> None:
    file_in = command.split()[1]
    file_out = command.split()[2]
    if file_in != file_out:
        with open(file_in, "r") as to_copy, open(file_out, "w") as copied:
            copied.write(to_copy.read())
