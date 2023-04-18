def copy_file(command: str) -> None:
    file_in = command.split(" ")[1]
    file_out = command.split(" ")[2]
    if file_in != file_out:
        with open(file_in, "r") as file_orig, open(file_out, "w") as file_copy:
            file_copy.write(file_orig.read())
