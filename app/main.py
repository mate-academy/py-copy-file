def copy_file(command: str) -> None:
    _, file_to_copy, file_copy_name = command.split(" ")

    if file_to_copy == file_copy_name:
        return

    with open(file_to_copy, "r") as file_in, \
         open(file_copy_name, "w") as file_out:
        file_out.write(file_in.read())


copy_file("cp file.txt file-new.txt")
