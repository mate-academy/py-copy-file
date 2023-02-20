def copy_file(command: str) -> None:
    com, file_to_copy, copy = command.split()
    if com == "cp" and file_to_copy != copy:
        with open(file_to_copy, "r") as file_in, open(copy, "w") as file_out:
            file_out.write(file_in.read())
