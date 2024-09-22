def copy_file(command: str) -> None:
    command_parts = command.split(" ")

    file_to_copy = command_parts[1]
    file_copy_name = command_parts[2]

    if file_to_copy == file_copy_name:
        return

    with open(file_to_copy, "r") as file_in, \
         open(file_copy_name, "w") as file_out:
        file_out.write(file_in.read())


copy_file("cp file.txt file-new.txt")
